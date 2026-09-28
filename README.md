# Prompt-Lib

A library of practical prompts and mini-systems. Behaviour is **model-agnostic**. Each use case ships **native instruction packs** so ChatGPT (Custom GPTs), Gemini (Gems), Claude (Skills / Projects), Copilot, Cursor, Grok, Perplexity, Poe, and local models are taught the way those products actually work — not with a pasted blob from another vendor.

## Use cases

| Folder | What it does |
|---|---|
| [personalized-study-planner](./personalized-study-planner) | Personalized exam study plan. **Instagram / Student Edition:** [`STUDENT-FRIENDLY.md`](./personalized-study-planner/STUDENT-FRIENDLY.md) — plain English/Urdu, no jargon, WhatsApp friendly. **Web builder:** [`tools/study-os-builder.html`](./personalized-study-planner/tools/study-os-builder.html) — fill form → copy → ChatGPT. **30s start:** [`FOR-INSTAGRAM.md`](./personalized-study-planner/FOR-INSTAGRAM.md). **People receiving this:** [`START-HERE.md`](./personalized-study-planner/START-HERE.md). |

## Pattern for every use case

```text
use-case/
├── STUDENT-FRIENDLY.md  ← plain language edition (Instagram / WhatsApp)
├── FOR-INSTAGRAM.md     ← DM kit + story templates
├── tools/               ← dynamic web builder (no backend)
├── core/                ← source of truth (rules, schemas)
├── native/              ← one pack per product
├── prompts/             ← modular prompts
├── templates/           ← 60-second intake etc
├── eval/                ← quality gate
└── examples/
```

Study OS is the reference implementation — Student Edition is what you share on Instagram, core/ is what builders edit.
