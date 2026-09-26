"""
jalankan_semua.py — menjalankan seluruh analisis dan menyimpan hasilnya.

    python jalankan_semua.py            # ± 30 detik

Keluaran (folder ../hasil):
    angka_kunci.json           semua angka yang dikutip di naskah
    tabel_model.csv            Tabel 3 naskah (kosmologi alternatif dan γ)
    tabel_data_fs8.csv         Tabel 4 naskah (kompilasi fσ8)
    kurva_pertumbuhan.csv      D, f, fD, V, Ddot terhadap z dan t_lb (Planck 2018)
Gambar dibuat terpisah oleh buat_gambar.py.
"""
from __future__ import annotations

import csv
import json
import os
import platform

import numpy as np
import scipy

from modul_A_pertumbuhan import (SejarahPertumbuhan, analisis, epoch_latar, omega_m,
                                 waktu_lihat_balik)
from modul_B_ketahanan import (cek_silang_camb, dengan_radiasi, konvergensi_numerik,
                               kosmologi_alternatif, validasi_heath)
from modul_C_ketidakpastian import kisi_Om, monte_carlo, turunan_terhadap_Om
from modul_D_data_fs8 import DATA, posterior_kisi, rasio_lokal_terhadap_puncak, uji_planck
from modul_E_masa_depan import masa_depan
from parameter import MODEL_DESI, PLANCK18

FOLDER_HASIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hasil")


def _bersih(x):
    """Ubah tipe numpy menjadi tipe JSON biasa."""
    if isinstance(x, dict):
        return {k: _bersih(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_bersih(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if not np.isfinite(x) else float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    return x


def main():
    os.makedirs(FOLDER_HASIL, exist_ok=True)
    hasil = {}

    print("1/7 model fiducial ...")
    hasil["planck18"] = analisis(PLANCK18)
    hasil["epoch_latar"] = epoch_latar(PLANCK18)
    # nilai tiga "jam" pada epoch puncak f·D, relatif terhadap hari ini (§3.3)
    p = SejarahPertumbuhan(PLANCK18)
    a_pk = hasil["planck18"]["a_pk"]
    hasil["tiga_jam_di_puncak_fD"] = {
        "fD_per_kini": float(p.fD(a_pk) / p.fD(1.0)),
        "V_per_kini": float(p.V(a_pk) / p.V(1.0)),
        "Ddot_per_kini": float(p.Ddot(a_pk) / p.Ddot(1.0)),
        "Ddot_EdS_per_kini": float(a_pk ** -0.5),
    }

    print("2/7 validasi numerik ...")
    hasil["validasi_heath"] = validasi_heath(PLANCK18)
    konv = konvergensi_numerik(PLANCK18)
    hasil["konvergensi"] = {
        "rentang_z_pk": float(np.ptp([b["z_pk"] for b in konv])),
        "rentang_Delta_fD": float(np.ptp([b["Delta_fD"] for b in konv])),
        "rincian": konv,
    }
    hasil["radiasi"] = dengan_radiasi(PLANCK18)

    print("3/7 cek silang CAMB ...")
    hasil["camb"] = cek_silang_camb()

    print("4/7 ketidakpastian Planck ...")
    tabel = kisi_Om()
    hasil["ketidakpastian"] = monte_carlo(tabel=tabel)
    hasil["kepekaan_Om"] = turunan_terhadap_Om(tabel)
    hasil["Om_di_puncak_universal"] = {
        "min": float(np.min(tabel["Om_di_puncak"])), "maks": float(np.max(tabel["Om_di_puncak"])),
        "rentang_Om0": [float(tabel["Om"][0]), float(tabel["Om"][-1])],
    }
    x_pk = hasil["planck18"]["Om_di_puncak"]
    x_V = hasil["planck18"]["Om_di_puncak_V"]
    hasil["rasio_rhoDE_rhom"] = {
        "puncak_fD": (1 - x_pk) / x_pk,
        "puncak_V": (1 - x_V) / x_V,
        "awal_percepatan": 0.5,
        "kesetaraan": 1.0,
    }
    # pendekatan Linder: 1.5 x^(1-γ) + 1.5 x = 2 dengan γ = 0.55
    from scipy.optimize import brentq
    hasil["Om_di_puncak_pendekatan_Linder"] = brentq(
        lambda x: 1.5 * x**0.45 + 1.5 * x - 2.0, 0.3, 0.9)
    hasil["Om_di_puncak_V_pendekatan_Linder"] = 1.5 ** (-1 / 0.45)

    print("5/7 kosmologi alternatif ...")
    alternatif = kosmologi_alternatif()
    hasil["model_alternatif"] = alternatif

    print("6/7 data fσ8 ...")
    hasil["data_fs8"] = {
        "planck": {k: v for k, v in uji_planck().items() if k != "model"},
        "rasio_lokal": rasio_lokal_terhadap_puncak(PLANCK18),
        "fit_Om": posterior_kisi("Om", np.linspace(0.12, 0.60, 97)),
        "fit_gamma": posterior_kisi("gamma", np.linspace(0.20, 1.20, 101)),
    }

    print("7/7 masa depan ...")
    hasil["masa_depan"] = masa_depan(PLANCK18)

    hasil["lingkungan"] = {"python": platform.python_version(), "numpy": np.__version__,
                           "scipy": scipy.__version__}
    try:
        import camb
        hasil["lingkungan"]["camb"] = camb.__version__
    except ImportError:
        pass

    with open(os.path.join(FOLDER_HASIL, "angka_kunci.json"), "w", encoding="utf-8") as f:
        json.dump(_bersih(hasil), f, ensure_ascii=False, indent=1)

    # --- Tabel model ---------------------------------------------------------
    with open(os.path.join(FOLDER_HASIL, "tabel_model.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["model", "Om", "w0", "wa", "gamma", "z_pk", "t_lb_pk_Gyr", "Delta_fD_persen",
                    "z_V", "Delta_V_persen", "f_hari_ini"])
        for h in alternatif:
            w.writerow([h["model"], f"{h['Om']:.4f}", f"{h['w0']:.3f}", f"{h['wa']:.2f}",
                        "" if h["gamma"] is None else f"{h['gamma']:.4f}",
                        f"{h['z_pk']:.3f}", f"{h['t_lb_pk_Gyr']:.2f}", f"{100 * h['Delta_fD']:.2f}",
                        f"{h['z_V']:.3f}", f"{100 * h['Delta_V']:.2f}", f"{h['f_hari_ini']:.4f}"])

    # --- Tabel data ----------------------------------------------------------
    with open(os.path.join(FOLDER_HASIL, "tabel_data_fs8.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["survei", "z", "fsigma8", "sigma", "jenis", "rujukan"])
        for d in DATA:
            w.writerow([d[0], d[1], f"{d[2]:.4f}", f"{d[3]:.4f}", d[4], d[5]])

    # --- Kurva ---------------------------------------------------------------
    p = SejarahPertumbuhan(PLANCK18)
    z = np.round(np.concatenate([np.linspace(0, 2, 201), np.linspace(2.05, 10, 160)]), 4)
    a = 1 / (1 + z)
    t_lb = waktu_lihat_balik(a, PLANCK18)
    with open(os.path.join(FOLDER_HASIL, "kurva_pertumbuhan.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["z", "a", "t_lb_Gyr", "Om_a", "D", "f", "fD", "V_aHfD_per_H0", "Ddot_per_H0"])
        for zi, ai, ti in zip(z, a, t_lb):
            w.writerow([f"{zi:.4f}", f"{ai:.6f}", f"{ti:.4f}", f"{omega_m(ai, PLANCK18):.6f}",
                        f"{p.D(ai):.6f}", f"{p.f(ai):.6f}", f"{p.fD(ai):.6f}", f"{p.V(ai):.6f}",
                        f"{p.Ddot(ai):.6f}"])
    print("Selesai. Hasil di", os.path.normpath(FOLDER_HASIL))
    print("DESI:", [m.nama for m in MODEL_DESI])


if __name__ == "__main__":
    main()
