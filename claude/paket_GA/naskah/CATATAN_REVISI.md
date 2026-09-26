# Catatan revisi untuk penulis

Catatan ini menjelaskan apa yang diambil dari draf Anda, apa yang diubah, apa yang
ditambahkan, dan hal-hal yang perlu Anda periksa sebelum naskah dikirim.

## 1. Bagian draf Anda yang dipakai

| Bagian | Status |
|:--|:--|
| Paragraf pembuka (analogi lembah, dua pertanyaan) | dipakai sebagai paragraf 1 Pendahuluan, tanpa perubahan |
| Kalimat penutup paragraf 3 | dipakai apa adanya |
| Paragraf 4 | dipakai, dengan satu kata diganti (lihat §2 di bawah) |
| Paragraf 5 | dipakai, ditambah satu kalimat tentang uji-uji baru |
| Metode §2.1–2.5 | dipakai apa adanya; persamaan (1)–(11) tidak berubah |
| Abstrak | struktur dan kalimat kesimpulan dipertahankan; angka dan hasil baru ditambahkan |

## 2. Perubahan pada teks Anda (dan alasannya)

1. **Paragraf 4, kalimat terakhir: "derasnya air" → "debit air".** Hasil baru
   menunjukkan bahwa *kecepatan* aliran menuju basin (V = aHfD) justru praktis masih di
   puncaknya (hanya 0,67% di bawah maksimum). Yang menurun adalah *jumlah* materi yang
   dibawa aliran (fluks massa), karena ekspansi mengencerkan materi. "Deras" dapat dibaca
   sebagai kecepatan, sehingga berisiko bertentangan dengan hasil Anda sendiri; "debit"
   (volume per satuan waktu) tepat. Analogi ini diperluas di §4.1: "air masih mengalir
   hampir sama cepat, tetapi hujannya kian tipis".
2. **Paragraf 5:** ditambah satu kalimat yang menyebut uji-uji baru; peta naskah tetap.
3. **Metode §2.4:** ditambah anak kalimat bahwa maksimisasi numerik dipertajam dengan
   mencari akar persamaan (9) (sesuai implementasi kode).
4. **Metode:** baris "Sumber persamaan: `claude/paket_GA/...`" dihapus dari naskah
   (itu catatan kerja, bukan isi makalah); gantinya ada bagian *Ketersediaan kode dan data*.
5. **Abstrak:** "Great Attractors gravity" → "Great Attractor's gravity"; Methods dan
   Results dilengkapi angka dengan ketidakpastian dan hasil baru. Kalimat kesimpulan Anda
   dipertahankan kata per kata, ditambah satu kalimat tentang keberlakuan umum (keputusan
   yang Anda ambil di §2.5).
6. **Paragraf 2 dan 3 Pendahuluan ditulis baru**, karena yang tersedia hanya kalimat
   penutup paragraf 3. Jika Anda sudah punya versi sendiri, ganti keduanya; kalimat
   penutup paragraf 3 sudah menyambung ke paragraf 4.

## 3. Yang ditambahkan (pengembangan riset)

- **§2.6 dan §3.3 — tiga "jam" akresi.** f·D (per e-fold), Ḋ = HfD (per satuan waktu),
  dan V = aHfD (kecepatan aliran) diturunkan dari satu bola komoving di sekitar basin
  (persamaan 12–14). Ini menjawab pertanyaan reviewer yang hampir pasti muncul: "apakah
  puncak hanya artefak pemilihan ln a sebagai jam?" Jawabannya: Ḋ memang turun monoton
  (juga di alam semesta tanpa energi gelap), sedangkan f·D dan V hanya berbalik karena
  energi gelap. Hasil a·H·f·D (penurunan 0,67%) dari paket kode Anda sebelumnya ada di sini.
- **§3.2 — syarat puncak universal.** Dalam ΛCDM datar puncak f·D terjadi tepat pada
  Ωm(a) = 0,5619 (ρΛ/ρm = 0,78), berapa pun Ωm hari ini, dengan rumus tertutup untuk
  z_pk (persamaan 20). Ini hasil paling "bersih" di naskah dan menjelaskan mengapa hasil
  berlaku untuk struktur lain.
- **§3.4 — uji ketahanan:** solusi eksak Heath (cocok hingga 2×10⁻¹⁰), konvergensi,
  radiasi, CAMB dengan neutrino masif, Monte Carlo Planck, lima kosmologi DESI DR2, dan
  tiga nilai indeks pertumbuhan γ.
- **§3.5 — data fσ8.** f·D = fσ8/σ8,0, jadi data RSD dan kecepatan pekuliar mengukur bentuk
  kurva secara langsung. Data tanpa CMB menempatkan puncak di z = 0,56 ± 0,10.
- **§3.6 — masa depan:** D∞/D0 = 1,408; pertumbuhan praktis berhenti dalam ~33 Gyr, sejalan
  dengan simulasi Nagamine & Loeb (2003).
- **§4 — diskusi** lengkap, termasuk §4.3 yang menjawab isu "berlaku sama untuk struktur
  lain" sebagaimana Anda rencanakan, dan §4.2 tentang rezim kuasi-linear di posisi Bima Sakti.

## 4. Perbandingan DESI

Paket kode Anda sebelumnya (`modul_A_pertumbuhan.py`, `parameter.py`, dan perbandingan
DESI) tidak ada di repositori ini, jadi paket dibangun ulang dari awal. Perbandingan DESI
sekarang memakai lima kosmologi dari DESI DR2 (Phys. Rev. D 112, 083515). Jika hasil DESI
di paket lama Anda berbeda, kemungkinan karena memakai rilis DR1 atau kombinasi data yang
lain; periksa sebelum mengutip salah satunya.

## 5. Yang perlu Anda periksa

1. **Nama dan afiliasi penulis** diambil dari `_data/profil.yml` situs Anda. Tambahkan
   email korespondensi dan ucapan terima kasih.
2. **H0 untuk model DESI w0wa** tidak dikutip dari makalah DESI, tetapi diturunkan dari
   Ωm h² = 0,1430. Ini hanya memengaruhi kolom waktu lihat-balik (Tabel 5), tidak z_pk
   maupun Δ. Jika ingin, ganti dengan nilai H0 dari tabel makalah DESI DR2.
3. **Rentang 200–500 km/s** untuk kecepatan Grup Lokal menuju kawasan GA (§4.2) adalah
   asumsi ilustratif, dan sudah ditulis demikian. Jika Anda ingin angka spesifik, kutip
   dekomposisi kecepatan Grup Lokal dari literatur.
4. **Daftar pustaka** memakai gaya MNRAS (tiga penulis + "dkk."). Detail volume dan halaman
   sudah diperiksa, tetapi cocokkan lagi dengan gaya jurnal tujuan dan tambahkan DOI bila
   diminta.
5. **Jurnal tujuan.** Abstrak berformat A&A (Context/Aims/Methods/Results/Conclusions)
   sementara isi berbahasa Indonesia. Pastikan kombinasi ini sesuai dengan jurnal tujuan;
   bila perlu, naskah dapat diterjemahkan ke bahasa Inggris atau dipindah ke templat
   LaTeX jurnal.

## 6. Pertanyaan reviewer yang sudah diantisipasi

| Kemungkinan pertanyaan | Dijawab di |
|:--|:--|
| Apakah hasilnya khas GA, atau berlaku untuk semua struktur? | §2.5, §3.2, §4.3 |
| Apakah puncak hanya akibat pemilihan jam ln a? | §2.6, §3.3 |
| Apakah pendekatan linear berlaku di sekitar GA? | §2.5, §4.2 |
| Bagaimana dengan radiasi, baryon, neutrino masif? | §3.4 (CAMB) |
| Bagaimana jika energi gelap dinamis (DESI)? | §2.8, §3.4, Tabel 5 |
| Apakah prediksi ini dapat diuji dengan data? | §2.9, §3.5, Gambar 4 |
| Seberapa besar ketidakpastiannya? | §2.7, Tabel 3 |
| Apa kaitannya dengan studi masa depan struktur lokal? | §4.4 |
