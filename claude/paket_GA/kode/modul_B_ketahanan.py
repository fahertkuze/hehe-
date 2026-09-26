"""
modul_B_ketahanan.py — uji ketahanan hasil f·D (naskah §2.6–2.8 dan §3.4).

Isi:
  1. validasi numerik: integral Heath (1977), toleransi, faktor skala awal;
  2. radiasi dalam latar belakang (mode tumbuh Meszaros);
  3. cek silang Boltzmann penuh dengan CAMB (baryon, radiasi, neutrino masif);
  4. kosmologi alternatif DESI DR2 dan indeks pertumbuhan γ.

Besaran pembanding V = aHfD dan Ddot = HfD dihitung langsung oleh
modul_A_pertumbuhan.analisis().
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

from modul_A_pertumbuhan import E, SejarahPertumbuhan, analisis, dlnH_dlna
from parameter import MODEL_DESI, MODEL_GAMMA, OMEGA_R_h2, PLANCK18, Kosmologi


# ---------------------------------------------------------------------------
# 1. Validasi terhadap solusi integral eksak (Heath 1977)
# ---------------------------------------------------------------------------
def heath_D_f(a, k: Kosmologi):
    """D(a) ∝ E(a) ∫_0^a da'/(a' E)^3 dan f = dlnH/dlna + 1/(a^2 E^3 I); eksak untuk ΛCDM."""
    def I(x):
        return quad(lambda s: 1.0 / (s * E(s, k)) ** 3, 0.0, x, epsabs=0, epsrel=1e-13, limit=400)[0]
    I1 = I(1.0)
    a = np.atleast_1d(a)
    Ia = np.array([I(ai) for ai in a])
    D = E(a, k) * Ia / (E(1.0, k) * I1)
    f = dlnH_dlna(a, k) + 1.0 / (a**2 * E(a, k) ** 3 * Ia)
    return D, f


def validasi_heath(k: Kosmologi = PLANCK18) -> dict:
    p = SejarahPertumbuhan(k)
    a = np.geomspace(0.05, 1.0, 60)
    D_h, f_h = heath_D_f(a, k)
    return {
        "selisih_maks_D": float(np.max(np.abs(p.D(a) / D_h - 1))),
        "selisih_maks_f": float(np.max(np.abs(p.f(a) / f_h - 1))),
    }


def konvergensi_numerik(k: Kosmologi = PLANCK18) -> list[dict]:
    baris = []
    for a_awal in (1e-4, 1e-3, 1e-2):
        for rtol in (1e-8, 1e-10, 1e-12):
            h = analisis(k, a_awal=a_awal, rtol=rtol)
            baris.append({"a_awal": a_awal, "rtol": rtol, "z_pk": h["z_pk"],
                          "Delta_fD": h["Delta_fD"], "f_hari_ini": h["f_hari_ini"]})
    return baris


# ---------------------------------------------------------------------------
# 2. Radiasi
# ---------------------------------------------------------------------------
def dengan_radiasi(k: Kosmologi = PLANCK18) -> dict:
    Or = OMEGA_R_h2 / k.h**2
    kr = k.dengan(nama=k.nama + " + radiasi", Or=Or)
    h = analisis(kr, a_awal=1e-6, syarat_awal="meszaros")
    h["Or"] = Or
    return h


# ---------------------------------------------------------------------------
# 3. Cek silang Boltzmann penuh (CAMB; Lewis, Challinor & Lasenby 2000)
# ---------------------------------------------------------------------------
# Parameter dasar Planck 2018, TT,TE,EE+lowE+lensing (Planck Collaboration 2020, Tabel 2)
CAMB_PLANCK18 = dict(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, omk=0.0,
                     tau=0.0544, As=np.exp(3.044) * 1e-10, ns=0.9649)


def fsigma8_camb(z: np.ndarray, **ubah):
    """fσ8(z) dan σ8(z) dari CAMB; mengembalikan juga Om efektif (CDM+baryon+ν)."""
    import camb

    par = dict(CAMB_PLANCK18)
    par.update(ubah)
    pars = camb.set_params(H0=par["H0"], ombh2=par["ombh2"], omch2=par["omch2"], mnu=par["mnu"],
                           omk=par["omk"], tau=par["tau"], As=par["As"], ns=par["ns"],
                           WantTransfer=True)
    pars.set_matter_power(redshifts=list(np.sort(z)[::-1]), kmax=2.0)
    hasil = camb.get_results(pars)
    fs8 = np.array(hasil.get_fsigma8())[::-1]      # CAMB: urutan z menurun -> dibalik
    s8 = np.array(hasil.get_sigma8())[::-1]
    z_urut = np.sort(z)
    h = par["H0"] / 100
    Om = (par["ombh2"] + par["omch2"] + hasil.get_Omega("nu") * h**2) / h**2
    return z_urut, fs8, s8, float(Om)


def cek_silang_camb() -> dict:
    """Puncak fσ8(z)/σ8,0 dari CAMB dibandingkan dengan persamaan (4)."""
    z = np.round(np.linspace(0.0, 1.2, 121), 4)
    keluaran = {}
    for label, ubah in (("camb_mnu006", {}), ("camb_mnu0", {"mnu": 0.0})):
        zz, fs8, s8, Om = fsigma8_camb(z, **ubah)
        # Puncak dari spline kubik pada ln a
        x = np.log(1.0 / (1.0 + zz))[::-1]
        y = (fs8 / s8[0])[::-1]
        cs = CubicSpline(x, y)
        xf = np.linspace(x[0], x[-1], 200001)
        i = np.argmax(cs(xf))
        a_pk = float(np.exp(xf[i]))
        keluaran[label] = {
            "Om_efektif": Om,
            "sigma8_0": float(s8[0]),
            "fsigma8_0": float(fs8[0]),
            "z_pk": 1.0 / a_pk - 1.0,
            "Delta_fD": float(1.0 - fs8[0] / (s8[0] * cs(xf[i]))),
            "kurva_z": zz.tolist(),
            "kurva_fsigma8": fs8.tolist(),
        }
        # Persamaan (4) dengan Om dan h yang sama (dan radiasi) sebagai pembanding
        k_eq4 = PLANCK18.dengan(Om=Om, h=CAMB_PLANCK18["H0"] / 100)
        h4 = analisis(k_eq4)
        keluaran[label]["z_pk_persamaan4"] = h4["z_pk"]
        keluaran[label]["Delta_fD_persamaan4"] = h4["Delta_fD"]
    return keluaran


# ---------------------------------------------------------------------------
# 4. Kosmologi alternatif dan indeks pertumbuhan
# ---------------------------------------------------------------------------
def kosmologi_alternatif() -> list[dict]:
    return [analisis(k) for k in [PLANCK18] + MODEL_DESI + MODEL_GAMMA]


if __name__ == "__main__":
    print("Validasi Heath:", validasi_heath())
    for b in konvergensi_numerik():
        print(b)
    r = dengan_radiasi()
    print(f"+radiasi: Or = {r['Or']:.3e}, z_pk = {r['z_pk']:.4f}, Δ = {100 * r['Delta_fD']:.3f} %, "
          f"f(1) = {r['f_hari_ini']:.4f}")
    for kunci, nilai in cek_silang_camb().items():
        print(kunci, {k: v for k, v in nilai.items() if not k.startswith("kurva")})
    for h in kosmologi_alternatif():
        print(f"{h['model']:32s} z_pk = {h['z_pk']:.3f}  t_lb = {h['t_lb_pk_Gyr']:.2f} Gyr  "
              f"Δ = {100 * h['Delta_fD']:.2f} %  z_V = {h['z_V']:.3f}  Δ_V = {100 * h['Delta_V']:.2f} %")
