# Situs Pribadi, CV & Arsip Penelitian

Situs statis (tampilan berbahasa Inggris) untuk **membangun profil pribadi**, menampilkan **CV**, dan **menyimpan arsip
penelitian** (makalah, dataset, poster, tesis, dll.) yang bisa dibaca, diunduh, dibagikan,
dan disitasi oleh publik. Dibangun dengan Jekyll sehingga bisa di-hosting **gratis di
GitHub Pages**, tanpa server dan tanpa database.

## Fitur

- **Home**: profil singkat, minat penelitian, statistik karya, penelitian pilihan, dan kontak.
- **CV**: pendidikan, pengalaman, penghargaan, organisasi, keahlian, plus daftar publikasi
  yang **diambil otomatis** dari arsip. Tombol *Print / Save as PDF* menghasilkan CV rapi siap cetak.
- **Research** (arsip penelitian): pencarian cepat, saring per jenis & tahun, urutkan. Hasil penyaringan
  punya URL sendiri (mis. `/research/?jenis=dataset`) sehingga bisa dibagikan.
- **Halaman per karya** dengan tautan permanen: abstrak, berkas unduhan, DOI, kata kunci,
  tombol bagikan (WhatsApp, LinkedIn, X, Facebook, email, salin tautan), dan
  **sitasi otomatis** dalam format APA & BibTeX.
- Meta tag **Google Scholar** dan **Open Graph** agar karya mudah ditemukan dan tampil rapi
  saat tautannya dibagikan.
- Mode terang/gelap, ramah ponsel, tanpa pustaka JavaScript eksternal.

## Struktur folder

```
_config.yml            ← judul situs, alamat (url/baseurl), lisensi bawaan
_data/profil.yml       ← nama, jabatan, bio, foto, minat, tautan kontak
_data/cv.yml           ← isi CV (pendidikan, pengalaman, penghargaan, dll.)
_data/jenis.yml        ← daftar jenis karya (jurnal, dataset, tesis, …)
_penelitian/*.md       ← SATU FILE = SATU KARYA di arsip
arsip/                 ← berkas PDF/CSV/dll. yang bisa diunduh publik
assets/img/            ← foto profil
assets/css/situs.css   ← tampilan (warna, huruf)
assets/js/situs.js     ← pencarian, sitasi, tombol bagikan
```

Semua isi saat ini adalah **contoh**. Ganti dengan data Anda sendiri.

## 1. Mengaktifkan situs di GitHub Pages

1. Gabungkan (merge) branch ini ke `main`.
2. Di GitHub buka **Settings → Pages**.
3. Pada *Build and deployment* pilih **Source: Deploy from a branch**, lalu
   **Branch: `main`** dan folder **`/ (root)`**, klik **Save**.
4. Tunggu 1–2 menit. Situs akan tersedia di `https://fahertkuze.github.io/hehe-/`.

> Ingin alamat yang lebih pendek (`https://fahertkuze.github.io/`)? Ganti nama repositori
> menjadi `fahertkuze.github.io`, lalu ubah `baseurl: ""` di `_config.yml`.
> Jika memakai nama repositori lain, sesuaikan `baseurl: "/nama-repo"`.

## 2. Mengisi profil dan CV

Semua bisa diedit langsung dari situs GitHub (klik file → ikon pensil → *Commit changes*).

- **`_data/profil.yml`**: nama, gelar, jabatan, afiliasi, bio, minat penelitian, dan tautan
  (email, ORCID, Google Scholar, SINTA, ResearchGate, GitHub, LinkedIn). Baris yang
  dikosongkan (`""`) tidak akan ditampilkan.
- **Foto profil**: unggah foto (disarankan rasio 4:5, mis. 800×1000 px) ke `assets/img/`,
  lalu isi `foto: "assets/img/nama-file.jpg"`. Jika kosong, tampil inisial nama.
- **`_data/cv.yml`**: isi riwayat Anda. Hapus bagian yang tidak diperlukan.
- **CV dalam PDF** (opsional): unggah ke `arsip/` lalu isi `cv_pdf: "arsip/cv.pdf"`.
  Tanpa itu pun, pengunjung tetap bisa menekan *Print / Save as PDF* di halaman CV.

## 3. Menambah penelitian ke arsip

1. Unggah berkas (PDF, CSV, PPTX, …) ke folder **`arsip/`**.
2. Buat file baru di folder **`_penelitian/`**, misalnya `_penelitian/judul-singkat.md`.
   Nama file menjadi alamat halamannya: `/research/judul-singkat/`
   (gunakan huruf kecil dan tanda hubung, tanpa spasi).
3. Salin templat ini dan isi (tulis judul, abstrak, dll. dalam bahasa Inggris agar
   sesuai dengan tampilan situs):

```yaml
---
judul: "Judul Lengkap Penelitian"
penulis:
  - "Nama Lengkap Anda"
  - "Nama Rekan Penulis"
tahun: 2025
tanggal: 2025-05-20        # opsional, untuk urutan yang lebih tepat
jenis: jurnal              # jurnal | prosiding | preprint | tesis | laporan | dataset | presentasi | buku
terbitan: "Nama Jurnal, 10(2), 1–15"   # jurnal/konferensi/universitas/penyelenggara
doi: "10.1234/abcd.2025.001"           # opsional, tanpa https://doi.org/
unggulan: true             # opsional, tampilkan di halaman Home
kata_kunci: [kata satu, kata dua]
abstrak: >
  Tulis abstrak di sini. Boleh beberapa baris.
berkas:
  - label: "Naskah lengkap"
    url: "arsip/nama-berkas.pdf"
tautan:                    # opsional, tautan luar (kode, repositori data, video, dll.)
  - label: "Kode sumber"
    url: "https://github.com/..."
lisensi: "CC BY 4.0"       # opsional, jika berbeda dari lisensi bawaan
---

(Opsional) Catatan tambahan dalam Markdown: temuan utama, metode, gambar, dll.
```

4. *Commit* dan tunggu ±1 menit. Karya langsung muncul di halaman Research, Home (jika `unggulan`),
   dan daftar publikasi di CV.

Hapus file contoh di `_penelitian/` serta `arsip/example-*` bila sudah tidak diperlukan.

### Tips arsip terbuka

- **Berkas besar**: GitHub membatasi 100 MB per file (disarankan < 50 MB). Untuk dataset besar,
  unggah ke [Zenodo](https://zenodo.org) atau Figshare — Anda juga **mendapat DOI gratis** —
  lalu cantumkan tautannya di `berkas` (`url: "https://zenodo.org/records/..."`).
- **Hak cipta**: sebelum mengunggah naskah yang sudah terbit, periksa kebijakan penerbit
  (banyak jurnal mengizinkan versi *preprint*/*accepted manuscript*), misalnya lewat
  layanan Sherpa Romeo.
- **Nama penulis ditebalkan** otomatis jika sama persis dengan `nama` di `profil.yml`.
  Jika nama Anda ditulis berbeda di publikasi, isi `nama_di_publikasi` di `profil.yml`.
- **Jenis karya baru** bisa ditambahkan di `_data/jenis.yml`.

## 4. Mengubah tampilan

Teks menu dan tombol (bahasa Inggris) ada di `_layouts/`, `_includes/`, `index.html`,
`research.html`, `cv.html`, dan `assets/js/situs.js`. Label jenis karya ada di `_data/jenis.yml`.


Warna diatur di bagian atas `assets/css/situs.css`. Contoh: ubah `--aksen: #0e6b5c;` menjadi
`--aksen: #1f4e79;` untuk aksen biru (ubah juga nilai `--aksen` pada blok mode gelap).

## Menjalankan di komputer sendiri (opsional)

Butuh Ruby. Lalu:

```bash
bundle install
bundle exec jekyll serve
```

Buka `http://localhost:4000/hehe-/`.
