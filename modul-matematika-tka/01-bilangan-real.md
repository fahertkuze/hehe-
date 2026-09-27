# BAB 1 — BILANGAN REAL

> **Elemen:** Bilangan · **Sub-elemen:** Bilangan Real
>
> **Cakupan TKA:** jenis dan sifat bilangan; operasi bilangan (penjumlahan, pengurangan, perkalian, pembagian, dan gabungannya) beserta sifat komutatif, asosiatif, dan distributif; bilangan berpangkat bilangan bulat atau pecahan (termasuk bentuk akar).

---

## A. Ringkasan Materi

### A.1 Jenis-Jenis Bilangan

Bayangkan bilangan seperti "keluarga besar" yang saling bersarang. Setiap himpunan di bawah ini termasuk di dalam himpunan sesudahnya.

| Himpunan | Simbol | Anggota / Ciri | Contoh |
|---|:--:|---|---|
| Bilangan asli | $\mathbb{N}$ | $1, 2, 3, 4, \dots$ | $1, 7, 100$ |
| Bilangan cacah | $\mathbb{W}$ | $0, 1, 2, 3, \dots$ (asli + nol) | $0, 5, 12$ |
| Bilangan bulat | $\mathbb{Z}$ | $\dots, -2, -1, 0, 1, 2, \dots$ | $-8, 0, 15$ |
| Bilangan rasional | $\mathbb{Q}$ | dapat ditulis $\frac{a}{b}$ ($a, b$ bulat, $b \neq 0$); desimalnya **berhenti** atau **berulang** | $\frac{3}{4},\ -5,\ 0{,}25,\ 0{,}333\dots$ |
| Bilangan irasional | $\mathbb{I}$ | **tidak** dapat ditulis $\frac{a}{b}$; desimalnya tidak berhenti dan tidak berulang | $\sqrt{2},\ \sqrt{3},\ \pi,\ e$ |
| Bilangan real | $\mathbb{R}$ | gabungan rasional dan irasional | semua bilangan di garis bilangan |

$$\mathbb{N} \subset \mathbb{W} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}, \qquad \mathbb{I} \subset \mathbb{R}, \qquad \mathbb{Q} \cap \mathbb{I} = \varnothing$$

**Cara cepat mengenali rasional vs irasional**

- Desimal berhenti ($0{,}125$) atau berulang ($0{,}2727\dots$) → **rasional**.
- Akar dari bilangan yang **bukan** kuadrat sempurna ($\sqrt{2}, \sqrt{12}, \sqrt{50}$) → **irasional**.
- Akar yang hasilnya "bulat/pecahan" ($\sqrt{49} = 7$, $\sqrt{0{,}25} = 0{,}5$, $\sqrt{\tfrac{4}{9}} = \tfrac{2}{3}$) → **rasional**.
- $\pi$ dan $e$ → irasional. Tetapi $\frac{22}{7}$ dan $3{,}14$ hanyalah **pendekatan** $\pi$, jadi keduanya **rasional**.

**Istilah lain yang sering muncul**

- **Bilangan prima**: tepat punya dua faktor (1 dan dirinya sendiri): $2, 3, 5, 7, 11, 13, \dots$ Angka $1$ **bukan** prima; $2$ adalah satu-satunya prima genap.
- **Bilangan komposit**: bilangan asli $> 1$ yang bukan prima: $4, 6, 8, 9, \dots$

**Mengubah desimal berulang menjadi pecahan**

*Cara aljabar.* Misal $x = 0{,}1666\dots$

$$10x = 1{,}666\dots, \qquad 100x = 16{,}666\dots \quad\Rightarrow\quad 100x - 10x = 15 \quad\Rightarrow\quad x = \frac{15}{90} = \frac{1}{6}$$

*Cara cepat.*

- Berulang murni: $0{,}\overline{6} = \frac{6}{9} = \frac{2}{3}$, $\ 0{,}\overline{27} = \frac{27}{99} = \frac{3}{11}$, $\ 0{,}\overline{123} = \frac{123}{999}$.
- Berulang campuran: $0{,}1\overline{6} = \frac{16 - 1}{90} = \frac{15}{90} = \frac{1}{6}$.  
  Pembilang = (semua angka sampai akhir pola pertama) − (angka yang tidak berulang); penyebut = angka 9 sebanyak digit berulang, diikuti angka 0 sebanyak digit tak berulang.

### A.2 Operasi Bilangan dan Sifat-Sifatnya

**Urutan operasi** (wajib!):

1. Tanda kurung
2. Pangkat dan akar
3. Perkalian dan pembagian (kerjakan dari **kiri ke kanan**)
4. Penjumlahan dan pengurangan (kerjakan dari **kiri ke kanan**)

> Contoh: $20 - 12 \div 4 \times 3 = 20 - 3 \times 3 = 20 - 9 = 11$ (bukan $20 - 1 = 19$).

**Sifat-sifat operasi pada bilangan real**

| Sifat | Penjumlahan | Perkalian |
|---|---|---|
| Komutatif (tukar) | $a + b = b + a$ | $a \times b = b \times a$ |
| Asosiatif (kelompok) | $(a + b) + c = a + (b + c)$ | $(a \times b) \times c = a \times (b \times c)$ |
| Distributif (sebaran) | $a(b + c) = ab + ac$ | $a(b - c) = ab - ac$ |
| Unsur identitas | $a + 0 = a$ (identitasnya 0) | $a \times 1 = a$ (identitasnya 1) |
| Invers (lawan/kebalikan) | $a + (-a) = 0$ | $a \times \frac{1}{a} = 1$, $a \neq 0$ |

⚠️ **Pengurangan dan pembagian tidak komutatif dan tidak asosiatif.**  
Contoh: $5 - 3 \neq 3 - 5$ dan $(12 \div 6) \div 2 = 1$, sedangkan $12 \div (6 \div 2) = 4$.

**Sifat tertutup.** Suatu himpunan *tertutup* terhadap operasi jika hasil operasi dua anggotanya **selalu** masih anggota himpunan itu.

| Himpunan | $+$ | $-$ | $\times$ | $\div$ |
|---|:--:|:--:|:--:|:--:|
| Asli | ✓ | ✗ ($2 - 5 = -3$) | ✓ | ✗ ($1 \div 2$) |
| Bulat | ✓ | ✓ | ✓ | ✗ ($1 \div 2$) |
| Rasional | ✓ | ✓ | ✓ | ✓ (pembagi $\neq 0$) |
| Irasional | ✗ ($\sqrt{2} + (-\sqrt{2}) = 0$) | ✗ | ✗ ($\sqrt{2}\cdot\sqrt{2} = 2$) | ✗ ($\sqrt{2} \div \sqrt{2} = 1$) |
| Real | ✓ | ✓ | ✓ | ✓ (pembagi $\neq 0$) |

Fakta penting: **rasional + irasional = irasional**, dan **rasional (≠ 0) × irasional = irasional**.

**Distributif untuk berhitung cepat**

$$25 \times 48 = 25 \times (50 - 2) = 1250 - 50 = 1200, \qquad 99 \times 37 = (100 - 1)\times 37 = 3700 - 37 = 3663$$

### A.3 Bilangan Berpangkat (Eksponen)

$$a^n = \underbrace{a \times a \times \dots \times a}_{n \text{ faktor}} \qquad (a = \text{basis},\ n = \text{pangkat})$$

**Sifat-sifat eksponen** ($a, b \neq 0$):

| No | Sifat | Contoh |
|:--:|---|---|
| 1 | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7 = 128$ |
| 2 | $\dfrac{a^m}{a^n} = a^{m-n}$ | $\dfrac{5^6}{5^4} = 5^2 = 25$ |
| 3 | $(a^m)^n = a^{m n}$ | $(3^2)^3 = 3^6 = 729$ |
| 4 | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| 5 | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $\left(\dfrac{2}{3}\right)^2 = \dfrac{4}{9}$ |
| 6 | $a^0 = 1$ | $2025^0 = 1$ |
| 7 | $a^{-n} = \dfrac{1}{a^n}$ | $2^{-3} = \dfrac{1}{8}$ |
| 8 | $a^{\frac{m}{n}} = \sqrt[n]{a^m} = \left(\sqrt[n]{a}\right)^m$ | $8^{\frac{2}{3}} = \left(\sqrt[3]{8}\right)^2 = 4$ |

**Contoh 1.** $16^{-\frac{3}{4}} = \dfrac{1}{16^{3/4}} = \dfrac{1}{(\sqrt[4]{16})^3} = \dfrac{1}{2^3} = \dfrac{1}{8}$

**Contoh 2.** Sederhanakan $(x^2 y^{-3})^{-2}$.  
$(x^2 y^{-3})^{-2} = x^{-4} y^{6} = \dfrac{y^6}{x^4}$

**Tanda negatif — sering menjebak!**

$$(-2)^4 = 16, \qquad -2^4 = -(2^4) = -16, \qquad (-2)^3 = -8$$

Bilangan negatif berpangkat **genap** → positif; berpangkat **ganjil** → negatif.

**Notasi ilmiah:** $a \times 10^n$ dengan $1 \le a < 10$.  
Contoh: $0{,}00045 = 4{,}5 \times 10^{-4}$ dan $32\ 000\ 000 = 3{,}2 \times 10^{7}$.

**Persamaan eksponen sederhana.** Jika $a^{f(x)} = a^{g(x)}$ (dengan $a > 0$, $a \neq 1$), maka $f(x) = g(x)$.

> Contoh: $4^{x+1} = 8^{x-1} \Rightarrow 2^{2x+2} = 2^{3x-3} \Rightarrow 2x + 2 = 3x - 3 \Rightarrow x = 5$.

### A.4 Bentuk Akar

$$\sqrt{a} = a^{\frac{1}{2}}, \qquad \sqrt[n]{a} = a^{\frac{1}{n}}, \qquad \sqrt{a^2} = |a|$$

**Sifat-sifat** ($a, b \ge 0$):

1. $\sqrt{ab} = \sqrt{a}\cdot\sqrt{b}$ dan $\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}$ ($b \neq 0$)
2. $p\sqrt{a} + q\sqrt{a} = (p + q)\sqrt{a}$ — hanya untuk akar **sejenis**
3. ⚠️ $\sqrt{a} + \sqrt{b} \neq \sqrt{a + b}$. Contoh: $\sqrt{9} + \sqrt{16} = 7$, sedangkan $\sqrt{25} = 5$.

**Menyederhanakan akar:** cari faktor kuadrat sempurna **terbesar**.

$$\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt{2}, \qquad \sqrt{48} = \sqrt{16\cdot 3} = 4\sqrt{3}, \qquad \sqrt{200} = 10\sqrt{2}$$

**Perkalian istimewa**

$$(a + \sqrt{b})(a - \sqrt{b}) = a^2 - b, \qquad (\sqrt{a} + \sqrt{b})^2 = a + b + 2\sqrt{ab}$$

**Merasionalkan penyebut** (menghilangkan akar dari penyebut) — kalikan dengan **sekawan**:

| Bentuk | Kalikan dengan | Hasil |
|---|---|---|
| $\dfrac{c}{\sqrt{b}}$ | $\dfrac{\sqrt{b}}{\sqrt{b}}$ | $\dfrac{c\sqrt{b}}{b}$ |
| $\dfrac{c}{a + \sqrt{b}}$ | $\dfrac{a - \sqrt{b}}{a - \sqrt{b}}$ | $\dfrac{c(a - \sqrt{b})}{a^2 - b}$ |
| $\dfrac{c}{\sqrt{a} - \sqrt{b}}$ | $\dfrac{\sqrt{a} + \sqrt{b}}{\sqrt{a} + \sqrt{b}}$ | $\dfrac{c(\sqrt{a} + \sqrt{b})}{a - b}$ |

> Contoh: $\dfrac{4}{\sqrt{2}} = \dfrac{4\sqrt{2}}{2} = 2\sqrt{2}$ dan $\dfrac{2}{\sqrt{5} - \sqrt{3}} = \dfrac{2(\sqrt{5} + \sqrt{3})}{5 - 3} = \sqrt{5} + \sqrt{3}$.

**Akar bersusun** (bentuk $\sqrt{p \pm 2\sqrt{q}}$). Cari dua bilangan $a > b$ dengan $a + b = p$ dan $a \cdot b = q$:

$$\sqrt{(a + b) + 2\sqrt{ab}} = \sqrt{a} + \sqrt{b}, \qquad \sqrt{(a + b) - 2\sqrt{ab}} = \sqrt{a} - \sqrt{b}$$

> Contoh: $\sqrt{5 + 2\sqrt{6}} = \sqrt{3} + \sqrt{2}$ (karena $3 + 2 = 5$, $3 \times 2 = 6$).  
> Jika belum ada angka 2 di depan akar, buat dulu: $\sqrt{7 - \sqrt{40}} = \sqrt{7 - 2\sqrt{10}} = \sqrt{5} - \sqrt{2}$.

---

## B. Tips & Trik

1. **Samakan basis ke bilangan prima.** $4 = 2^2$, $8 = 2^3$, $16 = 2^4$, $32 = 2^5$, $27 = 3^3$, $81 = 3^4$, $125 = 5^3$, $0{,}25 = 2^{-2}$, $0{,}008 = (0{,}2)^3 = 5^{-3}$.
2. **Hafalkan tabel pangkat** — menghemat banyak waktu:

   | Basis | Pangkat 1, 2, 3, … |
   |:--:|---|
   | 2 | 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 |
   | 3 | 3, 9, 27, 81, 243, 729 |
   | 5 | 5, 25, 125, 625, 3125 |
   | Kuadrat 11–25 | 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625 |
   | Kubik 1–10 | 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000 |

3. **Faktorkan pangkat terkecil.** $2^{n+3} - 2^{n+1} = 2^{n+1}(2^2 - 1) = 3 \cdot 2^{n+1}$.
4. **Bandingkan bilangan berpangkat besar dengan menyamakan pangkatnya.** $2^{30} = (2^3)^{10} = 8^{10}$, $\ 3^{20} = (3^2)^{10} = 9^{10}$, jadi $3^{20} > 2^{30}$.
5. **Sekawan** adalah kunci merasionalkan: pasangan $a + \sqrt{b} \leftrightarrow a - \sqrt{b}$.
6. **Deret teleskopik akar:** $\dfrac{1}{\sqrt{n} + \sqrt{n+1}} = \sqrt{n+1} - \sqrt{n}$ — suku-suku di tengah saling menghapus.
7. **Uji dengan angka.** Kalau ragu dengan jawaban bentuk aljabar (misalnya ada $n$), substitusikan $n = 1$ ke soal dan ke setiap opsi.
8. **Pola $p$ dan $q$ sekawan.** Jika $p = a + \sqrt{b}$ dan $q = a - \sqrt{b}$: $p + q = 2a$ dan $pq = a^2 - b$ (keduanya rasional). Lalu $p^2 + q^2 = (p + q)^2 - 2pq$.
9. **Jebakan klasik:** $-3^2 = -9$; $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$; $(a + b)^2 \neq a^2 + b^2$; $0$ bukan bilangan asli; $1$ bukan prima; $\frac{22}{7}$ rasional; $0^0$ tidak didefinisikan.
10. **Soal pilihan ganda kompleks:** nilai setiap pernyataan satu per satu seperti soal benar–salah, jangan menebak dari "kesan umum".

---

## C. Latihan Soal

> **Petunjuk:** Kerjakan dulu tanpa melihat kunci. Beri tanda pada soal yang ragu, lalu cocokkan dengan pembahasan di bagian D.

### Bagian I — Pilihan Ganda (pilih satu jawaban paling tepat)

**1.** Bilangan berikut yang merupakan bilangan irasional adalah ….

- A. $0{,}125$
- B. $\sqrt{49}$
- C. $\frac{22}{7}$
- D. $\sqrt{12}$
- E. $0{,}333\dots$

**2.** Bentuk pecahan paling sederhana dari $0{,}363636\dots$ adalah ….

- A. $\frac{4}{11}$
- B. $\frac{36}{100}$
- C. $\frac{9}{25}$
- D. $\frac{3}{11}$
- E. $\frac{12}{37}$

**3.** Bentuk pecahan dari $1{,}2333\dots$ (angka 3 berulang) adalah ….

- A. $\frac{123}{100}$
- B. $\frac{11}{9}$
- C. $\frac{12}{10}$
- D. $\frac{41}{33}$
- E. $\frac{37}{30}$

**4.** Pernyataan berikut yang menunjukkan sifat distributif adalah ….

- A. $3 + 5 = 5 + 3$
- B. $(2 \times 3) \times 4 = 2 \times (3 \times 4)$
- C. $4 \times (5 + 6) = 4 \times 5 + 4 \times 6$
- D. $7 + 0 = 7$
- E. $6 \times \frac{1}{6} = 1$

**5.** Operasi yang **tidak** tertutup pada himpunan bilangan bulat adalah ….

- A. penjumlahan
- B. pengurangan
- C. perkalian
- D. pembagian
- E. perpangkatan dengan pangkat bilangan asli

**6.** Hasil dari $-2^2 + (-3)^2 - 12 \div 4 \times 3$ adalah ….

- A. $-4$
- B. $4$
- C. $12$
- D. $-10$
- E. $6$

**7.** Hasil dari $2^5 \times 2^{-3} \div 2^{-2}$ adalah ….

- A. $4$
- B. $16$
- C. $8$
- D. $32$
- E. $\frac{1}{4}$

**8.** Bentuk sederhana dari $\dfrac{(a^3 b^{-2})^2}{a^{-1} b^3}$ adalah ….

- A. $\dfrac{a^5}{b^5}$
- B. $\dfrac{a^7}{b^7}$
- C. $a^7 b$
- D. $\dfrac{a^5}{b}$
- E. $\dfrac{a^6}{b^7}$

**9.** Nilai dari $27^{\frac{2}{3}} + 16^{\frac{3}{4}} - 32^{\frac{2}{5}}$ adalah ….

- A. $11$
- B. $12$
- C. $13$
- D. $15$
- E. $17$

**10.** Nilai dari $\left(\frac{1}{27}\right)^{-\frac{2}{3}} \times 4^{-\frac{1}{2}}$ adalah ….

- A. $\frac{3}{2}$
- B. $\frac{9}{4}$
- C. $6$
- D. $18$
- E. $\frac{9}{2}$

**11.** Bentuk sederhana dari $\sqrt{75} + \sqrt{48} - \sqrt{27}$ adalah ….

- A. $4\sqrt{3}$
- B. $5\sqrt{3}$
- C. $6\sqrt{3}$
- D. $12\sqrt{3}$
- E. $2\sqrt{6}$

**12.** Hasil dari $(2\sqrt{3} + \sqrt{2})(2\sqrt{3} - \sqrt{2})$ adalah ….

- A. $10$
- B. $14$
- C. $8$
- D. $12 - \sqrt{6}$
- E. $10 + 4\sqrt{6}$

**13.** Bentuk rasional dari $\dfrac{6}{3 - \sqrt{3}}$ adalah ….

- A. $3 - \sqrt{3}$
- B. $3 + \sqrt{3}$
- C. $2 + \sqrt{3}$
- D. $6 + 2\sqrt{3}$
- E. $\dfrac{3 + \sqrt{3}}{2}$

**14.** Bentuk sederhana dari $\sqrt{7 + 2\sqrt{10}}$ adalah ….

- A. $\sqrt{7} + \sqrt{10}$
- B. $\sqrt{5} - \sqrt{2}$
- C. $\sqrt{10} + 1$
- D. $\sqrt{5} + \sqrt{2}$
- E. $2 + \sqrt{3}$

**15.** Nilai $x$ yang memenuhi $3^{x+1} = 81^{x-2}$ adalah ….

- A. $1$
- B. $2$
- C. $3$
- D. $4$
- E. $5$

**16.** Urutan bilangan $2^{30}$, $3^{20}$, dan $5^{10}$ dari yang **terkecil** adalah ….

- A. $2^{30},\ 3^{20},\ 5^{10}$
- B. $5^{10},\ 2^{30},\ 3^{20}$
- C. $5^{10},\ 3^{20},\ 2^{30}$
- D. $3^{20},\ 2^{30},\ 5^{10}$
- E. $2^{30},\ 5^{10},\ 3^{20}$

**17.** Massa sebuah bakteri adalah $2{,}5 \times 10^{-12}$ gram. Massa $4 \times 10^{8}$ bakteri sejenis adalah … gram.

- A. $1 \times 10^{-4}$
- B. $6{,}5 \times 10^{-4}$
- C. $1 \times 10^{-2}$
- D. $1 \times 10^{-20}$
- E. $1 \times 10^{-3}$

**18.** Jika $2^x = 5$, maka nilai $4^{x+1}$ adalah ….

- A. $20$
- B. $25$
- C. $50$
- D. $100$
- E. $125$

**19.** Bentuk sederhana dari $\dfrac{2^{n+2} - 2^{n}}{2^{n+1}}$ adalah ….

- A. $\frac{3}{2}$
- B. $\frac{1}{2}$
- C. $1$
- D. $2$
- E. $2^n$

**20.** Diketahui $a = \sqrt{2} + 1$ dan $b = \sqrt{2} - 1$. Nilai $\dfrac{a}{b} + \dfrac{b}{a}$ adalah ….

- A. $2$
- B. $2\sqrt{2}$
- C. $4$
- D. $6$
- E. $8$

### Bagian II — Pilihan Ganda Kompleks (jawaban benar bisa lebih dari satu)

**21.** Manakah yang merupakan bilangan rasional? *Pilih semua yang benar.*

- ☐ (1) $\sqrt{0{,}25}$
- ☐ (2) $\pi$
- ☐ (3) $0{,}121212\dots$
- ☐ (4) $\dfrac{\sqrt{8}}{\sqrt{2}}$
- ☐ (5) $\sqrt{5}$

**22.** Untuk sembarang bilangan real $a, b, c$ (pembagi tidak nol), pernyataan yang **selalu benar** adalah ….

- ☐ (1) $a - b = b - a$
- ☐ (2) $(a + b) + c = a + (b + c)$
- ☐ (3) $a \times (b - c) = ab - ac$
- ☐ (4) $(a \div b) \div c = a \div (b \div c)$
- ☐ (5) Invers perkalian dari $-\frac{2}{3}$ adalah $-\frac{3}{2}$

**23.** Bentuk-bentuk berikut yang bernilai $4$ adalah ….

- ☐ (1) $16^{\frac{1}{2}}$
- ☐ (2) $8^{\frac{2}{3}}$
- ☐ (3) $2^{-2}$
- ☐ (4) $\left(\frac{1}{2}\right)^{-2}$
- ☐ (5) $64^{\frac{1}{2}}$

**24.** Pernyataan tentang bentuk akar berikut yang benar adalah ….

- ☐ (1) $\sqrt{2} + \sqrt{3} = \sqrt{5}$
- ☐ (2) $\sqrt{2} \times \sqrt{8} = 4$
- ☐ (3) $\dfrac{\sqrt{18}}{\sqrt{2}} = 3$
- ☐ (4) $(\sqrt{3} + 1)^2 = 4 + 2\sqrt{3}$
- ☐ (5) $\sqrt{9 + 16} = 3 + 4$

**25.** Diketahui $x = 2^{10}$. Pernyataan yang benar adalah ….

- ☐ (1) $\sqrt{x} = 32$
- ☐ (2) $x^{\frac{1}{5}} = 4$
- ☐ (3) $4^5 = x$
- ☐ (4) $\dfrac{x}{2^5} = 2^2$
- ☐ (5) $x > 1000$

### Bagian III — Benar atau Salah

**26.** Tentukan benar (B) atau salah (S) setiap pernyataan tentang jenis bilangan berikut.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Setiap bilangan bulat adalah bilangan rasional. | ☐ | ☐ |
| b | $0$ termasuk bilangan asli. | ☐ | ☐ |
| c | Hasil kali dua bilangan irasional selalu irasional. | ☐ | ☐ |
| d | Jumlah sebuah bilangan rasional dan sebuah bilangan irasional selalu irasional. | ☐ | ☐ |

**27.** Diketahui $p = 3 + \sqrt{5}$ dan $q = 3 - \sqrt{5}$.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | $p + q = 6$ | ☐ | ☐ |
| b | $pq = 4$ | ☐ | ☐ |
| c | $p^2 + q^2 = 28$ | ☐ | ☐ |
| d | $\dfrac{1}{p} + \dfrac{1}{q} = \dfrac{3}{4}$ | ☐ | ☐ |

**28.** Tentukan benar atau salah.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | $(-3)^2 = -3^2$ | ☐ | ☐ |
| b | $5^0 + 0^5 = 1$ | ☐ | ☐ |
| c | $(2^3)^2 = 2^{(3^2)}$ | ☐ | ☐ |
| d | $9^{\frac{1}{2}} \cdot 27^{\frac{1}{3}} = 9$ | ☐ | ☐ |

**29.** Mula-mula terdapat 500 bakteri. Setiap 20 menit, setiap bakteri membelah menjadi 2.

| | Pernyataan | B | S |
|:--:|---|:--:|:--:|
| a | Setelah 1 jam, banyak bakteri adalah 4.000. | ☐ | ☐ |
| b | Setelah 2 jam, banyak bakteri adalah 64.000. | ☐ | ☐ |
| c | Banyak bakteri setelah $t$ menit dapat dinyatakan dengan $500 \cdot 2^{t/20}$. | ☐ | ☐ |
| d | Banyak bakteri mencapai 16.000 setelah 100 menit. | ☐ | ☐ |

### Bagian IV — Isian Singkat

**30.** Nilai dari $(0{,}008)^{-\frac{1}{3}} + (0{,}25)^{-\frac{1}{2}}$ adalah ….

**31.** Nilai dari $\dfrac{1}{\sqrt{1} + \sqrt{2}} + \dfrac{1}{\sqrt{2} + \sqrt{3}} + \dfrac{1}{\sqrt{3} + \sqrt{4}} + \dots + \dfrac{1}{\sqrt{99} + \sqrt{100}}$ adalah ….

**32.** Jika $2^x + 2^x + 2^x + 2^x = 2^{10}$, nilai $x$ adalah ….

**33.** Diketahui $\dfrac{\sqrt{5} - \sqrt{3}}{\sqrt{5} + \sqrt{3}} = a + b\sqrt{15}$ dengan $a$ dan $b$ bilangan bulat. Nilai $a + b$ adalah ….

---

## D. Kunci Jawaban dan Pembahasan

### Kunci Ringkas

| No | Kunci | No | Kunci | No | Kunci | No | Kunci |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | D | 10 | E | 19 | A | 28 | S, B, S, B |
| 2 | A | 11 | C | 20 | D | 29 | B, S, B, B |
| 3 | E | 12 | A | 21 | (1), (3), (4) | 30 | 7 |
| 4 | C | 13 | B | 22 | (2), (3), (5) | 31 | 9 |
| 5 | D | 14 | D | 23 | (1), (2), (4) | 32 | 8 |
| 6 | A | 15 | C | 24 | (2), (3), (4) | 33 | 3 |
| 7 | B | 16 | B | 25 | (1), (2), (3), (5) | | |
| 8 | B | 17 | E | 26 | B, S, S, B | | |
| 9 | C | 18 | D | 27 | B, B, B, S | | |

### Pembahasan

**1. Jawaban: D**
- $0{,}125 = \frac{1}{8}$ → rasional (desimal berhenti).
- $\sqrt{49} = 7$ → rasional.
- $\frac{22}{7}$ → rasional (bentuk pecahan).
- $\sqrt{12} = 2\sqrt{3}$ → $12$ bukan kuadrat sempurna, jadi **irasional**. ✔
- $0{,}333\dots = \frac{1}{3}$ → rasional (desimal berulang).

**2. Jawaban: A**  
Pola berulang "36" terdiri dari 2 digit, sehingga $0{,}\overline{36} = \dfrac{36}{99} = \dfrac{4}{11}$ (pembilang dan penyebut dibagi 9).

**3. Jawaban: E**  
Misal $x = 1{,}2333\dots$  
$10x = 12{,}333\dots$ dan $100x = 123{,}333\dots$  
$100x - 10x = 123{,}333\dots - 12{,}333\dots \Rightarrow 90x = 111 \Rightarrow x = \dfrac{111}{90} = \dfrac{37}{30}$.  
*Cara cepat:* $1{,}2\overline{3} = \dfrac{123 - 12}{90} = \dfrac{111}{90} = \dfrac{37}{30}$.

**4. Jawaban: C**  
Distributif artinya perkalian "disebar" ke setiap suku penjumlahan: $a(b + c) = ab + ac$. Opsi A = komutatif, B = asosiatif, D = identitas penjumlahan, E = invers perkalian.

**5. Jawaban: D**  
Pembagian dua bilangan bulat belum tentu bulat, misalnya $1 \div 2 = \frac{1}{2}$. Penjumlahan, pengurangan, perkalian, dan pemangkatan dengan pangkat asli selalu menghasilkan bilangan bulat.

**6. Jawaban: A**  
Kerjakan sesuai urutan operasi:
- $-2^2 = -(2^2) = -4$ (tanda minus **tidak** ikut dikuadratkan)
- $(-3)^2 = 9$
- $12 \div 4 \times 3$ dikerjakan dari kiri: $3 \times 3 = 9$

Jadi $-4 + 9 - 9 = -4$.

**7. Jawaban: B**  
$2^5 \times 2^{-3} \div 2^{-2} = 2^{5 + (-3) - (-2)} = 2^{4} = 16$.

**8. Jawaban: B**  
$(a^3 b^{-2})^2 = a^6 b^{-4}$. Lalu
$$\frac{a^6 b^{-4}}{a^{-1} b^{3}} = a^{6 - (-1)}\  b^{-4 - 3} = a^7 b^{-7} = \frac{a^7}{b^7}$$

**9. Jawaban: C**
- $27^{\frac{2}{3}} = (3^3)^{\frac{2}{3}} = 3^2 = 9$
- $16^{\frac{3}{4}} = (2^4)^{\frac{3}{4}} = 2^3 = 8$
- $32^{\frac{2}{5}} = (2^5)^{\frac{2}{5}} = 2^2 = 4$

Jadi $9 + 8 - 4 = 13$.

**10. Jawaban: E**  
$\left(\frac{1}{27}\right)^{-\frac{2}{3}} = 27^{\frac{2}{3}} = 9$ dan $4^{-\frac{1}{2}} = \dfrac{1}{\sqrt{4}} = \dfrac{1}{2}$.  
Hasilnya $9 \times \frac{1}{2} = \frac{9}{2}$.

**11. Jawaban: C**  
$\sqrt{75} = 5\sqrt{3}$, $\sqrt{48} = 4\sqrt{3}$, $\sqrt{27} = 3\sqrt{3}$.  
Jadi $5\sqrt{3} + 4\sqrt{3} - 3\sqrt{3} = 6\sqrt{3}$.

**12. Jawaban: A**  
Bentuk $(a + b)(a - b) = a^2 - b^2$:  
$(2\sqrt{3})^2 - (\sqrt{2})^2 = 12 - 2 = 10$.

**13. Jawaban: B**  
Kalikan dengan sekawan $3 + \sqrt{3}$:
$$\frac{6}{3 - \sqrt{3}} \cdot \frac{3 + \sqrt{3}}{3 + \sqrt{3}} = \frac{6(3 + \sqrt{3})}{9 - 3} = \frac{6(3 + \sqrt{3})}{6} = 3 + \sqrt{3}$$

**14. Jawaban: D**  
Cari dua bilangan yang jumlahnya $7$ dan hasil kalinya $10$: yaitu $5$ dan $2$.  
$\sqrt{7 + 2\sqrt{10}} = \sqrt{5} + \sqrt{2}$.  
*Cek:* $(\sqrt{5} + \sqrt{2})^2 = 5 + 2 + 2\sqrt{10} = 7 + 2\sqrt{10}$ ✔

**15. Jawaban: C**  
$81 = 3^4$, sehingga $3^{x+1} = 3^{4(x-2)} = 3^{4x - 8}$.  
$x + 1 = 4x - 8 \Rightarrow 9 = 3x \Rightarrow x = 3$.

**16. Jawaban: B**  
Samakan pangkatnya menjadi 10:  
$2^{30} = (2^3)^{10} = 8^{10}$, $\ 3^{20} = (3^2)^{10} = 9^{10}$, $\ 5^{10}$.  
Karena $5 < 8 < 9$, urutannya $5^{10} < 2^{30} < 3^{20}$.

**17. Jawaban: E**  
$(2{,}5 \times 10^{-12}) \times (4 \times 10^{8}) = (2{,}5 \times 4) \times 10^{-12 + 8} = 10 \times 10^{-4} = 1 \times 10^{-3}$ gram.

**18. Jawaban: D**  
$4^{x+1} = 4 \cdot 4^x = 4 \cdot (2^2)^x = 4 \cdot (2^x)^2 = 4 \cdot 5^2 = 100$.

**19. Jawaban: A**  
Faktorkan $2^n$ dari pembilang:
$$\frac{2^{n+2} - 2^n}{2^{n+1}} = \frac{2^n(2^2 - 1)}{2^n \cdot 2} = \frac{3}{2}$$
*Cek cepat:* ambil $n = 1$: $\dfrac{8 - 2}{4} = \dfrac{6}{4} = \dfrac{3}{2}$ ✔

**20. Jawaban: D**  
$ab = (\sqrt{2} + 1)(\sqrt{2} - 1) = 2 - 1 = 1$.  
$a^2 + b^2 = (3 + 2\sqrt{2}) + (3 - 2\sqrt{2}) = 6$.
$$\frac{a}{b} + \frac{b}{a} = \frac{a^2 + b^2}{ab} = \frac{6}{1} = 6$$

**21. Jawaban: (1), (3), (4)**
- (1) $\sqrt{0{,}25} = 0{,}5$ → rasional ✔
- (2) $\pi$ → irasional ✘
- (3) $0{,}\overline{12} = \frac{12}{99} = \frac{4}{33}$ → rasional ✔
- (4) $\dfrac{\sqrt{8}}{\sqrt{2}} = \sqrt{4} = 2$ → rasional ✔
- (5) $\sqrt{5}$ → irasional ✘

**22. Jawaban: (2), (3), (5)**
- (1) Salah, pengurangan tidak komutatif ($5 - 3 \neq 3 - 5$).
- (2) Benar, sifat asosiatif penjumlahan.
- (3) Benar, sifat distributif perkalian terhadap pengurangan.
- (4) Salah, pembagian tidak asosiatif: $(12 \div 6) \div 2 = 1$, sedangkan $12 \div (6 \div 2) = 4$.
- (5) Benar, karena $-\frac{2}{3} \times \left(-\frac{3}{2}\right) = 1$.

**23. Jawaban: (1), (2), (4)**
- (1) $16^{\frac{1}{2}} = \sqrt{16} = 4$ ✔
- (2) $8^{\frac{2}{3}} = (\sqrt[3]{8})^2 = 2^2 = 4$ ✔
- (3) $2^{-2} = \frac{1}{4}$ ✘
- (4) $\left(\frac{1}{2}\right)^{-2} = 2^2 = 4$ ✔
- (5) $64^{\frac{1}{2}} = 8$ ✘

**24. Jawaban: (2), (3), (4)**
- (1) Salah: $\sqrt{2} + \sqrt{3} \approx 1{,}414 + 1{,}732 = 3{,}146$, sedangkan $\sqrt{5} \approx 2{,}236$.
- (2) $\sqrt{2 \times 8} = \sqrt{16} = 4$ ✔
- (3) $\sqrt{18 \div 2} = \sqrt{9} = 3$ ✔
- (4) $(\sqrt{3})^2 + 2\sqrt{3} + 1 = 4 + 2\sqrt{3}$ ✔
- (5) Salah: $\sqrt{25} = 5 \neq 7$.

**25. Jawaban: (1), (2), (3), (5)**
- (1) $\sqrt{2^{10}} = 2^5 = 32$ ✔
- (2) $(2^{10})^{\frac{1}{5}} = 2^2 = 4$ ✔
- (3) $4^5 = (2^2)^5 = 2^{10}$ ✔
- (4) $\dfrac{2^{10}}{2^5} = 2^5$, bukan $2^2$ ✘
- (5) $2^{10} = 1024 > 1000$ ✔

**26. Jawaban: a. B, b. S, c. S, d. B**
- a. Benar: setiap bilangan bulat $n$ bisa ditulis $\frac{n}{1}$.
- b. Salah: bilangan asli dimulai dari 1. Angka 0 termasuk bilangan cacah.
- c. Salah: contoh penyangkal $\sqrt{2} \times \sqrt{2} = 2$ (rasional).
- d. Benar: jika $r + i$ rasional, maka $i = (r + i) - r$ juga rasional, dan itu mustahil.

**27. Jawaban: a. B, b. B, c. B, d. S**
- a. $p + q = (3 + \sqrt{5}) + (3 - \sqrt{5}) = 6$ ✔
- b. $pq = 9 - 5 = 4$ ✔
- c. $p^2 + q^2 = (p + q)^2 - 2pq = 36 - 8 = 28$ ✔
- d. $\dfrac{1}{p} + \dfrac{1}{q} = \dfrac{p + q}{pq} = \dfrac{6}{4} = \dfrac{3}{2}$, bukan $\dfrac{3}{4}$ ✘

**28. Jawaban: a. S, b. B, c. S, d. B**
- a. $(-3)^2 = 9$, sedangkan $-3^2 = -9$. Salah.
- b. $5^0 = 1$ dan $0^5 = 0$, jumlahnya $1$. Benar.
- c. $(2^3)^2 = 2^6 = 64$, sedangkan $2^{(3^2)} = 2^9 = 512$. Salah.
- d. $9^{\frac{1}{2}} = 3$ dan $27^{\frac{1}{3}} = 3$, hasil kalinya $9$. Benar.

**29. Jawaban: a. B, b. S, c. B, d. B**  
Setiap 20 menit jumlahnya dikali 2, jadi setelah $t$ menit terjadi $\frac{t}{20}$ kali pembelahan: $N(t) = 500 \cdot 2^{t/20}$ (pernyataan c benar).
- a. 1 jam = 60 menit → $2^3 = 8$ → $500 \times 8 = 4000$ ✔
- b. 2 jam = 120 menit → $2^6 = 64$ → $500 \times 64 = 32\ 000$, bukan $64\ 000$ ✘
- d. $500 \cdot 2^{t/20} = 16\ 000 \Rightarrow 2^{t/20} = 32 = 2^5 \Rightarrow t = 100$ menit ✔

**30. Jawaban: 7**  
$0{,}008 = \dfrac{8}{1000} = \left(\dfrac{2}{10}\right)^3 = (0{,}2)^3$, sehingga $(0{,}008)^{-\frac{1}{3}} = (0{,}2)^{-1} = 5$.  
$(0{,}25)^{-\frac{1}{2}} = \left(\dfrac{1}{4}\right)^{-\frac{1}{2}} = 4^{\frac{1}{2}} = 2$.  
Jumlahnya $5 + 2 = 7$.

**31. Jawaban: 9**  
Rasionalkan satu suku: $\dfrac{1}{\sqrt{n} + \sqrt{n+1}} \cdot \dfrac{\sqrt{n+1} - \sqrt{n}}{\sqrt{n+1} - \sqrt{n}} = \dfrac{\sqrt{n+1} - \sqrt{n}}{(n + 1) - n} = \sqrt{n+1} - \sqrt{n}$.  
Jumlahnya menjadi
$$(\sqrt{2} - \sqrt{1}) + (\sqrt{3} - \sqrt{2}) + \dots + (\sqrt{100} - \sqrt{99}) = \sqrt{100} - \sqrt{1} = 10 - 1 = 9$$
Semua suku di tengah saling menghapus (teleskopik).

**32. Jawaban: 8**  
$2^x + 2^x + 2^x + 2^x = 4 \cdot 2^x = 2^2 \cdot 2^x = 2^{x+2}$.  
$2^{x+2} = 2^{10} \Rightarrow x = 8$.

**33. Jawaban: 3**  
Kalikan dengan sekawan penyebut:
$$\frac{\sqrt{5} - \sqrt{3}}{\sqrt{5} + \sqrt{3}} \cdot \frac{\sqrt{5} - \sqrt{3}}{\sqrt{5} - \sqrt{3}} = \frac{5 + 3 - 2\sqrt{15}}{5 - 3} = \frac{8 - 2\sqrt{15}}{2} = 4 - \sqrt{15}$$
Jadi $a = 4$, $b = -1$, dan $a + b = 3$.
