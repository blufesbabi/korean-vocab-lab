KVL MERC MODE — FLASHCARD REV19 (template PNG + overlay)

STRUKTUR (REV19.2)
  index.html                          app penuh (blok REV19: <style id="kvl-flashcard-rev19">, <script id="kvl-flashcard-rev19-js">)
  assets/template_flashcard.png       background card (868x1536)
  assets/roboto-condensed-700.woff, assets/roboto-condensed-700-italic.woff, assets/noto-sans-kr-900.woff   font lokal (offline aman), langsung di assets/ tanpa subfolder
  assets/                             aset app lama (menu/mode lain), tidak ditimpa
  README.txt, bugfix.txt
  Hanya ada satu folder aset: assets/ (pakai s). Tidak ada folder lain untuk aset.

LAYOUT & SCROLL (REV19.2)
  #flashcardPanel = <section> biasa di dalam #flashcardView (container konten yang sama dengan fitur lain). Tidak ada position:fixed, inset, atau z-index tinggi.
  Header app (KOREAN VOCAB LAB) dan nav 9 fitur dikelola layout app seperti fitur lain: HP <=640px nav fixed di bawah (.app sudah punya padding-bottom setinggi nav + safe-area,
  jadi kartu/footer tidak tertutup); tablet/desktop nav = sidebar sticky di kiri. Panel tidak mengukur/menempatkan apa pun lagi (placePanel dihapus).
  Card = width 100% container (aspect-ratio 868/1536), tanpa margin/padding kiri-kanan, tanpa letterbox. Di HP (<=640px) container sudah tanpa padding => edge-to-edge.
  Di tablet/desktop lebar card = lebar kolom konten (main) -> card tinggi (1366px: ~1139x2016). Itu konsekuensi 9:16 full lebar; halaman discroll normal.
  Opsional: batasi lebar desktop dengan custom property --fc-max di #flashcardPanel (mis. --fc-max:640px). Default: tidak dibatasi.
  Scroll: tidak ada overflow:hidden / overscroll-behavior / touch-action pemblokir di html, body, panel, card (card pakai overflow:clip, bukan scroll container).
  Zona arti (.fc-arti) overflow-y:auto, overscroll-behavior:auto, touch-action:pan-y: kalau tidak overflow, wheel/touch diteruskan ke halaman.
  Judul "Flash Card" + lead di atas setup disembunyikan selama kartu aktif (CSS :has), supaya kartu langsung di bawah header.
  Mulai sesi / ganti bab: halaman digulung ke atas (header + awal kartu terlihat).

CARA PAKAI
  Buka index.html (Flashcard > pilih bab/jumlah > Mulai). Keyboard: <- -> pindah kartu. Space/Enter lihat/sembunyikan arti HANYA bila fokus di dalam flashcard;
  di luar itu Space tetap scroll halaman. Klik nav fitur lain = sesi flashcard ditutup rapi (tidak dihitung selesai).
  Tombol: kembali, judul bab (dropdown native), LIHAT ARTI, speaker, SEBELUMNYA, SELANJUTNYA (jadi SELESAI di kartu terakhir).

TABEL ZONA (persen dari card; edit di CSS blok <style id="kvl-flashcard-rev19">, variabel --l --t --w --h, font --fs dalam cqw)
  zona            left  top   width height fs
  .fc-title       27.4  1.0   60    5.0    4.1   (judul bab, kanan ikon buku)
  .fc-counter     16.6  9.2   22    2.6    3.7
  .fc-mode        70.5  9.75  25.5  2.6    3.6
  .fc-no          62    36.3  26    3.3    4.4
  .fc-hangul      5     41.7  90    8.6    10
  .fc-roman       10    50.2  80    3.8    5.3   (tengah di garis merah y=52.1%)
  .fc-bab         28    55.3  44    4.6    5.2
  .fc-instr       5     59.9  90    4.3    3.85
  .fc-lihat       33.2  67.0  30    4.4    5.2
  .fc-arti        8.7   75.1  72    7.8    3.9
  .fc-prev        16.5  91.8  26    5.5    3.9
  .fc-next        57.2  91.8  28.4  5.5    3.9
  Area klik (.fc-h-*): back 1.2/0.7/12/6.2; chapter 15.2/0.7/81/6.2; reveal 5.8/66/70/6.5; speaker 77/65/22/12.4 (bulat);
  prev 1.2/90.2/47.8/8.2; next 51.3/90.2/47.2/8.2.
  Beda dari estimasi di brief (sudah diukur ke piksel template): judul bab & mode digeser karena ikon buku/orang ke-bake; romanisasi dipusatkan di garis merah.

SUMBER DATA
  Hangeul = item.korean (lewat kvlFormText, ikut bentuk soal). Arti = item.meaning. Plat BAB = item.category.
  No. = item.no, zero-pad 3 digit. Judul/Mode = pilihan user: "Semua Bab", nama bab, atau "Custom" (sesi Custom Study).
  Counter/bar = index+1 / jumlah kartu deck. Romanisasi = digenerate dari Hangeul (data tidak punya field romanisasi).

KEPUTUSAN TEKNIS
  Bar progress: template punya fill merah ke-bake (x141-190px). Ditutup patch .fc-bar-patch (gradient hasil sample kolom track kosong,
  ujung kiri membulat, kanan lurus), lalu .fc-bar-fill dinamis (gradient sample dari fill template). Lebar = max(16px, pos/total*312px).
  Garis romanisasi: .fc-line-patch menampilkan potongan kertas template 11px tepat di atas garis (y784-794px) di lebar teks + gap 2.6cqw,
  jadi garis terputus di sekitar teks seperti sampel. Posisi/lebar dihitung JS tiap fit.
  Auto-fit: fitZone() kecilkan font 3%/langkah sampai muat; min 55% hangeul (lalu lanjut ke 40% hanya untuk kalimat ekstrem),
  60% arti/lainnya; romanisasi ellipsis terakhir; arti scroll vertikal tanpa scrollbar. Jalan ulang saat ganti kartu, resize, orientationchange, font load.
  Dropdown bab: <select> transparan di atas judul; ganti bab = set #flashChapter lalu startFlashcards() (deck baru, indeks 1).
  Speaker: speakKorean() app (ko-KR, cancel dulu); teks "A/B" dibaca "A. B"; gagal -> toast kecil.

GANTI TEMPLATE
  Timpa assets/template_flashcard.png dengan gambar rasio 868x1536. Kalau layout beda, ukur ulang: zona (CSS --l/--t/--w/--h),
  .fc-bar-patch/.fc-bar-fill (px template di CSS + BAR_MAX_PCT di JS), .fc-line-patch (top 795px, sumber 784px di ui.js patchLine).
