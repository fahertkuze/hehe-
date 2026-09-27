# BAB 10 — ATURAN PENCACAHAN DAN PELUANG

> **Elemen:** Data dan Peluang · **Sub-elemen:** Aturan Pencacahan dan Peluang
>
> **Cakupan:** aturan penjumlahan dan perkalian, permutasi, kombinasi, ruang sampel, peluang kejadian, komplemen, frekuensi harapan, serta peluang kejadian majemuk (saling lepas, saling bebas, bersyarat).
>
> *Catatan: tangkapan layar kisi-kisi terpotong pada kata "Aturan…". Bab ini disiapkan agar seluruh kemungkinan cakupan (aturan pencacahan dan peluang) tetap terlatih.*

---

## A. Ringkasan Materi

### A.1 Aturan Penjumlahan dan Aturan Perkalian

**Aturan penjumlahan** (kata kunci "**atau**"): jika kejadian pertama dapat terjadi dengan $m$ cara dan kejadian kedua dengan $n$ cara, dan keduanya **tidak** dapat terjadi bersamaan, maka banyak cara terjadinya salah satu adalah $m + n$.

**Aturan perkalian / pengisian tempat** (kata kunci "**dan**", "lalu", tahap demi tahap): jika tahap pertama dapat dilakukan dengan $m$ cara dan tahap kedua dengan $n$ cara, maka seluruhnya dapat dilakukan dengan $m \times n$ cara.

> **Contoh.** Dari kota A ke B ada 3 jalan, dan dari B ke C ada 4 jalan. Banyak rute dari A ke C melalui B $= 3 \times 4 = 12$.

> **Contoh (pengisian tempat).** Berapa banyak bilangan tiga angka **berbeda** yang dapat disusun dari angka $1, 2, 3, 4, 5$?
>
> | Ratusan | Puluhan | Satuan |
> |:--:|:--:|:--:|
> | 5 pilihan | 4 pilihan | 3 pilihan |
>
> Banyaknya $5 \times 4 \times 3 = 60$ bilangan.

**Strategi:** isi dulu tempat yang **paling banyak syaratnya** (misalnya angka satuan untuk bilangan genap/ganjil, angka pertama yang tidak boleh 0, atau angka ratusan untuk bilangan "kurang dari 400").

**Faktorial:** $n! = n \times (n - 1) \times \dots \times 2 \times 1$, dengan $0! = 1$ dan $1! = 1$.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $n!$ | 1 | 1 | 2 | 6 | 24 | 120 | 720 | 5.040 |

### A.2 Permutasi (Urutan Diperhatikan)

**Permutasi $r$ unsur dari $n$ unsur berbeda:**

$$P(n, r) = {}_nP_r = \frac{n!}{(n - r)!}$$

> **Contoh.** Memilih ketua, sekretaris, dan bendahara dari 8 orang: $P(8, 3) = 8 \times 7 \times 6 = 336$.

**Permutasi dengan unsur yang sama:** dari $n$ unsur, terdapat $k_1$ unsur sama, $k_2$ unsur sama, dan seterusnya:

$$P = \frac{n!}{k_1! \  k_2! \  \cdots}$$

> **Contoh.** Susunan huruf dari kata "KAKAK": $n = 5$, K muncul 3 kali, A muncul 2 kali → $\dfrac{5!}{3!\ 2!} = 10$.

**Permutasi siklis** (melingkar): $n$ unsur disusun melingkar → $(n - 1)!$ cara.

> **Contoh.** 5 orang duduk mengelilingi meja bundar: $4! = 24$ cara.

**Unsur yang harus berdampingan:** anggap unsur-unsur yang berdampingan sebagai **satu blok**, lalu kalikan dengan banyak susunan di dalam blok.

### A.3 Kombinasi (Urutan Tidak Diperhatikan)

$$C(n, r) = {}_nC_r = \binom{n}{r} = \frac{n!}{r!\ (n - r)!}$$

Sifat: $C(n, r) = C(n, n - r)$, $\ C(n, 0) = C(n, n) = 1$, $\ C(n, 1) = n$.

> **Contoh.** Memilih 3 siswa dari 10 siswa untuk mengikuti lomba (tanpa jabatan): $C(10, 3) = \dfrac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.

**Permutasi atau kombinasi?**

| Permutasi (urutan penting) | Kombinasi (urutan tidak penting) |
|---|---|
| menyusun kata, nomor, kode, PIN | memilih anggota tim, panitia, delegasi |
| memilih ketua–sekretaris–bendahara | memilih $r$ soal dari $n$ soal |
| juara 1, 2, 3 | jabat tangan, banyak garis/segitiga dari titik |
| urutan duduk | mengambil beberapa bola **sekaligus** |

**Rumus turunan yang sering muncul**
- Banyak jabat tangan $n$ orang $= C(n, 2) = \dfrac{n(n - 1)}{2}$.
- Banyak garis dari $n$ titik (tak ada 3 yang segaris) $= C(n, 2)$; banyak segitiga $= C(n, 3)$.
- Banyak diagonal segi-$n$ $= C(n, 2) - n = \dfrac{n(n - 3)}{2}$.

### A.4 Ruang Sampel dan Peluang Kejadian

- **Percobaan**: kegiatan yang hasilnya tidak pasti (melempar koin, dadu, mengambil kartu).
- **Ruang sampel** $S$: himpunan semua hasil yang mungkin; $n(S)$ = banyaknya.
- **Kejadian** $A$: himpunan bagian dari $S$.

$$P(A) = \frac{n(A)}{n(S)}, \qquad 0 \le P(A) \le 1$$

$P(A) = 0$ → mustahil; $P(A) = 1$ → pasti terjadi.

**Ruang sampel yang wajib dihafal**

| Percobaan | $n(S)$ |
|---|---|
| $k$ koin | $2^k$ (1 koin: 2; 2 koin: 4; 3 koin: 8) |
| $k$ dadu | $6^k$ (1 dadu: 6; 2 dadu: 36) |
| 1 kartu dari satu set kartu bridge | 52 (4 jenis × 13 kartu; ada 4 As, 12 kartu gambar J/Q/K, 26 merah, 26 hitam) |

**Jumlah mata dua dadu**

| Jumlah | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Banyak pasangan | 1 | 2 | 3 | 4 | 5 | **6** | 5 | 4 | 3 | 2 | 1 |

**Peluang komplemen** ("bukan $A$"):

$$P(A^c) = 1 - P(A)$$

Sangat berguna untuk soal "**paling sedikit satu**": $P(\text{paling sedikit satu}) = 1 - P(\text{tidak ada sama sekali})$.

**Frekuensi harapan:** jika percobaan dilakukan $N$ kali,

$$F_h(A) = N \times P(A)$$

**Frekuensi relatif (peluang empiris)** $= \dfrac{\text{banyak kejadian muncul}}{\text{banyak percobaan}}$. Makin banyak percobaan, frekuensi relatif makin mendekati peluang teoretis.

### A.5 Peluang Kejadian Majemuk

**Gabungan dua kejadian:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

| Jenis | Syarat | Rumus |
|---|---|---|
| **Saling lepas** (tidak bisa terjadi bersamaan) | $A \cap B = \varnothing$ | $P(A \cup B) = P(A) + P(B)$ |
| **Saling bebas** (tidak saling memengaruhi) | — | $P(A \cap B) = P(A) \times P(B)$ |
| **Bersyarat** ($A$ jika diketahui $B$ terjadi) | $P(B) > 0$ | $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ |

> **Contoh (gabungan).** Satu kartu diambil dari satu set kartu bridge. Peluang terambil kartu As **atau** kartu hati:  
> $P = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}$ (dikurangi As hati yang terhitung dua kali).

**Pengambilan dengan/tanpa pengembalian**

- **Dengan pengembalian** → kejadian saling bebas, peluang setiap pengambilan tetap.
- **Tanpa pengembalian** → peluang pengambilan berikutnya berubah (isi kotak berkurang).
- Mengambil beberapa bola **sekaligus** → gunakan kombinasi.

> **Contoh.** Kotak berisi 4 bola merah dan 6 bola biru. Diambil 2 bola satu per satu **tanpa pengembalian**. Peluang bola pertama merah dan bola kedua biru:  
> $\frac{4}{10} \times \frac{6}{9} = \frac{24}{90} = \frac{4}{15}$.

> **Contoh (sekaligus).** Dari kotak berisi 5 bola merah dan 3 bola putih diambil 2 bola sekaligus. Peluang keduanya merah:  
> $\dfrac{C(5, 2)}{C(8, 2)} = \dfrac{10}{28} = \dfrac{5}{14}$.

**Diagram Venn** membantu soal seperti "suka matematika, suka fisika, suka keduanya":

$$n(A \cup B) = n(A) + n(B) - n(A \cap B), \qquad n(\text{tidak keduanya}) = n(S) - n(A \cup B)$$

---

## B. Tips & Trik

1. **Tanya diri sendiri: "Apakah urutan berpengaruh?"** Jika menukar posisi menghasilkan susunan berbeda → permutasi; jika tidak → kombinasi.
2. **Pengisian tempat:** mulai dari tempat dengan syarat paling ketat. Jika syarat saling berbenturan (misalnya ratusan < 4 **dan** satuan genap), pecah menjadi kasus.
3. **Angka 0** tidak boleh menjadi angka pertama sebuah bilangan.
4. **"Paling sedikit satu"** → gunakan komplemen.
5. **Hitung $C(n, r)$ dengan cepat:** $C(n, r) = \dfrac{n \times (n - 1) \times \dots \text{ (sebanyak } r \text{ faktor)}}{r!}$. Contoh: $C(9, 4) = \frac{9 \cdot 8 \cdot 7 \cdot 6}{24} = 126$.
6. **Berdampingan → blok; tidak boleh berdampingan → total dikurangi yang berdampingan.**
7. **Dua dadu:** jumlah 7 paling sering (6 dari 36). Hafalkan pola $1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1$.
8. **Kartu bridge:** 52 kartu; 4 jenis (hati ♥, wajik ♦, sekop ♠, keriting ♣); tiap jenis 13 kartu (As, 2–10, J, Q, K).
9. **Saling lepas ≠ saling bebas.** Saling lepas: $P(A \cap B) = 0$. Saling bebas: $P(A \cap B) = P(A)P(B)$. Dua kejadian dengan peluang positif yang saling lepas **pasti tidak** saling bebas.
10. **Peluang bersyarat = perkecil ruang sampel.** "Diketahui jumlah mata dadu 8" → ruang sampel baru hanya 5 pasangan.

---

## C. Latihan Soal

### Bagian I — Pilihan Ganda

**1.** Dari kota A ke kota B terdapat 3 jalan, dan dari kota B ke kota C terdapat 4 jalan. Banyak rute perjalanan pulang-pergi dari A ke C melalui B, dengan syarat jalan yang dilalui saat pulang tidak boleh sama dengan saat pergi, adalah ….

- A. $12$
- B. $24$
- C. $36$
- D. $72$
- E. $144$

**2.** Dari angka-angka $1, 2, 3, 4, 5, 6$ akan disusun bilangan genap tiga angka **berbeda** yang kurang dari 400. Banyak bilangan yang dapat disusun adalah ….

- A. $24$
- B. $32$
- C. $30$
- D. $36$
- E. $60$

**3.** Dari 8 orang calon akan dipilih seorang ketua, seorang sekretaris, dan seorang bendahara. Banyak susunan pengurus yang mungkin adalah ….

- A. $56$
- B. $112$
- C. $168$
- D. $512$
- E. $336$

**4.** Banyak susunan huruf berbeda yang dapat dibentuk dari huruf-huruf pada kata "MATEMATIKA" adalah ….

- A. $151.200$
- B. $302.400$
- C. $75.600$
- D. $3.628.800$
- E. $50.400$

**5.** Enam orang duduk mengelilingi sebuah meja bundar. Banyak susunan duduk yang berbeda adalah ….

- A. $60$
- B. $720$
- C. $120$
- D. $360$
- E. $24$

**6.** Dari 9 siswa akan dipilih 4 siswa untuk mewakili sekolah dalam lomba cerdas cermat. Banyak cara memilih adalah ….

- A. $36$
- B. $84$
- C. $3.024$
- D. $126$
- E. $252$

**7.** Sebuah tim terdiri atas 5 orang yang dipilih dari 6 putra dan 4 putri. Jika tim harus terdiri atas 3 putra dan 2 putri, banyak cara membentuk tim adalah ….

- A. $26$
- B. $120$
- C. $60$
- D. $240$
- E. $252$

**8.** Dalam sebuah pertemuan, 12 orang saling berjabat tangan. Setiap dua orang berjabat tangan tepat satu kali. Banyak jabat tangan yang terjadi adalah ….

- A. $24$
- B. $132$
- C. $144$
- D. $72$
- E. $66$

**9.** Dua buah dadu dilempar bersamaan satu kali. Peluang muncul jumlah mata dadu 8 adalah ….

- A. $\frac{5}{36}$
- B. $\frac{4}{36}$
- C. $\frac{6}{36}$
- D. $\frac{7}{36}$
- E. $\frac{8}{36}$

**10.** Tiga keping uang logam dilempar bersamaan. Peluang muncul **paling sedikit satu** sisi angka adalah ….

- A. $\frac{1}{8}$
- B. $\frac{3}{8}$
- C. $\frac{7}{8}$
- D. $\frac{1}{2}$
- E. $1$

**11.** Sebuah kartu diambil secara acak dari satu set kartu bridge (52 kartu). Peluang terambil kartu As atau kartu hati adalah ….

- A. $\frac{17}{52}$
- B. $\frac{1}{4}$
- C. $\frac{1}{13}$
- D. $\frac{4}{13}$
- E. $\frac{1}{52}$

**12.** Sebuah kotak berisi 5 bola merah dan 3 bola putih. Diambil 2 bola sekaligus secara acak. Peluang terambil keduanya bola merah adalah ….

- A. $\frac{5}{8}$
- B. $\frac{5}{14}$
- C. $\frac{25}{64}$
- D. $\frac{3}{14}$
- E. $\frac{15}{28}$

**13.** Sebuah dadu dilempar 120 kali. Frekuensi harapan muncul mata dadu bilangan prima adalah ….

- A. $60$
- B. $20$
- C. $40$
- D. $80$
- E. $90$

**14.** Kejadian $A$ dan $B$ saling bebas dengan $P(A) = 0{,}4$ dan $P(B) = 0{,}5$. Nilai $P(A \cup B)$ adalah ….

- A. $0{,}2$
- B. $0{,}5$
- C. $0{,}9$
- D. $0{,}1$
- E. $0{,}7$

**15.** Sebuah kotak berisi 4 bola merah dan 6 bola biru. Diambil 2 bola satu per satu tanpa pengembalian. Peluang terambil bola merah pada pengambilan pertama dan bola biru pada pengambilan kedua adalah ….

- A. $\frac{6}{25}$
- B. $\frac{2}{15}$
- C. $\frac{4}{15}$
- D. $\frac{1}{3}$
- E. $\frac{2}{5}$

**16.** Dua dadu dilempar bersamaan. Jika diketahui jumlah mata kedua dadu adalah 8, peluang salah satu dadu menunjukkan mata 3 adalah ….

- A. $\frac{2}{5}$
- B. $\frac{1}{6}$
- C. $\frac{1}{18}$
- D. $\frac{1}{3}$
- E. $\frac{5}{36}$

**17.** Banyak bilangan empat angka **berbeda** yang dapat disusun dari angka-angka $0, 1, 2, 3, 4, 5$ adalah ….

- A. $360$
- B. $240$
- C. $180$
- D. $300$
- E. $1.296$

**18.** Banyak diagonal pada segi sepuluh (dekagon) adalah ….

- A. $45$
- B. $35$
- C. $40$
- D. $20$
- E. $90$

**19.** Empat siswa putra dan tiga siswa putri akan duduk berjajar dalam satu baris. Jika ketiga siswa putri harus selalu duduk berdampingan, banyak susunan duduk yang mungkin adalah ….

- A. $144$
- B. $1.440$
- C. $5.040$
- D. $240$
- E. $720$

**20.** Sebuah kata sandi terdiri atas 2 huruf (A–Z, 26 huruf) diikuti 2 angka (0–9). Huruf boleh berulang, tetapi kedua angka harus berbeda. Banyak kata sandi yang dapat dibuat adalah ….

- A. $67.600$
- B. $58.500$
- C. $60.840$
- D. $6.760$
- E. $650$

### Bagian II — Pilihan Ganda Kompleks (jawaban benar bisa lebih dari satu)

**21.** Pernyataan yang benar adalah ….

- ☐ (1) $0! = 1$
- ☐ (2) $C(10, 3) = C(10, 7)$
- ☐ (3) $P(5, 2) = 10$
- ☐ (4) $C(6, 2) = 30$
- ☐ (5) $\dfrac{5!}{3!} = 20$

**22.** Permasalahan berikut yang diselesaikan dengan **kombinasi** adalah ….

- ☐ (1) memilih 3 perwakilan kelas untuk rapat
- ☐ (2) menyusun nomor antrean 5 orang
- ☐ (3) memilih ketua dan wakil ketua kelas
- ☐ (4) menghitung banyak jabat tangan
- ☐ (5) memilih 4 soal yang dikerjakan dari 6 soal

**23.** Dua dadu dilempar bersamaan satu kali. Pernyataan yang benar adalah ….

- ☐ (1) Banyak anggota ruang sampelnya 36.
- ☐ (2) Peluang muncul jumlah mata 7 adalah $\frac{1}{6}$.
- ☐ (3) Peluang muncul mata dadu kembar adalah $\frac{1}{12}$.
- ☐ (4) Peluang muncul jumlah mata 13 adalah 0.
- ☐ (5) Peluang muncul jumlah mata paling sedikit 10 adalah $\frac{1}{4}$.

**24.** Kejadian $A$ dan $B$ saling lepas dengan $P(A) = 0{,}3$ dan $P(B) = 0{,}5$. Pernyataan yang benar adalah ….

- ☐ (1) $P(A \cap B) = 0$
- ☐ (2) $P(A \cup B) = 0{,}8$
- ☐ (3) $P(A^c) = 0{,}7$
- ☐ (4) $A$ dan $B$ saling bebas.
- ☐ (5) $P(A \cap B) = 0{,}15$

**25.** Sebuah kotak berisi 3 bola merah, 2 bola kuning, dan 5 bola hijau. Diambil satu bola secara acak. Pernyataan yang benar adalah ….

- ☐ (1) Peluang terambil bola merah 0,3.
- ☐ (2) Peluang terambil bola yang bukan hijau 0,5.
- ☐ (3) Peluang terambil bola merah atau kuning 0,6.
- ☐ (4) Peluang terambil bola biru 0.
- ☐ (5) Peluang terambil bola hijau 0,4.

### Bagian III — Benar atau Salah

**26.** Perhatikan huruf-huruf pada kata "BUKU".

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Banyak susunan huruf berbeda yang dapat dibentuk adalah 12. | ☐ | ☐ |
| b | Jika keempat hurufnya berbeda, banyak susunannya menjadi 24. | ☐ | ☐ |
| c | Jika satu susunan dipilih acak, peluang susunan itu diawali huruf U adalah $\frac{1}{4}$. | ☐ | ☐ |
| d | Banyak susunan dengan kedua huruf U berdampingan adalah 6. | ☐ | ☐ |

**27.** Dari 30 siswa sebuah kelas, 18 siswa menyukai matematika, 15 siswa menyukai fisika, dan 8 siswa menyukai keduanya. Seorang siswa dipilih secara acak.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Banyak siswa yang tidak menyukai keduanya adalah 5. | ☐ | ☐ |
| b | Peluang terpilih siswa yang hanya menyukai matematika adalah $\frac{1}{3}$. | ☐ | ☐ |
| c | Jika diketahui siswa yang terpilih menyukai matematika, peluang ia juga menyukai fisika adalah $\frac{4}{9}$. | ☐ | ☐ |
| d | Kejadian "menyukai matematika" dan "menyukai fisika" saling lepas. | ☐ | ☐ |

**28.** Tiga keping uang logam dilempar bersamaan.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Banyak anggota ruang sampelnya 8. | ☐ | ☐ |
| b | Peluang muncul tepat 2 angka adalah $\frac{1}{4}$. | ☐ | ☐ |
| c | Jika pelemparan dilakukan 80 kali, frekuensi harapan muncul 3 gambar adalah 10. | ☐ | ☐ |
| d | Peluang muncul paling sedikit 1 gambar adalah $\frac{1}{8}$. | ☐ | ☐ |

**29.** Dari 5 calon pengurus OSIS (3 putra dan 2 putri) akan dipilih seorang ketua dan seorang wakil ketua.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Banyak susunan ketua dan wakil ketua yang mungkin adalah 10. | ☐ | ☐ |
| b | Jika ketua harus putri, banyak susunannya 8. | ☐ | ☐ |
| c | Jika hanya dipilih 2 orang tanpa jabatan, banyak caranya 10. | ☐ | ☐ |
| d | Jika pemilihan dilakukan secara acak, peluang ketua dan wakil ketua keduanya putra adalah $\frac{3}{5}$. | ☐ | ☐ |

### Bagian IV — Isian Singkat

**30.** Banyak bilangan ganjil tiga angka **berbeda** yang dapat disusun dari angka $1, 2, 3, 4, 5$ adalah ….

**31.** Dari 10 siswa, termasuk Andi dan Budi, akan dipilih 3 siswa secara acak. Peluang Andi dan Budi keduanya terpilih adalah ….

**32.** Peluang seorang siswa lulus ujian adalah 0,9. Dari 400 siswa yang mengikuti ujian, banyak siswa yang diharapkan **tidak** lulus adalah ….

**33.** Dua dadu dilempar bersamaan satu kali. Peluang muncul jumlah mata dadu 5 atau 10 adalah ….

---

## D. Kunci Jawaban dan Pembahasan

### Kunci Ringkas

| No | Kunci | No | Kunci | No | Kunci | No | Kunci |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | D | 10 | C | 19 | E | 28 | B, S, B, S |
| 2 | B | 11 | D | 20 | C | 29 | S, B, B, S |
| 3 | E | 12 | B | 21 | (1), (2), (5) | 30 | 36 |
| 4 | A | 13 | A | 22 | (1), (4), (5) | 31 | $\frac{1}{15}$ |
| 5 | C | 14 | E | 23 | (1), (2), (4) | 32 | 40 |
| 6 | D | 15 | C | 24 | (1), (2), (3) | 33 | $\frac{7}{36}$ |
| 7 | B | 16 | A | 25 | (1), (2), (4) | | |
| 8 | E | 17 | D | 26 | B, B, S, B | | |
| 9 | A | 18 | B | 27 | B, B, B, S | | |

### Pembahasan

**1. Jawaban: D**  
Pergi: A→B (3 cara), B→C (4 cara). Pulang: C→B (sisa $4 - 1 = 3$ cara), B→A (sisa $3 - 1 = 2$ cara).  
Total $= 3 \times 4 \times 3 \times 2 = 72$.

**2. Jawaban: B**  
Syarat: angka ratusan $\in \lbrace 1, 2, 3 \rbrace$ (agar $< 400$) dan angka satuan $\in \lbrace 2, 4, 6 \rbrace$ (genap). Karena angka 2 muncul di kedua syarat, pecah menjadi kasus:
- *Ratusan = 2:* satuan $\in \lbrace 4, 6 \rbrace$ (2 cara), puluhan: sisa 4 angka → $1 \times 4 \times 2 = 8$.
- *Ratusan = 1 atau 3:* 2 cara; satuan $\in \lbrace 2, 4, 6 \rbrace$ (3 cara); puluhan: sisa 4 angka → $2 \times 4 \times 3 = 24$.

Total $= 8 + 24 = 32$.

**3. Jawaban: E**  
Jabatan berbeda → urutan penting → $P(8, 3) = 8 \times 7 \times 6 = 336$.

**4. Jawaban: A**  
MATEMATIKA: 10 huruf dengan M = 2, A = 3, T = 2.  
$\dfrac{10!}{2!\ 3!\ 2!} = \dfrac{3\ 628\ 800}{2 \times 6 \times 2} = \dfrac{3\ 628\ 800}{24} = 151\ 200$.

**5. Jawaban: C**  
Permutasi siklis: $(6 - 1)! = 5! = 120$.

**6. Jawaban: D**  
$C(9, 4) = \dfrac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = \dfrac{3\ 024}{24} = 126$.

**7. Jawaban: B**  
$C(6, 3) \times C(4, 2) = 20 \times 6 = 120$.

**8. Jawaban: E**  
$C(12, 2) = \dfrac{12 \times 11}{2} = 66$.

**9. Jawaban: A**  
Pasangan berjumlah 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$ → 5 pasangan. $P = \frac{5}{36}$.

**10. Jawaban: C**  
$P(\text{tidak ada angka}) = P(GGG) = \frac{1}{8}$. Maka $P(\text{paling sedikit satu angka}) = 1 - \frac{1}{8} = \frac{7}{8}$.

**11. Jawaban: D**  
$P(\text{As}) = \frac{4}{52}$, $P(\text{hati}) = \frac{13}{52}$, $P(\text{As hati}) = \frac{1}{52}$.  
$P = \frac{4 + 13 - 1}{52} = \frac{16}{52} = \frac{4}{13}$.

**12. Jawaban: B**  
$\dfrac{C(5, 2)}{C(8, 2)} = \dfrac{10}{28} = \dfrac{5}{14}$.

**13. Jawaban: A**  
Mata dadu prima: $2, 3, 5$ → $P = \frac{3}{6} = \frac{1}{2}$. $F_h = 120 \times \frac{1}{2} = 60$.

**14. Jawaban: E**  
Saling bebas: $P(A \cap B) = 0{,}4 \times 0{,}5 = 0{,}2$.  
$P(A \cup B) = 0{,}4 + 0{,}5 - 0{,}2 = 0{,}7$.

**15. Jawaban: C**  
$P = \frac{4}{10} \times \frac{6}{9} = \frac{24}{90} = \frac{4}{15}$.

**16. Jawaban: A**  
Ruang sampel baru (jumlah 8): $(2,6), (3,5), (4,4), (5,3), (6,2)$ → 5 anggota.  
Yang memuat mata 3: $(3,5)$ dan $(5,3)$ → 2 anggota. $P = \frac{2}{5}$.

**17. Jawaban: D**  
Ribuan: tidak boleh 0 → 5 pilihan. Ratusan: sisa 5 angka (0 boleh). Puluhan: 4. Satuan: 3.  
$5 \times 5 \times 4 \times 3 = 300$.

**18. Jawaban: B**  
$C(10, 2) - 10 = 45 - 10 = 35$, atau $\dfrac{10 \times 7}{2} = 35$.

**19. Jawaban: E**  
Anggap 3 putri sebagai satu blok → ada 5 unit (4 putra + 1 blok) → $5! = 120$ susunan.  
Di dalam blok, 3 putri dapat bertukar tempat: $3! = 6$. Total $= 120 \times 6 = 720$.

**20. Jawaban: C**  
Huruf pertama 26, huruf kedua 26 (boleh berulang), angka pertama 10, angka kedua 9 (harus berbeda).  
$26 \times 26 \times 10 \times 9 = 676 \times 90 = 60\ 840$.

**21. Jawaban: (1), (2), (5)**
- (1) ✔ (definisi)
- (2) $C(n, r) = C(n, n - r)$ ✔ (keduanya 120)
- (3) $P(5, 2) = 5 \times 4 = 20$, bukan 10 ✘
- (4) $C(6, 2) = 15$, bukan 30 ✘
- (5) $\frac{120}{6} = 20$ ✔

**22. Jawaban: (1), (4), (5)**  
Nomor antrean (2) dan jabatan ketua–wakil (3) memperhatikan urutan → permutasi.

**23. Jawaban: (1), (2), (4)**
- (2) jumlah 7: 6 pasangan → $\frac{6}{36} = \frac{1}{6}$ ✔
- (3) kembar: $(1,1), \dots, (6,6)$ → 6 pasangan → $\frac{1}{6}$, bukan $\frac{1}{12}$ ✘
- (4) jumlah maksimum 12, sehingga jumlah 13 mustahil ✔
- (5) jumlah 10, 11, 12: $3 + 2 + 1 = 6$ pasangan → $\frac{1}{6}$, bukan $\frac{1}{4}$ ✘

**24. Jawaban: (1), (2), (3)**  
Saling lepas → $P(A \cap B) = 0$ dan $P(A \cup B) = 0{,}3 + 0{,}5 = 0{,}8$. $P(A^c) = 1 - 0{,}3 = 0{,}7$.  
Saling bebas mensyaratkan $P(A \cap B) = 0{,}3 \times 0{,}5 = 0{,}15 \neq 0$ → **tidak** saling bebas ✘.

**25. Jawaban: (1), (2), (4)**  
Total 10 bola. (1) $\frac{3}{10}$ ✔ · (2) $\frac{5}{10}$ ✔ · (3) $\frac{3 + 2}{10} = 0{,}5$, bukan 0,6 ✘ · (4) tidak ada bola biru ✔ · (5) $\frac{5}{10} = 0{,}5$ ✘

**26. Jawaban: a. B, b. B, c. S, d. B**
- a. $\dfrac{4!}{2!} = 12$ ✔ (U muncul 2 kali)
- b. $4! = 24$ ✔
- c. Diawali U: sisa huruf B, K, U disusun $3! = 6$ cara. Peluang $= \frac{6}{12} = \frac{1}{2}$, bukan $\frac{1}{4}$ ✘
- d. Blok "UU" + B + K → $3! = 6$ ✔ (di dalam blok, kedua U identik sehingga tidak dikali 2)

**27. Jawaban: a. B, b. B, c. B, d. S**  
Suka matematika atau fisika $= 18 + 15 - 8 = 25$.
- a. $30 - 25 = 5$ ✔
- b. Hanya matematika $= 18 - 8 = 10$ → $\frac{10}{30} = \frac{1}{3}$ ✔
- c. $P(F \mid M) = \dfrac{8}{18} = \dfrac{4}{9}$ ✔
- d. Ada 8 siswa yang menyukai keduanya, jadi $M \cap F \neq \varnothing$ → tidak saling lepas ✘

**28. Jawaban: a. B, b. S, c. B, d. S**
- a. $2^3 = 8$ ✔
- b. Tepat 2 angka: $AAG, AGA, GAA$ → $\frac{3}{8}$, bukan $\frac{1}{4}$ ✘
- c. $P(GGG) = \frac{1}{8}$ → $80 \times \frac{1}{8} = 10$ ✔
- d. $1 - P(AAA) = 1 - \frac{1}{8} = \frac{7}{8}$ ✘

**29. Jawaban: a. S, b. B, c. B, d. S**
- a. $P(5, 2) = 5 \times 4 = 20$, bukan 10 ✘
- b. Ketua putri: 2 cara; wakil: sisa 4 orang → $2 \times 4 = 8$ ✔
- c. $C(5, 2) = 10$ ✔
- d. Ketua dan wakil putra: $3 \times 2 = 6$ susunan → $\frac{6}{20} = \frac{3}{10}$, bukan $\frac{3}{5}$ ✘

**30. Jawaban: 36**  
Satuan ganjil $\in \lbrace 1, 3, 5 \rbrace$ → 3 cara. Ratusan: sisa 4 angka. Puluhan: sisa 3 angka.  
$3 \times 4 \times 3 = 36$.

**31. Jawaban: $\frac{1}{15}$**  
$n(S) = C(10, 3) = 120$. Andi dan Budi terpilih, lalu pilih 1 orang lagi dari 8 siswa lain: $C(8, 1) = 8$.  
$P = \frac{8}{120} = \frac{1}{15}$.

**32. Jawaban: 40**  
$P(\text{tidak lulus}) = 1 - 0{,}9 = 0{,}1$. $F_h = 400 \times 0{,}1 = 40$ siswa.

**33. Jawaban: $\frac{7}{36}$**  
Jumlah 5: $(1,4), (2,3), (3,2), (4,1)$ → 4. Jumlah 10: $(4,6), (5,5), (6,4)$ → 3.  
Kedua kejadian saling lepas: $P = \frac{4 + 3}{36} = \frac{7}{36}$.
