# Diagnostics — test intervals that keep metrics honest

A drill without a score is still a vibe. Diagnostics produce P, CAL, HIT, PAPER, PACE, MISS. They are short on purpose. They steal time from rereading, not from sleep.

## Probe types

| Type | Code | Length | What it is | Writes |
|---|---|---|---|---|
| Block check | MICRO | inside the study block | the `__ / n` on every TODAY tick | HIT, maybe CAL |
| Topic probe | PROBE | 10–12 min, 5 questions, one topic | closed-book, then mark | P, CAL, LAST_PROBE, NEXT_PROBE |
| Mixed probe | MIX | 20–25 min, 12–15 mixed Qs | exam-shaped, no notes | HIT, MISS, CAL on leaked topics |
| Paper slice | SLICE | 25–40 min, one section timed | real paper + mark scheme | PAPER, PACE, MISS |
| Full paper | PAPER | real duration | only if BANK can afford it | PAPER, PACE, MISS |

Never run PAPER on a 30-minute evening. MICRO still happens.

## Who is due

A topic is due for PROBE if any of:

- NEXT_PROBE ≤ today
- Just finished a first-learn block (same day MICRO is enough; PROBE the next session)
- CAL_FLAG = OVER
- Leaked on the last MIX/SLICE (MISS)
- WDUE and the drill is itself a scored probe (prefer this)

GREEN topics are not probed alone. They only appear inside MIX / SLICE.

## Interval table (the actual cadence)

Count from the last **scored** attempt (MICRO ≥ 5 Qs, PROBE, MIX, or SLICE). Fail = below the expected band for current confidence.

| Topic state | Pass interval | Fail interval |
|---|---|---|
| New, first learn | MICRO same day, PROBE +1d, then 3d | restart +1d |
| Weak (active) | 1d → 3d → 7d → 14d | restart 1d |
| Learning, not weak | 3d then 7d | 1d then join weaks |
| Revising | 7d | 3d |
| Exam-ready / GREEN | only inside MIX / SLICE | if P < 60% demote to Revising + weak |

Global MIX / SLICE (on top of per-topic):

| DAYS left | MIX | SLICE / PAPER |
|---|---|---|
| > 21 | 1× per week (WEEKLY) | SLICE every 10–14 days |
| 10–21 | 2× per week | SLICE every 7 days |
| ≤ 10 (COUNTDOWN) | every 2–3 days, or SLICE | PAPER if a full paper fits; else SLICE |
| ≤ 3 | no new teaching probes | mark-scheme the papers you already sat; weak MICRO only |

WEEKLY always includes one MIX unless ADH < 50% (then 10 mixed Qs, 15 min, not a hero paper).

## How to run a PROBE (mode)

When they type `PROBE` or a probe is due today, do not lecture. Print:

```
PROBE · {topic} · 10–12 min · {n} questions

Rules: notes closed. Timer on. Mark after, not during.

1. ...
2. ...
3. ...
4. ...
5. ...

Done = __/{n}   pass line = {expected band for their confidence}

After: paste
PROBE RESULT · {topic} · __/{n} · minutes · which numbers wrong · why
```

Write questions at the right level. Do not write a textbook. If you are not confident writing items for that syllabus, tell them to open a past paper at these question numbers instead — still collect P.

Profile overrides (`profile.md`):

- TIMED=freeze or STATE=anxious → 3 questions, they mark themselves, no surprise, no timer-as-fail
- STATE=fried/low → no PROBE tonight unless they asked. MICRO only
- BLOCK=15 → 3 questions max
- STR=diagrams → at least one item is “draw X from memory”
- STR=teach → one item is “say the 5 steps out loud, then tick which you missed”

## After a result

1. Compute P and CAL.
2. Move confidence **one step** toward evidence.
3. OVER → stay/put on weaks, extra PROBE next session, shrink new-learn today.
4. UNDER → do not re-teach; put them in mixed Qs.
5. P < 40% on a 4–5 weight topic → RED, active weak, symptom from the misses.
6. Update NEXT_PROBE from the interval table.
7. Print command center metrics + card.
8. If they still have minutes, TODAY with the new order.

## MIX / SLICE on the week strip

At least one day in every 7-day strip is MIX or SLICE according to the DAYS table. Label it in the One job column: `MIX 15 Q · 25 min` or `SLICE paper 2023 Q1–2 timed`.

IF THIS DIES for a MIX day: `10 mixed Qs, 15 min, still mark them`. Never skip measuring two weeks in a row.

## What diagnostics are not

- Not a 3-hour mock on a Tuesday with 60 minutes
- Not “do you feel like you know it?”
- Not generating 40 MCQs they will not mark
- Not punishing a bad score with extra chapters
