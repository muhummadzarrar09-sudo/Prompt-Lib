# Worked example — Maya, 26 days out

This is what a good first reply should look like. Use it as a quality check: if your assistant returns a 30-day hourly calendar and “revise all of organic chemistry”, it ignored the prompt. Start a new chat and paste [`../STUDY-OS.md`](../STUDY-OS.md) again.

Must also match [`output-gallery.md`](./output-gallery.md): command center first, 3 non-negotiables, do-not-open list, `- [ ]` ticks, a score on every block, DONE stamp, card last.

Names and dates are fictional. The structure is the point.

## What Maya pasted

```text
Exam: Grade 12 Chemistry + Biology combined science paper
Exam date: 23 October 2026
Today: 27 September 2026
Level: school
Format: mixed — 40% MCQ, 40% short answer, 20% one long question. Chemistry and Biology equally weighted.
Weekdays: 75 min, usually 19:00–20:15
Weekend: Sat 3 hours (10:00–13:00), Sun 90 min (16:00–17:30)
Football Tue 17:30–19:00 so Tuesday is 45 min max

Syllabus:
Chemistry
- Atomic structure & bonding
- Stoichiometry & moles
- Acids, bases, salts
- Rates & equilibrium
- Organic: alkanes/alkenes, alcohols, carboxylic acids, mechanisms (cracking, addition, substitution)
- Electrochemistry

Biology
- Cell structure & mitosis
- Enzymes
- Photosynthesis & respiration
- Human physiology: digestion, circulation, breathing, nerves, hormones, nephron
- Genetics: Mendel, DNA, protein synthesis, meiosis
- Ecology

Progress:
Chemistry: bonding done, moles okay, acids done, rates half, organic barely started, electrochemistry not started
Biology: cells + enzymes solid, photosynthesis okay, physiology messy (nephron and hormones blank), genetics mixed, ecology strong

Confidence:
Bonding 4, moles 3, acids 4, rates 2, organic mechanisms 1, electrochemistry 1
Cells 4, enzymes 4, photosynthesis 3, digestion 3, circulation 3, breathing 3, nerves 2, hormones 1, nephron 1, Mendel 3, meiosis 2, protein synthesis 2, ecology 5

Weak: organic mechanisms (I never know which reaction), nephron (blank), hormones (mix up who secretes what), meiosis (mix with mitosis), rates calculations
Past papers: yes, 4 papers + mark schemes
Today I can study: 75 minutes starting 19:00
```

## What Study OS should return (abridged but realistic)

### 1. Command center

```text
COMMAND CENTER
Exam: Grade 12 Chem + Bio  |  23 Oct 2026  |  DAYS=26
Clock: Twd=75 min (Tue 45)  /  weekend=Sat 180 Sun 90
BANK=24.0h  NEED=32.0h  LOAD=1.33  TIGHT
COV=20%  WCOV=18%  CAVG=2.8  RED/AMBER/GREEN=6/5/3
WK=5 due today=2  ADH_7=n/a%  CAL=OVER  NEXT_PROBE=2026-09-28
PROFILE  HARD=memory  STR=questions  BLOCK=25m  START=ok  TIMED=fine  WEAKHOW=face  STATE=ok
THIS WEEK'S 3 NON-NEGOTIABLES
1. 8-reaction organic map from memory, 6/8 correct
2. Nephron labelled without notes + 4 process Qs
3. Hormones: 12-row gland → effect table, closed book
DO NOT OPEN THIS WEEK
- Ecology notes (already exam-ready)
- Rewriting bonding summaries
```

Two new chemistry units + four biology landmines. Full coverage of every sub-topic is not honest.

### 2. Topic map (excerpt, RED first)

| Topic | Subject | Weight | Confidence | Signal | Status | Priority | Next action |
|---|---|---|---|---|---|---|---|
| Organic mechanisms | Chem | 5 | 1 | RED | Not started | 22.5 | 25 min reaction-map from memory + 5 “which reaction?” Qs |
| Nephron | Bio | 4 | 1 | RED | Not started | 18 | 20 min labelled sketch + 4 process questions |
| Hormones | Bio | 4 | 1 | RED | Not started | 18 | 20 min gland → hormone → effect table, closed book |
| Rates & equilibrium | Chem | 4 | 2 | RED | Learning | 16 | 2 calculation questions + 1 graph |
| Meiosis | Bio | 4 | 2 | RED | Learning | 16 | Mitosis vs meiosis T-chart + 5 MCQ |
| Electrochemistry | Chem | 4 | 1 | RED | Not started | 15 | 25 min cell diagram + 3 Qs (starts this weekend) |
| Protein synthesis | Bio | 3 | 2 | RED | Learning | 12 | 15 min transcription/translation brain dump |
| Moles | Chem | 4 | 3 | AMBER | Revising | 8 | 3 mixed calculation Qs, Sat |
| Ecology | Bio | 3 | 5 | GREEN | Exam-ready | 3 | Do not restudy this week |

GREEN (maintenance only): bonding, cells, enzymes, acids.

### 3. Weak-topic board

| Topic | Symptom | Drill (15–25 min) | Next due | If you blank |
|---|---|---|---|---|
| Organic mechanisms | Cannot pick addition vs substitution vs cracking | Blank A4: reagent → condition → product for 8 reactions, then check | 27 Sep | Write reagent + condition only, check, retry 3 |
| Nephron | Goes blank on names and direction of flow | Draw and label from memory, arrow the 4 processes, 4 short Qs | 27 Sep | Trace one drop of filtrate, say the 4 processes out loud |
| Hormones | Mixes glands and effects | 12-row table from memory: gland / hormone / target / effect | 28 Sep | 4 rows only (insulin, adrenaline, ADH, oestrogen) |
| Meiosis | Mixes with mitosis | One page: purpose, where, steps, chromosome number. Then 5 MCQ | 29 Sep | Two columns, three rows: purpose / where / n |
| Rates calculations | Setup is wrong, arithmetic is fine | 3 past-paper rate Qs, write the formula before touching the numbers | 30 Sep | Formula on paper, no numbers until it is written |

Waiting: protein synthesis (rotates in once hormones hits streak 2).

### 4. Time budget

- Calendar days: 26. Minus 4 lighter Sundays-style blocks and 2 buffers → ~20 study days.
- Usable hours: ~20 × ~1.4h × 0.85 ≈ **24 hours**.
- Needed if everything is fully exam-ready: ~32 hours.
- **Triage:** full coverage on organic, rates, electrochemistry, nephron, hormones, meiosis, moles. Skim: nerves, breathing recap. Drop extra ecology depth and pretty rewriting of bonding notes.

### 5. Week-by-week targets

- **Week 1 (now):** organic map built, nephron + hormones off “blank”, rates calculations started, meiosis distinction clean.
- **Week 2:** electrochemistry in, organic questions not just notes, first full mixed paper (timed 50%).
- **Week 3:** second paper full timed, protein synthesis + moles mixed, weaks on 7-day spacing.
- **Final 5 days:** papers and mark schemes, lightning weaks, sleep. No new topics.

### 6. Next 7 days (one job + if this dies)

| Day | Clock | One job | If this dies |
|---|---|---|---|
| Sun 27 Sep | 19:00–20:15 | Organic 8-map + nephron sketch | 20 min organic map tomorrow. Not 23:00. |
| Mon 28 | 19:00–20:15 | Organic which-reaction Qs + hormones table | Hormones 4-row mini-table only |
| Tue 29 | 20:00–20:45 | Hormones redo + meiosis T-chart (45 min) | Meiosis 3-row T-chart only |
| Wed 30 | 19:00–20:15 | Rates 2 calc + 1 graph, then organic spaced | Organic 8-map redo, drop the graph |
| Thu 1 Oct | 19:00–20:15 | Electrochem cell diagram + nephron Qs | Nephron 4 Qs only |
| Fri 2 | 19:00–20:15 | Mixed 15 MCQ on weaks | 10 MCQ, stop |
| Sat 3 | 10:00–13:00 | Electrochem + moles + weaks | Last 40 min = organic + nephron. Drop moles. |

Catch-up rule: first leftover block goes to organic mechanisms. Never recover a dead weeknight after 22:30.

### 7. Today’s session (tick list)

```text
TODAY · Sun 27 · 75 min · 19:00–20:15

- [ ] 19:00–19:05  Recall: mole triangle + 1 example, no notes
      Done = written without looking
- [ ] 19:05–19:40  Organic: 8-reaction blank map (cracking, +Br2, +H2, alcohol ox, esterification, substitution, polymer, fermentation)
      Done = __/8  (need 6). Star misses.
- [ ] 19:40–19:45  Break. Stand up.
- [ ] 19:45–20:10  Nephron: draw, label, arrow 4 processes, 4 Qs
      Done = diagram complete, __/4 Qs
- [ ] 20:10–20:15  Fill the DONE stamp

IF THIS DIES → 20 min organic map tomorrow. Do not start at 23:00.

TOMORROW FIRST → hormones 12-row table from memory

DONE STAMP (paste back after you finish)
DONE
Minutes:
Finished:
Scores: organic __/8   nephron __/4
Shaky:
Skipped?:
```

Organic confidence 1→2 only if ≥6/8. Nephron stays 1 unless the diagram was fully labelled.

### 8. How to talk to me tomorrow

Paste the card. Type `TODAY — 75 minutes from 19:00` or paste the DONE stamp with numbers. That is enough.

### 9. Study OS Card (what Maya saves)

```
# STUDY OS CARD
Date: 2026-09-27
Student: Maya
Exam: Grade 12 combined science (Chem + Bio)
Exam date: 2026-10-23
Days left: 26
Format: 40% MCQ / 40% short / 20% long; Chem = Bio
Weekday time: 75 min (usually 19:00–20:15); Tue 45 min
Weekend time: Sat 180 min (10:00–13:00); Sun 90 min
Constraints: football Tue 17:30–19:00
Verdict: TIGHT

## Topics
| Topic | Subject | Weight | Confidence | Status | Last studied | Next action |
| Organic mechanisms | Chem | 5 | 1 | Learning | 2026-09-27 | 8-reaction map + which-reaction Qs |
| Nephron | Bio | 4 | 1 | Learning | 2026-09-27 | Labelled sketch + 4 Qs |
| Hormones | Bio | 4 | 1 | Not started | — | 12-row closed-book table |
| Rates & equilibrium | Chem | 4 | 2 | Learning | — | 2 calc + 1 graph |
| Meiosis | Bio | 4 | 2 | Learning | — | vs mitosis T-chart + 5 MCQ |
| Electrochemistry | Chem | 4 | 1 | Not started | — | Cell diagram + 3 Qs (Thu/Sat) |
| Protein synthesis | Bio | 3 | 2 | Learning | — | Waiting weak; brain dump week 2 |
| Moles | Chem | 4 | 3 | Revising | — | 3 mixed calc, Sat |
| Acids, bases, salts | Chem | 3 | 4 | Revising | — | Maintenance MCQ Fri |
| Bonding | Chem | 3 | 4 | Exam-ready | — | Do not restudy |
| Cells + mitosis | Bio | 3 | 4 | Exam-ready | — | Only if mixed paper misses |
| Enzymes | Bio | 3 | 4 | Exam-ready | — | Maintenance |
| Photosynthesis & respiration | Bio | 3 | 3 | Revising | — | Week 2 recap |
| Ecology | Bio | 3 | 5 | Exam-ready | — | Week 3, 10 min only |

## Weak topics
| Topic | Symptom | Drill | Next due | Streak |
| Organic mechanisms | Can't pick the reaction | 8-reaction blank map | 2026-09-27 | 0 |
| Nephron | Blank on names/flow | Draw + 4 Qs | 2026-09-27 | 0 |
| Hormones | Mix glands and effects | 12-row table from memory | 2026-09-28 | 0 |
| Meiosis | Mix with mitosis | T-chart + 5 MCQ | 2026-09-29 | 0 |
| Rates calculations | Wrong setup | 3 paper Qs, formula first | 2026-09-30 | 0 |

## Waiting weaks
- Protein synthesis

## This week
Focus: organic map, nephron, hormones, rates, meiosis; electrochemistry starts Thu
Mon: organic Qs + hormones table
Tue: hormones redo + meiosis (45 min)
Wed: rates + organic spaced
Thu: electrochemistry + nephron
Fri: mixed 15 MCQ
Sat: electrochemistry + moles + weaks
Sun: lighter — paper slice or rest if football extra
Catch-up rule: first leftover block goes to organic mechanisms

## Log (last 7 days, one line each)
- 2026-09-27: (fill after session)

## Notes
Past papers: 4 remaining. First half-timed paper in week 2. Do not rewrite bonding notes.
```

## What Maya does tomorrow

She does not start a new chat from scratch. She pastes the card and writes:

```text
DONE — organic 6/8, missed cracking conditions and esterification. Nephron diagram complete but I forgot secretion. 75 min done.

TODAY — 75 minutes from 19:00
```

The assistant should bump organic to confidence 2, keep it on the weak board with those two reactions starred, put secretion into the nephron drill, and build Monday’s session. That loop is the product.
