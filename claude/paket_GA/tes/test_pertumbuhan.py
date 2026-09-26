"""
Uji validasi paket GA-f·D. Jalankan dari folder paket_GA:

    python -m pytest tes            # bila pytest terpasang
    python tes/test_pertumbuhan.py  # tanpa pytest
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "kode"))

from modul_A_pertumbuhan import (SejarahPertumbuhan, analisis, epoch_latar,  # noqa: E402
                                 omega_m, waktu_kosmik)
from modul_B_ketahanan import heath_D_f, validasi_heath  # noqa: E402
from modul_E_masa_depan import masa_depan  # noqa: E402
from parameter import PLANCK18  # noqa: E402


def test_einstein_de_sitter():
    """Om = 1: D = a dan f = 1 secara eksak."""
    k = PLANCK18.dengan(Om=1.0)
    p = SejarahPertumbuhan(k)
    a = np.geomspace(0.01, 2.0, 50)
    assert np.allclose(p.D(a), a, rtol=1e-8)
    assert np.allclose(p.f(a), 1.0, rtol=1e-8)
    # umur EdS: t0 = 2 / (3 H0)
    assert np.isclose(waktu_kosmik(1.0, k), 2.0 / 3.0 * k.waktu_hubble_gyr, rtol=1e-8)


def test_heath_lcdm():
    """Persamaan (4) sama dengan solusi integral Heath (1977) untuk ΛCDM."""
    v = validasi_heath(PLANCK18)
    assert v["selisih_maks_D"] < 1e-8
    assert v["selisih_maks_f"] < 1e-8


def test_angka_naskah():
    """Angka yang dikutip di abstrak dan Metode §2.3."""
    h = analisis(PLANCK18)
    assert round(h["f_hari_ini"], 3) == 0.527
    assert round(h["Om_pangkat_055"], 3) == 0.530
    assert abs(h["t_lb_pk_Gyr"] - 4.5) < 0.05
    assert abs(h["Delta_fD"] - 0.10) < 0.005
    assert abs(h["Delta_V"] - 0.0067) < 0.0002
    assert h["Ddot_monoton_turun"]


def test_syarat_puncak():
    """Di a_pk berlaku persamaan (9): d(fD)/dln a = 0, dan fD memang maksimum."""
    p = SejarahPertumbuhan(PLANCK18)
    h = analisis(PLANCK18)
    a = h["a_pk"]
    assert abs(p.turunan_fD(a)) < 1e-10
    assert p.fD(a) > p.fD(a * 1.01) and p.fD(a) > p.fD(a / 1.01)


def test_puncak_universal_lcdm():
    """Untuk ΛCDM datar, Om(a_pk) tidak bergantung pada Om hari ini."""
    nilai = [analisis(PLANCK18.dengan(Om=om))["Om_di_puncak"] for om in (0.25, 0.30, 0.35)]
    assert np.ptp(nilai) < 1e-7
    assert abs(nilai[0] - 0.5619) < 1e-4


def test_epoch_latar():
    """Awal percepatan pada Om(a) = 2/3 dan kesetaraan pada Om(a) = 1/2."""
    e = epoch_latar(PLANCK18)
    assert np.isclose(omega_m(e["a_percepatan"], PLANCK18), 2.0 / 3.0, atol=1e-10)
    a_eq_analitik = (PLANCK18.Om / PLANCK18.Ode) ** (1 / 3)
    assert np.isclose(e["a_setara_materi_DE"], a_eq_analitik, rtol=1e-10)


def test_masa_depan_heath():
    """D_∞/D_0 dari integrasi ODE cocok dengan integral Heath pada a = 1000."""
    D_h, _ = heath_D_f(np.array([1000.0]), PLANCK18)
    assert np.isclose(masa_depan(PLANCK18)["D_inf_per_D0"], D_h[0], rtol=1e-6)


if __name__ == "__main__":
    uji = [v for n, v in sorted(globals().items()) if n.startswith("test_")]
    for fungsi in uji:
        fungsi()
        print(f"LULUS  {fungsi.__name__}")
    print(f"{len(uji)} uji lulus")
