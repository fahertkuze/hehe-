"""
modul_E_masa_depan.py — ke mana pertumbuhan linear basin menuju (naskah §3.5).

Dalam era dominasi energi gelap D(a) mendekati konstanta D_∞ dan f → 0, sehingga
pertumbuhan kontras kerapatan di lingkungan basin membeku. Modul ini menghitung
D_∞/D_0, waktu (dari sekarang) ketika f·D turun ke fraksi tertentu dari puncaknya,
dan kapan D mencapai 99% dari nilai akhirnya.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq

from modul_A_pertumbuhan import SejarahPertumbuhan, puncak_fD, waktu_kosmik
from parameter import PLANCK18, Kosmologi

A_JAUH = 1.0e3  # a = 1000: D sudah konvergen (koreksi ~ a^-3)


def masa_depan(k: Kosmologi = PLANCK18) -> dict:
    p = SejarahPertumbuhan(k, a_akhir=A_JAUH * 1.01)
    t0 = float(waktu_kosmik(1.0, k))
    D_inf = float(p.D(A_JAUH))
    a_pk = puncak_fD(p)
    fD_max = float(p.fD(a_pk))

    def waktu_saat(fungsi, target, a_lo=1.0, a_hi=A_JAUH):
        ln_a = brentq(lambda x: fungsi(np.exp(x)) - target, np.log(a_lo), np.log(a_hi), xtol=1e-12)
        return float(waktu_kosmik(np.exp(ln_a), k)) - t0, float(np.exp(ln_a))

    t_fD50, a_fD50 = waktu_saat(p.fD, 0.5 * fD_max)
    t_fD10, a_fD10 = waktu_saat(p.fD, 0.1 * fD_max)
    t_D99, a_D99 = waktu_saat(p.D, 0.99 * D_inf)
    return {
        "D_inf_per_D0": D_inf,
        "sisa_pertumbuhan": D_inf - 1.0,
        "fraksi_tercapai_hari_ini": 1.0 / D_inf,
        "fraksi_tercapai_di_puncak": float(p.D(a_pk)) / D_inf,
        "t_fD_50persen_Gyr_dari_kini": t_fD50, "a_fD_50persen": a_fD50,
        "t_fD_10persen_Gyr_dari_kini": t_fD10, "a_fD_10persen": a_fD10,
        "t_D_99persen_Gyr_dari_kini": t_D99, "a_D_99persen": a_D99,
    }


if __name__ == "__main__":
    for k, v in masa_depan().items():
        print(f"{k:30s} {v:.4f}")
