"""
modul_A_pertumbuhan.py — pertumbuhan struktur linear untuk basin Great Attractor.

Mengimplementasikan §2.1–2.4 naskah:

    E^2(a)          = Om a^-3 + Or a^-4 + Ode g(a)                        (1)
    Om(a)           = Om a^-3 / E^2(a)                                    (2)
    dlnH/dlna       = -1/2 [3 Om(a) + 4 Or(a) + 3 (1 + w) Ode(a)]         (3)
    δ'' + (2 + dlnH/dlna) δ' - 3/2 Om(a) δ = 0,   ' = d/dln a             (4)
    δ(a_i) = a_i,  δ'(a_i) = a_i,  a_i = 1e-3                             (5)
    D(a) = δ(a) / δ(1)                                                    (6)
    f = dlnD/dlna                                                         (7)
    fD = dD/dlna                                                          (8)
    d(fD)/dlna = 0  di a_pk                                               (9)
    t(a) = H0^-1 ∫_0^a da'/(a' E(a'))                                     (10)
    Δ_fD = 1 - (fD)_{a=1} / (fD)_max                                      (11)

Untuk ΛCDM tanpa radiasi (model fiducial) g(a) = 1 dan (3) menjadi
-3/2 Om(a). g(a) umum mengikuti parameterisasi CPL w(a) = w0 + wa (1 - a).

Selain fD, modul ini juga menyediakan dua besaran pembanding (§2.6):
    V(a)    = a E(a) f D   ∝ amplitudo kecepatan pekuliar linear pada jarak komoving tetap
    Ddot(a) = E(a) f D     = (dD/dt) / H0, laju pertumbuhan per satuan waktu kosmik

Jalankan `python modul_A_pertumbuhan.py` untuk mencetak angka inti.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar

from parameter import A_AWAL, A_PENCARIAN, ATOL, PLANCK18, RTOL, Kosmologi


# ---------------------------------------------------------------------------
# Latar belakang (persamaan 1–3)
# ---------------------------------------------------------------------------
def rasio_energi_gelap(a, k: Kosmologi):
    """rho_DE(a) / rho_DE(1) untuk w(a) = w0 + wa (1 - a)."""
    a = np.asarray(a, dtype=float)
    return a ** (-3.0 * (1.0 + k.w0 + k.wa)) * np.exp(-3.0 * k.wa * (1.0 - a))


def E2(a, k: Kosmologi):
    a = np.asarray(a, dtype=float)
    return k.Om * a**-3 + k.Or * a**-4 + k.Ode * rasio_energi_gelap(a, k)


def E(a, k: Kosmologi):
    return np.sqrt(E2(a, k))


def omega_m(a, k: Kosmologi):
    a = np.asarray(a, dtype=float)
    return k.Om * a**-3 / E2(a, k)


def omega_r(a, k: Kosmologi):
    a = np.asarray(a, dtype=float)
    return k.Or * a**-4 / E2(a, k)


def omega_de(a, k: Kosmologi):
    return k.Ode * rasio_energi_gelap(a, k) / E2(a, k)


def w_de(a, k: Kosmologi):
    return k.w0 + k.wa * (1.0 - np.asarray(a, dtype=float))


def dlnH_dlna(a, k: Kosmologi):
    """Persamaan (3); untuk ΛCDM tanpa radiasi sama dengan -3/2 Om(a)."""
    return -0.5 * (
        3.0 * omega_m(a, k) + 4.0 * omega_r(a, k) + 3.0 * (1.0 + w_de(a, k)) * omega_de(a, k)
    )


def parameter_perlambatan(a, k: Kosmologi):
    """q = -1 - dlnH/dlna. Ekspansi dipercepat bila q < 0."""
    return -1.0 - dlnH_dlna(a, k)


# ---------------------------------------------------------------------------
# Waktu kosmik (persamaan 10)
# ---------------------------------------------------------------------------
_LN_A_MIN = np.log(1.0e-12)


def waktu_kosmik(a, k: Kosmologi) -> np.ndarray:
    """Umur alam semesta pada faktor skala a, dalam Gyr.

    Integral (10) dievaluasi dalam ln a; kontribusi a < 1e-12 (~1e-18 Gyr)
    diabaikan.
    """
    a_arr = np.atleast_1d(np.asarray(a, dtype=float))
    hasil = np.empty_like(a_arr)
    for i, ai in enumerate(a_arr):
        nilai, _ = quad(
            lambda x: 1.0 / E(np.exp(x), k), _LN_A_MIN, np.log(ai),
            epsabs=0.0, epsrel=1e-12, limit=400,
        )
        hasil[i] = nilai * k.waktu_hubble_gyr
    return hasil if np.ndim(a) else hasil[0]


def waktu_lihat_balik(a, k: Kosmologi):
    """t_lb(a) = t(1) - t(a) dalam Gyr (negatif untuk a > 1, yaitu masa depan)."""
    return waktu_kosmik(1.0, k) - waktu_kosmik(a, k)


def a_dari_waktu_lihat_balik(t_lb: float, k: Kosmologi) -> float:
    """Kebalikan dari waktu_lihat_balik (t_lb < 0 = masa depan)."""
    return brentq(lambda ln_a: waktu_lihat_balik(np.exp(ln_a), k) - t_lb, np.log(1e-6), np.log(1e4),
                  xtol=1e-13)


# ---------------------------------------------------------------------------
# Persamaan pertumbuhan (4)–(8)
# ---------------------------------------------------------------------------
class SejarahPertumbuhan:
    """Solusi D(a) ternormalisasi D(1) = 1, beserta f, fD, V dan Ddot.

    Parameter
    ---------
    k : Kosmologi
        Model latar. Bila k.gamma bernilai angka, pertumbuhan dihitung dari
        f(a) = Om(a)^gamma (parameterisasi indeks pertumbuhan, Linder 2005)
        alih-alih dari persamaan (4).
    a_awal : float
        Faktor skala awal integrasi (persamaan 5).
    a_akhir : float
        Batas atas integrasi (dipakai untuk masa depan, §3.5).
    syarat_awal : {"materi", "meszaros"}
        "materi": persamaan (5). "meszaros": mode tumbuh 1 + 3y/2,
        y = a / a_eq (Meszaros 1974), untuk uji dengan radiasi.
    """

    def __init__(self, k: Kosmologi, a_awal: float = A_AWAL, a_akhir: float = 1.0e3,
                 rtol: float = RTOL, atol: float = ATOL, syarat_awal: str = "materi"):
        self.k = k
        self.a_awal = a_awal
        self.a_akhir = a_akhir
        x0, x1 = np.log(a_awal), np.log(a_akhir)

        if k.gamma is None:
            if syarat_awal == "materi":
                y0 = [a_awal, a_awal]
            elif syarat_awal == "meszaros":
                if k.Or <= 0:
                    raise ValueError("syarat_awal='meszaros' memerlukan Or > 0")
                y = a_awal / (k.Or / k.Om)
                y0 = [1.0 + 1.5 * y, 1.5 * y]
            else:
                raise ValueError(syarat_awal)

            def rhs(x, s):
                a = np.exp(x)
                d, dp = s
                return [dp, -(2.0 + dlnH_dlna(a, k)) * dp + 1.5 * omega_m(a, k) * d]

            sol = solve_ivp(rhs, (x0, x1), y0, method="DOP853", rtol=rtol, atol=atol,
                            dense_output=True)
            if not sol.success:
                raise RuntimeError(sol.message)
            self._sol = sol
            self._norm = sol.sol(0.0)[0]
        else:
            g = k.gamma

            def rhs_gamma(x, s):
                return [omega_m(np.exp(x), k) ** g]

            sol = solve_ivp(rhs_gamma, (x0, x1), [np.log(a_awal)], method="DOP853", rtol=rtol,
                            atol=atol, dense_output=True)
            if not sol.success:
                raise RuntimeError(sol.message)
            self._sol = sol
            self._lnnorm = sol.sol(0.0)[0]

    # --- besaran dasar -----------------------------------------------------
    def D(self, a):
        x = np.log(np.asarray(a, dtype=float))
        if self.k.gamma is None:
            return self._sol.sol(x)[0] / self._norm
        return np.exp(self._sol.sol(x)[0] - self._lnnorm)

    def fD(self, a):
        """dD/dln a — pertambahan kontras kerapatan per e-fold (persamaan 8)."""
        a = np.asarray(a, dtype=float)
        if self.k.gamma is None:
            return self._sol.sol(np.log(a))[1] / self._norm
        return omega_m(a, self.k) ** self.k.gamma * self.D(a)

    def f(self, a):
        return self.fD(a) / self.D(a)

    def turunan_fD(self, a):
        """d(fD)/dln a = D''. Untuk RU memakai persamaan (4) secara analitik."""
        a = np.asarray(a, dtype=float)
        k = self.k
        if k.gamma is None:
            return 1.5 * omega_m(a, k) * self.D(a) - (2.0 + dlnH_dlna(a, k)) * self.fD(a)
        # D'' = D (f^2 + f'), f' = gamma f dlnOm/dlna, dlnOm/dlna = -3 - 2 dlnH/dlna
        f = self.f(a)
        dln_om = -3.0 - 2.0 * dlnH_dlna(a, k)
        return self.D(a) * (f**2 + k.gamma * f * dln_om)

    # --- besaran pembanding (§2.6) ------------------------------------------
    def V(self, a):
        """a E f D: amplitudo kecepatan pekuliar linear pada jarak komoving tetap (satuan H0)."""
        a = np.asarray(a, dtype=float)
        return a * E(a, self.k) * self.fD(a)

    def Ddot(self, a):
        """E f D = (dD/dt)/H0: laju pertumbuhan per satuan waktu kosmik."""
        a = np.asarray(a, dtype=float)
        return E(a, self.k) * self.fD(a)


# ---------------------------------------------------------------------------
# Puncak dan penurunan (persamaan 9 dan 11)
# ---------------------------------------------------------------------------
def cari_maksimum(fungsi, a_min: float, a_max: float) -> float:
    """Faktor skala tempat `fungsi(a)` maksimum di [a_min, a_max] (pencarian dalam ln a)."""
    hasil = minimize_scalar(lambda x: -fungsi(np.exp(x)), bounds=(np.log(a_min), np.log(a_max)),
                            method="bounded", options={"xatol": 1e-12, "maxiter": 1000})
    a_pk = float(np.exp(hasil.x))
    if np.isclose(a_pk, a_min, rtol=1e-6) or np.isclose(a_pk, a_max, rtol=1e-6):
        raise ValueError("maksimum berada di tepi rentang pencarian — tidak ada puncak interior")
    return a_pk


def puncak_fD(p: SejarahPertumbuhan, a_rentang=A_PENCARIAN) -> float:
    """a_pk dari persamaan (9): akar d(fD)/dln a = 0, disaring dengan maksimisasi numerik."""
    a_kasar = cari_maksimum(p.fD, *a_rentang)
    try:
        ln_a = brentq(lambda x: p.turunan_fD(np.exp(x)), np.log(a_kasar) - 0.05,
                      np.log(a_kasar) + 0.05, xtol=1e-14)
        return float(np.exp(ln_a))
    except ValueError:
        return a_kasar


def analisis(k: Kosmologi = PLANCK18, a_rentang=A_PENCARIAN, **kwargs) -> dict:
    """Menghitung seluruh angka inti §3 untuk satu kosmologi."""
    p = SejarahPertumbuhan(k, **kwargs)
    t0 = float(waktu_kosmik(1.0, k))

    a_pk = puncak_fD(p, a_rentang)
    fD_max, fD_0 = float(p.fD(a_pk)), float(p.fD(1.0))

    try:
        a_V = cari_maksimum(p.V, 0.1, 3.0)
        V_max, V_0 = float(p.V(a_V)), float(p.V(1.0))
    except ValueError:  # mis. γ ekstrem: V tidak memiliki puncak interior
        a_V, V_max, V_0 = np.nan, np.nan, np.nan

    # Ddot: periksa monoton turun pada 0.05 <= a <= 1
    a_grid = np.geomspace(0.05, 1.0, 2000)
    ddot = p.Ddot(a_grid)
    ddot_monoton = bool(np.all(np.diff(ddot) < 0))

    hasil = {
        "model": k.nama,
        "Om": k.Om, "h": k.h, "w0": k.w0, "wa": k.wa, "gamma": k.gamma,
        "t0_Gyr": t0,
        "f_hari_ini": float(p.f(1.0)),
        "Om_pangkat_055": k.Om ** 0.55,
        "a_pk": a_pk,
        "z_pk": 1.0 / a_pk - 1.0,
        "Om_di_puncak": float(omega_m(a_pk, k)),
        "f_di_puncak": float(p.f(a_pk)),
        "D_di_puncak": float(p.D(a_pk)),
        "t_pk_Gyr": float(waktu_kosmik(a_pk, k)),
        "t_lb_pk_Gyr": t0 - float(waktu_kosmik(a_pk, k)),
        "fD_max": fD_max,
        "fD_hari_ini": fD_0,
        "Delta_fD": 1.0 - fD_0 / fD_max,
        "a_V": a_V,
        "z_V": 1.0 / a_V - 1.0,
        "Om_di_puncak_V": float(omega_m(a_V, k)),
        "t_lb_V_Gyr": t0 - float(waktu_kosmik(a_V, k)) if np.isfinite(a_V) else np.nan,
        "Delta_V": 1.0 - V_0 / V_max,
        "Ddot_monoton_turun": ddot_monoton,
    }
    if k.sigma8 is not None:
        hasil["fsigma8_hari_ini"] = k.sigma8 * fD_0
        hasil["fsigma8_max"] = k.sigma8 * fD_max
    return hasil


def epoch_latar(k: Kosmologi = PLANCK18) -> dict:
    """Epoch acuan latar belakang: awal percepatan (q = 0) dan kesetaraan materi–energi gelap."""
    t0 = float(waktu_kosmik(1.0, k))
    a_acc = float(np.exp(brentq(lambda x: parameter_perlambatan(np.exp(x), k), np.log(0.2), 0.0,
                                xtol=1e-14)))
    a_eq = float(np.exp(brentq(lambda x: omega_m(np.exp(x), k) - 0.5, np.log(0.2), 0.0, xtol=1e-14)))
    return {
        "a_percepatan": a_acc, "z_percepatan": 1 / a_acc - 1,
        "t_lb_percepatan_Gyr": t0 - float(waktu_kosmik(a_acc, k)),
        "Om_di_percepatan": float(omega_m(a_acc, k)),
        "a_setara_materi_DE": a_eq, "z_setara_materi_DE": 1 / a_eq - 1,
        "t_lb_setara_Gyr": t0 - float(waktu_kosmik(a_eq, k)),
    }


if __name__ == "__main__":
    h = analisis(PLANCK18)
    e = epoch_latar(PLANCK18)
    print(f"Model                : {h['model']}")
    print(f"t0                   : {h['t0_Gyr']:.3f} Gyr")
    print(f"f(1)                 : {h['f_hari_ini']:.4f}  (Om^0,55 = {h['Om_pangkat_055']:.4f})")
    print(f"puncak fD            : a = {h['a_pk']:.4f}, z = {h['z_pk']:.4f}, "
          f"t_lb = {h['t_lb_pk_Gyr']:.3f} Gyr, Om(a_pk) = {h['Om_di_puncak']:.4f}")
    print(f"fD_max, fD(1)        : {h['fD_max']:.4f}, {h['fD_hari_ini']:.4f}")
    print(f"Δ_fD                 : {100 * h['Delta_fD']:.2f} %")
    print(f"puncak V = aHfD      : z = {h['z_V']:.4f}, t_lb = {h['t_lb_V_Gyr']:.3f} Gyr, "
          f"Δ_V = {100 * h['Delta_V']:.3f} %")
    print(f"Ddot monoton turun   : {h['Ddot_monoton_turun']}")
    print(f"awal percepatan      : z = {e['z_percepatan']:.4f}, t_lb = {e['t_lb_percepatan_Gyr']:.3f} Gyr")
    print(f"kesetaraan materi–DE : z = {e['z_setara_materi_DE']:.4f}, t_lb = {e['t_lb_setara_Gyr']:.3f} Gyr")
