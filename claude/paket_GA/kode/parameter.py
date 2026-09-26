"""
parameter.py — parameter kosmologi dan konstanta untuk paket GA-f·D.

Semua model datar. Kolom `Or` (radiasi) bernilai nol pada model fiducial,
sesuai persamaan (1) naskah; radiasi hanya dinyalakan pada uji ketahanan
(modul_B_ketahanan.py).

Sumber setiap angka dicantumkan di samping nilainya.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

# ---------------------------------------------------------------------------
# Konstanta
# ---------------------------------------------------------------------------
# 1/H0 dalam Gyr untuk H0 = 100 h km/s/Mpc:
#   1 Mpc = 3.0856775814913673e19 km, 1 Gyr (Julian) = 3.15576e16 s
MPC_KM = 3.0856775814913673e19
GYR_S = 3.15576e16
WAKTU_HUBBLE_GYR_PER_h = MPC_KM / 100.0 / GYR_S  # = 9.7779... Gyr / h

# Batas bawah integrasi pertumbuhan (persamaan 5 naskah)
A_AWAL = 1.0e-3
# Toleransi relatif integrator (naskah §2.2)
RTOL = 1.0e-10
ATOL = 1.0e-14
# Rentang pencarian puncak (naskah §2.4)
A_PENCARIAN = (0.2, 1.2)


@dataclass(frozen=True)
class Kosmologi:
    """Model latar datar: materi + radiasi + energi gelap CPL (w0, wa)."""

    nama: str
    Om: float                 # parameter kerapatan materi hari ini
    h: float                  # H0 / (100 km/s/Mpc)
    w0: float = -1.0          # w(a) = w0 + wa (1 - a)  (Chevallier & Polarski 2001; Linder 2003)
    wa: float = 0.0
    Or: float = 0.0           # radiasi (fiducial: diabaikan, persamaan 1)
    sigma8: float | None = None
    gamma: float | None = None  # None = relativitas umum (persamaan 4); angka = f = Om(a)^gamma
    sumber: str = ""

    @property
    def Ode(self) -> float:
        return 1.0 - self.Om - self.Or

    @property
    def waktu_hubble_gyr(self) -> float:
        return WAKTU_HUBBLE_GYR_PER_h / self.h

    def dengan(self, **ubah) -> "Kosmologi":
        return replace(self, **ubah)


# ---------------------------------------------------------------------------
# Model fiducial: Planck 2018 (TT,TE,EE+lowE+lensing), dibulatkan seperti
# pada abstrak Planck Collaboration (2020): Om = 0.315 ± 0.007,
# H0 = 67.4 ± 0.5 km/s/Mpc, sigma8 = 0.811 ± 0.006.
# ---------------------------------------------------------------------------
PLANCK18 = Kosmologi(
    nama="Planck 2018 (ΛCDM)",
    Om=0.315,
    h=0.674,
    sigma8=0.811,
    sumber="Planck Collaboration 2020, A&A 641, A6 (TT,TE,EE+lowE+lensing)",
)

# Ketidakpastian 1σ Planck 2018 (Tabel 2, TT,TE,EE+lowE+lensing):
# Om = 0.3153 ± 0.0073, H0 = 67.36 ± 0.54, sigma8 = 0.8111 ± 0.0060
PLANCK18_SIGMA_Om = 0.0073
PLANCK18_SIGMA_H0 = 0.54
PLANCK18_SIGMA_sigma8 = 0.0060

# Kerapatan radiasi (foton + 3,046 neutrino tak bermassa), untuk uji ketahanan:
# Omega_gamma h^2 = 2.47e-5 (T_CMB = 2.7255 K), faktor neutrino 1 + 0.2271*3.046
OMEGA_R_h2 = 2.47e-5 * (1.0 + 0.2271 * 3.046)

# ---------------------------------------------------------------------------
# DESI DR2 (DESI Collaboration 2025, Phys. Rev. D 112, 083515; arXiv:2503.14738)
# ---------------------------------------------------------------------------
# Kerapatan materi fisis dari CMB, dipakai untuk menurunkan h pada model DESI
# yang H0-nya tidak kami kutip: h = sqrt(OMEGA_M_h2 / Om). Waktu lihat-balik
# hanya berskala 1/h, sehingga pilihan ini tidak memengaruhi z_pk maupun Δ.
OMEGA_M_h2_CMB = 0.1430  # Planck 2018: Omega_m h^2 = 0.1430 ± 0.0011


def _h_dari_omh2(Om: float) -> float:
    return (OMEGA_M_h2_CMB / Om) ** 0.5


DESI_BAO_LCDM = Kosmologi(
    nama="DESI DR2 BAO (ΛCDM)",
    Om=0.2975,
    h=_h_dari_omh2(0.2975),
    sumber="DESI Collaboration 2025: Om = 0.2975 ± 0.0086 (BAO saja)",
)
DESI_CMB_LCDM = Kosmologi(
    nama="DESI DR2 BAO+CMB (ΛCDM)",
    Om=0.3027,
    h=0.6817,
    sumber="DESI Collaboration 2025: Om = 0.3027 ± 0.0036, H0 = 68.17 ± 0.28",
)
DESI_W0WA_PANTHEON = Kosmologi(
    nama="DESI+CMB+Pantheon+ (w0wa)",
    Om=0.3114,
    h=_h_dari_omh2(0.3114),
    w0=-0.838,
    wa=-0.62,
    sumber="DESI Collaboration 2025: w0 = -0.838 ± 0.055, wa = -0.62 (+0.22 -0.19)",
)
DESI_W0WA_UNION3 = Kosmologi(
    nama="DESI+CMB+Union3 (w0wa)",
    Om=0.3275,
    h=_h_dari_omh2(0.3275),
    w0=-0.667,
    wa=-1.09,
    sumber="DESI Collaboration 2025: w0 = -0.667 ± 0.088, wa = -1.09 (+0.31 -0.27)",
)
DESI_W0WA_DESY5 = Kosmologi(
    nama="DESI+CMB+DESY5 (w0wa)",
    Om=0.3191,
    h=_h_dari_omh2(0.3191),
    w0=-0.752,
    wa=-0.86,
    sumber="DESI Collaboration 2025: w0 = -0.752 ± 0.057, wa = -0.86 (+0.23 -0.20)",
)

MODEL_DESI = [
    DESI_BAO_LCDM,
    DESI_CMB_LCDM,
    DESI_W0WA_PANTHEON,
    DESI_W0WA_UNION3,
    DESI_W0WA_DESY5,
]

# ---------------------------------------------------------------------------
# Indeks pertumbuhan (latar Planck 2018), f = Om(a)^gamma
# ---------------------------------------------------------------------------
GAMMA_GR = 0.55          # Linder 2005 (pendekatan RU untuk ΛCDM)
GAMMA_NHW23 = 0.633      # Nguyen, Huterer & Wen 2023: 0.633 (+0.025 -0.024)
GAMMA_DGP = 11.0 / 16.0  # Linder & Cahn 2007 (gravitasi DGP)

MODEL_GAMMA = [
    PLANCK18.dengan(nama="γ = 0,55 (pendekatan RU)", gamma=GAMMA_GR),
    PLANCK18.dengan(nama="γ = 0,633 (Nguyen dkk. 2023)", gamma=GAMMA_NHW23),
    PLANCK18.dengan(nama="γ = 11/16 (DGP)", gamma=GAMMA_DGP),
]

# ---------------------------------------------------------------------------
# Great Attractor (untuk diskusi rezim linear, §4)
# ---------------------------------------------------------------------------
# Gugus Norma (ACO 3627), Woudt dkk. 2008: kecepatan rerata 4871 ± 54 km/s,
# dispersi kecepatan 925 km/s.
NORMA_CZ_KMS = 4871.0
NORMA_SIGMA_V_KMS = 925.0
