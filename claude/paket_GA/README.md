# Paket GA-f·D: sejarah pertumbuhan linear basin Great Attractor

Paket ini berisi naskah makalah, kode, hasil numerik, dan gambar untuk penelitian
*"Puncak dan Perlambatan Pertumbuhan Struktur di Basin Great Attractor: Sejarah Laju
Pertumbuhan Linear f·D dalam Kosmologi ΛCDM"*. Setiap angka, tabel, dan gambar dalam
naskah dapat direproduksi dari kode di sini.

## Isi

```
paket_GA/
├── naskah/
│   ├── makalah_GA_fD.md      ← naskah induk (Markdown + LaTeX)
│   ├── makalah_GA_fD.pdf     ← hasil bangun (XeLaTeX)
│   ├── makalah_GA_fD.docx    ← hasil bangun (Word)
│   ├── bangun_naskah.py      ← Markdown → PDF & DOCX
│   └── CATATAN_REVISI.md     ← apa yang diubah/ditambahkan dan hal yang perlu dicek penulis
├── kode/
│   ├── parameter.py              kosmologi Planck 2018, DESI DR2, indeks pertumbuhan γ
│   ├── modul_A_pertumbuhan.py    persamaan (1)–(14): D, f, f·D, V = aHfD, Ḋ, puncak, waktu
│   ├── modul_B_ketahanan.py      validasi Heath, konvergensi, radiasi, CAMB, model alternatif
│   ├── modul_C_ketidakpastian.py Monte Carlo parameter Planck
│   ├── modul_D_data_fs8.py       data fσ8 (RSD + kecepatan pekuliar), χ², posterior kisi
│   ├── modul_E_masa_depan.py     D∞, waktu pembekuan pertumbuhan
│   ├── jalankan_semua.py         menjalankan semuanya → hasil/
│   └── buat_gambar.py            Gambar 1–5 → gambar/
├── hasil/
│   ├── angka_kunci.json          semua angka yang dikutip naskah
│   ├── tabel_model.csv, tabel_data_fs8.csv, kurva_pertumbuhan.csv
├── gambar/                       gambar1…gambar5 (.pdf vektor dan .png 300 dpi)
└── tes/
    ├── test_pertumbuhan.py       7 uji validasi fisika/numerik
    └── test_naskah_sinkron.py    angka di naskah = angka di hasil/angka_kunci.json
```

## Menjalankan

```bash
pip install -r requirements.txt       # numpy, scipy, matplotlib, camb (+ pypandoc_binary untuk naskah)
cd kode
python modul_A_pertumbuhan.py         # angka inti, < 1 detik
python jalankan_semua.py              # seluruh analisis, ± 20 detik
python buat_gambar.py                 # Gambar 1–5, ± 40 detik
cd ..
python tes/test_pertumbuhan.py        # 7 uji validasi
python tes/test_naskah_sinkron.py     # cek angka naskah
python naskah/bangun_naskah.py        # PDF (butuh XeLaTeX) dan DOCX
```

CAMB hanya dipakai untuk cek silang Boltzmann (§3.4); bila tidak terpasang, hapus
pemanggilan `cek_silang_camb()` di `jalankan_semua.py`.

## Hasil utama (Planck 2018)

| Besaran | Nilai |
|:--|:--|
| f(1) | 0,527 (pendekatan Ωm^0,55 = 0,530) |
| Puncak f·D | z = 0,408 ± 0,016, 4,49 ± 0,10 Gyr lalu |
| Ωm(a) saat puncak | 0,5619, sama untuk setiap ΛCDM datar (ρΛ/ρm = 0,78) |
| Penurunan f·D sejak puncak | 10,2 ± 0,6 % |
| Puncak V = aHfD | z = 0,138, 1,82 Gyr lalu; penurunan 0,67 % |
| Ḋ = HfD | turun monoton, tanpa puncak |
| Cek silang CAMB (Σmν = 0,06 eV) | z_pk = 0,409, Δ = 10,27 % |
| DESI DR2 (5 kosmologi) | z_pk = 0,435–0,473, Δ = 6,7–11,8 % |
| Data fσ8 saja (ΛCDM) | z_pk = 0,56 ± 0,10, Δ = 17 ± 4 % |
| Sisa pertumbuhan linear | D∞/D0 = 1,408 (71 % sudah tercapai) |

## Sumber data

Parameter kosmologi: Planck Collaboration (2020); DESI Collaboration (2025).
Data fσ8: Boruah dkk. (2020), Beutler dkk. (2012), Alam dkk. (2017, 2021). Nilai
BOSS/eBOSS dan kovariansnya disalin dari berkas rilis resmi SDSS sebagaimana
didistribusikan di <https://github.com/CobayaSampler/bao_data> (commit `bb0c1c9`);
rinciannya ada di docstring `kode/modul_D_data_fs8.py`.
