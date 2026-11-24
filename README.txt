KVL MERC MODE — COLLECTION REV17 (update data kosakata Bab 13, dari REV16)

REV17 — KOSAKATA BAB 13
- Ditambahkan 87 kosakata Bab 13 (no 1-87, category "Bab 13") ke builtinVocabulary. Arti Indonesia mengikuti teks dari user apa adanya.
- Bab 13 ditambahkan ke dropdown statis, picker Custom Study, dan daftar urutan bab (listCategories / syncChapterSelects).
- Koreksi Hangeul/spasi: 생횔->생활, 모일->모임, 되지고기->돼지고기, 여불을->예불을, 신안 생활->신앙 생활, 여런 속의 여런->여론 속의 여론, 기도를하다->기도를 하다, 활동을하다->활동을 하다. Baris yang terpotong digabung (고향 사람을 만나다, 고향 음식을 먹다, 예배를 드리다).
- Tidak diubah: bab lain, Partikel, UI, quiz, memory, TTS, LocalStorage, aset.

----- RIWAYAT SEBELUMNYA -----
KVL MERC MODE — COLLECTION REV16 (revisi kecil tab "Partikel", dari REV15)

REV16 — PARTIKEL
- Desktop: #ptkList selalu 1 kolom di semua lebar (media query 2 kolom min-width:720px dihapus). Tiap kartu dibatasi max-width: min(100%, 760px) dan di-center; detail accordion mengikuti lebar kartu. Auto-fit kartu tidak diubah (pelanggaran zona teks = 0).
- Toolbar: aturan REV15 "#reviewView #ptkPanel .list-tools > input.control { grid-column: 1 / -1 !important; }" dihapus (penyebab input melebar satu baris penuh). Grid .list-tools Partikel kembali ke layout artwork seperti Kosakata: kiri-atas "All Particles" (span non-interaktif #ptkScope, aria-hidden), kanan-atas input pencarian, kiri-bawah #ptkCount.
- Placeholder pencarian kini penuh di dalam kotak (padding kanan 3%, satu baris, tidak terpotong di 320px). Ikon search = SVG inline data-URI sebagai background-image pada input (tanpa elemen pembungkus), ikon + placeholder rata kiri sebagai satu grup.
- Tipografi tiga kotak disamakan (system-ui, 560, letter-spacing .01em, warna rgba(229,221,218,.9), placeholder rgba(220,213,210,.7), text-shadow tipis). Ukuran font: clamp(10px, 2.6vw, 14px) di mobile, clamp(12px, 1.15vw, 15px) di >=641px. Fokus: outline tipis di dalam kotak.
- Semua CSS baru ada di blok <style id="kvl-collection-rev15-ptk> yang sama, di-scope ke #ptkPanel / #ptkList. Tidak ada patch bertumpuk.

BATAS PERUBAHAN REV16
- Tidak diubah: tab Kosakata, navigasi, quiz, memory, TTS, LocalStorage, 85 data Partikel, logika auto-fit. Tidak ada framework/library/CDN/aset baru. Seluruh aset byte-for-byte dari REV15.
- Kartu dan toolbar Kosakata pixel-identik dengan REV15 (diuji 6 lebar, 100 kartu terender).
- tests/rev16-verify.py ditambahkan (harness REV16). File tests/rev15-verify.py tidak ada di ZIP REV15 yang diterima, jadi harness ditulis ulang.

----- RIWAYAT SEBELUMNYA -----
KVL MERC MODE — COLLECTION REV12

CARA PAKAI
1. Ekstrak ZIP ini.
2. Pastikan index.html dan folder assets berada pada direktori yang sama.
3. Buka index.html melalui browser modern. Untuk penggunaan penuh, gunakan browser/perangkat yang mendukung LocalStorage dan Web Speech API.

STRUKTUR PAKET
- index.html: aplikasi utama.
- readme.txt: petunjuk penggunaan dan ringkasan revisi.
- bugfix.txt: riwayat perbaikan dan catatan pengujian.
- assets/: seluruh gambar, ikon, font lokal, dan aset UI aplikasi.

FINISHING REV9 — COLLECTION
- Penanda kategori kosakata dipindahkan ke satu baris di antara Hangeul dan arti Indonesia, dengan label visual "𒇫 Bentuk". Informasi mode aktual tetap disimpan pada atribut data/aksesibilitas dan mekanisme pergantian bentuk tetap terhubung.
- Judul Kosakata/Partikel dan deskripsinya diposisikan rapat di atas tab. Judul menggunakan sans-serif tebal dengan finishing kontras bergaya industrial; deskripsi menggunakan sans-serif bersih.
- Dropdown, pencarian, dan penghitung data pada desktop dirapikan agar terpusat di slot artwork.
- Kartu Kosakata dan Partikel pada desktop/Mac disusun satu baris horizontal, termasuk nomor, Hangeul, penanda Bentuk bila ada, arti, dan audio.
- Ikon dan teks tab diperkecil sedikit; chevron dipindahkan ke rel paling kanan. Frame aktif merah dan nonaktif gunmetal dipertahankan.
- Tombol HTML Kembali pada hero Collection dihapus tanpa menghapus navigasi aplikasi lainnya.

BATAS PERUBAHAN
- Data kosakata, Partikel, terjemahan, materi, routing, event aplikasi, filter, pencarian, audio/TTS, LocalStorage, dan sembilan menu navigasi tidak diganti sebagai bagian dari finishing ini.
- Tidak ada framework, library, CDN, atau dependency baru.
- Seluruh 41 file aset dipertahankan byte-for-byte; gambar tidak diolah ulang.


FINISHING REV10 — FORM MODE, AUDIO SLOT, TAB ALIGNMENT
- Indikator kosakata menampilkan mode aktual: 𒇫 dasar, formal, informal, atau banmal. Label diperbarui bersamaan dengan bentuk Hangeul saat swipe.
- Arah swipe dikunci sesuai urutan: swipe kiri = dasar → formal → informal → banmal; swipe kanan = dasar → banmal → informal → formal.
- Kosakata tanpa variasi tingkat tutur tetap pada dasar, berwarna lebih redup, disabled, dan tidak bisa digeser.
- Indikator diturunkan ke area bawah di antara kolom Hangeul dan arti Indonesia tanpa memindahkan kedua kolom tersebut.
- Tombol audio dipusatkan di slot kanan kartu, diberi batas ukuran agar tetap berada di dalam frame pada ukuran mobile dan desktop.
- Ikon dan label tab dijadikan satu grup terpusat dengan jarak 2x; chevron kanan dipertahankan pada rel paling kanan.
- Tidak ada perubahan data kosakata/Partikel, terjemahan, routing, LocalStorage, TTS, atau aset.


FINISHING REV11 — AUDIO / TITLE / PARTIKEL TEXT
- Audio Kosakata dan Partikel dirapikan ke tengah rel kanan kartu, dengan ukuran adaptif untuk mobile, Mac, dan desktop.
- Judul Daftar semua kosakata dan Daftar partikel & tata bahasa menggunakan warna warm ivory putih-kecoklatan yang menyatu dengan background industrial.
- Arti Indonesia pada daftar Partikel dan isi detailnya dapat membungkus ke baris berikutnya tanpa melewati batas atau menabrak tombol audio.


FINISHING REV12 — AUDIO SLOT + PARTIKEL COLUMN ALIGNMENT
- Rel audio pada kartu Kosakata dan Partikel dikembalikan ke lebar 13% sesuai area speaker yang dicetak pada artwork. Tombol dan ikon dipusatkan secara geometris di tengah rel tersebut, bukan menempel ke tepi kanan.
- Posisi dan ukuran audio adaptif untuk mobile kecil, mobile umum, tablet, Mac, dan desktop.
- Kolom Partikel mengikuti garis artwork: nomor 13%, Hangeul 60%, arti Indonesia 27% dari bidang teks; 13% sisi kanan tetap khusus untuk audio.
- Arti Indonesia disejajarkan di tengah secara horizontal dan vertikal pada bidang di antara divider Hangeul dan rel audio. Teks panjang membungkus ke baris berikutnya di dalam kolomnya.
- Tampilan lain, isi/data, aset, TTS, filter, pencarian, navigasi, dan perilaku detail Partikel tidak diubah.


FINISHING REV15 — PARTIKEL (DATA DOCX + KARTU PRESISI + ACCORDION)
- Data Partikel diganti total: array lama (68 item) dihapus, diganti 85 item dari Catatan_Partikel_Korea.docx. Urutan & isi mengikuti tabel "Shortcut Partikel" (No | Partikel | Arti), detail mengikuti bagian "## N. partikel = arti". Skema item: { n, ko, a, tts, blocks[] }. blocks[] menyimpan blok detail dalam urutan asli docx (label-teks, bullet, tabel, contoh a/b/c + "Artinya"). Isi materi tidak diubah/diperbaiki; tidak ada catatan data lama yang dibawa.
- Dropdown #ptkGroup dan logikanya dihapus (docx tidak punya kategori). Pencarian #ptkSearch mencocokkan nomor, partikel, dan arti (tanda "-", "(", ")" diabaikan). #ptkCount menampilkan "85 poin". Teks legenda Partikel disesuaikan: hanya KB/KK/KS (notasi (V)/(K) milik data lama dibuang).
- Kartu depan = [No | Partikel | Arti] + audio, tanpa rumus/kategori. Klik kartu membuka detail DI BAWAH kartu (accordion, satu terbuka, klik lagi menutup, scrollIntoView nearest, Enter/Space, aria-expanded).
- DOM baru: <div class="ptk-item"><div class="ptk-row">kartu</div><div class="ptk-detail">detail</div></div>. Detail berada di luar frame, gaya panel gelap, lebar penuh kolom, teks wrap bebas.
- Kartu presisi ke collection-card-frame.png (1379x225): aspect-ratio tetap, container-type:inline-size, frame ::before 100% 100%. Zona teks (persen lebar kartu): No 4.6-12.1, Partikel 13.7-63.2, Arti 64.7-88.4; vertikal 16-84%. Audio berpusat 92.9%/50%, ikon 4.2cqw (<= 4.6cqw), hit-area transparan 88.9-96.9%.
- AUTO-FIT per sel (font cqw+clamp, turun 0.2cqw sampai muat; maks 1 baris No, 2 baris Partikel, 3 baris Arti; minimum 9px). Dijalankan ulang pada document.fonts.ready/loadingdone, ResizeObserver, dan saat tab Partikel dibuka.
- CSS dibersihkan: ~98 rule dan 148 selector override Partikel lama (REV9-REV12 dan blok dasar) dihapus; diganti SATU blok "kvl-collection-rev15-ptk" yang seluruhnya di-scope ke #ptkList/#ptkPanel. Kartu Kosakata identik dengan REV14 (pixel-identik pada 320/360/390/430/768/1280).
- Daftar Partikel tidak lagi memakai kelas .vocab-list/.vocab-line sehingga tidak terpengaruh CSS Kosakata.
- Yang TIDAK diubah: tab Kosakata, navigasi, quiz, memory, TTS (speakKorean), LocalStorage, seluruh aset (byte-for-byte), tanpa framework/library/CDN baru.
- Bukti pengujian: tests/rev15-screens/ (screenshot 6 lebar + summary.json), tests/rev15-verify.py. Validasi data: REV15_VALIDASI_PARTIKEL.txt.
