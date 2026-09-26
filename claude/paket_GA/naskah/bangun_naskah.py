"""
bangun_naskah.py — membangun makalah_GA_fD.pdf dan makalah_GA_fD.docx dari makalah_GA_fD.md.

    python bangun_naskah.py

Memerlukan pandoc (atau paket Python `pypandoc_binary`) dan XeLaTeX. Sumber
Markdown tetap menjadi satu-satunya naskah induk: skrip ini hanya
menyesuaikan judul, keterangan gambar/tabel, dan nomor persamaan untuk tiap
format keluaran.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile

FOLDER = os.path.dirname(os.path.abspath(__file__))
SUMBER = os.path.join(FOLDER, "makalah_GA_fD.md")

METADATA_PDF = r"""---
title: "Puncak dan Perlambatan Pertumbuhan Struktur di Basin Great Attractor: Sejarah Laju Pertumbuhan Linear f·D dalam Kosmologi ΛCDM"
author: "Muhammad Farhan H — MAN Insan Cendekia Gorontalo, Indonesia"
date: "Draf naskah, 26 September 2026"
lang: id
documentclass: article
classoption: [a4paper]
fontsize: 11pt
geometry: [margin=2.4cm]
linestretch: 1.15
mainfont: "Liberation Serif"
sansfont: "Liberation Sans"
monofont: "DejaVu Sans Mono"
mathfont: "Latin Modern Math"
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
header-includes:
  - \usepackage{caption}
  - \captionsetup{font=small,labelfont=bf,labelsep=period}
  - \AtBeginDocument{\renewcommand{\figurename}{Gambar}\renewcommand{\tablename}{Tabel}}
  - \usepackage{float}
  - \floatplacement{figure}{htbp}
  - \setlength{\emergencystretch}{3em}
---
"""


def pandoc_bin() -> str:
    exe = shutil.which("pandoc")
    if exe:
        return exe
    import pypandoc  # pypandoc_binary membawa pandoc sendiri

    return pypandoc.get_pandoc_path()


def buang_blok_judul(teks: str) -> str:
    """Hapus judul, penulis, dan tanggal di awal (metadata dipasok terpisah)."""
    return re.sub(r"\A# .*?\n\*Draf naskah[^\n]*\*\n", "", teks, flags=re.S)


def gambar_ke_figure(teks: str, ekstensi: str) -> str:
    """![](x.png) + '**Gambar N.** keterangan' -> figure bernomor otomatis."""
    pola = re.compile(r"!\[\]\((\.\./gambar/[^)]+)\.png\)\n\n\*\*Gambar \d+\.\*\* ([^\n]+)\n")

    def ganti(m):
        return f"![{m.group(2)}]({m.group(1)}.{ekstensi}){{width=92%}}\n"

    return pola.sub(ganti, teks)


def tabel_ke_caption(teks: str) -> str:
    """'**Tabel N.** keterangan' sebelum tabel pipa -> caption pandoc bernomor otomatis."""
    return re.sub(r"\*\*Tabel \d+\.\*\* ([^\n]+)\n\n(?=\|)", r": \1\n\n", teks)


def bangun_pdf(teks: str, pandoc: str) -> str:
    teks = buang_blok_judul(teks)
    teks = gambar_ke_figure(teks, "pdf")
    teks = tabel_ke_caption(teks)
    keluaran = os.path.join(FOLDER, "makalah_GA_fD.pdf")
    with tempfile.TemporaryDirectory() as tmp:
        md = os.path.join(tmp, "naskah.md")
        with open(md, "w", encoding="utf-8") as f:
            f.write(METADATA_PDF + "\n" + teks)
        subprocess.run([pandoc, md, "-o", keluaran, "--pdf-engine=xelatex",
                        "--shift-heading-level-by=-1", f"--resource-path={FOLDER}",
                        "-V", "secnumdepth=-1"], check=True, cwd=FOLDER)
    return keluaran


def bangun_docx(teks: str, pandoc: str) -> str:
    # Word tidak mengenal \tag: nomor persamaan ditulis di dalam persamaan
    teks = re.sub(r"\\tag\{(\d+)\}", r"\\qquad (\1)", teks)
    teks = re.sub(r"!\[\]\((\.\./gambar/[^)]+)\)", r"![](\1){width=15cm}", teks)
    keluaran = os.path.join(FOLDER, "makalah_GA_fD.docx")
    with tempfile.TemporaryDirectory() as tmp:
        md = os.path.join(tmp, "naskah.md")
        with open(md, "w", encoding="utf-8") as f:
            f.write(teks)
        subprocess.run([pandoc, md, "-o", keluaran, f"--resource-path={FOLDER}"], check=True,
                       cwd=FOLDER)
    return keluaran


def main():
    with open(SUMBER, encoding="utf-8") as f:
        teks = f.read()
    pandoc = pandoc_bin()
    print("PDF :", bangun_pdf(teks, pandoc))
    print("DOCX:", bangun_docx(teks, pandoc))


if __name__ == "__main__":
    main()
