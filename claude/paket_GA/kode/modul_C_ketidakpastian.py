"""
modul_C_ketidakpastian.py — propagasi ketidakpastian parameter Planck 2018 (naskah §2.7).

z_pk, Δ_fD, z_V dan Δ_V hanya bergantung pada Om (untuk ΛCDM datar), sedangkan
waktu lihat-balik berskala 1/h. CMB mengukur skala sudut akustik sangat presisi,
sehingga Om dan h berkorelasi kuat di sepanjang Om h^3 ≈ konstan (Planck
Collaboration 2020). Sampel Monte Carlo karena itu diambil dari Om ~ N(0.315, 0.0073) dengan
h = 0.674 (0.315 / Om)^(1/3); cara ini menghasilkan σ(H0) = 0,52 km/s/Mpc,
sesuai dengan 0,54 km/s/Mpc dari Planck Collaboration (2020).

Besaran dihitung pada kisi Om lalu diinterpolasi spline kubik.
"""
from __future__ import annotations

import numpy as np
from scipy.interpolate import CubicSpline

from modul_A_pertumbuhan import analisis
from parameter import PLANCK18, PLANCK18_SIGMA_Om, PLANCK18_SIGMA_sigma8

KUNCI = ["z_pk", "Delta_fD", "t_lb_pk_Gyr", "f_hari_ini", "Om_di_puncak", "z_V", "Delta_V",
         "t_lb_V_Gyr", "fD_max"]


def kisi_Om(Om_min: float = 0.20, Om_maks: float = 0.45, n: int = 101) -> dict:
    """Besaran inti pada kisi Om (h tetap 0.674; t_lb diskalakan kemudian)."""
    Om = np.linspace(Om_min, Om_maks, n)
    tabel = {k: np.empty(n) for k in KUNCI}
    for i, om in enumerate(Om):
        h = analisis(PLANCK18.dengan(Om=om), a_rentang=(0.15, 1.5))
        for k in KUNCI:
            tabel[k][i] = h[k]
    tabel["Om"] = Om
    return tabel


def spline_dari_kisi(tabel: dict) -> dict:
    return {k: CubicSpline(tabel["Om"], tabel[k]) for k in KUNCI}


def monte_carlo(n: int = 200_000, benih: int = 20260926, tabel: dict | None = None) -> dict:
    rng = np.random.default_rng(benih)
    tabel = tabel or kisi_Om()
    sp = spline_dari_kisi(tabel)
    Om = rng.normal(PLANCK18.Om, PLANCK18_SIGMA_Om, n)
    h = PLANCK18.h * (PLANCK18.Om / Om) ** (1.0 / 3.0)
    sigma8 = rng.normal(PLANCK18.sigma8, PLANCK18_SIGMA_sigma8, n)
    sampel = {k: sp[k](Om) for k in KUNCI}
    # waktu lihat-balik pada kisi dihitung untuk h = 0.674
    sampel["t_lb_pk_Gyr"] *= PLANCK18.h / h
    sampel["t_lb_V_Gyr"] *= PLANCK18.h / h
    sampel["fsigma8_hari_ini"] = sigma8 * sp["f_hari_ini"](Om)
    sampel["H0"] = 100 * h
    ringkasan = {}
    for k, v in sampel.items():
        p16, p50, p84 = np.percentile(v, [16, 50, 84])
        ringkasan[k] = {"median": float(p50), "minus": float(p50 - p16), "plus": float(p84 - p50),
                        "std": float(np.std(v))}
    return {"n": n, "benih": benih, "ringkasan": ringkasan}


def turunan_terhadap_Om(tabel: dict, Om0: float = PLANCK18.Om) -> dict:
    """Kepekaan linear d(besaran)/dOm di Om0."""
    sp = spline_dari_kisi(tabel)
    return {k: float(sp[k].derivative()(Om0)) for k in ("z_pk", "Delta_fD", "Om_di_puncak")}


if __name__ == "__main__":
    tabel = kisi_Om()
    print("Om(a_pk) pada 0.20 <= Om <= 0.45: min %.4f, maks %.4f"
          % (tabel["Om_di_puncak"].min(), tabel["Om_di_puncak"].max()))
    print("Turunan:", turunan_terhadap_Om(tabel))
    mc = monte_carlo(tabel=tabel)
    for k, v in mc["ringkasan"].items():
        print(f"{k:18s} {v['median']:.4f} -{v['minus']:.4f} +{v['plus']:.4f}")
