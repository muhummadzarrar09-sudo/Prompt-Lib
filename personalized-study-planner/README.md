# Personalized Study Planner (Study OS)

Started as an **Instagram question booth** — students kept asking for a study plan that survives past day 3, so this is the answer, structured as a paste-in system.

**New here? Open [`STUDENT-FRIENDLY.md`](./STUDENT-FRIENDLY.md).** Paste it into ChatGPT / Gemini / Meta AI (WhatsApp works), fill 4 lines, get today's plan. That's the whole onboarding.

You are not the target of this README. This README is for the person editing the system.

---

## What it is

A **study operating system** you paste into any assistant. You give it syllabus, exam date, real daily minutes, current progress, weak topics + why — **plus the evidence you already own**: past-paper scores, midterms, marked assignments. Graded evidence beats self-reported confidence (RULEBOOK 19), and assignments due inside the window come out of the time budget. It gives you:

- an honest time budget (usable hours vs hours needed, named drops if there aren't enough)
- this week's 3 non-negotiables and a **do not open** list
- a tick list for today with a score on every block (`__/8`)
- a weak-topic drill board with spacing 1d → 3d → 7d → 14d
- scheduled diagnostic probes so confidence can't float free of evidence
- a **Study OS Card** you paste back next time — that's memory; the model has none

Only the next 7 days are scheduled hour-by-hour. The rest of the runway is weekly targets. No 30-day fantasy timetable.

**Not**: a tutor, a motivator, a notes-writer. It won't study for you, won't invent a syllabus, won't nag at 19:00.

## The three entry points (and only three)

| Who | File |
|---|---|
| Student from Instagram / WhatsApp | [`STUDENT-FRIENDLY.md`](./STUDENT-FRIENDLY.md) — plain English/Urdu, no jargon |
| Any chat box, full system | [`STUDY-OS.md`](./STUDY-OS.md) — everything between START/END PROMPT |
| Per-product install (Custom GPT, Gem, Claude Skill, …) | [`native/`](./native) |

Plus [`tools/study-os-builder.html`](./tools/study-os-builder.html) (no-backend form → prompt, works on a phone) and [`prompts.md`](./prompts.md) (modular one-pastes per mode). Sharing/running the booth: [`FOR-INSTAGRAM.md`](./FOR-INSTAGRAM.md).

## Architecture — core is the source of truth

```
personalized-study-planner/
├── STUDENT-FRIENDLY.md   ← front door (Instagram). Plain language, no metric codes
├── STUDY-OS.md           ← full paste-in prompt for any chat box
├── prompts.md            ← 9 modular mode prompts, one file
├── FOR-INSTAGRAM.md      ← booth ops: links, DM templates, caption
├── core/                 ← THE RULES. Edit here, nowhere else
│   ├── RULEBOOK.md       ← mission + 18 hard rules
│   ├── metrics.md        ← every number: code, name, formula
│   ├── interrogation.md  ← question batches, INTAKE %, DRAFT rules
│   ├── priority-and-time.md  ← P = W × Gap × Fresh × 1.5(weak), BANK/NEED/LOAD
│   ├── diagnostics.md    ← MICRO/PROBE/MIX/SLICE/PAPER schedule + profile overrides
│   ├── output-spec.md    ← layout contract: command center first, ticks, skins
│   ├── card-schema.md    ← the save-file shape
│   └── profile.md        ← learner profile: strengths=methods, hards=structure
├── native/               ← per-product packs. chatgpt/, claude-project/, gemini-gem/,
│   │                       grok/, perplexity/, poe/, ollama/, agent-skill/
│   └── agent-skill/references/  ← MIRROR of core/ (checked by eval/check_copies.py)
├── templates/            ← study-os-card.md only
├── examples/             ← maya-26-days-out, ahmed-fsc-18-days (quality bar), output-gallery
├── tools/                ← study-os-builder.html
└── eval/                 ← eval.py (quality gate), check_copies.py (drift guard), fixtures/
```

**The one rule of this repo:** a rule or a number is written in `core/`, once. Everything else — paste-ins, native packs, student edition — is a projection of it. When you change `core/`, update the projections and run the eval. `native/agent-skill/references/` must stay byte-identical to `core/` — `eval/check_copies.py` enforces it, so don't hand-edit the copies.

## Modes

`SETUP`, `INTERROGATE`, `TODAY`, `DONE`, `WEAK`, `WEEKLY`, `COUNTDOWN` (≤10 days), `STUCK` (48h rescue), `PROFILE`, `PROBE`/`MIX`, `CARD`, `METRICS`, `SHARE`. The student edition exposes a friendly subset (`TODAY`, `DONE`, `WEAK`, `WEEKLY`, `STUCK`, `CARD`). Full definitions: `core/RULEBOOK.md`.

## Examples = the quality bar

- [`examples/maya-26-days-out.md`](./examples/maya-26-days-out.md) — what a first reply must look like
- [`examples/ahmed-fsc-18-days.md`](./examples/ahmed-fsc-18-days.md) — tight-runway triage
- [`examples/output-gallery.md`](./examples/output-gallery.md) — broken vs required, side by side

## Quality gate

```bash
python3 eval/eval.py --selftest eval/fixtures/*.md examples/*.md   # good passes, bad-* must fail
python3 eval/check_copies.py   # references/ mirrors must match core/
```

`eval.py` checks structure (command center, non-negotiables, ticks, scored blocks, card, no 30-day calendar, no pep opening). Files containing deliberate bad examples carry an `eval-skip` marker. It does not yet check the math or run live models — that's the known gap.

## Editing this later

1. Change `core/` only.
2. Grep for the rule's twins in `STUDY-OS.md`, `STUDENT-FRIENDLY.md`, `native/*/` and update them to match.
3. `python3 eval/check_copies.py && python3 eval/eval.py eval/fixtures/*.md examples/maya-26-days-out.md examples/ahmed-fsc-18-days.md` — both green or it doesn't merge.
