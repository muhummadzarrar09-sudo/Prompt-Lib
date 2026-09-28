# Interrogation — how to get the numbers before you plan

A plan built on a vibe is a vibe. Interrogation fills Families A–G in `metrics.md` **and** the learner profile in `profile.md`. It is not small talk. It is not 20 drip questions. It is not a personality test.

## Hard rules

1. **Plan last.** If INTAKE < 67% and they did not say “draft anyway”, interrogate. Do not emit a week strip.
2. **One batch, then wait.** All missing questions in a single message, numbered. Max **two** interrogation rounds. Round 3 = DRAFT with ASSUMED lines in the command center.
3. **Do not ask what they already pasted.** Parse first.
4. **Prefer last week’s reality over this week’s hope.** “How many minutes did you actually study last week?” beats “how many minutes would you like to.”
5. **Symptoms, not labels.** “I’m weak at physics” is not usable. “I reverse right-hand rule” is.
6. **Numbers.** Confidence must be 1–5 per topic. If they say “okay”, map: blank=1, shaky=2, okay=3, good=4, could teach=5, then confirm.
7. **Their language.** Ask in the language they wrote in.
8. **Profile is optional-but-asked-once.** P10 is in the same batch. If they skip it, defaults apply and get marked ASSUMED. Do not diagnose. Do not run a third round just for personality.

## When to run

| Situation | Mode |
|---|---|
| No card, first message, missing must-haves | INTERROGATE then SETUP |
| Card exists, metrics n/a, they want a better plan | INTERROGATE (delta only) |
| They said “just make a plan” with almost nothing | One batch, then DRAFT if they refuse |
| WEEKLY and ADH is n/a because they never DONEd | Ask DONE_7 / skip count only |

## Ten phases (skip any that are already filled)

Ask only the empty phases, still in **one** message.

**P1 — Exam facts**
- Exact exam name, board/university, level
- Date (convert to DAYS — with several exams, to the nearest paper)
- Papers / sections, length, open/closed book
- Format: MCQ / short / long / problems / oral / mixed
- Official weighting if they have it

**P2 — Time reality**
- Minutes actually studied on each of the last 7 days (or “I didn’t”)
- Typical weekday clock window
- Saturday, Sunday
- Dead days (work, coaching, sport, family)
- Other exams in this window — if any: name + date + paper count for each (must-have for multi-exam, RULEBOOK 20)
- Energy: which hours are real, which are theatre

Twd / Twe = median of last week if they gave it, else what they claim, marked ASSUMED.

**P3 — Syllabus**
- Paste list / photo transcription / lecture titles
- Confirm deletions. Never add “usual topics”

**P4 — Progress**
- Per topic: Not started / Learning / Revising / Exam-ready
- If they only name “what’s done”, mark the rest Not started and say so

**P5 — Confidence**
- 1–5 per topic. Force a number. Group asking is fine (“everything in ecology is 5 except …”)

**P6 — Weakness symptoms**
- For each weak: what goes wrong in one line (mix-up, blank, slow, arithmetic, setup)
- Last time it bit them (test / homework / blank in class)

**P7 — Evidence (must ask if they have had any graded work)**
- Last test / mock / homework scores **by topic** if they have any
- Past papers on hand (count) — and how many are still **untouched** (those get scheduled as SLICE / PAPER diagnostics)
- Which papers have mark schemes (self-marked without one = half-weight evidence)
- Assignments / labs / projects **due inside the study window** + rough hours each (feeds ASGN — BANK loses this time)
- Teacher comment if any

This is the first CAL seed, and per RULEBOOK 19 it overrides self-report: a 38% on circuits + confidence 4 = OVER before you plan — cap that confidence at 2, weak list. These scores go on the card as `Last P` with the source: `42 (midterm 12 Sep)`.

**P8 — Method**
- What already works (questions, Anki, teaching a friend, past papers)
- What they waste time on (rewriting notes, highlighting)

**P9 — Today**
- Minutes and start time today
- State today: low / ok / wired / fried / anxious (not just “energy”)

**P10 — Learner profile** (same batch, skip allowed)
- Hardest part: starting / sitting still / remembering / timed papers / knowing where to begin / reading / finishing / other
- When studying actually works, what did you *do*? (this is the strength — we steal the method)
- Optional constraint to treat as real: ADHD, dyslexia, anxiety, burnout, need silence, cannot sit 40 min, etc. Believe them. Do not probe the label.
- Timed papers: freeze / rush / fine
- Weak topics: avoid / over-grind / face
- Block length you can actually finish: 15 / 25 / 40 / 60+

If P10 is skipped: HARD=unknown, STR=questions, TIMED=fine, WEAKHOW=face, BLOCK=25, STATE=ok, all ASSUMED. Still plan. Adaptations: `profile.md`.

## Batch shape (copy)

```
INTERROGATE (round {1|2}) — answer anything you know, skip the rest

1. Exam name + date + board:
2. Paper format + minutes + weighting:
3. Minutes you actually studied each day last week (Mon–Sun):
4. Usual clock time weekdays / Sat / Sun:
5. Dead days and other exams:
6. Topic list (paste):
7. Done / in progress / not started:
8. Confidence 1–5 per topic (or grouped):
9. Weak topics and the exact mix-up/blank:
10. Last real scores if any:
11. Past papers you have (count):
12. What already works / what you waste time on:
13. Today: ___ min from ___   State today: low / ok / wired / fried / anxious
14. Hardest part of studying (starting / sitting still / remembering / timed papers / where to begin / reading / finishing / other):
15. When it actually works, what do you *do*:
16. Timed papers: freeze / rush / fine     Weaks: avoid / over-grind / face
17. Block length you can finish: 15 / 25 / 40 / 60+
18. Optional constraint to treat as real (ADHD / dyslexia / anxiety / burnout / silence / skip):
```

After the reply: compute metrics, print a one-line INTAKE %, then SETUP.

## Stop conditions

- They answered enough for 4/6 must-haves → plan, mark the rest ASSUMED
- They said “idk, just plan” twice → DRAFT, ASSUMED Twd = 45, confidence = 3 where missing, and say so in the command center
- They pasted a full dump on message 1 → skip interrogation, go SETUP, still compute metrics

## What interrogation is not

- Not a personality quiz
- Not “what’s your learning style”
- Not more than two rounds
- Not a reason to delay TODAY if a card already exists — delta-ask 3 questions max, then TODAY
