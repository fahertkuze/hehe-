"""
modul_D_data_fs8.py — perbandingan kurva f·D dengan pengukuran fσ8(z) (naskah §2.8, §3.6).

Dengan normalisasi D(1) = 1, fσ8(z) = σ8,0 · f(z) D(z). Jadi f·D adalah fσ8
yang dibagi σ8 hari ini: data distorsi ruang-pergeseran merah (RSD) dan
kecepatan pekuliar (PV) mengukur bentuk kurva f·D secara langsung.

Sumber data (nilai disalin dari berkas rilis resmi yang didistribusikan di
https://github.com/CobayaSampler/bao_data, commit bb0c1c9, kecuali disebut lain):
  - BOSS DR12 z = 0.38, 0.51 (analisis konsensus seperti dipakai Alam dkk. 2021):
      sdss_DR16_BAOplus_LRG_FSBAO_DMDHfs8.dat + _covtot.txt
  - eBOSS DR16 LRG z = 0.698: berkas yang sama
  - eBOSS DR16 ELG z = 0.845: marginal fσ8 dari sdss_DR16_ELG_FSBAO_DMDHfs8gridlikelihood.txt
      (rerata 0.3147, simpangan baku 0.0960)
  - eBOSS DR16 QSO z = 1.48: sdss_DR16_BAOplus_QSO_FSBAO_DMDHfs8.dat + _covtot.txt
  - 6dFGS z = 0.067 (RSD): Beutler dkk. 2012, fσ8 = 0.423 ± 0.055
  - PV SN Ia × 2M++ (z ≈ 0): Boruah, Hudson & Lavaux 2020, fσ8 = 0.400 ± 0.017
"""
from __future__ import annotations

import numpy as np

from modul_A_pertumbuhan import SejarahPertumbuhan, analisis
from parameter import PLANCK18, Kosmologi

DATA = [
    # (label, z, fσ8, σ, jenis, rujukan)
    ("SN Ia PV × 2M++", 0.0, 0.400, 0.017, "PV", "Boruah dkk. 2020"),
    ("6dFGS", 0.067, 0.423, 0.055, "RSD", "Beutler dkk. 2012"),
    ("BOSS DR12", 0.38, 0.4974, np.sqrt(2.033550e-03), "RSD", "Alam dkk. 2021"),
    ("BOSS DR12", 0.51, 0.4590, np.sqrt(1.422890e-03), "RSD", "Alam dkk. 2021"),
    ("eBOSS LRG", 0.698, 0.4730, np.sqrt(1.961624e-03), "RSD", "Alam dkk. 2021"),
    ("eBOSS ELG", 0.845, 0.3147, 0.0960, "RSD", "Alam dkk. 2021"),
    ("eBOSS QSO", 1.48, 0.4620, np.sqrt(2.019570e-03), "RSD", "Alam dkk. 2021"),
]
# Kovarians silang BOSS z = 0.38 – 0.51 (elemen [2,5] berkas _covtot)
KOV_BOSS_038_051 = 8.118290e-04


def matriks_kovarians() -> np.ndarray:
    s = np.array([d[3] for d in DATA])
    C = np.diag(s**2)
    i, j = 2, 3
    C[i, j] = C[j, i] = KOV_BOSS_038_051
    return C


def vektor_data():
    z = np.array([d[1] for d in DATA])
    y = np.array([d[2] for d in DATA])
    return z, y


def model_fsigma8(z, k: Kosmologi, sigma8: float | None = None, p: SejarahPertumbuhan | None = None):
    p = p or SejarahPertumbuhan(k)
    s8 = k.sigma8 if sigma8 is None else sigma8
    return s8 * p.fD(1.0 / (1.0 + np.asarray(z)))


def chi2(model: np.ndarray) -> float:
    _, y = vektor_data()
    r = y - model
    return float(r @ np.linalg.solve(matriks_kovarians(), r))


def uji_planck() -> dict:
    z, y = vektor_data()
    m = model_fsigma8(z, PLANCK18)
    return {"chi2": chi2(m), "dof": len(y), "model": m.tolist()}


def _sigma8_terbaik(t: np.ndarray) -> tuple[float, float]:
    """σ8 yang meminimalkan χ² untuk templat t (model linear dalam σ8), beserta χ²-nya."""
    _, y = vektor_data()
    Ci = np.linalg.inv(matriks_kovarians())
    s8 = float((t @ Ci @ y) / (t @ Ci @ t))
    return s8, chi2(s8 * t)


def posterior_kisi(parameter: str, nilai: np.ndarray, k_dasar: Kosmologi = PLANCK18,
                   sigma8_kisi: np.ndarray | None = None) -> dict:
    """Posterior kisi 2D (parameter × σ8), prior datar; mengembalikan marginal + turunan.

    parameter = "Om"    : ΛCDM datar, bentuk kurva ditentukan Om
    parameter = "gamma" : latar Planck 2018, f = Om(a)^gamma
    """
    z, _ = vektor_data()
    a_data = 1.0 / (1.0 + z)
    s8 = np.linspace(0.55, 1.10, 441) if sigma8_kisi is None else sigma8_kisi
    Ci = np.linalg.inv(matriks_kovarians())
    _, y = vektor_data()
    lnL = np.empty((len(nilai), len(s8)))
    z_pk = np.empty(len(nilai))
    delta = np.empty(len(nilai))
    for i, v in enumerate(nilai):
        k = k_dasar.dengan(**{parameter: float(v)})
        p = SejarahPertumbuhan(k)
        t = p.fD(a_data)
        R = y[None, :] - s8[:, None] * t[None, :]
        lnL[i] = -0.5 * np.einsum("ij,jk,ik->i", R, Ci, R)
        h = analisis(k, a_rentang=(0.1, 3.0))
        z_pk[i], delta[i] = h["z_pk"], h["Delta_fD"]
    P = np.exp(lnL - lnL.max())
    P /= P.sum()
    marg = P.sum(axis=1)

    def ringkas(x, w):
        idx = np.argsort(x)
        c = np.cumsum(w[idx])
        c /= c[-1]
        p16, p50, p84 = np.interp([0.16, 0.5, 0.84], c, x[idx])
        return {"median": float(p50), "minus": float(p50 - p16), "plus": float(p84 - p50)}

    return {
        "parameter": parameter,
        "nilai": nilai.tolist(),
        "marginal": marg.tolist(),
        parameter: ringkas(nilai, marg),
        "sigma8": ringkas(s8, P.sum(axis=0)),
        "z_pk": ringkas(z_pk, marg),
        "Delta_fD": ringkas(delta, marg),
        "chi2_min": float(-2 * lnL.max()),
        "dof": len(y) - 2,
    }


def rasio_lokal_terhadap_puncak(k: Kosmologi = PLANCK18) -> dict:
    """Uji tanpa σ8: rasio fσ8 lokal (PV, z≈0) terhadap rerata terbobot BOSS (z = 0.38, 0.51)."""
    C = matriks_kovarians()
    _, y = vektor_data()
    # rerata terbobot BOSS dengan kovariansnya
    Cb = C[2:4, 2:4]
    w = np.linalg.solve(Cb, np.ones(2))
    w /= w.sum()
    boss = float(w @ y[2:4])
    s_boss = float(np.sqrt(w @ Cb @ w))
    z_boss = float(w @ np.array([0.38, 0.51]))
    lokal, s_lokal = y[0], np.sqrt(C[0, 0])
    r = lokal / boss
    s_r = r * np.sqrt((s_lokal / lokal) ** 2 + (s_boss / boss) ** 2)
    p = SejarahPertumbuhan(k)
    r_model = float(p.fD(1.0) / (w @ p.fD(1.0 / (1.0 + np.array([0.38, 0.51])))))
    return {"rasio_data": float(r), "sigma": float(s_r), "rasio_model": r_model,
            "z_efektif_boss": z_boss, "fsigma8_boss": boss, "sigma_boss": s_boss,
            "selisih_sigma": float((r_model - r) / s_r)}


if __name__ == "__main__":
    print("χ² Planck:", {k: v for k, v in uji_planck().items() if k != "model"})
    print("Rasio lokal/BOSS:", rasio_lokal_terhadap_puncak())
    pos_om = posterior_kisi("Om", np.linspace(0.12, 0.60, 97))
    print("Fit Om:", {k: v for k, v in pos_om.items() if k not in ("nilai", "marginal")})
    pos_g = posterior_kisi("gamma", np.linspace(0.20, 1.20, 101))
    print("Fit γ :", {k: v for k, v in pos_g.items() if k not in ("nilai", "marginal")})
