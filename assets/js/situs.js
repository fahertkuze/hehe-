/* ==========================================================
   Site script: theme toggle, copy/share links, automatic
   citations, and search + filtering for the research archive.
   No external libraries.
   ========================================================== */
(function () {
  "use strict";

  var $ = function (sel, el) { return (el || document).querySelector(sel); };
  var $$ = function (sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); };

  /* ---------- Notifikasi kecil (toast) ---------- */
  var timerToast;
  function toast(pesan) {
    var el = $("[data-toast]");
    if (!el) return;
    el.textContent = pesan;
    el.classList.add("tampil");
    clearTimeout(timerToast);
    timerToast = setTimeout(function () { el.classList.remove("tampil"); }, 2200);
  }

  /* ---------- Salin ke papan klip ---------- */
  function salin(teks) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(teks);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = teks;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy") ? resolve() : reject(); } catch (e) { reject(e); }
      document.body.removeChild(ta);
    });
  }

  /* ---------- Tema terang / gelap ---------- */
  function initTema() {
    var root = document.documentElement;
    var tombol = $("[data-tombol-tema]");
    if (!tombol) return;
    tombol.addEventListener("click", function () {
      var kini = root.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var baru = kini === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", baru);
      try { localStorage.setItem("tema", baru); } catch (e) { /* abaikan */ }
    });
  }

  /* ---------- Salin tautan, bagikan, cetak ---------- */
  function initBagikan() {
    document.addEventListener("click", function (ev) {
      var t = ev.target.closest("[data-salin-tautan]");
      if (!t) return;
      salin(t.getAttribute("data-salin-tautan")).then(
        function () { toast("Link copied — ready to share"); },
        function () { toast("Couldn't copy the link"); }
      );
    });

    var native = $("[data-bagikan-native]");
    if (native && navigator.share) {
      native.hidden = false;
      native.addEventListener("click", function () {
        navigator.share({
          title: document.title,
          url: (document.querySelector('link[rel="canonical"]') || location).href
        }).catch(function () { /* dibatalkan pengguna */ });
      });
    }

    $$("[data-cetak]").forEach(function (b) {
      b.addEventListener("click", function () { window.print(); });
    });
  }

  /* ---------- Sitasi (APA & BibTeX) ---------- */
  function namaAPA(nama) {
    var b = String(nama).trim().split(/\s+/);
    if (b.length === 1) return b[0];
    var belakang = b.pop();
    return belakang + ", " + b.map(function (x) { return x.charAt(0).toUpperCase() + "."; }).join(" ");
  }

  function penulisAPA(daftar) {
    var n = (daftar || []).map(namaAPA);
    if (n.length === 0) return "";
    if (n.length === 1) return n[0];
    if (n.length > 20) return n.slice(0, 19).join(", ") + ", … " + n[n.length - 1];
    return n.slice(0, -1).join(", ") + ", & " + n[n.length - 1];
  }

  function namaBibtex(nama) {
    var b = String(nama).trim().split(/\s+/);
    if (b.length === 1) return b[0];
    var belakang = b.pop();
    return belakang + ", " + b.join(" ");
  }

  function ascii(s) {
    return String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]/g, "");
  }

  function titikAkhir(s) {
    s = String(s).trim();
    return /[.?!]$/.test(s) ? s : s + ".";
  }

  function buatAPA(d) {
    var bagian = [];
    var p = penulisAPA(d.penulis);
    bagian.push((p ? titikAkhir(p) + " " : "") + "(" + d.tahun + ").");
    var judul = String(d.judul).trim();
    if (d.jenis === "dataset") judul += " [Data set]";
    else if (d.jenis === "presentasi") judul += " [Presentation]";
    else if (d.jenis === "preprint") judul += " [Preprint]";
    bagian.push(titikAkhir(judul));
    if (d.terbitan) bagian.push(titikAkhir(d.terbitan));
    bagian.push(d.doi ? "https://doi.org/" + d.doi : d.url);
    return bagian.join(" ");
  }

  function buatBibtex(d) {
    var pertama = (d.penulis && d.penulis[0]) ? String(d.penulis[0]).trim().split(/\s+/).pop() : "anon";
    var kata = String(d.judul).split(/\s+/).map(ascii).filter(function (w) { return w.length > 3; })[0] || "work";
    var kunci = ascii(pertama) + d.tahun + kata;
    var jenis = d.bibtex || "misc";
    var tempat = {
      article: "journal", inproceedings: "booktitle", mastersthesis: "school",
      phdthesis: "school", techreport: "institution", book: "publisher"
    }[jenis] || "howpublished";

    var kolom = [
      ["title", "{" + d.judul + "}"],
      ["author", (d.penulis || []).map(namaBibtex).join(" and ")],
      ["year", d.tahun]
    ];
    if (d.terbitan) kolom.push([tempat, d.terbitan]);
    if (d.doi) kolom.push(["doi", d.doi]);
    kolom.push(["url", d.doi ? "https://doi.org/" + d.doi : d.url]);
    if (jenis === "misc" && d.labelJenis) kolom.push(["note", d.labelJenis]);

    var lebar = Math.max.apply(null, kolom.map(function (k) { return k[0].length; }));
    var isi = kolom.map(function (k) {
      return "  " + k[0] + new Array(lebar - k[0].length + 2).join(" ") + "= {" + k[1] + "}";
    }).join(",\n");
    return "@" + jenis + "{" + kunci + ",\n" + isi + "\n}";
  }

  function initSitasi() {
    var sumber = $("#data-karya");
    var kotak = $("[data-sitasi-teks]");
    if (!sumber || !kotak) return;
    var data;
    try { data = JSON.parse(sumber.textContent); } catch (e) { return; }

    var format = { apa: buatAPA(data), bibtex: buatBibtex(data) };
    var aktif = "apa";
    kotak.textContent = format.apa;

    $$(".sitasi__tab [data-format]").forEach(function (tab) {
      tab.addEventListener("click", function () {
        aktif = tab.getAttribute("data-format");
        $$(".sitasi__tab [data-format]").forEach(function (t) {
          t.setAttribute("aria-selected", String(t === tab));
        });
        kotak.textContent = format[aktif];
      });
    });

    var tombol = $("[data-salin-sitasi]");
    if (tombol) {
      tombol.addEventListener("click", function () {
        salin(format[aktif]).then(
          function () { toast(aktif === "apa" ? "APA citation copied" : "BibTeX copied"); },
          function () { toast("Couldn't copy"); }
        );
      });
    }
  }

  /* ---------- Arsip: cari, saring, urutkan ---------- */
  function normal(s) {
    return String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  function initArsip() {
    var wadah = $("[data-saring]");
    var daftar = $("[data-daftar]");
    if (!wadah || !daftar) return;

    var kartu = $$("[data-karya]", daftar);
    kartu.forEach(function (k) { k._teks = normal(k.getAttribute("data-cari")); });

    var input = $("[data-input-cari]", wadah);
    var pilihTahun = $("[data-tahun-filter]", wadah);
    var pilihUrut = $("[data-urut]", wadah);
    var chip = $$("[data-jenis-filter]", wadah);
    var jumlah = $("[data-jumlah]", wadah);
    var kosong = $("[data-kosong]");

    var awal = new URLSearchParams(location.search);
    var keadaan = {
      q: awal.get("q") || "",
      jenis: awal.get("jenis") || "",
      tahun: awal.get("tahun") || "",
      urut: awal.get("urut") || "baru"
    };

    function bandingkan(a, b) {
      if (keadaan.urut === "judul") return a.getAttribute("data-judul").localeCompare(b.getAttribute("data-judul"), "en");
      var x = a.getAttribute("data-tanggal"), y = b.getAttribute("data-tanggal");
      return keadaan.urut === "lama" ? x.localeCompare(y) : y.localeCompare(x);
    }

    function terapkan(perbaruiUrl) {
      input.value = keadaan.q;
      pilihTahun.value = keadaan.tahun;
      pilihUrut.value = keadaan.urut;
      chip.forEach(function (c) {
        c.setAttribute("aria-pressed", String(c.getAttribute("data-jenis-filter") === keadaan.jenis));
      });

      var kata = normal(keadaan.q).split(/\s+/).filter(Boolean);
      var tampil = 0;
      kartu.slice().sort(bandingkan).forEach(function (k) {
        var cocok =
          (!keadaan.jenis || k.getAttribute("data-jenis") === keadaan.jenis) &&
          (!keadaan.tahun || k.getAttribute("data-tahun") === keadaan.tahun) &&
          kata.every(function (w) { return k._teks.indexOf(w) !== -1; });
        k.hidden = !cocok;
        if (cocok) tampil++;
        daftar.appendChild(k);
      });

      // Sembunyikan tahun yang berulang agar daftar terbaca per tahun.
      var sebelum = null;
      kartu.forEach(function (k) { k.removeAttribute("data-tahun-ulang"); });
      if (keadaan.urut !== "judul") {
        $$("[data-karya]:not([hidden])", daftar).forEach(function (k) {
          var t = k.getAttribute("data-tahun");
          if (t === sebelum) k.setAttribute("data-tahun-ulang", "");
          sebelum = t;
        });
      }

      var disaring = keadaan.q || keadaan.jenis || keadaan.tahun;
      var kata_karya = function (n) { return n === 1 ? " work" : " works"; };
      jumlah.textContent = disaring
        ? tampil + " of " + kartu.length + kata_karya(kartu.length)
        : kartu.length + kata_karya(kartu.length);
      if (kosong) kosong.hidden = tampil !== 0;

      if (perbaruiUrl) {
        var p = new URLSearchParams();
        if (keadaan.q) p.set("q", keadaan.q);
        if (keadaan.jenis) p.set("jenis", keadaan.jenis);
        if (keadaan.tahun) p.set("tahun", keadaan.tahun);
        if (keadaan.urut !== "baru") p.set("urut", keadaan.urut);
        var qs = p.toString();
        history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
      }
    }

    input.addEventListener("input", function () { keadaan.q = input.value; terapkan(true); });
    pilihTahun.addEventListener("change", function () { keadaan.tahun = pilihTahun.value; terapkan(true); });
    pilihUrut.addEventListener("change", function () { keadaan.urut = pilihUrut.value; terapkan(true); });
    chip.forEach(function (c) {
      c.addEventListener("click", function () { keadaan.jenis = c.getAttribute("data-jenis-filter"); terapkan(true); });
    });

    daftar.addEventListener("click", function (ev) {
      var k = ev.target.closest("[data-kata-kunci]");
      if (!k) return;
      keadaan.q = k.getAttribute("data-kata-kunci");
      terapkan(true);
      wadah.scrollIntoView({ behavior: "smooth", block: "start" });
    });

    var reset = $("[data-reset]");
    if (reset) {
      reset.addEventListener("click", function () {
        keadaan = { q: "", jenis: "", tahun: "", urut: keadaan.urut };
        terapkan(true);
        input.focus();
      });
    }

    document.addEventListener("keydown", function (ev) {
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if (ev.key === "/" && !/INPUT|TEXTAREA|SELECT/.test(tag)) {
        ev.preventDefault();
        input.focus();
      } else if (ev.key === "Escape" && document.activeElement === input && input.value) {
        keadaan.q = "";
        terapkan(true);
      }
    });

    terapkan(false);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTema();
    initBagikan();
    initSitasi();
    initArsip();
  });
})();
