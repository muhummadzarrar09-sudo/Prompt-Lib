# Core — source of truth

This folder is the **model-agnostic rulebook**. Every native pack in [`../native`](../native) is a wrapper around these files.

Edit behaviour here first. Then, if a native pack inlines the rules (Ollama, Grok, Poe, paste-prompt), copy the change through. Packs that **upload** these files (Custom GPTs, Gems, Claude Projects) pick up changes on re-upload.

| File | What it is |
|---|---|
| [RULEBOOK.md](./RULEBOOK.md) | Full operating spec: role, hard rules, intake, scoring, sessions, weaks, modes, outputs |
| [metrics.md](./metrics.md) | Every number Study OS is allowed to print, with codes and formulas |
| [interrogation.md](./interrogation.md) | How to fill those numbers — and the profile — before planning |
| [profile.md](./profile.md) | Learner profile: what’s hard, what’s a strength, today’s state, how the plan changes |
| [diagnostics.md](./diagnostics.md) | Probe types, intervals, what happens to CAL |
| [output-spec.md](./output-spec.md) | What other people actually receive: command center, ticks, skins, broken-output tests |
| [card-schema.md](./card-schema.md) | The save-file format. Memory lives here, not in the model. |
| [priority-and-time.md](./priority-and-time.md) | Scoring formula and hour budget, isolated so skills can load it on demand |

Do not put platform UI copy in this folder (no “Create a GPT”, no YAML frontmatter, no Gem character limits). That belongs under `native/`.
