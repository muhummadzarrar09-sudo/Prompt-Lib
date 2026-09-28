# Metrics — source of truth for every number Study OS prints

Do not invent extra KPIs. Use these, with these codes, computed this way. If a number cannot be computed, print `n/a` — never a fake 0.

A plan is a function of metrics. Interrogation exists to fill them. Diagnostics exist to keep them honest.

---

## Family A — Time and capacity

| Code | Name | Formula | Unit |
|---|---|---|---|
| DAYS | Days to next paper | nearest paper date (any exam in the window) − today; single exam unchanged | days |
| NEXAM | Next paper | name + date of that nearest paper | name, date |
| REST | Lighter days reserved | floor(DAYS / 7) | days |
| BUF | Buffer days | 2 if DAYS ≥ 21, else 0 | days |
| SDAYS | Study days | DAYS − REST − BUF (min 1) | days |
| Twd | Weekday minutes | what they **actually** did last week, not the fantasy. If unknown, take what they typed and mark it ASSUMED | min |
| Twe | Weekend minutes | same rule | min |
| TAVG | Average daily minutes | (5×Twd + Twe_sat + Twe_sun) / 7 | min |
| ASGN | Assignment tax | hours of assignments / labs / projects due inside the study window (P7). A deadline inside the window is not study time | hours, 1 decimal |
| BANK | Usable hours | SDAYS × (TAVG/60) × 0.85 − ASGN | hours, 1 decimal |
| NEED | Hours to cover well | sum of per-topic estimates (see below) | hours, 1 decimal |
| LOAD | Load ratio | NEED / BANK | 2 decimals |
| VERDICT | Capacity verdict | LOAD ≤ 1.00 ON TRACK; 1.01–1.25 TIGHT; > 1.25 NOT ENOUGH TIME | enum |

Per-topic NEED hours:

| Topic state | Hours |
|---|---|
| Not started | 2.2 (use 1.5 if they are fast / short topic, 3.0 if heavy) |
| Uni course-unit, lecture-based | 3.0 (2.0 short unit, 5.0 heavy / problem-heavy) |
| Learning | 1.3 |
| Revising | 0.85 |
| Exam-ready | 0.2 (maintenance) |
| On weak list | × 1.4 on top of the row above |

---

## Family B — Coverage and readiness

| Code | Name | Formula |
|---|---|---|
| N | Topic count | rows on the topic map |
| ER | Exam-ready count | status = Exam-ready |
| COV | Coverage | ER / N | 0–100%, integer |
| WCOV | Weighted coverage | Σ (Weight × readyFlag) / Σ Weight | 0–100%. ReadyFlag = 1 if Exam-ready, 0.5 if Revising, 0 else |
| CAVG | Mean confidence | mean of topic confidence | 1 decimal |
| RED / AMBER / GREEN | Signal counts | RED: conf ≤ 2 or weak. AMBER: conf = 3 or stale > 21d. GREEN: conf ≥ 4 and not weak | counts |
| WCOV_GAP | Remaining weighted work | 100 − WCOV | % |

WCOV is the coverage number that matters. COV lies when they “finished” three tiny topics and blanked a 5-weight one.

---

## Family C — Weakness

| Code | Name | Formula |
|---|---|---|
| WK | Active weaks | count, cap 5 |
| WWAIT | Waiting weaks | parked |
| WLOAD | Weak exam-weight | Σ Weight of active weaks | 1–25 |
| WDUE | Drills due today | next due ≤ today | count |
| WSTREAK | Best current streak | max streak on active weaks | integer |
| WPROMO_7 | Promoted in last 7 days | count |

Priority: `P = Weight × (6 − confidence) × Freshness × Weak(1.5) × PROX`.

| Code | Name | Rule |
|---|---|---|
| PROX | Proximity boost | ×1.5 the topic's exam is the next paper, ×1.25 the one after, ×1.0 otherwise (single exam: always ×1.0) |

Freshness: 1 if practiced ≤ 7d, 2 if 8–21d, 3 if never or > 21d.

---

## Family D — Calibration (self vs evidence)

This is why diagnostics exist. Confidence without a score is a vibe.

Map confidence → expected probe %:

| Confidence | Expected band | Midpoint E |
|---|---|---|
| 1 | 0–20% | 10 |
| 2 | 20–40% | 30 |
| 3 | 40–60% | 50 |
| 4 | 60–80% | 70 |
| 5 | 80–100% | 90 |

| Code | Name | Formula |
|---|---|---|
| P | Probe score | correct / attempted × 100 | 0–100, integer |
| CAL | Calibration gap | E − P for that topic | points. Positive = overconfident |
| CAL_FLAG | Flag | OVER if CAL > 15; UNDER if CAL < −15; OK else | enum |
| LAST_PROBE | Last diagnostic date | ISO date | |
| NEXT_PROBE | Next diagnostic due | from the interval table | date |

OVER topics get an extra probe next session even if the student feels fine. UNDER topics can skip a re-teach and go to mixed questions.

At intake, graded work the student already has seeds this family: a midterm, quiz, or marked assignment score counts as P with source and date (`Last P: 42 (midterm 12 Sep)`), and RULEBOOK 19 caps / floors confidence accordingly. Probes keep it honest after that. Evidence they walk in with is never thrown away.

On DONE: if they report a score, recompute CAL and **move confidence toward the evidence**, not toward their mood. One step per probe (4→3 if they scored 40% etc). Never jump 5→1 on one quiz unless they asked to.

---

## Family E — Adherence and retrieval

| Code | Name | Formula |
|---|---|---|
| PLAN_7 | Minutes planned last 7 days | from the week strip / log | min |
| DONE_7 | Minutes actually done last 7 days | from DONE stamps | min |
| ADH | Adherence | DONE_7 / PLAN_7 | 0–100%. n/a if PLAN_7 = 0 |
| SKIP_7 | Sessions skipped | planned days with 0 minutes | count |
| HIT | Retrieval hit rate | Σ scores / Σ attempted on probes + block `__ / n` in last 7 days | 0–100% |
| SPACE | Spacing compliance | drills done on/before due / drills that came due | 0–100% |

ADH policy:

- ADH ≥ 80% — keep volume, add one paper slice if DAYS ≤ 21
- ADH 50–79% — keep topics, shrink minutes 20%
- ADH < 50% — STUCK rules: cut scope, 70% volume, no new topics this week

---

## Family F — Exam simulation

| Code | Name | Formula |
|---|---|---|
| PAPER | Last paper / slice % | marks / max | 0–100% |
| PACE | Pacing | time used / time allowed | 2 decimals. > 1.10 = too slow |
| MISS | Topics that leaked on the last paper | list | |
| PAPERS_LEFT | Unused past papers | count | |

MISS topics become weaks with symptom “leaked on paper {date}”.

---

## Family G — Intake completeness

| Code | Name | Rule |
|---|---|---|
| INTAKE | Completeness | must-haves filled / 6 | 0–100% |
| Must-haves | exam name, exam date, Twd/Twe, topic list, progress, confidence | |
| Must-haves (multi-exam) | every exam's name + date when more than one shares the window | |
| Nice-to-haves | format, weights, past papers, other exams, dead days, method that works, last real scores | |

Do not lock a plan at INTAKE < 67% (fewer than 4/6) unless they explicitly said “draft it anyway”. Label it DRAFT.

---

## What the command center must print

```
COMMAND CENTER
Exam: {name}  |  {date}  |  DAYS={n}
Clock: Twd={..}  /  weekend={..}
BANK={h}h  NEED={h}h  LOAD={x.xx}  {VERDICT}
COV={n}%  WCOV={n}%  CAVG={x.x}  RED/AMBER/GREEN={a}/{b}/{c}
WK={n} due today={n}  ADH_7={n}%  CAL={FLAG}  NEXT_PROBE={date}
THIS WEEK'S 3 NON-NEGOTIABLES
...
DO NOT OPEN THIS WEEK
...
```

If a metric is n/a, write `n/a` (e.g. ADH_7 before any DONE). Do not hide LOAD.

---

## Priority of metrics when they fight

1. LOAD / VERDICT — if NOT ENOUGH TIME, triage before anything else
2. CAL_FLAG = OVER — probe beats new learning
3. WDUE — due weaks eat first
4. WCOV_GAP on high-weight RED — next learn block
5. ADH < 50% — shrink, don’t add
6. PAPER / PACE — in COUNTDOWN, these outrank new topics

---

## Rounding

- Hours: 1 decimal
- Ratios: 2 decimals
- Percents: integer
- Confidence: integer 1–5 on the card, CAVG 1 decimal
