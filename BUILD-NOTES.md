# Build notes — One-Star Review of Something Essential (slot 1)

## Scope verdict: LAYAK, digarap
- Prize $5, top 5 × $1. Kecil, tapi gratis, build murah (program 1 baris), deadline 26 Nov 22:20 UTC (masih ~2,5 hari dari build 24 Nov ~06:00 WIB).
- 264 entri saat build. Board blind (6 ronde, pertama 24 Nov 10:20 UTC); skor tidak terlihat sampai final.
- Tidak butuh API key / wallet / resource khusus. transcripts_required: true, strict_transcripts: TIDAK ada di competition.yaml — tidak perlu sealed recording.
- submission_rule: Force_Last, max 5/hari, license osi, repo_created_after_open: true.
- Program: program/v1, node22/python3.13, tulis /output/entry.txt, gate 1–160 karakter UTF-8, wall budget 60 dtk.
- thinking_reproduces min 30%, thinking_revised min 2 file writes — main.py ditulis 2x (v1 + revisi guard assert), keduanya di sesi ini.

## Entry final
`One star. Electricity is invisible until it leaves, and it only ever leaves mid-shower.` — 87 karakter.
sha256 entry.txt: b795d77d97d0acf1b7053ecec055f4f8bf0369da7189910a1580b50cde8cb698
Deterministik: 4x run, sha identik. Tanpa network saat runtime.

## Turnamen self-judge (Hermes nemotron-3.5-super-vl:free via CrowLLM, brief judge resmi)
- R1: C01 Blinking > C02 Memory; C03 Teeth > C04 Knees; C05 Electricity > C06 Ageing; C08 Monday > C07 Weekend; C10 Water > C09 Time; C12 Sneeze > C11 Hair
- SF: C03 > C01; C05 > C12; C10 > C08
- Final: C05 > C03 (2–0, dua urutan); C05 > C10 (2–0, dua urutan)
- Catatan: CrowLLM free rate-limit 15 req/menit — 2 panggilan awal kena 429, diulang dengan jeda 75 dtk. Total ~13 panggilan judge.
- Log: tournament-r1.log, tournament-r1b.log, tournament-sf.log, tournament-f1.log, tournament-final.log

## Peluang jujur
- Rendah–sedang. Hadiah hanya $1 untuk top 5 dari 264+ entri; judge AI pairwise dengan varians tinggi. Keunggulan kami: topik segar (electricity tidak ada di field yang didominasi sleep/gravity), grievance spesifik yang diakui semua orang, turn di kata terakhir. Tapi satu baris teks = lotere rasa judge; tidak ada local grade yang bisa memprediksi skor server.
- Slot 1 ini layak disubmit apa adanya. Slot 2 (kalau mau) bisa coba varian runner-up Water atau Teeth — tapi ingat Force_Last: slot 2 menggantikan slot 1 di papan.

## Yang parent perlu lakukan (BUKAN bagian builder)
- Buat repo SETELAH bounty buka (sudah buka 23 Nov 22:21 UTC — aman), push via browser, bundle + submit via CLI (flag: --provider meta --model muse-spark-1.3 --effort default --mcp none; parent session hanya --parent-session).
- File entry: main.py, README.md, LICENSE (MIT, SPDX ok), entry.txt (contoh output).
- Kit resmi tersimpan di: u-0xb3e689-one-star-review-of-something-essential-c7234629-kit/ (kit.tar.gz + RULES.txt + competition.yaml).
