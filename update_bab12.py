from pathlib import Path
import re

path = Path('/mnt/data/bab12_work/index.html')
s = path.read_text(encoding='utf-8')

items = [
('대중교통','transportasi umum'),
('시내','dalam kota'),
('어떻게','bagaimana'),
('교통수단','alat transportasi'),
('이동','perpindahan'),
('행동','tindakan'),
('이유','alasan'),
('타다','naik'),
('마을버스','bis perdesaan'),
('시내버스','bis dalam kota'),
('시외버스','bis luar kota'),
('고속버스','bis ekspres/cepat'),
('택시','taksi'),
('기차','kereta api'),
('고속 열차','kereta ekspres /ktx'),
('지하철','kereta bawah tanah'),
('비행기','pesawat'),
('배','kapal, perut, pir'),
('자전거','sepeda onthel'),
('오토바이','sepeda motor'),
('버스 정류장','halte bus'),
('버스 터미널','terminal bus'),
('기차역','stasiun kereta api'),
('지하철역','stasiun kereta bawah tanah'),
('공항','bandara'),
('번','nomer'),
('얼마나','berapa lama'),
('트럭','truk'),
('쯤','kira kira, sekitar'),
('걸리다','memakan waktu'),
('얼마나 걸려요?','memakan waktu berapa lama?'),
('타고 가다','pergi dengan naik'),
('타고 오다','datang dengan naik'),
('걸어가다','pergi dengan berjalan'),
('걸어오다','datang dengan berjalan'),
('내리다','turun'),
('갈아타다/환승하다','transit'),
('지나다','melewati'),
('걷다','jalan kaki'),
('출근 시간','waktu berangkat kerja'),
('퇴근 시간','waktu pulang kerja'),
('늦다','terlambat'),
('미안하다','maaf'),
('차가 막히다','kendaraannya macet'),
('좀 천천히 말씀해 주세요','tolong katakan pelan pelan'),
('발달되다','dikembangkan'),
('이용하다','menggunakan'),
('가깝다','dekat'),
('곳','tempat'),
('멀다','jauh'),
('편리하다','nyaman'),
('이동하다','pindah'),
('도시','kota'),
('간','antara'),
('가장','paling'),
('널리다','luas'),
('대도시','kota besar'),
('중도시','kota menengah'),
('노선','jalur'),
('주요','penting'),
('심야 시간','waktu malam'),
('운영되다','beroperasi'),
('짧다','pendek'),
('거리','jarak'),
('그리고','kemudian'),
('내','dalam'),
('곳곳','tempat tempat'),
('쉽다','mudah'),
('철도','rel kereta api'),
('가능하다','memungkinkan, bisa'),
('새마을호','nama kereta'),
('무궁화호','nama kereta'),
('일반','biasa'),
('요금','tarif'),
('빠르다','cepat'),
('최남단','paling selatan'),
('장거리','jarak jauh'),
('인터넷','internet'),
('모바일 앱','aplikasi mobile'),
('표','tiket'),
('예매하다','mereserfasi'),
('는 것이 좋습니다','sebaiknya'),
('손을 들다','mengangkat tangan'),
('지나가다','pergi melewati'),
('빈','kosong'),
('택시를 잡다','menghentikan taksi'),
('부르다','memanggil'),
]

# Confirm the source dataset does not already contain Bab 12.
if 'category: "Bab 12"' in s:
    raise SystemExit('Bab 12 already exists; aborting to avoid duplicate insertion.')

last_b11 = s.rfind('category: "Bab 11"')
if last_b11 < 0:
    raise SystemExit('Could not locate Bab 11 data in source HTML.')
array_end = s.find('\n      ];', last_b11)
if array_end < 0:
    raise SystemExit('Could not locate end of builtinVocabulary array.')

lines = []
for no, (korean, meaning) in enumerate(items, 1):
    # JSON-style JS strings; ensure exact user-provided Indonesian gloss is retained.
    k = korean.replace('\\', '\\\\').replace('"', '\\"')
    m = meaning.replace('\\', '\\\\').replace('"', '\\"')
    lines.append(f'        {{ no: {no}, korean: "{k}", meaning: "{m}", category: "Bab 12" }},')
insert = '\n' + '\n'.join(lines)
s = s[:array_end] + insert + s[array_end:]

# Replace the headline phrase exactly once in the primary top-line list.
old_line = '    "Well, well, well. Look who the fuck showed up. You dumbass bitch ass motherfucker."'
new_line = '    "떡 치는 것보다 한국어 공부가 낫지, 씨발."'
if s.count(old_line) != 1:
    raise SystemExit(f'Expected exactly one headline phrase, found {s.count(old_line)}.')
s = s.replace(old_line, new_line, 1)

# Keep the initial static chapter filter consistent with the populated categories.
old_select_tail = '<option value="Bab 9">Bab 9</option></select>'
new_select_tail = ('<option value="Bab 9">Bab 9</option>'
                   '<option value="Bab 10">Bab 10</option>'
                   '<option value="Bab 11">Bab 11</option>'
                   '<option value="Bab 12">Bab 12</option></select>')
if old_select_tail not in s:
    raise SystemExit('Could not find static chapterFilter ending at Bab 9.')
s = s.replace(old_select_tail, new_select_tail, 1)

# Custom Study uses a hand-authored checkbox list, so extend that list too.
old_checkbox = '<label class="chapter-picker-item"><input type="checkbox" data-cs-cat="Bab 9" /> Bab 9</label>'
new_checkbox = (old_checkbox + '\n'
    + '                      <label class="chapter-picker-item"><input type="checkbox" data-cs-cat="Bab 10" /> Bab 10</label>\n'
    + '                      <label class="chapter-picker-item"><input type="checkbox" data-cs-cat="Bab 11" /> Bab 11</label>\n'
    + '                      <label class="chapter-picker-item"><input type="checkbox" data-cs-cat="Bab 12" /> Bab 12</label>')
if s.count(old_checkbox) != 1:
    raise SystemExit(f'Expected one custom-study Bab 9 checkbox, found {s.count(old_checkbox)}.')
s = s.replace(old_checkbox, new_checkbox, 1)

# Add Bab 12 to both fallback/priority category arrays.
old_pref = '"Bab 9", "Bab 10", "Bab 11"'
new_pref = '"Bab 9", "Bab 10", "Bab 11", "Bab 12"'
count_pref = s.count(old_pref)
if count_pref < 2:
    raise SystemExit(f'Expected at least two Bab 1-11 preference arrays, found {count_pref}.')
s = s.replace(old_pref, new_pref)

path.write_text(s, encoding='utf-8')
print(f'Inserted {len(items)} Bab 12 entries.')
print('Updated headline, chapter filter, Custom Study picker, and category priority arrays.')
print('Audit modifications: 시외 버스→시외버스; 출근시간→출근 시간; 퇴근시간→퇴근 시간; 말씀해주세요→말씀해 주세요; 심야시간→심야 시간; 모바일 압→모바일 앱; 손을들다→손을 들다.')
