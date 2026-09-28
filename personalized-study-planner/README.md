# Personalized Study Planner (Study OS)

**If someone sent you this folder, open [START-HERE.md](./START-HERE.md) first.**  
Sending it on: [SHARE.md](./SHARE.md).  
What a good reply looks like: [examples/output-gallery.md](./examples/output-gallery.md).

This README is the full manual — metrics, interrogation, **learner profile (mental state / what’s hard / what’s a strength)**, diagnostic intervals, modes, output, files, native packs, loops, failure modes. The coach itself lives in [`core/`](./core). Native install packs live in [`native/`](./native).

---

## Contents

1. [What this is](#what-this-is)
2. [What this is not](#what-this-is-not)
3. [60-second start](#60-second-start)
4. [The metric system](#the-metric-system) ← read this before anything else in core
5. [User interrogation](#user-interrogation)
6. [Learner profile — not the same machine](#learner-profile--not-the-same-machine)
7. [Diagnostic test intervals](#diagnostic-test-intervals)
8. [How a plan is built from the metrics](#how-a-plan-is-built-from-the-metrics)
9. [Output other people actually receive](#output-other-people-actually-receive)
10. [The Study OS Card](#the-study-os-card)
11. [Modes](#modes)
12. [Daily / weekly / exam loops](#daily--weekly--exam-loops)
13. [Pick your model](#pick-your-model)
14. [File-by-file](#file-by-file)
15. [Examples](#examples)
16. [Sharing this](#sharing-this)
17. [Honest time math](#honest-time-math)
18. [Quality bar / broken output](#quality-bar--broken-output)
19. [FAQ](#faq)
20. [Folder map](#folder-map)
21. [How to edit this later](#how-to-edit-this-later)

---

## What this is

A **study operating system** you paste into ChatGPT, Claude, Gemini, Grok, Copilot, Cursor, Poe, Perplexity, Ollama, or anything with a text box.

You give it:

- syllabus / topic list
- exam date
- minutes you actually have
- current progress
- what’s weak and *why*

It gives you:

- a **metric command center** (days left, hours in the bank vs hours needed, coverage, weak load, adherence, calibration, next probe)
- this week’s **3 non-negotiables** and a **do not open** list
- a **tick list for today** with a score on every block (`__/8`)
- a **weak-topic drill list** with spacing 1d → 3d → 7d → 14d
- scheduled **diagnostic probes** so confidence cannot float free of evidence
- a **Study OS Card** you paste back tomorrow (that is memory — the model has none)

It is not a 30-day fantasy timetable. Those die on day 3. Only the next 7 days are scheduled hour-by-hour. The rest of the runway is weekly targets.

Behaviour is **model-agnostic** ([`core/`](./core)). Each product is taught in **its own native format** ([`native/`](./native)). A Custom GPT is not a Gem is not a Claude Skill.

---

## What this is not

- It will not study for you.
- It will not fit 12 chapters into 6 hours without naming what gets dropped.
- It will not invent your syllabus.
- It will not replace past papers, mark schemes, or a teacher.
- It will not nag you at 19:00. Put a calendar reminder on your phone.
- It will not remember last week unless you paste the card. Custom GPTs and Gems start empty every chat.
- It is not a personality / “learning style” quiz. Interrogation is for **numbers**.

---

## 60-second start

Three tiers — pick your time:

**Tier 1 — 60 seconds, phone, no questions:** [`60-SECOND.md`](./60-SECOND.md) + 4-line intake in [`templates/60-second-intake.md`](./templates/60-second-intake.md). Instant plan + TODAY + card. No interrogation.

**Tier 2 — 2 minutes:** [`QUICK-PROMPT.md`](./QUICK-PROMPT.md) (short prompt, still interrogates if thin).

**Tier 3 — Full OS:** [`STUDY-OS.md`](./STUDY-OS.md) or native pack if you will use this until exam ([Pick your model](#pick-your-model)).

Otherwise:

1. Open any assistant.
2. Copy everything between `START PROMPT` and `END PROMPT` in [`STUDY-OS.md`](./STUDY-OS.md) (Tier 1: [`60-SECOND.md`](./60-SECOND.md), Tier 2: [`QUICK-PROMPT.md`](./QUICK-PROMPT.md)).
3. Under it, paste whatever you have. Blank is allowed — it will interrogate (Tier 1 assumes and labels ASSUMED).

```text
Exam:
Date:
Weekdays: ___ min     Weekends: ___
Minutes I actually studied last week (Mon–Sun):
Topics / syllabus:
Done so far:
Confidence 1–5 if I know it:
Weak topics and what goes wrong:
Last test scores if any:
Past papers I have:
Hardest part of studying + what I do when it works:
Timed papers: freeze / rush / fine     Weaks: avoid / over-grind / face
Block I can finish: 15 / 25 / 40 / 60+
State today: low / ok / wired / fried / anxious
Today I can study: ___ minutes from ___
```

4. If it asks a numbered batch, answer it. That is interrogation. Do not skip it if you want a non-fiction plan.
5. Save the **Study OS Card**. Notes app is fine.
6. Every study day: paste the card + `TODAY — I have ___ minutes from ___`
7. When you stop: paste the **DONE stamp** with scores.
8. When it prints `PROBE`, do the questions closed-book and send `PROBE RESULT`.

---

## The metric system

**A plan is a function of metrics.** Interrogation fills them. Diagnostics keep them honest. The command center prints them. The card stores them.

Canonical formulas: [`core/metrics.md`](./core/metrics.md). Do not invent extra KPIs. Unknown = `n/a`, never a fake 0.

### Family A — Time and capacity

| Code | What | How |
|---|---|---|
| DAYS | Calendar days left | exam date − today |
| REST | Lighter days reserved | floor(DAYS / 7) |
| BUF | Buffer | 2 if DAYS ≥ 21, else 0 |
| SDAYS | Study days | DAYS − REST − BUF (min 1) |
| Twd / Twe | Weekday / weekend minutes | **last week’s reality**, not this week’s hope. Otherwise marked ASSUMED |
| TAVG | Average daily minutes | (5×Twd + Sat + Sun) / 7 |
| BANK | Usable hours | SDAYS × (TAVG/60) × 0.85 |
| NEED | Hours to cover well | sum of per-topic estimates |
| LOAD | Load ratio | NEED / BANK |
| VERDICT | | LOAD ≤ 1.00 **ON TRACK**; 1.01–1.25 **TIGHT**; > 1.25 **NOT ENOUGH TIME** |

NEED hours per topic: Not started 2.2 · Learning 1.3 · Revising 0.85 · Exam-ready 0.2 · on weak list ×1.4.

**LOAD is the adult in the room.** If it is 1.40, the plan names drops. It does not whisper “you’ve got this”.

### Family B — Coverage and readiness

| Code | What | How |
|---|---|---|
| N | Topic count | rows on the map |
| ER | Exam-ready count | status = Exam-ready |
| COV | Raw coverage | ER / N |
| WCOV | Weighted coverage | Σ(Weight × readyFlag) / Σ Weight. ReadyFlag = 1 if exam-ready, 0.5 if revising, 0 else |
| CAVG | Mean confidence | mean of 1–5 |
| RED / AMBER / GREEN | Signal counts | RED: conf ≤ 2 or weak. AMBER: conf = 3 or stale > 21d. GREEN: conf ≥ 4 and not weak |

**WCOV is the coverage number that matters.** COV lies when three tiny topics are “done” and a weight-5 topic is blank.

### Family C — Weakness

| Code | What |
|---|---|
| WK | Active weaks (cap 5) |
| WWAIT | Parked weaks |
| WLOAD | Σ Weight of active weaks |
| WDUE | Drills due today |
| WSTREAK | Best current streak |
| WPROMO_7 | Promoted off the list in the last 7 days |

Topic priority: `P = Weight × (6 − confidence) × Freshness × 1.5 if weak`.  
Freshness: 1 if practiced ≤ 7d, 2 if 8–21d, 3 if never or > 21d.

### Family D — Calibration (self vs evidence)

This is why probes exist. Confidence without a score is a vibe.

| Confidence | Expected probe % (E) |
|---|---|
| 1 | 10 |
| 2 | 30 |
| 3 | 50 |
| 4 | 70 |
| 5 | 90 |

| Code | What |
|---|---|
| P | Probe score, 0–100 |
| CAL | E − P. Positive = overconfident |
| CAL_FLAG | OVER if CAL > 15; UNDER if CAL < −15; else OK |
| LAST_PROBE / NEXT_PROBE | dates |

OVER topics get probed **before** they get taught again. UNDER topics skip the re-teach and go to mixed questions. Confidence moves **one step** toward evidence per probe, never toward mood.

### Family E — Adherence and retrieval

| Code | What |
|---|---|
| PLAN_7 / DONE_7 | Minutes planned vs done, last 7 days |
| ADH | DONE_7 / PLAN_7 |
| SKIP_7 | Planned days with 0 minutes |
| HIT | Retrieval hit rate on `__ / n` + probes, last 7 days |
| SPACE | Drills done on/before due / drills that came due |

ADH ≥ 80% keep volume. 50–79% shrink 20%. **< 50% auto-STUCK** (cut scope, 70% volume, no new topics).

### Family F — Exam simulation

| Code | What |
|---|---|
| PAPER | Last paper / slice % |
| PACE | Time used / time allowed. > 1.10 = too slow |
| MISS | Topics that leaked — they become weaks |
| PAPERS_LEFT | Unused past papers |

### Family G — Intake completeness

| Code | What |
|---|---|
| INTAKE | Must-haves filled / 6 |
| Must-haves | exam name, date, Twd/Twe, topic list, progress, confidence |
| Nice-to-haves | format, weights, past papers, other exams, dead days, method, last real scores |

Do not lock a plan at INTAKE < 67% unless they said “draft anyway”. Label it DRAFT.

### When metrics fight (priority)

1. LOAD / VERDICT — triage first if NOT ENOUGH TIME  
2. CAL_FLAG = OVER — probe beats new learning  
3. WDUE — due weaks eat first  
4. WCOV_GAP on high-weight RED — next learn block  
5. ADH < 50% — shrink, don’t add  
6. PAPER / PACE — in COUNTDOWN these outrank new topics  

---

## User interrogation

Canonical protocol: [`core/interrogation.md`](./core/interrogation.md). Standalone paste: [`prompts/0-interrogation.md`](./prompts/0-interrogation.md).

The first message is usually garbage (“make me a study plan for physics”). Interrogation turns it into metrics.

Rules:

- **Plan last.** INTAKE < 67% → ask, don’t emit a week strip.
- **One numbered batch, then wait.** Not 20 drip questions.
- **Max two rounds.** Round 3 = DRAFT with ASSUMED lines in the command center.
- **Do not re-ask** what they already pasted.
- **Last week’s minutes beat this week’s hope.**
- **Symptoms, not labels.** “I reverse the right-hand rule”, not “I’m weak at physics”.
- **Numbers.** Confidence is 1–5. “Okay” maps to 3 and gets confirmed.

Nine phases (skip any already filled, still one message):

| # | Phase | Fills |
|---|---|---|
| P1 | Exam facts (name, date, board, papers, format, weights) | DAYS, format |
| P2 | Time reality (last 7 days, clock windows, dead days, other exams) | Twd, Twe, TAVG, BANK |
| P3 | Syllabus paste + deletions | N, topic map |
| P4 | Progress per topic | NEED, COV, WCOV |
| P5 | Confidence 1–5 | CAVG, RED/AMBER/GREEN, priority |
| P6 | Weakness symptoms | WK, drills |
| P7 | Evidence (last scores, papers on hand) | CAL seed, PAPERS_LEFT |
| P8 | What already works / what they waste time on | methods, do-not-open |
| P9 | Today’s minutes + STATE (low / ok / wired / fried / anxious) | tonight’s volume |
| P10 | Learner profile — what’s hard, what works, block length, timed freeze, avoid vs overgrind | HOW the plan is shaped |

If they dump a complete block on message 1, skip interrogation and SETUP. Still compute metrics. Still ask P10 once if Profile is empty — same batch, not a third round.

Mode: type `INTERROGATE`. Profile-only: `PROFILE`.

---

## Learner profile — not the same machine

Canonical rules: [`core/profile.md`](./core/profile.md). Standalone paste: [`prompts/8-profile.md`](./prompts/8-profile.md).

Metrics say *what* to study. The profile says *how this human can actually do it*.

This is **not** “visual/auditory/kinesthetic”. That is not a plan. A **strength** becomes the method on the tick. A **hard thing** becomes a structure change (block cap, ignition, untimed first paper). **Tonight’s state** can override the week strip without rewriting their personality.

The coach does **not** diagnose. If they name ADHD, dyslexia, anxiety, burnout — believe them and adapt. If they describe a crisis, stop coaching and tell them to talk to a person.

### Two layers

| Layer | Lives | Changes |
|---|---|---|
| Trait profile | Card `## Profile` | Slow. Asked once in interrogation P10, or `PROFILE` |
| State today | TODAY | Fast. `low / ok / wired / fried / anxious` |

Fried tonight ≠ new identity. It means a 10–20 min rescue, not a 3-hour paper.

### What it asks (once)

1. Hardest part: starting / sitting still / remembering / timed papers / where to begin / reading / finishing / other  
2. When it actually works, what did you *do*? (steal this method)  
3. Optional constraint: ADHD / dyslexia / anxiety / burnout / silence / cannot sit 40 min / skip  
4. Timed papers: freeze / rush / fine  
5. Weaks: avoid / over-grind / face  
6. Block length you can finish: 15 / 25 / 40 / 60+  
7. State today  

Skip allowed. Defaults: STR=questions, BLOCK=25, TIMED=fine, WEAKHOW=face, STATE=ok, marked ASSUMED.

### How the plan changes (stack every matching row)

| If | Then |
|---|---|
| Cannot start (START=friction) | Tick 1 is 5-min ignition. Hardest weak is tick 2. |
| Cannot sit / BLOCK ≤ 25 / ADHD named | Every block capped at BLOCK. Hard stop on the tick. |
| Timed freeze | First SLICE untimed. PROBE is 3 Qs, they mark themselves. No surprise tests. |
| Avoids weaks | After ignition, weak is mandatory. No GREEN comfort first. |
| Over-grinds weaks | Weaks capped at 40% of T. Force MIX as block 2. |
| Strength = questions / papers | Questions first, notes only on misses. |
| Strength = diagrams / teach / walk-talk | Done-line is a map / 60s out loud / standing voice note. |
| STATE fried or low | Ignore the week strip tonight. 10–20 min rescue. Sleep wins. |
| STATE anxious | No new topics. 3-question probe they have seen. Shorter tone. |
| STATE wired | Cap T at 90 even if they offered 4 hours. |
| Burnout named | Slippage 0.70 not 0.85. One non-negotiable, not 3. |
| Perfectionism / cannot finish | Pass line 6/8 not 8/8. Ship the drill. |
| Loses the thread | One topic per block. Two subjects max per day. |

Command center prints:

```text
PROFILE  HARD=start  STR=questions  BLOCK=25m  START=friction  TIMED=freeze  WEAKHOW=avoid  STATE=fried
```

Avoiders still face weaks — after ignition, in BLOCK-sized pieces. The profile is not a free pass to only do comfort topics.

---

## Diagnostic test intervals

Canonical cadence: [`core/diagnostics.md`](./core/diagnostics.md). Standalone paste: [`prompts/7-probe.md`](./prompts/7-probe.md).

Unscored work **does not move confidence**. Every teach/drill tick has `__ / n`. That is already a MICRO diagnostic.

### Probe types

| Type | Length | Use |
|---|---|---|
| MICRO | inside the block | the `__ / n` on TODAY |
| PROBE | 10–12 min, 5 questions, one topic | due weaks, OVER topics, after first-learn |
| MIX | 20–25 min, 12–15 mixed | weekly (and 2×/week when DAYS ≤ 21) |
| SLICE | 25–40 min, one timed section | every 10–14d, then weekly, then every 2–3d in countdown |
| PAPER | real duration | only if BANK can afford it |

### Per-topic interval (from last **scored** attempt)

| State | Pass | Fail |
|---|---|---|
| New, first learn | MICRO same day, PROBE +1d, then 3d | restart +1d |
| Weak (active) | 1d → 3d → 7d → 14d | restart 1d |
| Learning, not weak | 3d then 7d | 1d, join weaks |
| Revising | 7d | 3d |
| GREEN / exam-ready | only inside MIX / SLICE | P < 60% → demote |

### Global MIX / SLICE on top

| DAYS left | MIX | SLICE / PAPER |
|---|---|---|
| > 21 | 1× per week (on WEEKLY) | SLICE every 10–14 days |
| 10–21 | 2× per week | SLICE every 7 days |
| ≤ 10 | every 2–3 days | PAPER if it fits, else SLICE |
| ≤ 3 | no new teaching probes | mark-scheme papers you already sat + weak MICRO |

WEEKLY always includes one MIX unless ADH < 50% (then 10 Qs, 15 min).  
IF THIS DIES on a MIX day: still 10 mixed Qs, 15 min, marked. Never skip measuring two weeks in a row.

Type `PROBE` or `MIX`. If NEXT_PROBE ≤ today, TODAY puts it in block 1 automatically.

After `PROBE RESULT · topic · __/n · minutes · wrong · why`:

1. Compute P and CAL  
2. Move confidence one step toward evidence  
3. OVER → stay on weaks, extra probe next session  
4. P < 40% on a heavy topic → RED weak  
5. Update NEXT_PROBE  
6. Print command center + card  

---

## How a plan is built from the metrics

```text
interrogation → INTAKE, Twd, topics, confidence, symptoms, scores
                         ↓
              compute DAYS, BANK, NEED, LOAD, WCOV, RED, WK, CAL, NEXT_PROBE
                         ↓
              VERDICT: on track / tight / not enough time
                         ↓
              triage: FULL / SKIM / DROP (named)
                         ↓
              priority P = Weight × Gap × Freshness × weak×1.5
                         ↓
              week targets + next 7 days (one job + if this dies)
              at least one MIX/SLICE per interval table
                         ↓
              TODAY ticks, due probe first, every block scored
                         ↓
              you study → DONE / PROBE RESULT → metrics move → repeat
```

Phase split of BANK by DAYS:

- **> 21 days:** 50% close gaps, 30% weak + questions, 20% recap  
- **10–21:** 25% gaps, 50% questions + weaks, 25% mixed papers  
- **≤ 10:** 10% patch, 70% papers / mixed, 20% weak lightning  
- **≤ 3:** papers, mark schemes, weak MICRO, sleep. No new topics  

Session builder by minutes T:

- ≤ 30: 100% one weak / due probe + 3–5 questions  
- 31–60: 60% highest priority, 40% weak  
- 61–120: two blocks + break  
- > 120: max three blocks, two subjects, last 20 min mixed, break each hour  
Always 5 min yesterday-recall unless day 1.

---

## Output other people actually receive

Canonical layout: [`core/output-spec.md`](./core/output-spec.md). Gallery: [`examples/output-gallery.md`](./examples/output-gallery.md).

Skins: SETUP/WEEKLY/COUNTDOWN → **FULL**. TODAY/DONE/WEAK/STUCK/PROBE → **PHONE**. “Print / wall / parent” → **PRINT**. `SHARE` → command center + week strip + ticks, **no card**.

Command center (always first, this is the screenshot):

```text
COMMAND CENTER
Exam: {name}  |  {date}  |  DAYS={n}
Clock: Twd={min} weekday  /  weekend={..}
BANK={h}h  NEED={h}h  LOAD={x.xx}  {VERDICT}
COV={n}%  WCOV={n}%  CAVG={x.x}  RED/AMBER/GREEN={a}/{b}/{c}
WK={n} due today={n}  ADH_7={n}%  CAL={FLAG}  NEXT_PROBE={date}
THIS WEEK'S 3 NON-NEGOTIABLES
1. {action with a number, not a unit name}
2. …
3. …
DO NOT OPEN THIS WEEK
- {comfort topic}
```

TODAY is `- [ ]` ticks with `Done = __/n`, then **IF THIS DIES**, **TOMORROW FIRST**, a **DONE stamp**. No tables inside TODAY (they wrap on a phone).

---

## The Study OS Card

Schema: [`core/card-schema.md`](./core/card-schema.md). Blank: [`templates/study-os-card.md`](./templates/study-os-card.md).

The card is the save game. It holds topics, weaks, **metrics**, **last 5 probes**, this week, and a 7-day log. Paste it every session. If the chat forgets, the card does not.

Status: `Not started | Learning | Revising | Exam-ready`.  
Confidence 1–5. Weight 1–5. Signal RED/AMBER/GREEN.

---

## Modes

Type these after the card (or alone on day 1). If you paste a card with no mode, it runs TODAY.

| You type | It does |
|---|---|
| `INTERROGATE` | One numbered question batch (metrics **and** profile). No week strip. |
| `PROFILE` | Update what’s hard / what works / tonight’s state. Changes TODAY. No new week strip. |
| `SETUP` | If intake is thin, interrogate first. Else full plan + metrics + card. |
| `TODAY` | Tick list. Due probe/mix is block 1. |
| `DONE` | Updates ADH, HIT, CAL, confidence, weaks, log. |
| `PROBE` | 5 scored questions, 10–12 min, one topic. Wait for `PROBE RESULT`. |
| `MIX` | 12–15 mixed questions, timed. |
| `WEAK` | Landmine drills only (still scored). |
| `WEEKLY` | Recompute all metrics, one MIX, rebuild 7 days. |
| `COUNTDOWN` | Last 10 days. Diagnostics dominate. |
| `STUCK` | Cut scope, 48-hour rescue, 70% volume. Auto if ADH < 50%. |
| `CARD` | Save file only. |
| `METRICS` | Command center + numbers. No new plan. |
| `SHARE` | Screenshot-able plan, no card. |
| `FORMAT: FULL \| PHONE \| PRINT` | Skin override. |

---

## Daily / weekly / exam loops

**Day**

```text
paste card → TODAY → tick the blocks → DONE stamp with scores
if it printed PROBE → closed book → PROBE RESULT
```

**Week (Sunday night / Monday morning)**

```text
paste card → WEEKLY
it scores ADH, HIT, CAL, WCOV
one MIX lands on the new week strip
```

**Last 10 days**

Auto COUNTDOWN. 70% papers/mixed, 20% weak lightning, 10% hole patches. Last 3 days: no new topics.

**Fell off**

`STUCK`. Or just `TODAY` with honest minutes. No lecture.

---

## Pick your model

Full picker and the “why native” notes: [`native/README.md`](./native/README.md).

| You use | Open this | Native format |
|---|---|---|
| ChatGPT Custom GPT or Project | [`native/chatgpt`](./native/chatgpt) | Name, description, instructions, starters, knowledge files |
| Claude Skill / Claude Code / Copilot / Cursor / Codex / Gemini CLI | [`native/agent-skill`](./native/agent-skill) | Agent Skills `SKILL.md` + `references/` |
| Claude Project | [`native/claude-project`](./native/claude-project) | Project instructions + files |
| Gemini Gem | [`native/gemini-gem`](./native/gemini-gem) | Gem instructions + knowledge |
| Grok | [`native/grok`](./native/grok) | System / custom instructions |
| Perplexity Space | [`native/perplexity`](./native/perplexity) | Space instructions, search off by default |
| Poe bot | [`native/poe`](./native/poe) | Bot prompt + greeting |
| Ollama / LM Studio / local | [`native/ollama`](./native/ollama) | `Modelfile` SYSTEM |
| Any other chat box | [`native/any-chat`](./native/any-chat) | Paste [`STUDY-OS.md`](./STUDY-OS.md) |

Do not paste a Custom GPT blob into a Gem. Use the pack for the product you are actually in.

Recommended:

- **Best:** install the native pack so you stop re-pasting the rulebook. Still paste the card every chat — GPTs/Gems have no memory.
- **Fine:** one long chat with `STUDY-OS.md` at the top until the exam.
- **Phone:** card in Notes → copy → TODAY/DONE.

---

## File-by-file

### Front door

| File | What it is |
|---|---|
| [START-HERE.md](./START-HERE.md) | Two-minute front door if someone sent you this |
| [SHARE.md](./SHARE.md) | What to put in a DM / caption — not the git tree |
| [README.md](./README.md) | This manual |
| [60-SECOND.md](./60-SECOND.md) | **60-second instant — 4-line intake, no questions, phone-first** |
| [QUICK-PROMPT.md](./QUICK-PROMPT.md) | Short paste-in prompt (2 min) |
| [STUDY-OS.md](./STUDY-OS.md) | Full paste-in system prompt |

### Eval (quality gate)

| File | What it is |
|---|---|
| [eval/README.md](./eval/README.md) | How to run the gate |
| [eval/eval.py](./eval/eval.py) | Checks COMMAND CENTER, LOAD/WCOV, 3 non-negotiables, checkboxes, __/n, card, no 30-day calendar, no pep |
| [eval/fixtures/](./eval/fixtures/) | good-minimal.md (should PASS), bad-pep-calendar.md / bad-no-metrics.md (should FAIL) |

### Core (edit behaviour here)

| File | What it is |
|---|---|
| [core/RULEBOOK.md](./core/RULEBOOK.md) | Operating spec |
| [core/metrics.md](./core/metrics.md) | Every legal number, with codes and formulas |
| [core/interrogation.md](./core/interrogation.md) | How to fill those numbers — and the profile |
| [core/profile.md](./core/profile.md) | What’s hard, what’s a strength, today’s state, how TODAY changes |
| [core/diagnostics.md](./core/diagnostics.md) | Probe types and intervals |
| [core/output-spec.md](./core/output-spec.md) | Layout other people receive |
| [core/card-schema.md](./core/card-schema.md) | Save-file shape |
| [core/priority-and-time.md](./core/priority-and-time.md) | Priority math + hour budget, for skills to load on demand |

### Native packs

See [Pick your model](#pick-your-model). Each folder has a README with install steps.

### Modular prompts

| File | When |
|---|---|
| [prompts/0-interrogation.md](./prompts/0-interrogation.md) | Facts are thin |
| [prompts/1-setup.md](./prompts/1-setup.md) | First plan |
| [prompts/2-today.md](./prompts/2-today.md) | Every study day |
| [prompts/3-weak-topics.md](./prompts/3-weak-topics.md) | After a test / same topic keeps breaking |
| [prompts/4-weekly-reset.md](./prompts/4-weekly-reset.md) | Once a week |
| [prompts/5-exam-countdown.md](./prompts/5-exam-countdown.md) | ≤ 10 days |
| [prompts/6-fell-behind.md](./prompts/6-fell-behind.md) | Plan is fiction |
| [prompts/7-probe.md](./prompts/7-probe.md) | Scored diagnostic |
| [prompts/8-profile.md](./prompts/8-profile.md) | What’s hard / what works / tonight’s state |
| [prompts/9-instant.md](./prompts/9-instant.md) | 60-second instant, no questions |

### Templates (Notes / Notion / Docs)

| File | When |
|---|---|
| [templates/intake.md](./templates/intake.md) | Fill before the first chat |
| [templates/60-second-intake.md](./templates/60-second-intake.md) | **4-line intake for 60-SECOND.md** |
| [templates/study-os-card.md](./templates/study-os-card.md) | Save file |
| [templates/today-session.md](./templates/today-session.md) | Tick list if the chat is closed |
| [templates/metrics-dashboard.md](./templates/metrics-dashboard.md) | Trend table |
| [templates/probe-log.md](./templates/probe-log.md) | Longer than the 5 rows on the card |
| [templates/weak-topic-log.md](./templates/weak-topic-log.md) | Longer weak memory |
| [templates/daily-session-log.md](./templates/daily-session-log.md) | Evidence for WEEKLY |

### Examples

| File | What |
|---|---|
| [examples/output-gallery.md](./examples/output-gallery.md) | Garbage plan vs required plan |
| [examples/maya-26-days-out.md](./examples/maya-26-days-out.md) | School science, 26 days, two subjects |
| [examples/ahmed-fsc-18-days.md](./examples/ahmed-fsc-18-days.md) | One subject, 18 days, honest triage |

---

## Examples

Use Maya as the quality bar for SETUP. Use Ahmed when BANK is obviously too small. Use the gallery if your assistant sounds like “Week 1: revise chapters 1–3”.

If the first reply has no command center, no 3 non-negotiables, and no `- [ ]` ticks, new chat, paste the prompt as message 1.

---

## Sharing this

Read [SHARE.md](./SHARE.md).

To a student in DMs: one sentence + [`QUICK-PROMPT.md`](./QUICK-PROMPT.md) + optionally START-HERE.  
Do not send `core/` or `native/` unless they asked how to **build** a GPT/Gem/Skill.  
If you built them a GPT/Gem, send the **link**, and still tell them the card is the save file.

---

## Honest time math

Same numbers the coach uses. Sanity-check it.

| Kind of topic | Hours to exam-ready |
|---|---|
| New, never studied | 1.5–3 (default 2.2) |
| Seen in class, not revised | ~1.3 |
| Revised, needs practice | ~0.85 |
| Weak / repeatedly failed | ×1.4 on top |
| Exam-ready maintenance | 0.2 |
| Full past-paper block | 1–1.5 |

Then 15% slippage, rest days, 2 buffers if ≥ 3 weeks. If BANK < NEED, it triages. That is a feature.

What counts as “syllabus”: official PDF text, chapter list, lecture titles, teacher’s “what’s on the exam”, past-paper topic list. A subject name alone → labelled DRAFT map they must edit.

---

## Quality bar / broken output

A reply is **broken** (throw away, redo) if any of these is true:

- Opens with a pep paragraph or “sure, here’s a study plan”
- TODAY has no `- [ ]` checkboxes
- SETUP has no 3 non-negotiables and no do-not-open list
- SETUP/WEEKLY command center is missing LOAD, WCOV, or NEXT_PROBE
- A block says “revise” / “go over” / “study chapter” with no observable done-line
- No `__ / n` to score
- Hourly-schedules past 7 days
- No card after a plan-changing reply
- Invented syllabus topics
- Fake 0s instead of `n/a`

**Automated gate:** `python eval/eval.py <file.md>` — same checks as above + fixtures. See [`eval/README.md`](./eval/README.md). Use in CI.

```bash
python eval/eval.py examples/maya-26-days-out.md
python eval/eval.py eval/fixtures/good-minimal.md  # should PASS
python eval/eval.py eval/fixtures/bad-*.md         # should FAIL
```

---

## FAQ

**The model forgot my plan.** Paste the card. The card is memory.

**It wrote a 30-day calendar.** New chat. Prompt as message 1. Details underneath.

**I only have 20 minutes.** It must give a 20-minute plan, usually one weak probe. If it lectures instead, it failed.

**I don’t know my confidence numbers.** Interrogation will force 1–5. Blank=1, shaky=2, okay=3, good=4, could teach=5.

**It keeps searching the web (Perplexity).** Use [`native/perplexity`](./native/perplexity). Search is forbidden unless you hand it a syllabus URL.

**Which model is best?** The one you will actually open every day. Install that native pack.

**Can I use this for two exams?** One card per exam. Separate chats/projects. Other exams go in Constraints so LOAD stays honest.

**Does this work in Urdu / any language?** Yes. Prose in the student’s language, topic names in the exam’s language.

**I have ADHD / anxiety / I freeze / I cannot start.** Type `PROFILE` or answer P10. The coach must change block length, ignition, probe style, and tonight’s volume — not give a speech. It will not diagnose you.

**I’m fried tonight.** Say `STATE=fried`. You get a 10–20 min rescue. That is not a skip on your character.

**I want a parent/teacher version.** Type `SHARE` or `FORMAT: PRINT`.

---

## Folder map

```text
personalized-study-planner/
├── START-HERE.md
├── SHARE.md
├── README.md                 ← you are here
├── 60-SECOND.md              ← 60s instant, 4-line intake
├── QUICK-PROMPT.md
├── STUDY-OS.md
├── core/
│   ├── RULEBOOK.md
│   ├── metrics.md
│   ├── interrogation.md
│   ├── profile.md
│   ├── diagnostics.md
│   ├── output-spec.md
│   ├── card-schema.md
│   └── priority-and-time.md
├── eval/                     ← quality gate: eval.py + fixtures
├── native/                   ← one pack per product (incl. ollama Modelfile + Modelfile.7b)
├── prompts/                  ← 0 interrogate … 9 instant
├── templates/                ← includes 60-second-intake.md
└── examples/
```

---

## How to edit this later

1. Change **behaviour** in `core/` (metrics, interrogation, diagnostics, rulebook, output-spec, card).
2. Re-upload knowledge files for GPT / Gem / Claude Project.
3. Copy `core/metrics.md`, `card-schema.md`, `diagnostics.md`, `output-spec.md` into `native/agent-skill/references/` if those changed.
4. System-prompt packs (Grok, Poe, Ollama, STUDY-OS.md) need a copy-through of hard rules.
5. Keep the README metric tables in sync with `core/metrics.md` — that file wins.

Same split for the next use case in Prompt-Lib: `core/` for the law, `native/` for how that product wants to be taught.
