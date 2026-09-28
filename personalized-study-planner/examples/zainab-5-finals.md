# Worked example — Zainab, 5 finals in one window (uni)

This is what a **multi-exam / finals-season** first reply must look like. Uni students do not have one exam; they have five papers in fifteen days, shared hours, and a lab report due in the middle. Use it as the quality bar for RULEBOOK 20: one shared plan, DAYS measured to the next paper, PROX on the next paper's topics, bridge day after every paper, last 48 hours before a paper = that paper only.

Names and dates are fictional. The structure is the point.

## What Zainab pasted

```text
Level: uni — BS Computer Science, semester 5
Today: 2026-12-11
Finals (all compulsory):
- Data Structures (DS): Mon 14 Dec, 09:00
- OOP: Thu 17 Dec, 14:00
- Databases (DB): Sun 20 Dec, 09:00
- COAL: Wed 23 Dec, 14:00
- Calculus: Sat 26 Dec, 09:00

Time: weekdays 210 min (19:00–22:15), weekends 5h + 3h
Deadline inside the window: FP-style lab report + demo, Tue 15 Dec, ≈3h work left
Past papers: 2 per course with mark schemes, none attempted. Calc: none exist, only the professor's 30 exercise sheets
Recent evidence:
- DS midterm 42% (trees section 25%)
- OOP midterm 85%
- DB quiz 2: 7/10 (joins chapter 4/10 on that quiz)
- COAL midterm 58% (pipelines blank)
- Calc assignment 14/20 (integration by parts messy)

Topics (uni units, self-reported confidence 1–5):
DS: arrays/linked 4, trees 2, AVL 1, graphs 1, hashing 3
OOP: classes/objects 5, inheritance 4, polymorphism 4, patterns 4, file handling 4
DB: ER 4, relational algebra 3, SQL joins 3, normalization 2, transactions 2
COAL: bits/registers 3, assembly ops 2, memory map 2, pipelines 1, interrupts 2
Calc: derivatives 3, integration by parts 1, series 2, multivariable intro 2

Weak: AVL rotations (blank under pressure), graphs traversal code (mix DFS/BFS), SQL joins (wrong row counts), normalization forms (mix 2NF/3NF), pipelines hazards (blank), integration by parts (sign errors)
Today: 180 min from 19:00 (started late)
```

## What Study OS must return

```
COMMAND CENTER
Exam: BS CS semester 5 finals — 5 papers, 14–26 Dec  |  DAYS=3 (next: DS, Mon 14 Dec)
NEXT: Data Structures — Mon 14 Dec 09:00  (then OOP 17, DB 20, COAL 23, Calc 26)
Clock: Twd=210 weekday  /  weekend=480
ASGN=3h (lab report + demo, due Tue 15 Dec)  BANK=41.0h  NEED=46.5h  LOAD=1.13  TIGHT
COV=0%  WCOV=4%  CAVG=2.5  RED/AMBER/GREEN=9/9/7
WK=6 due today=3  ADH_7=81%  CAL=OVER on DS-trees (midterm 25% vs claimed 2)  NEXT_PROBE=2026-12-12
PROFILE  HARD=timed  STR=questions  BLOCK=40m  START=ok  TIMED=freeze  WEAKHOW=avoid  STATE=ok
THIS WEEK'S 3 NON-NEGOTIABLES
1. DS trees: 20 traversal + AVL rotation reps on paper, 16/20 correct before Mon 09:00
2. Lab report: method + results sections drafted, demo runs clean — Tue 15 Dec handover
3. SQL joins: 15 join queries against the practice DB, ≥12 with correct row counts
DO NOT OPEN THIS WEEK
- OOP (midterm 85%, floor 4 — one MIX before the 17th is enough)
- Pretty DB ER diagrams (ER is already 4)
- Any Calc series theory until after COAL (26th paper, PROX ×1.0 this week)
```

Assumptions: weekend split Sat 5h / Sun 3h (ASSUMED from "5h + 3h"). Calc has no past papers — the professor's 30 exercise sheets are the substitute; the plan uses them as scored sets.

## Topic map (next-paper first)

| Topic | Course | Weight | Confidence | Signal | Status | PROX | Priority | Next action |
|---|---|---|---|---|---|---|---|---|
| Trees + AVL | DS | 5 | 2 (capped from 2, midterm 25%) | RED | Learning | 1.5 | 30.0 | 20 reps on paper |
| Graphs traversal | DS | 4 | 1 | RED | Not started | 1.5 | 30.0 | code BFS/DFS ×3 each |
| Hashing | DS | 3 | 3 | AMBER | Learning | 1.5 | 9.0 | 10 MCQ |
| Lab report + demo | — | — | — | — | Deadline | — | fixed | Tue 3h block |
| SQL joins | DB | 5 | 3 (quiz 4/10 on joins) | RED | Learning | 1.25 | 11.3 | 15 queries |
| Normalization | DB | 4 | 2 | RED | Learning | 1.25 | 15.0 | 2NF/3NF sort cards |
| Integration by parts | Calc | 3 | 1 | RED | Learning | 1.0 | 7.5 | sign-error drill |
| Assembly ops | COAL | 4 | 2 | RED | Learning | 1.25 | 15.0 | trace 8 programs |
| Pipelines | COAL | 4 | 1 | RED | Not started | 1.25 | 22.5 | hazard identification set |
| Inheritance→patterns | OOP | 4 | 4 | GREEN | Exam-ready | 1.25 | 2.5 | one MIX, do not restudy |

Priority = Weight × (6 − confidence) × Freshness × Weak(1.5) × PROX. DS topics carry ×1.5 until Monday 09:00 is done; then OOP takes ×1.5.

## Weak board

| Topic | Symptom | Drill (15–25 min) | Next due | If you blank |
|---|---|---|---|---|
| Trees/AVL | rotations blank under pressure | 8 rotations on paper, no IDE, time-boxed | 2026-12-12 | draw the 3 cases, then redo |
| Graphs | mix DFS/BFS order | trace both on same graph, mark queue vs stack | 2026-12-12 | write visit-order rule first |
| SQL joins | wrong row counts | 15 queries vs practice DB, predict count first | 2026-12-13 | draw the Venn before writing |
| Normalization | mix 2NF/3NF | sort 12 relations into forms, check against key list | 2026-12-14 | find the partial dependency first |
| Pipelines | hazards blank | 5-stage diagram, mark stalls on 4 snippets | 2026-12-16 | draw the pipeline fill table |
| Int. by parts | sign errors | 6 integrals, check each sign against LIATE | 2026-12-18 | LIATE choice first, then integrate |

Max 5 active after DS is examined on the 14th — graphs promotes off if the mock crosses 6/8, normalization takes the slot.

## Time budget

Usable: 15 days − 1 lighter day = 14 study days. Weekday 210 × 9 + weekend 480 × 5... capped honestly: 41.0h after 0.85 slippage, minus ASGN 3h (lab report + demo, Tue). Needed: 46.5h with uni constants (3–5h per heavy unit). LOAD 1.13 → **TIGHT**. Triage: OOP goes maintenance-only (evidence backs it), Calc series theory drops to "professor's sheet pass only", nothing else drops. If the lab demo slips, Calc multivariable is the named sacrifice.

Phases inside the window (per paper, not per week): each paper gets its last 48 hours exclusively; the day after each paper is a bridge day — half volume, 10-minute post-mortem of what leaked, then the next paper's weaks. Post-mortems go in the log; leaked items join the weak board with next-due dates.

## Week strip

| Date | Clock | One job | If this dies |
|---|---|---|---|
| Fri 12 | 19:00–22:15 | DS: trees 20 reps + graphs drill | 20-min fallback: 8 rotation reps only |
| Sat 13 | 10:00–13:00 | DS: timed mock paper 1 + mark | mark with scheme, log P |
| Sun 14 eve | 16:00–19:00 | DS light: hashing MCQ + formula sheet | sleep by 22:30, paper at 09:00 |
| Mon 15 | 19:00–22:15 | **DS paper 09:00** → bridge: post-mortem + lab report | lab only, no guilt |
| Tue 16 | 19:00–22:15 | Lab demo → OOP MIX (one shot) | demo first, MIX 12 Qs minimum |
| Wed 17 | 19:00–22:15 | **OOP paper 14:00** → bridge + DB joins drill | post-mortem is the job |
| Thu 18 | 19:00–22:15 | DB: joins 15 Qs + normalization cards | joins half only |
| Fri 19 | 19:00–22:15 | DB: timed paper 1 + mark | section A timed only |
| Sat 20 | 10:00–13:00 | **DB paper 09:00** → bridge + COAL assembly trace | post-mortem + 1 trace |
| Sun 21 | 16:00–19:00 | COAL: pipelines hazards + assembly 8 traces | pipelines only |
| Mon 22 | 19:00–22:15 | COAL: timed paper 1 + mark | section B timed only |
| Tue 23 | 19:00–22:15 | **COAL paper 14:00** → bridge + Calc by-parts drill | post-mortem + 3 integrals |
| Wed 24 | 19:00–22:15 | Calc: by-parts set 2 + series sheet pass | by-parts only |
| Thu 25 | 19:00–22:15 | Calc: professor sheet, timed selection | section 1 only, sleep by 23:00 |

## TODAY — Fri 12 Dec, 180 min from 19:00

- [ ] 19:00 — Trees/AVL drill, 8 rotations on paper, no IDE (25 min) — Done = __/8
- [ ] 19:30 — Graphs: code BFS + DFS on the same graph, mark visit order (20 min) — Done = 2/2 correct orders
- [ ] 19:55 — Break (10 min)
- [ ] 20:05 — DS past paper 1, section A timed (40 min) — Done = __/20
- [ ] 20:45 — Mark with scheme, log misses to weak board (15 min) — Done = log has ≥3 entries
- [ ] 21:00 — Break (10 min)
- [ ] 21:10 — SQL joins: 8 of 15 queries, predict row count first (40 min) — Done = ≥6/8 correct counts
- [ ] 21:50 — Lab report: draft method section (25 min) — Done = method section exists
- [ ] 22:15 — Card update + DONE stamp

IF THIS DIES → 20 minutes: 8 AVL rotations on paper + 4 join queries. That still counts.

DONE stamp: `DONE minutes: __ scores: trees __/8 graphs 2/2 secA __/20 joins __/8 shaky: ___`

TOMORROW FIRST → Sat 13, 10:00: DS past paper 1 section B, timed.

```
# STUDY OS CARD
Date: 2026-12-11
Student: Zainab
Exam(s): DS — 14 Dec | OOP — 17 Dec | DB — 20 Dec | COAL — 23 Dec | Calc — 26 Dec
Next paper: Data Structures, Mon 14 Dec 09:00
Days left: 3 (to next paper)
Format: uni written finals, problem-solving + short answer
Weekday time: 210 min (usually 19:00–22:15)
Weekend time: Sat 300 / Sun 180
Constraints: lab report + demo due Tue 16 Dec window (≈3h); paper times vary 09:00/14:00
Verdict: TIGHT (LOAD 1.13)
INTAKE: 92%   (ASSUMED: weekend split)

## Profile
HARD: timed
STR: questions
BLOCK: 40
START: ok
TIMED: freeze
WEAKHOW: avoid
STATE: ok
CONSTRAINT: none declared

## Metrics
DAYS: 3 (next paper)
NEXAM: DS — 2026-12-14
BANK: 41.0h (already minus ASGN)
ASGN: 3h
NEED: 46.5h
LOAD: 1.13
COV: 0%
WCOV: 4%
CAVG: 2.5
RED/AMBER/GREEN: 9/9/7
WK: 6 (post-DS cap: 5 active)
ADH_7: 81%
CAL: OVER on DS-trees (25% vs conf 2); seeded from midterms
NEXT_PROBE: 2026-12-12

## Topics
| Topic | Course | Weight | Confidence | Status | Last studied | Last P | Next probe | Next action |
| Trees+AVL | DS | 5 | 2 | Learning | 2026-12-04 | 25 (midterm) | 2026-12-12 | 20 rotation reps |
| Graphs | DS | 4 | 1 | Not started | n/a | n/a | 2026-12-12 | BFS/DFS ×3 |
| Hashing | DS | 3 | 3 | Learning | 2026-11-28 | n/a | 2026-12-13 | 10 MCQ |
| SQL joins | DB | 5 | 3 | Learning | 2026-12-02 | 40 (quiz) | 2026-12-13 | 15 queries |
| Normalization | DB | 4 | 2 | Learning | 2026-11-25 | n/a | 2026-12-14 | sort cards |
| Assembly | COAL | 4 | 2 | Learning | 2026-11-30 | n/a | 2026-12-16 | trace 8 |
| Pipelines | COAL | 4 | 1 | Not started | n/a | 42 (midterm 58% overall) | 2026-12-16 | hazards set |
| By parts | Calc | 3 | 1 | Learning | 2026-12-08 | 30 (assignment) | 2026-12-18 | sign drill |
| Patterns | OOP | 4 | 4 | Exam-ready | 2026-12-05 | 85 (midterm) | inside MIX | do not restudy |

## Weak topics
| Topic | Symptom | Drill | Next due | Streak | CAL |
| Trees/AVL | rotations blank | 8 on paper | 2026-12-12 | 0 | OVER |
| Graphs | DFS/BFS mix | trace both | 2026-12-12 | 0 | n/a |
| SQL joins | row counts | 15 queries | 2026-12-13 | 0 | OVER |
| Normalization | 2NF/3NF mix | sort 12 | 2026-12-14 | 0 | n/a |
| Pipelines | hazards blank | stall marking | 2026-12-16 | 0 | n/a |
| By parts | sign errors | 6 integrals | 2026-12-18 | 0 | OK |

## Waiting weaks (max 5 active above)
- (activates after DS paper: graphs promotes off if mock ≥ 6/8)

## This week
Focus: DS paper + lab deadline, DB joins seeded
Mon: DS paper 09:00 → bridge + lab
Tue: lab demo → OOP MIX
Wed: OOP paper 14:00 → bridge + joins
Thu: DB drills
Fri: DB paper 1
Sat: DB paper 09:00 → bridge + COAL
Sun: COAL drills
Catch-up rule: first leftover block goes to the highest weak topic of the NEXT paper

## Log (last 7 days, one line each)
- 2026-12-05: 190 min, OOP patterns revision, MICRO 7/8
- 2026-12-06: 0
- 2026-12-07: 240 min, DS trees first pass, MICRO 4/8 (weak)
- 2026-12-08: 180 min, Calc assignment redo, 3 sign errors found
- 2026-12-09: 210 min, DB joins practice, 5/8 correct
- 2026-12-10: 160 min, COAL midterm corrections, pipelines blank
- 2026-12-11: this plan

## Notes
No Calc past papers exist — professor's 30 exercise sheets are the scored substitute. Untouched papers: 8 with mark schemes, scheduled one per paper as SLICE baseline. Post-mortem after every paper is mandatory — it feeds the weak board for the next paper.
```
