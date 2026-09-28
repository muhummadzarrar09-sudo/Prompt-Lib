# Prompt-Lib

A library of practical prompts and mini-systems. Behaviour is **model-agnostic**: each use case ships one source-of-truth rulebook plus **native instruction packs** — a Custom GPT is not a Gem is not a Claude Skill is not a Modelfile, and each is taught the way that product actually works.

## Use cases

| Folder | What it does |
|---|---|
| [personalized-study-planner](./personalized-study-planner) | Personalized exam study plan ("Study OS"). Born from an Instagram question booth. **Start:** [`STUDENT-FRIENDLY.md`](./personalized-study-planner/STUDENT-FRIENDLY.md) (plain English/Urdu, WhatsApp-friendly) or the full [`STUDY-OS.md`](./personalized-study-planner/STUDY-OS.md). Web builder: [`tools/study-os-builder.html`](./personalized-study-planner/tools/study-os-builder.html). Native packs: [`native/`](./personalized-study-planner/native). |

One use case today — honest about that. The structure (core rules → projections → native skins → eval) is built so the next use case is a folder, not a rewrite.

## Pattern

```text
use-case/
├── core/          ← source of truth: rules, schemas, metrics. Written once.
├── STUDY-OS.md    ← paste-in projection of core (any chat box)
├── STUDENT-FRIENDLY.md  ← plain-language front door (Instagram/WhatsApp)
├── native/        ← per-product packs wrapping core (chatgpt, claude, gemini, …)
├── prompts.md     ← modular mode prompts
├── tools/         ← no-backend web builder
├── examples/      ← the quality bar
└── eval/          ← quality gate + drift guard
```

Rule: anything user-facing is a projection of `core/`. If a copy and core disagree, core wins and the copy gets regenerated — `personalized-study-planner/eval/check_copies.py` enforces this for the mirrors it knows about.
