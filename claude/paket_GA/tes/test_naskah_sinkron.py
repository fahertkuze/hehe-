"""
Memastikan angka yang dikutip naskah (naskah/makalah_GA_fD.md) sama dengan
hasil perhitungan (hasil/angka_kunci.json). Jalankan setelah jalankan_semua.py:

    python tes/test_naskah_sinkron.py
"""
import json
import os

AKAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def _muat():
    with open(os.path.join(AKAR, "hasil", "angka_kunci.json"), encoding="utf-8") as f:
        hasil = json.load(f)
    with open(os.path.join(AKAR, "naskah", "makalah_GA_fD.md"), encoding="utf-8") as f:
        naskah = f.read()
    # di dalam persamaan LaTeX koma desimal ditulis 0{,}527
    return hasil, naskah.replace("{,}", ",")


def k(x, d):
    """Format desimal koma, seperti di naskah berbahasa Indonesia."""
    return f"{x:.{d}f}".replace(".", ",")


def angka_yang_diharapkan(h):
    p, mc, e = h["planck18"], h["ketidakpastian"]["ringkasan"], h["epoch_latar"]
    alt = {m["model"]: m for m in h["model_alternatif"]}
    camb, rad = h["camb"]["camb_mnu006"], h["radiasi"]
    fom, fg = h["data_fs8"]["fit_Om"], h["data_fs8"]["fit_gamma"]
    md, jam = h["masa_depan"], h["tiga_jam_di_puncak_fD"]
    daftar = [
        k(p["f_hari_ini"], 3), k(p["Om_pangkat_055"], 3), k(p["a_pk"], 3), k(p["z_pk"], 3),
        k(p["t_lb_pk_Gyr"], 2), k(p["t_pk_Gyr"], 2), k(p["fD_max"], 3), k(p["f_di_puncak"], 3),
        k(p["D_di_puncak"], 3), k(100 * p["Delta_fD"], 1), k(p["Om_di_puncak"], 4),
        k(p["z_V"], 3), k(p["t_lb_V_Gyr"], 2), k(100 * p["Delta_V"], 2),
        k(mc["z_pk"]["std"], 3), k(mc["t_lb_pk_Gyr"]["std"], 2), k(100 * mc["Delta_fD"]["std"], 1),
        k(mc["fsigma8_hari_ini"]["median"], 3), k(mc["H0"]["std"], 2),
        k(e["z_percepatan"], 3), k(e["t_lb_percepatan_Gyr"], 2), k(e["z_setara_materi_DE"], 3),
        k(e["t_lb_setara_Gyr"], 2), k(h["rasio_rhoDE_rhom"]["puncak_fD"], 3),
        k(h["rasio_rhoDE_rhom"]["puncak_V"], 2), k(h["Om_di_puncak_pendekatan_Linder"], 4),
        k(h["kepekaan_Om"]["z_pk"], 2), k(h["kepekaan_Om"]["Delta_fD"], 2),
        k(rad["z_pk"], 3), k(100 * rad["Delta_fD"], 2),
        k(camb["z_pk"], 3), k(100 * camb["Delta_fD"], 2), k(camb["fsigma8_0"], 3),
        k(camb["z_pk_persamaan4"], 3), k(100 * camb["Delta_fD_persamaan4"], 2),
        k(fom["Om"]["median"], 3), k(fom["sigma8"]["median"], 3), k(fom["z_pk"]["median"], 2),
        k(fg["gamma"]["median"], 2), k(fg["z_pk"]["median"], 2),
        k(h["data_fs8"]["planck"]["chi2"], 1), k(h["data_fs8"]["rasio_lokal"]["rasio_data"], 2),
        k(md["D_inf_per_D0"], 3), k(md["t_fD_50persen_Gyr_dari_kini"], 1),
        k(md["t_fD_10persen_Gyr_dari_kini"], 1), k(md["t_D_99persen_Gyr_dari_kini"], 1),
        k(100 * (jam["fD_per_kini"] - 1), 1),
    ]
    for nama in ("DESI DR2 BAO (ΛCDM)", "DESI DR2 BAO+CMB (ΛCDM)", "DESI+CMB+Pantheon+ (w0wa)",
                 "DESI+CMB+Union3 (w0wa)", "DESI+CMB+DESY5 (w0wa)", "γ = 0,633 (Nguyen dkk. 2023)",
                 "γ = 11/16 (DGP)", "γ = 0,55 (pendekatan RU)"):
        m = alt[nama]
        daftar += [k(m["z_pk"], 3), k(m["t_lb_pk_Gyr"], 2), k(100 * m["Delta_fD"], 2),
                   k(m["z_V"], 3), k(100 * m["Delta_V"], 2)]
    return daftar


def test_angka_naskah_sama_dengan_hasil():
    hasil, naskah = _muat()
    hilang = [a for a in angka_yang_diharapkan(hasil) if a not in naskah]
    assert not hilang, f"angka tidak ditemukan di naskah: {hilang}"


if __name__ == "__main__":
    test_angka_naskah_sama_dengan_hasil()
    print("LULUS  semua angka kunci di naskah cocok dengan hasil/angka_kunci.json")
