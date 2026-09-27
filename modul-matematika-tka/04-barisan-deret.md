# BAB 4 — BARISAN DAN DERET

> **Elemen:** Aljabar · **Sub-elemen:** Barisan dan Deret
>
> **Cakupan TKA:** barisan dan deret aritmetika; barisan dan deret geometri.  
> **Batasan:** penerapan barisan dan deret, termasuk dalam masalah **pertumbuhan, peluruhan, bunga tunggal, dan bunga majemuk**.

---

## A. Ringkasan Materi

### A.1 Pengertian

- **Barisan** adalah urutan bilangan yang mengikuti pola tertentu: $U_1, U_2, U_3, \dots, U_n$.  
  $U_n$ disebut **suku ke-$n$**.
- **Deret** adalah **jumlah** suku-suku barisan: $S_n = U_1 + U_2 + \dots + U_n$.
- Hubungan penting: $U_n = S_n - S_{n-1}$ dan $U_1 = S_1$.

### A.2 Barisan dan Deret Aritmetika

Barisan aritmetika memiliki **selisih (beda) tetap** antara dua suku berurutan.

$$b = U_2 - U_1 = U_3 - U_2 = \dots$$

| Rumus | Keterangan |
|---|---|
| $U_n = a + (n - 1)b$ | suku ke-$n$ ($a = U_1$ = suku pertama) |
| $S_n = \dfrac{n}{2}\big(2a + (n - 1)b\big) = \dfrac{n}{2}(a + U_n)$ | jumlah $n$ suku pertama |
| $U_t = \dfrac{a + U_n}{2}$ | suku tengah ($n$ ganjil) |
| $b' = \dfrac{b}{k + 1}$ | beda baru jika di antara dua suku berurutan disisipkan $k$ bilangan |
| $b = \dfrac{U_p - U_q}{p - q}$ | beda dari dua suku yang diketahui |

> **Contoh 1.** Barisan $3, 7, 11, 15, \dots$ memiliki $a = 3$ dan $b = 4$.  
> $U_n = 3 + (n - 1)4 = 4n - 1$, sehingga $U_{20} = 79$.  
> $S_{20} = \dfrac{20}{2}(3 + 79) = 10 \times 82 = 820$.

> **Contoh 2.** Diketahui $U_3 = 10$ dan $U_7 = 22$. Maka $b = \dfrac{22 - 10}{7 - 3} = 3$ dan $a = U_3 - 2b = 4$.

**Ciri khas:** jika $S_n$ berbentuk $pn^2 + qn$ (fungsi kuadrat dalam $n$ tanpa konstanta), deretnya aritmetika dengan $b = 2p$ dan $a = p + q$.

### A.3 Barisan dan Deret Geometri

Barisan geometri memiliki **perbandingan (rasio) tetap** antara dua suku berurutan.

$$r = \frac{U_2}{U_1} = \frac{U_3}{U_2} = \dots$$

| Rumus | Keterangan |
|---|---|
| $U_n = a r^{n-1}$ | suku ke-$n$ |
| $S_n = \dfrac{a(r^n - 1)}{r - 1}$ (untuk $r > 1$) atau $S_n = \dfrac{a(1 - r^n)}{1 - r}$ (untuk $r < 1$) | jumlah $n$ suku pertama |
| $U_t = \sqrt{a \cdot U_n}$ | suku tengah ($n$ ganjil) |
| $r' = \sqrt[k+1]{r}$ | rasio baru jika disisipkan $k$ bilangan |
| $r^{p - q} = \dfrac{U_p}{U_q}$ | rasio dari dua suku yang diketahui |

> **Contoh.** $2, 6, 18, 54, \dots$ memiliki $a = 2$, $r = 3$.  
> $U_6 = 2 \cdot 3^5 = 486$ dan $S_6 = \dfrac{2(3^6 - 1)}{3 - 1} = 728$.

**Deret geometri tak hingga.** Jika $-1 < r < 1$ (deret **konvergen**):

$$S_\infty = \frac{a}{1 - r}$$

Jika $r \le -1$ atau $r \ge 1$, deretnya **divergen** (jumlahnya tidak terbatas).

> **Contoh.** $12 + 6 + 3 + \dots = \dfrac{12}{1 - \frac{1}{2}} = 24$.

**Bola memantul.** Bola dijatuhkan dari ketinggian $h$ dan setiap kali memantul mencapai $\frac{p}{q}$ tinggi sebelumnya:

$$\text{Panjang lintasan total} = h \cdot \frac{q + p}{q - p}$$

Jika bola **dilempar ke atas** dari tanah hingga tinggi $h$ lalu jatuh dan memantul dengan rasio yang sama: panjang lintasan $= \dfrac{2hq}{q - p}$.

### A.4 Tiga Suku Berurutan

| Jenis | Misalkan | Syarat |
|---|---|---|
| Aritmetika | $a - b,\ a,\ a + b$ | $2U_2 = U_1 + U_3$ |
| Geometri | $\dfrac{a}{r},\ a,\ ar$ | $(U_2)^2 = U_1 \cdot U_3$ |

### A.5 Penerapan: Pertumbuhan, Peluruhan, dan Bunga

| Masalah | Rumus | Jenis barisan |
|---|---|---|
| **Bunga tunggal** (bunga dihitung dari modal awal saja) | $M_n = M_0(1 + n\ i)$; besar bunga $= M_0 \cdot i \cdot n$ | aritmetika |
| **Bunga majemuk** (bunga ikut berbunga) | $M_n = M_0(1 + i)^n$ | geometri |
| **Pertumbuhan** (penduduk, bakteri, investasi) | $P_n = P_0(1 + p)^n$ | geometri |
| **Peluruhan / penyusutan** (radioaktif, harga mobil) | $P_n = P_0(1 - p)^n$ | geometri |
| **Waktu paruh** $T$ | $P_t = P_0\left(\tfrac{1}{2}\right)^{t/T}$ | geometri |

Keterangan: $M_0$ = modal awal, $i$ = suku bunga per periode, $n$ = banyak periode, $p$ = persentase pertumbuhan/penyusutan per periode.

⚠️ **Satuan waktu harus cocok.** Jika bunga 6% **per tahun** dan waktunya 2 tahun 6 bulan, gunakan $n = 2{,}5$ (bunga tunggal). Jika bunga 1% **per bulan**, gunakan $n$ dalam bulan.

> **Contoh bunga tunggal.** Rp5.000.000 dengan bunga tunggal 6% per tahun selama 2,5 tahun.  
> Bunga $= 5\ 000\ 000 \times 0{,}06 \times 2{,}5 = 750\ 000$. Tabungan akhir Rp5.750.000.

> **Contoh bunga majemuk.** Rp10.000.000 dengan bunga majemuk 10% per tahun selama 3 tahun.  
> $M_3 = 10\ 000\ 000 \times (1{,}1)^3 = 10\ 000\ 000 \times 1{,}331 = 13\ 310\ 000$.

> **Contoh peluruhan.** Harga mobil Rp200.000.000 menyusut 20% per tahun. Setelah 2 tahun:  
> $200\ 000\ 000 \times (0{,}8)^2 = 128\ 000\ 000$.

---

## B. Tips & Trik

1. **Kenali jenis barisan dulu.** Cek selisih (aritmetika) atau perbandingan (geometri) antara suku-suku berurutan.
2. **Dua suku diketahui:** aritmetika → $b = \dfrac{U_p - U_q}{p - q}$; geometri → bagi kedua suku untuk mendapat $r^{p - q}$.
3. **$S_n$ diketahui, cari $U_n$:** gunakan $U_n = S_n - S_{n-1}$. Contoh cepat: $S_n = 2n^2 + 3n \Rightarrow U_n = 4n + 1$ (koefisien $n^2$ dikali 2 menjadi beda; $U_1 = S_1$).
4. **Jumlah bilangan kelipatan $k$ antara $p$ dan $q$:** tentukan suku pertama, suku terakhir, dan banyak suku $n = \dfrac{U_n - a}{k} + 1$, lalu $S_n = \dfrac{n}{2}(a + U_n)$.
5. **Bunga tunggal = aritmetika; bunga majemuk = geometri.** Kata "majemuk", "pertumbuhan", "persen dari tahun sebelumnya" → pangkat.
6. **Hafalkan pangkat yang sering muncul:** $1{,}1^2 = 1{,}21$; $1{,}1^3 = 1{,}331$; $1{,}1^4 = 1{,}4641$; $1{,}05^2 = 1{,}1025$; $1{,}02^2 = 1{,}0404$; $0{,}9^2 = 0{,}81$; $0{,}9^3 = 0{,}729$; $0{,}8^2 = 0{,}64$; $0{,}8^3 = 0{,}512$.
7. **Waktu paruh / pembelahan:** hitung dulu "berapa kali" peristiwa terjadi ($\frac{\text{waktu total}}{\text{waktu per peristiwa}}$), lalu pangkatkan.
8. **Bola memantul:** langsung pakai $h\dfrac{q + p}{q - p}$ (dijatuhkan).
9. **Soal "terdapat tiga bilangan":** misalkan simetris ($a - b, a, a + b$ atau $\frac{a}{r}, a, ar$) agar perhitungan jauh lebih ringan.
10. **Periksa $n$.** Pada soal "berapa suku", pastikan $n$ bilangan asli. Jika tidak bulat, bilangan itu **bukan** suku barisan.

---

## C. Latihan Soal

### Bagian I — Pilihan Ganda

**1.** Suku ke-20 barisan $3, 7, 11, 15, \dots$ adalah ….

- A. $79$
- B. $75$
- C. $77$
- D. $81$
- E. $83$

**2.** Suku ke-3 dan suku ke-7 suatu barisan aritmetika berturut-turut adalah 10 dan 22. Suku ke-15 barisan tersebut adalah ….

- A. $40$
- B. $43$
- C. $44$
- D. $46$
- E. $49$

**3.** Jumlah 20 suku pertama deret $2 + 5 + 8 + 11 + \dots$ adalah ….

- A. $590$
- B. $610$
- C. $620$
- D. $630$
- E. $640$

**4.** Jumlah semua bilangan asli antara 1 dan 100 yang habis dibagi 3 adalah ….

- A. $1.683$
- B. $1.620$
- C. $1.717$
- D. $1.650$
- E. $1.584$

**5.** Jumlah $n$ suku pertama suatu deret aritmetika dinyatakan dengan $S_n = 2n^2 + 3n$. Suku ke-10 deret tersebut adalah ….

- A. $38$
- B. $39$
- C. $40$
- D. $43$
- E. $41$

**6.** Suku ke-7 barisan geometri $2, 6, 18, \dots$ adalah ….

- A. $486$
- B. $729$
- C. $1.458$
- D. $2.916$
- E. $4.374$

**7.** Suku ke-2 dan suku ke-5 suatu barisan geometri berturut-turut adalah 6 dan 48. Jumlah 6 suku pertamanya adalah ….

- A. $93$
- B. $189$
- C. $192$
- D. $381$
- E. $96$

**8.** Jumlah deret geometri tak hingga $12 + 6 + 3 + \frac{3}{2} + \dots$ adalah ….

- A. $18$
- B. $21$
- C. $36$
- D. $24$
- E. tak hingga

**9.** Di antara bilangan 5 dan 41 disisipkan 5 bilangan sehingga terbentuk barisan aritmetika. Jumlah semua suku barisan yang terbentuk adalah ….

- A. $138$
- B. $150$
- C. $161$
- D. $175$
- E. $184$

**10.** Tiga bilangan membentuk barisan aritmetika. Jumlah ketiga bilangan itu 24 dan hasil kalinya 440. Bilangan terbesarnya adalah ….

- A. $9$
- B. $10$
- C. $12$
- D. $13$
- E. $11$

**11.** Pak Andi menabung setiap bulan. Pada bulan pertama ia menabung Rp50.000, dan setiap bulan berikutnya tabungannya Rp10.000 lebih banyak daripada bulan sebelumnya. Jumlah seluruh uang yang ditabung selama 2 tahun adalah ….

- A. Rp3.960.000
- B. Rp3.600.000
- C. Rp3.840.000
- D. Rp4.080.000
- E. Rp4.200.000

**12.** Sebuah gedung pertunjukan memiliki 20 baris kursi. Baris pertama terdiri atas 15 kursi, dan setiap baris berikutnya bertambah 3 kursi. Banyak kursi seluruhnya adalah ….

- A. $780$
- B. $820$
- C. $900$
- D. $870$
- E. $945$

**13.** Budi menabung Rp5.000.000 di bank dengan bunga tunggal 6% per tahun. Besar tabungan Budi setelah 2 tahun 6 bulan adalah ….

- A. Rp5.600.000
- B. Rp5.750.000
- C. Rp5.800.000
- D. Rp6.000.000
- E. Rp5.300.000

**14.** Modal sebesar Rp10.000.000 diinvestasikan dengan bunga majemuk 10% per tahun. Besar modal setelah 3 tahun adalah ….

- A. Rp13.000.000
- B. Rp13.100.000
- C. Rp13.410.000
- D. Rp14.641.000
- E. Rp13.310.000

**15.** Penduduk suatu kota berjumlah 200.000 jiwa dan bertambah 2% setiap tahun. Banyak penduduk kota itu setelah 2 tahun adalah … jiwa.

- A. 204.000
- B. 208.000
- C. 208.080
- D. 208.800
- E. 212.000

**16.** Sebuah mobil dibeli seharga Rp200.000.000. Setiap tahun harganya menyusut 20% dari harga tahun sebelumnya. Harga mobil setelah 3 tahun adalah ….

- A. Rp102.400.000
- B. Rp80.000.000
- C. Rp120.000.000
- D. Rp128.000.000
- E. Rp160.000.000

**17.** Suatu zat radioaktif bermassa 160 gram meluruh menjadi setengahnya setiap 5 tahun. Massa zat yang tersisa setelah 20 tahun adalah … gram.

- A. $5$
- B. $20$
- C. $40$
- D. $10$
- E. $80$

**18.** Sebuah bola dijatuhkan dari ketinggian 10 m. Setiap kali memantul, bola mencapai $\frac{3}{4}$ tinggi sebelumnya. Panjang lintasan bola sampai berhenti adalah … m.

- A. $40$
- B. $70$
- C. $50$
- D. $60$
- E. $80$

**19.** Mula-mula terdapat 100 bakteri. Setiap 15 menit, setiap bakteri membelah menjadi dua. Banyak bakteri setelah 2 jam adalah ….

- A. $1.600$
- B. $3.200$
- C. $12.800$
- D. $51.200$
- E. $25.600$

**20.** Tiga bilangan membentuk barisan aritmetika dengan beda 4. Jika suku ketiga ditambah 8, ketiga bilangan tersebut membentuk barisan geometri. Jumlah ketiga bilangan semula adalah ….

- A. $12$
- B. $15$
- C. $18$
- D. $21$
- E. $26$

### Bagian II — Pilihan Ganda Kompleks (jawaban benar bisa lebih dari satu)

**21.** Diketahui barisan $5, 9, 13, 17, \dots$ Pernyataan yang benar adalah ….

- ☐ (1) Barisan tersebut adalah barisan aritmetika dengan beda 4.
- ☐ (2) Rumus suku ke-$n$-nya $U_n = 4n + 1$.
- ☐ (3) $U_{25} = 101$
- ☐ (4) $S_{10} = 240$
- ☐ (5) Bilangan 100 merupakan salah satu suku barisan tersebut.

**22.** Diketahui barisan geometri $81, 27, 9, 3, \dots$ Pernyataan yang benar adalah ….

- ☐ (1) Rasionya $\frac{1}{3}$.
- ☐ (2) $U_6 = \frac{1}{3}$
- ☐ (3) Jumlah tak hingganya $121{,}5$.
- ☐ (4) Barisan tersebut merupakan barisan naik.
- ☐ (5) $U_n = 3^{5 - n}$

**23.** Situasi berikut yang dapat dimodelkan dengan **barisan geometri** adalah ….

- ☐ (1) Tabungan dengan bunga tunggal.
- ☐ (2) Tabungan dengan bunga majemuk.
- ☐ (3) Banyak bakteri yang membelah menjadi dua setiap jam.
- ☐ (4) Gaji yang naik Rp100.000 setiap tahun.
- ☐ (5) Harga mobil yang menyusut 10% dari harga tahun sebelumnya.

**24.** Jumlah $n$ suku pertama suatu deret dirumuskan $S_n = n^2 + 4n$. Pernyataan yang benar adalah ….

- ☐ (1) $U_1 = 5$
- ☐ (2) Beda deret tersebut adalah 2.
- ☐ (3) $U_n = 2n + 3$
- ☐ (4) $U_{10} = 24$
- ☐ (5) $S_{10} = 140$

**25.** Deret geometri tak hingga berikut yang **konvergen** (memiliki jumlah) adalah ….

- ☐ (1) $1 + \frac{1}{2} + \frac{1}{4} + \dots$
- ☐ (2) $2 + 4 + 8 + \dots$
- ☐ (3) $9 - 3 + 1 - \frac{1}{3} + \dots$
- ☐ (4) $1 + 1 + 1 + \dots$
- ☐ (5) $5 + 5(0{,}9) + 5(0{,}9)^2 + \dots$

### Bagian III — Benar atau Salah

**26.** Pak Budi menabung Rp2.000.000 di koperasi dengan bunga tunggal 5% per tahun.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Bunga yang diterima setiap tahun adalah Rp100.000. | ☐ | ☐ |
| b | Setelah 4 tahun, tabungannya menjadi Rp2.400.000. | ☐ | ☐ |
| c | Besar tabungan di setiap akhir tahun membentuk barisan geometri. | ☐ | ☐ |
| d | Tabungannya menjadi Rp3.000.000 setelah 10 tahun. | ☐ | ☐ |

**27.** Populasi suatu hewan langka mula-mula 1.000 ekor dan berkurang 10% setiap tahun.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Setelah 1 tahun, populasinya 900 ekor. | ☐ | ☐ |
| b | Setelah 2 tahun, populasinya 800 ekor. | ☐ | ☐ |
| c | Populasi setelah $n$ tahun dirumuskan $P_n = 1\ 000(0{,}9)^n$. | ☐ | ☐ |
| d | Setelah 3 tahun, populasinya 729 ekor. | ☐ | ☐ |

**28.** Suatu barisan aritmetika memiliki $U_4 = 14$ dan $U_9 = 29$.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Bedanya 3. | ☐ | ☐ |
| b | Suku pertamanya 5. | ☐ | ☐ |
| c | $S_{10} = 185$ | ☐ | ☐ |
| d | $U_n = 3n + 1$ | ☐ | ☐ |

**29.** Sebuah bola dijatuhkan dari ketinggian 8 m dan setiap kali memantul mencapai $\frac{1}{2}$ tinggi sebelumnya.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Tinggi pantulan ketiga adalah 1 m. | ☐ | ☐ |
| b | Panjang lintasan bola sampai berhenti adalah 24 m. | ☐ | ☐ |
| c | Tinggi pantulan-pantulan bola membentuk barisan aritmetika. | ☐ | ☐ |
| d | Tinggi pantulan kelima adalah 0,5 m. | ☐ | ☐ |

### Bagian IV — Isian Singkat

**30.** Bilangan 76 adalah suku ke-… dari barisan $4, 7, 10, 13, \dots$

**31.** Jumlah deret geometri $3 + 6 + 12 + \dots + 384$ adalah ….

**32.** Modal Rp4.000.000 disimpan dengan bunga majemuk 5% per tahun. Besar modal setelah 2 tahun adalah Rp….

**33.** Seutas tali dipotong menjadi 5 bagian yang panjangnya membentuk barisan geometri. Potongan terpendek 3 cm dan potongan terpanjang 48 cm. Panjang tali semula adalah … cm.

---

## D. Kunci Jawaban dan Pembahasan

### Kunci Ringkas

| No | Kunci | No | Kunci | No | Kunci | No | Kunci |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | A | 10 | E | 19 | E | 28 | B, B, B, S |
| 2 | D | 11 | A | 20 | C | 29 | B, B, S, S |
| 3 | B | 12 | D | 21 | (1), (2), (3) | 30 | 25 |
| 4 | A | 13 | B | 22 | (1), (2), (3), (5) | 31 | 765 |
| 5 | E | 14 | E | 23 | (2), (3), (5) | 32 | 4.410.000 |
| 6 | C | 15 | C | 24 | (1), (2), (3), (5) | 33 | 93 |
| 7 | B | 16 | A | 25 | (1), (3), (5) | | |
| 8 | D | 17 | D | 26 | B, B, S, B | | |
| 9 | C | 18 | B | 27 | B, S, B, B | | |

### Pembahasan

**1. Jawaban: A**  
$a = 3$, $b = 4$. $U_{20} = 3 + 19 \times 4 = 79$.

**2. Jawaban: D**  
$b = \dfrac{U_7 - U_3}{7 - 3} = \dfrac{22 - 10}{4} = 3$ dan $a = U_3 - 2b = 10 - 6 = 4$.  
$U_{15} = 4 + 14 \times 3 = 46$.

**3. Jawaban: B**  
$a = 2$, $b = 3$. $S_{20} = \dfrac{20}{2}\big(2(2) + 19(3)\big) = 10(4 + 57) = 610$.

**4. Jawaban: A**  
Bilangannya $3, 6, 9, \dots, 99$. Banyak suku $n = \dfrac{99 - 3}{3} + 1 = 33$.  
$S_{33} = \dfrac{33}{2}(3 + 99) = 33 \times 51 = 1\ 683$.

**5. Jawaban: E**  
$U_{10} = S_{10} - S_9 = (200 + 30) - (162 + 27) = 230 - 189 = 41$.  
*Cara cepat:* $U_n = 4n + 1$ (beda $= 2 \times 2 = 4$, $U_1 = S_1 = 5$), sehingga $U_{10} = 41$.

**6. Jawaban: C**  
$a = 2$, $r = 3$. $U_7 = 2 \cdot 3^6 = 2 \times 729 = 1\ 458$.

**7. Jawaban: B**  
$\dfrac{U_5}{U_2} = r^3 = \dfrac{48}{6} = 8 \Rightarrow r = 2$, sehingga $a = \dfrac{U_2}{r} = 3$.  
$S_6 = \dfrac{3(2^6 - 1)}{2 - 1} = 3 \times 63 = 189$.

**8. Jawaban: D**  
$a = 12$, $r = \frac{1}{2}$ (konvergen karena $|r| < 1$).  
$S_\infty = \dfrac{12}{1 - \frac{1}{2}} = 24$.

**9. Jawaban: C**  
Setelah disisipi 5 bilangan, barisan terdiri atas $5 + 2 = 7$ suku dengan $U_1 = 5$ dan $U_7 = 41$.  
$S_7 = \dfrac{7}{2}(5 + 41) = 7 \times 23 = 161$.  
(Bedanya $b' = \dfrac{41 - 5}{5 + 1} = 6$: barisannya $5, 11, 17, 23, 29, 35, 41$.)

**10. Jawaban: E**  
Misal bilangannya $a - b$, $a$, $a + b$.  
Jumlah: $3a = 24 \Rightarrow a = 8$.  
Hasil kali: $(8 - b)(8)(8 + b) = 440 \Rightarrow 64 - b^2 = 55 \Rightarrow b = 3$.  
Bilangannya $5, 8, 11$ → terbesar $11$.

**11. Jawaban: A**  
Deret aritmetika dengan $a = 50\ 000$, $b = 10\ 000$, $n = 24$ bulan.  
$U_{24} = 50\ 000 + 23 \times 10\ 000 = 280\ 000$.  
$S_{24} = \dfrac{24}{2}(50\ 000 + 280\ 000) = 12 \times 330\ 000 = 3\ 960\ 000$.

**12. Jawaban: D**  
$a = 15$, $b = 3$, $n = 20$. $U_{20} = 15 + 19 \times 3 = 72$.  
$S_{20} = \dfrac{20}{2}(15 + 72) = 10 \times 87 = 870$.

**13. Jawaban: B**  
2 tahun 6 bulan $= 2{,}5$ tahun.  
Bunga $= 5\ 000\ 000 \times 6\% \times 2{,}5 = 750\ 000$. Tabungan $= 5\ 750\ 000$.

**14. Jawaban: E**  
$M_3 = 10\ 000\ 000 \times (1{,}1)^3 = 10\ 000\ 000 \times 1{,}331 = 13\ 310\ 000$.

**15. Jawaban: C**  
$P_2 = 200\ 000 \times (1{,}02)^2 = 200\ 000 \times 1{,}0404 = 208\ 080$.  
(Opsi B, 208.000, adalah hasil jika dihitung sebagai bunga tunggal — jebakan!)

**16. Jawaban: A**  
$200\ 000\ 000 \times (1 - 0{,}2)^3 = 200\ 000\ 000 \times 0{,}512 = 102\ 400\ 000$.

**17. Jawaban: D**  
Dalam 20 tahun terjadi $\dfrac{20}{5} = 4$ kali peluruhan.  
$160 \times \left(\frac{1}{2}\right)^4 = \dfrac{160}{16} = 10$ gram.

**18. Jawaban: B**  
$h = 10$, $\frac{p}{q} = \frac{3}{4}$. Panjang lintasan $= 10 \times \dfrac{4 + 3}{4 - 3} = 70$ m.  
*Cara lain:* lintasan turun pertama 10 m; setelah itu setiap pantulan naik lalu turun: $2 \times \dfrac{7{,}5}{1 - 0{,}75} = 60$. Total $10 + 60 = 70$ m.

**19. Jawaban: E**  
2 jam $= 120$ menit $= \dfrac{120}{15} = 8$ kali pembelahan.  
$100 \times 2^8 = 100 \times 256 = 25\ 600$.

**20. Jawaban: C**  
Misal bilangannya $a$, $a + 4$, $a + 8$. Setelah suku ketiga ditambah 8: $a$, $a + 4$, $a + 16$ membentuk barisan geometri.  
$(a + 4)^2 = a(a + 16) \Rightarrow a^2 + 8a + 16 = a^2 + 16a \Rightarrow 16 = 8a \Rightarrow a = 2$.  
Bilangan semula $2, 6, 10$ (jumlah $18$). Cek: $2, 6, 18$ adalah barisan geometri dengan $r = 3$ ✔

**21. Jawaban: (1), (2), (3)**
- (1) $9 - 5 = 13 - 9 = 4$ ✔
- (2) $U_n = 5 + (n - 1)4 = 4n + 1$ ✔
- (3) $U_{25} = 101$ ✔
- (4) $S_{10} = 5(5 + 41) = 230$, bukan 240 ✘
- (5) $4n + 1 = 100 \Rightarrow n = 24{,}75$ (tidak bulat) ✘

**22. Jawaban: (1), (2), (3), (5)**
- (1) $r = \frac{27}{81} = \frac{1}{3}$ ✔
- (2) $U_6 = 81 \cdot \left(\frac{1}{3}\right)^5 = \frac{81}{243} = \frac{1}{3}$ ✔
- (3) $S_\infty = \dfrac{81}{1 - \frac{1}{3}} = \dfrac{81}{\frac{2}{3}} = 121{,}5$ ✔
- (4) Nilai sukunya makin kecil → barisan **turun** ✘
- (5) $U_n = 81 \cdot 3^{-(n-1)} = 3^4 \cdot 3^{1 - n} = 3^{5 - n}$ ✔

**23. Jawaban: (2), (3), (5)**  
Bunga tunggal (1) dan kenaikan tetap Rp100.000 (4) bertambah dengan **selisih tetap** → aritmetika.  
Bunga majemuk (2), pembelahan bakteri (3), dan penyusutan persentase (5) berubah dengan **rasio tetap** → geometri.

**24. Jawaban: (1), (2), (3), (5)**  
$U_1 = S_1 = 1 + 4 = 5$ ✔.  
$U_n = S_n - S_{n-1} = (n^2 + 4n) - \big((n - 1)^2 + 4(n - 1)\big) = 2n + 3$ ✔, dengan beda 2 ✔.  
$U_{10} = 23$, bukan 24 ✘. $S_{10} = 100 + 40 = 140$ ✔.

**25. Jawaban: (1), (3), (5)**  
Konvergen jika $-1 < r < 1$.  
(1) $r = \frac{1}{2}$ ✔ · (2) $r = 2$ ✘ · (3) $r = -\frac{1}{3}$ ✔ · (4) $r = 1$ ✘ · (5) $r = 0{,}9$ ✔

**26. Jawaban: a. B, b. B, c. S, d. B**
- a. $5\% \times 2\ 000\ 000 = 100\ 000$ ✔
- b. $2\ 000\ 000 + 4 \times 100\ 000 = 2\ 400\ 000$ ✔
- c. Setiap tahun bertambah **tetap** Rp100.000 → barisan **aritmetika** ✘
- d. $2\ 000\ 000 + 10 \times 100\ 000 = 3\ 000\ 000$ ✔

**27. Jawaban: a. B, b. S, c. B, d. B**  
Rasio penyusutan $= 1 - 0{,}1 = 0{,}9$.
- a. $1\ 000 \times 0{,}9 = 900$ ✔
- b. $1\ 000 \times 0{,}81 = 810$, bukan 800 ✘
- c. ✔
- d. $1\ 000 \times 0{,}729 = 729$ ✔

**28. Jawaban: a. B, b. B, c. B, d. S**  
$b = \dfrac{29 - 14}{9 - 4} = 3$ ✔ dan $a = 14 - 3 \times 3 = 5$ ✔.  
$S_{10} = \dfrac{10}{2}(2 \cdot 5 + 9 \cdot 3) = 5 \times 37 = 185$ ✔.  
$U_n = 5 + (n - 1)3 = 3n + 2$, bukan $3n + 1$ ✘.

**29. Jawaban: a. B, b. B, c. S, d. S**  
Tinggi pantulan: $4, 2, 1, 0{,}5, 0{,}25, \dots$ (barisan **geometri** dengan $r = \frac{1}{2}$).
- a. Pantulan ke-3 $= 1$ m ✔
- b. $8 \times \dfrac{2 + 1}{2 - 1} = 24$ m ✔
- c. ✘ (geometri, bukan aritmetika)
- d. Pantulan ke-5 $= 0{,}25$ m ✘

**30. Jawaban: 25**  
$a = 4$, $b = 3$ → $U_n = 3n + 1$. $3n + 1 = 76 \Rightarrow n = 25$.

**31. Jawaban: 765**  
$a = 3$, $r = 2$. Suku terakhir: $3 \cdot 2^{n-1} = 384 \Rightarrow 2^{n-1} = 128 = 2^7 \Rightarrow n = 8$.  
$S_8 = \dfrac{3(2^8 - 1)}{2 - 1} = 3 \times 255 = 765$.

**32. Jawaban: Rp4.410.000**  
$M_2 = 4\ 000\ 000 \times (1{,}05)^2 = 4\ 000\ 000 \times 1{,}1025 = 4\ 410\ 000$.

**33. Jawaban: 93 cm**  
$U_1 = 3$ dan $U_5 = 3r^4 = 48 \Rightarrow r^4 = 16 \Rightarrow r = 2$.  
Potongannya $3, 6, 12, 24, 48$. Panjang tali $= 93$ cm.
