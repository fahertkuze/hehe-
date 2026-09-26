"""
buat_gambar.py — Gambar 1–5 naskah (PDF vektor + PNG 300 dpi) di ../gambar.

Jalankan jalankan_semua.py lebih dulu: gambar 3 dan 4 membaca hasil/angka_kunci.json.
"""
from __future__ import annotations

import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import ScalarFormatter  # noqa: E402

from modul_A_pertumbuhan import (SejarahPertumbuhan, a_dari_waktu_lihat_balik,  # noqa: E402
                                 omega_m, waktu_kosmik, waktu_lihat_balik)
from modul_D_data_fs8 import DATA, _sigma8_terbaik, vektor_data  # noqa: E402
from parameter import (DESI_W0WA_DESY5, GAMMA_NHW23, PLANCK18,  # noqa: E402
                       PLANCK18_SIGMA_Om, PLANCK18_SIGMA_sigma8)

AKAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FOLDER_GAMBAR = os.path.join(AKAR, "gambar")

# Palet kategorikal tervalidasi (3 slot pertama, lolos semua pasangan CVD)
BIRU, ORANYE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
TINTA, TINTA2, TINTA3 = "#0b0b0b", "#52514e", "#8a8983"
KISI = "#e4e3df"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "axes.labelsize": 8.5,
    "axes.titlesize": 9,
    "axes.edgecolor": TINTA3,
    "axes.labelcolor": TINTA,
    "axes.linewidth": 0.6,
    "axes.grid": True,
    "grid.color": KISI,
    "grid.linewidth": 0.6,
    "grid.linestyle": "-",
    "xtick.color": TINTA2,
    "ytick.color": TINTA2,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "lines.linewidth": 1.6,
    "lines.solid_capstyle": "round",
    "legend.frameon": False,
    "legend.fontsize": 7.5,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "figure.dpi": 110,
})


class FormatKoma(ScalarFormatter):
    """Label sumbu dengan koma desimal (kaidah bahasa Indonesia)."""

    def __call__(self, x, pos=None):
        return super().__call__(x, pos).replace(".", ",")


def simpan(fig, nama):
    for ax in fig.axes:
        for sumbu in (ax.xaxis, ax.yaxis):
            if isinstance(sumbu.get_major_formatter(), ScalarFormatter):
                sumbu.set_major_formatter(FormatKoma())
    os.makedirs(FOLDER_GAMBAR, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FOLDER_GAMBAR, f"{nama}.{ext}"), facecolor="white")
    plt.close(fig)


def sumbu_z_atas(ax, k=PLANCK18, z_ticks=(0, 0.2, 0.5, 1, 2, 5)):
    """Sumbu atas: pergeseran merah yang bersesuaian dengan waktu lihat-balik di sumbu bawah."""
    atas = ax.twiny()
    atas.set_xlim(ax.get_xlim())
    pos = [float(waktu_lihat_balik(1 / (1 + z), k)) for z in z_ticks]
    atas.set_xticks(pos)
    atas.set_xticklabels([f"{z:g}".replace(".", ",") for z in z_ticks])
    atas.set_xlabel("pergeseran merah z", color=TINTA2)
    atas.grid(False)
    atas.tick_params(colors=TINTA2)
    return atas


def koma(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


# ---------------------------------------------------------------------------
def gambar1(h):
    """Sejarah pertumbuhan: D, f, fD terhadap waktu lihat-balik."""
    p = SejarahPertumbuhan(PLANCK18)
    tlb = np.linspace(0.0, 12.5, 600)
    a = np.array([np.exp(a_dari_waktu_lihat_balik(t, PLANCK18)) for t in tlb])

    fig, axs = plt.subplots(3, 1, figsize=(5.6, 6.6), sharex=True,
                            gridspec_kw={"hspace": 0.12})
    # (a) D
    ax = axs[0]
    ax.plot(tlb, a, color=TINTA3, lw=1.1, label="Einstein–de Sitter, D = a")
    ax.plot(tlb, p.D(a), color=BIRU, label="ΛCDM Planck 2018")
    ax.set_ylabel("faktor pertumbuhan D")
    ax.set_ylim(0, 1.05)
    ax.legend(loc="upper right")
    ax.text(0.015, 0.05, "(a)", transform=ax.transAxes, color=TINTA, fontweight="bold")

    # (b) f
    ax = axs[1]
    ax.plot(tlb, p.f(a), color=BIRU, lw=2.4, label="f = dln D / dln a (persamaan 4)")
    ax.plot(tlb, omega_m(a, PLANCK18) ** 0.55, color=ORANYE, lw=1.0,
            label="Ωm(a)$^{0{,}55}$ (Linder 2005)", zorder=4)
    ax.set_ylabel("laju pertumbuhan f")
    ax.set_ylim(0.45, 1.02)
    ax.legend(loc="upper right")
    ax.text(0.015, 0.05, "(b)", transform=ax.transAxes, color=TINTA, fontweight="bold")

    # (c) fD
    ax = axs[2]
    ax.plot(tlb, p.fD(a), color=BIRU)
    t_pk, fD_max, fD_0 = h["t_lb_pk_Gyr"], h["fD_max"], h["fD_hari_ini"]
    ax.axvline(t_pk, color=TINTA3, lw=0.8)
    ax.plot([t_pk], [fD_max], "o", ms=6, color=BIRU, mec="white", mew=1.5, zorder=5)
    ax.plot([0], [fD_0], "o", ms=6, color=BIRU, mec="white", mew=1.5, zorder=5, clip_on=False)
    ax.annotate(f"puncak: z = {koma(h['z_pk'], 3)}\n{koma(t_pk)} Gyr lalu\nf·D = {koma(fD_max, 3)}",
                xy=(t_pk, fD_max), xytext=(t_pk + 3.3, fD_max - 0.1), color=TINTA, fontsize=7.5,
                va="top", arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    ax.annotate(f"kini: f·D = {koma(fD_0, 3)}\n(−{koma(100 * h['Delta_fD'], 1)}% dari puncak)",
                xy=(0, fD_0), xytext=(3.4, 0.36), color=TINTA, fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    ax.set_ylabel("f·D = dD / dln a")
    ax.set_ylim(0.0, 0.66)
    ax.set_xlabel("waktu lihat-balik (Gyr)")
    ax.text(0.015, 0.05, "(c)", transform=ax.transAxes, color=TINTA, fontweight="bold")

    for ax in axs:
        ax.set_xlim(12.5, 0)  # waktu mengalir ke kanan
    sumbu_z_atas(axs[0])
    simpan(fig, "gambar1_sejarah_pertumbuhan")


# ---------------------------------------------------------------------------
def gambar2(h, e):
    """Tiga 'jam': fD, V = aHfD, Ddot = HfD, masing-masing dinormalisasi ke nilai kini."""
    p = SejarahPertumbuhan(PLANCK18)
    tlb = np.linspace(0.0, 10.0, 500)
    a = np.array([np.exp(a_dari_waktu_lihat_balik(t, PLANCK18)) for t in tlb])

    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    kurva = [
        (p.Ddot(a) / p.Ddot(1.0), AQUA, "Ḋ = H f D  (per satuan waktu)"),
        (p.fD(a) / p.fD(1.0), BIRU, "f·D  (per e-fold ekspansi)"),
        (p.V(a) / p.V(1.0), ORANYE, "V = a H f D  (kecepatan pekuliar linear)"),
    ]
    for y, c, lab in kurva:
        ax.plot(tlb, y, color=c, label=lab)
    # penanda epoch latar belakang
    penanda = [
        (e["t_lb_percepatan_Gyr"], f"awal percepatan\nz = {koma(e['z_percepatan'])}"),
        (e["t_lb_setara_Gyr"], f"ρΛ = ρm\nz = {koma(e['z_setara_materi_DE'])}"),
    ]
    for t, lab in penanda:
        ax.axvline(t, color=TINTA3, lw=0.8)
        ax.text(t - 0.1, 0.62, lab, fontsize=7, color=TINTA2, ha="left", va="bottom")
    # puncak
    ax.plot([h["t_lb_pk_Gyr"]], [h["fD_max"] / h["fD_hari_ini"]], "o", ms=6, color=BIRU,
            mec="white", mew=1.5, zorder=5)
    ax.plot([h["t_lb_V_Gyr"]], [1 / (1 - h["Delta_V"])], "o", ms=6, color=ORANYE, mec="white",
            mew=1.5, zorder=5)
    ax.annotate(f"puncak f·D\n{koma(h['t_lb_pk_Gyr'])} Gyr lalu (+{koma(100 * h['Delta_fD'] / (1 - h['Delta_fD']), 1)}%)",
                xy=(h["t_lb_pk_Gyr"], h["fD_max"] / h["fD_hari_ini"]), xytext=(7.4, 1.22),
                fontsize=7.5, color=TINTA, arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    ax.annotate(f"puncak V\n{koma(h['t_lb_V_Gyr'])} Gyr lalu (+{koma(100 * h['Delta_V'] / (1 - h['Delta_V']), 2)}%)",
                xy=(h["t_lb_V_Gyr"], 1 / (1 - h["Delta_V"])), xytext=(3.3, 0.84),
                fontsize=7.5, color=TINTA, arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    ax.set_xlim(10, 0)
    ax.set_ylim(0.6, 1.5)
    ax.set_xlabel("waktu lihat-balik (Gyr)")
    ax.set_ylabel("besaran / nilai hari ini")
    ax.legend(loc="upper left", ncol=1)
    sumbu_z_atas(ax, z_ticks=(0, 0.2, 0.5, 1, 2))
    simpan(fig, "gambar2_tiga_jam")


# ---------------------------------------------------------------------------
def gambar4(hasil):
    """fσ8(z): data RSD/PV dibandingkan kurva σ8·fD."""
    z = np.linspace(0, 1.6, 321)
    a = 1 / (1 + z)
    # pita 68% Planck: sampel Om (h via Om h^3 tetap tidak memengaruhi fD) dan σ8
    rng = np.random.default_rng(1)
    Om_s = rng.normal(PLANCK18.Om, PLANCK18_SIGMA_Om, 300)
    s8_s = rng.normal(PLANCK18.sigma8, PLANCK18_SIGMA_sigma8, 300)
    kurva_s = np.array([s8 * SejarahPertumbuhan(PLANCK18.dengan(Om=om)).fD(a)
                        for om, s8 in zip(Om_s, s8_s)])
    lo, hi = np.percentile(kurva_s, [16, 84], axis=0)

    p_pl = SejarahPertumbuhan(PLANCK18)
    p_desi = SejarahPertumbuhan(DESI_W0WA_DESY5)
    p_g = SejarahPertumbuhan(PLANCK18.dengan(gamma=GAMMA_NHW23))
    fit_g = hasil["data_fs8"]["fit_gamma"]
    fit_om = hasil["data_fs8"]["fit_Om"]

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.fill_between(z, lo, hi, color=BIRU, alpha=0.12, lw=0)
    ax.plot(z, PLANCK18.sigma8 * p_pl.fD(a), color=BIRU, label="ΛCDM Planck 2018 (σ8 = 0,811)")
    # DESI w0wa: σ8 dipilih sama dengan Planck — hanya bentuk kurva yang dibandingkan
    ax.plot(z, PLANCK18.sigma8 * p_desi.fD(a), color=ORANYE, lw=1.2,
            label="w0wa DESI+CMB+DESY5 (σ8 = 0,811)")
    z_data, _ = vektor_data()
    s8_g, _ = _sigma8_terbaik(p_g.fD(1 / (1 + z_data)))
    ax.plot(z, s8_g * p_g.fD(a), color=AQUA, lw=1.2,
            label=f"γ = 0,633 (Nguyen dkk. 2023), σ8 terbaik = {koma(s8_g, 3)}")

    for lab, zi, y, s, jenis, _ in DATA:
        mk = "s" if jenis == "PV" else "o"
        ax.errorbar([zi], [y], yerr=[s], fmt=mk, ms=5, color=TINTA, mfc=TINTA, mec="white",
                    mew=1.0, elinewidth=0.9, capsize=0, zorder=6)
    # label data selektif, diletakkan di luar batang galat dan kurva
    posisi_label = {  # label: (x, y, ha)
        "SN Ia PV × 2M++": (0.0, 0.352, "left"),
        "6dFGS": (0.088, 0.412, "left"),
        "BOSS DR12": (0.445, 0.558, "center"),
        "eBOSS LRG": (0.698, 0.533, "center"),
        "eBOSS ELG": (0.87, 0.315, "left"),
        "eBOSS QSO": (1.48, 0.522, "center"),
    }
    for lab, (x, y, ha) in posisi_label.items():
        ax.text(x, y, lab, fontsize=6.8, color=TINTA2, ha=ha, va="center")
    z_pk = hasil["planck18"]["z_pk"]
    ax.axvline(z_pk, color=TINTA3, lw=0.8)
    ax.text(z_pk + 0.02, 0.215, f"puncak Planck\nz = {koma(z_pk, 3)}", fontsize=7, color=TINTA2)
    zf, s_lo, s_hi = fit_om["z_pk"]["median"], fit_om["z_pk"]["minus"], fit_om["z_pk"]["plus"]
    ax.errorbar([zf], [0.19], xerr=[[s_lo], [s_hi]], fmt="D", ms=4.5, color=TINTA2, mec="white",
                mew=0.8, elinewidth=0.9, capsize=0)
    ax.text(zf + s_hi + 0.03, 0.19, "puncak dari data saja (ΛCDM, Ωm & σ8 bebas)", fontsize=7,
            color=TINTA2, va="center")
    ax.set_xlim(-0.02, 1.6)
    ax.set_ylim(0.15, 0.62)
    ax.set_xlabel("pergeseran merah z")
    ax.set_ylabel("fσ$_8$(z) = σ$_{8,0}$ · f·D")
    ax.legend(loc="upper right", fontsize=7)
    simpan(fig, "gambar4_data_fsigma8")


# ---------------------------------------------------------------------------
def gambar3(hasil):
    """Diagram hutan: z_pk dan Δ_fD untuk semua model dan uji."""
    mc = hasil["ketidakpastian"]["ringkasan"]
    alt = {m["model"]: m for m in hasil["model_alternatif"]}
    camb = hasil["camb"]["camb_mnu006"]
    rad = hasil["radiasi"]
    fom, fg = hasil["data_fs8"]["fit_Om"], hasil["data_fs8"]["fit_gamma"]

    baris = [  # (label, z_pk, (-,+), Δ, (-,+), kelompok)
        ("Planck 2018, persamaan (4)", mc["z_pk"]["median"], (mc["z_pk"]["minus"], mc["z_pk"]["plus"]),
         mc["Delta_fD"]["median"], (mc["Delta_fD"]["minus"], mc["Delta_fD"]["plus"]), 0),
        ("+ radiasi (Meszaros)", rad["z_pk"], None, rad["Delta_fD"], None, 0),
        ("CAMB: baryon, radiasi, Σmν = 0,06 eV", camb["z_pk"], None, camb["Delta_fD"], None, 0),
    ]
    for nama in ["DESI DR2 BAO (ΛCDM)", "DESI DR2 BAO+CMB (ΛCDM)", "DESI+CMB+Pantheon+ (w0wa)",
                 "DESI+CMB+Union3 (w0wa)", "DESI+CMB+DESY5 (w0wa)"]:
        m = alt[nama]
        baris.append((nama, m["z_pk"], None, m["Delta_fD"], None, 1))
    for nama in ["γ = 0,633 (Nguyen dkk. 2023)", "γ = 11/16 (DGP)"]:
        m = alt[nama]
        baris.append((nama, m["z_pk"], None, m["Delta_fD"], None, 2))
    baris.append(("data fσ8: ΛCDM, Ωm & σ8 bebas", fom["z_pk"]["median"],
                  (fom["z_pk"]["minus"], fom["z_pk"]["plus"]), fom["Delta_fD"]["median"],
                  (fom["Delta_fD"]["minus"], fom["Delta_fD"]["plus"]), 3))
    baris.append(("data fσ8: latar Planck, γ & σ8 bebas", fg["z_pk"]["median"],
                  (fg["z_pk"]["minus"], fg["z_pk"]["plus"]), fg["Delta_fD"]["median"],
                  (fg["Delta_fD"]["minus"], fg["Delta_fD"]["plus"]), 3))

    warna = {0: BIRU, 1: ORANYE, 2: AQUA, 3: TINTA}
    n = len(baris)
    y = np.arange(n)[::-1].astype(float)
    # jarak antar kelompok
    for i, b in enumerate(baris):
        y[i] -= 0.6 * b[5]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 3.9), sharey=True,
                                 gridspec_kw={"wspace": 0.06, "width_ratios": [1, 1]})
    for yi, (lab, zp, ze, dl, de, g) in zip(y, baris):
        mk = "D" if g == 3 else "o"
        a1.errorbar([zp], [yi], xerr=None if ze is None else [[ze[0]], [ze[1]]], fmt=mk, ms=5,
                    color=warna[g], mec="white", mew=1.0, elinewidth=1.0, capsize=0)
        a2.errorbar([100 * dl], [yi], xerr=None if de is None else [[100 * de[0]], [100 * de[1]]],
                    fmt=mk, ms=5, color=warna[g], mec="white", mew=1.0, elinewidth=1.0, capsize=0)
    a1.axvline(hasil["planck18"]["z_pk"], color=TINTA3, lw=0.8)
    a2.axvline(100 * hasil["planck18"]["Delta_fD"], color=TINTA3, lw=0.8)
    a1.set_yticks(y)
    a1.set_yticklabels([b[0] for b in baris], fontsize=7.3)
    a1.set_xlabel("pergeseran merah puncak $z_{\\rm pk}$")
    a2.set_xlabel("penurunan sejak puncak $\\Delta_{fD}$ (%)")
    a1.grid(axis="y", visible=False)
    a2.grid(axis="y", visible=False)
    a1.set_xlim(0.3, 0.72)
    a2.set_xlim(4, 25)
    simpan(fig, "gambar3_ketahanan")


# ---------------------------------------------------------------------------
def gambar5(h, mdepan):
    """Masa depan: D/D∞, fD/maks dan V/maks terhadap waktu relatif terhadap kini."""
    p = SejarahPertumbuhan(PLANCK18, a_akhir=1100.0)
    t0 = float(waktu_kosmik(1.0, PLANCK18))
    a = np.geomspace(0.08, 50.0, 700)
    t_rel = waktu_kosmik(a, PLANCK18) - t0
    D_inf = mdepan["D_inf_per_D0"]
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.plot(t_rel, p.D(a) / D_inf, color=TINTA2, lw=1.3, label="D / D∞  (kedalaman linear basin)")
    ax.plot(t_rel, p.fD(a) / h["fD_max"], color=BIRU, label="f·D / maks")
    V_max = p.V(h["a_V"])
    ax.plot(t_rel, p.V(a) / V_max, color=ORANYE, label="V / maks")
    ax.axvline(0, color=TINTA3, lw=0.8)
    ax.text(0.5, 0.05, "kini", fontsize=7.5, color=TINTA2)
    ax.plot([0], [1 / D_inf], "o", ms=5, color=TINTA2, mec="white", mew=1.2, zorder=5)
    ax.annotate(f"kini tercapai {koma(100 / D_inf, 0)}% dari D∞", xy=(0, 1 / D_inf),
                xytext=(1.8, 0.2), fontsize=7.5, color=TINTA,
                arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    t50 = mdepan["t_fD_50persen_Gyr_dari_kini"]
    ax.plot([t50], [0.5], "o", ms=5, color=BIRU, mec="white", mew=1.2, zorder=5)
    ax.annotate(f"f·D = ½ puncak (+{koma(t50, 1)} Gyr)", xy=(t50, 0.5), xytext=(t50 + 3.2, 0.46),
                fontsize=7.5, color=TINTA, arrowprops=dict(arrowstyle="-", color=TINTA3, lw=0.6))
    ax.set_xlim(-11, 40)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("waktu relatif terhadap kini (Gyr)")
    ax.set_ylabel("besaran ternormalisasi")
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.74))
    simpan(fig, "gambar5_masa_depan")


def main():
    with open(os.path.join(AKAR, "hasil", "angka_kunci.json"), encoding="utf-8") as f:
        hasil = json.load(f)
    h, e = hasil["planck18"], hasil["epoch_latar"]
    gambar1(h)
    gambar2(h, e)
    gambar3(hasil)
    gambar4(hasil)
    gambar5(h, hasil["masa_depan"])
    print("Gambar tersimpan di", os.path.normpath(FOLDER_GAMBAR))


if __name__ == "__main__":
    main()
