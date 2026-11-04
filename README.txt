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
