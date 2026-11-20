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
