# Prompt-Lib

A library of practical prompts and mini-systems. Behaviour is **model-agnostic**. Each use case ships **native instruction packs** so ChatGPT (Custom GPTs), Gemini (Gems), Claude (Skills / Projects), Copilot, Cursor, Grok, Perplexity, Poe, and local models are taught the way those products actually work — not with a pasted blob from another vendor.

## Use cases

| Folder | What it does |
|---|---|
| [personalized-study-planner](./personalized-study-planner) | Personalized exam study plan from syllabus, exam date, daily time, and progress. Tracks weak topics. **60s instant:** [`60-SECOND.md`](./personalized-study-planner/60-SECOND.md). **People receiving this:** [`START-HERE.md`](./personalized-study-planner/START-HERE.md). **Builders:** [`native/`](./personalized-study-planner/native). **Quality gate:** [`eval/`](./personalized-study-planner/eval). |

## Pattern for every use case

```text
use-case/
├── core/      ← source of truth (rules, schemas)
├── native/    ← one pack per product (GPT / Gem / SKILL.md / Modelfile / …)
├── prompts/   ← optional small paste-in prompts
├── templates/ ← including 60-second intake
├── eval/      ← automated quality gate (eval.py + fixtures)
└── examples/
```

More use cases get their own folder in that pattern. Study OS is the reference 10/10 implementation.
