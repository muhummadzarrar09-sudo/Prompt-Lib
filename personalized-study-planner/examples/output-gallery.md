# Output gallery — what other people should receive
<!-- eval-skip: this gallery deliberately shows broken output side by side with required output — it is a quality reference, not a deliverable. -->

Use this as a quality check. Left is what a generic chat does with “make me a study plan”. Right is what Study OS must look like. If your assistant sounds like the left column, new chat, paste the prompt again.

## SETUP, first screen

**Broken (do not ship)**

```text
Of course! Here’s a comprehensive 4-week study plan to help you
ace your exams. Remember to stay positive and take breaks.

Week 1
Monday: Revise Chapter 1–3
Tuesday: Revise Chapter 4–6
...
Sunday: Rest and review all notes

You’ve got this! 💪
```

**Required**

```text
COMMAND CENTER
Exam: Grade 12 Chem + Bio  |  23 Oct 2026  |  26 days left
Clock: 75 min weeknights (Tue 45)  /  Sat 3h  /  Sun 90m
Bank: 24h available  ·  32h to cover well  ·  TIGHT
THIS WEEK'S 3 NON-NEGOTIABLES
1. 8-reaction organic map from memory, 6/8 correct
2. Nephron labelled without notes + 4 process Qs
3. Hormones: 12-row gland → effect table, closed book
DO NOT OPEN THIS WEEK
- Ecology notes (already exam-ready)
- Rewriting bonding summaries
```

Why the right side ships: a stranger can screenshot it. It names what to ignore. It admits the hours don’t fit.

## Today’s session

**Broken**

```text
Spend some time going over organic chemistry and then review
the nephron. Try some practice questions if you can.
```

**Required**

```text
TODAY · Sun 27 · 75 min · 19:00–20:15

- [ ] 19:00–19:05  Recall: mole triangle + 1 example, no notes
      Done = written without looking
- [ ] 19:05–19:40  Organic: 8-reaction blank map, then check
      Done = __/8  (need 6). Star misses.
- [ ] 19:40–19:45  Break. Stand up.
- [ ] 19:45–20:10  Nephron: draw, label, arrow 4 processes, 4 Qs
      Done = diagram complete, __/4 Qs
- [ ] 19:10–20:15  Fill the DONE stamp

IF THIS DIES → 20 min organic map only, tomorrow. Do not start at 23:00.

TOMORROW FIRST → hormones 12-row table from memory

DONE STAMP (paste back after you finish)
DONE
Minutes:
Finished:
Scores: organic __/8   nephron __/4
Shaky:
Skipped?:
```

Why the right side ships: they can tick it in Notes. Every block has a number. The evening is allowed to die.

## Weak topics

**Broken**

```text
Focus on your weak areas: organic, kidneys, hormones.
Review the chapters again and make notes.
```

**Required**

```text
| Topic | Symptom | Drill (15–25 min) | Next due | If you blank |
| Organic mechanisms | Can't pick the reaction | 8-reaction blank map | 27 Sep | Write reagent only, skip products, check, retry 3 |
| Nephron | Blank on names/flow | Draw + 4 Qs | 27 Sep | Trace one drop of blood, say the 4 words out loud |
```

Why the right side ships: a weak topic is a *symptom + a drill*, not a chapter title.

## Full first replies

- [`maya-26-days-out.md`](./maya-26-days-out.md) — school science, 26 days, two subjects
- [`ahmed-fsc-18-days.md`](./ahmed-fsc-18-days.md) — FSc Physics, 18 days, 60 min evenings

Both must still match this gallery. If they drift, the gallery wins.
