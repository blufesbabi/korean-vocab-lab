Korean Vocab Lab · Merc Mode — Cinematic Combat Feedback

To preview: open index.html in a modern browser with the assets folder beside it.

Cinematic feedback assets:
- assets/merc-feedback-target-lost.webp
- assets/merc-feedback-contract-confirmed.webp
- assets/merc-hangul-ungraphic-bold.woff2 (optimized browser font)
- assets/UnGraphicBold.ttf (original TTF source for the WOFF2 conversion)
- assets/FONT-LICENSE-UNFONT.txt (UnFonts copyright and GPL-2 license notice)

The template artwork is static, while the Korean vocabulary and Indonesian meaning are rendered as dynamic text from each active question. The same two templates work across Quiz, Typing, Listening, Memory Lab, and the shared Custom Study feedback path without baking one word into every answer image.

On both mobile and desktop, Hangeul and its Indonesian meaning are overlaid inside the template's intel panel. The mobile layout preserves the artwork's original aspect ratio, positions text inside its frame, and uses a locally bundled UnGraphic Bold Hangul font: bold and stylized, but more legible than the former brush font. Both the browser-optimized WOFF2 and original TTF source are included with the license notice. It does not depend on a device font or a Google Fonts network request.

The transparent question progress companion image remains at assets/question-progress-companion.png. Existing learning/scoring logic and app assets are preserved; the mobile cinematic feedback layout/font and answer-state visibility/restoration are the relevant changes in this revision.

Bab 8 correction (2026-10-29):
- 아내 = istri
- 작다 = kecil (added as a standalone Bab 8 vocabulary entry)
- 적다 = sedikit
- Bab 8 now contains 110 entries; other Indonesian meanings are unchanged.

Update (2026-11-05):
- Desktop right column no longer shows the sticky-note board ("Jangan lupa: kamu bisa lebih baik") or its frame. Mobile is unchanged.
- Wrong answers show only the cinematic template (assets/merc-feedback-target-lost.webp); the text insults were removed.

[2026-11-05] Bottom navigation mobile (hanya <=640px)
- Menu utama (.app > .main-nav) pindah ke bawah layar: fixed, horizontal, bisa digeser, snap, tanpa bingkai/tekstur.
- 9 item, +-4,5 terlihat (22vw), ikon di atas label; aktif = merah terang opacity 1, non-aktif opacity .55.
- Ruang konten + toast digeser lewat variabel --nav-h; safe-area iOS lewat viewport-fit=cover.
- JS: blok kecil terpisah (MutationObserver) men-scroll item aktif ke tengah; logika showView tidak diubah.
- Di atas 640px tidak ada perubahan (diverifikasi: computed style desktop 1280px identik dengan versi sebelumnya).

[2026-11-05] Perbaikan mobile (HANYA @media max-width 640px, blok baru di akhir CSS)
- Konten semua halaman full-width: .app tanpa margin, kolom grid tunggal, #flashcardView tanpa padding samping; padding dalam card tetap 13px.
- footer-portrait disembunyikan (display:none) di mobile; file aset tidak dihapus.
- Background cinematic: gambar 100% auto, center top, no-repeat, di atas warna dasar #0a0809; fixed + pointer-events none dipertahankan.
- Di atas 640px tidak ada perubahan (computed style 1280px dan 800px identik dengan versi sebelumnya). JS dan bottom nav tidak diubah.
- Penanda versi: judul halaman diakhiri [MFIX2] (cek di daftar tab browser untuk memastikan file terbaru ter-deploy).
