# Native packs — same coach, each model’s own instructions

The behaviour lives in [`../core`](../core). This folder is only **how each product wants to be taught**.

Do not paste a Custom GPT blob into Claude, and do not paste a SKILL.md into a Gemini Gem. Use the pack for the product you are actually in.

## Pick your product

| You are using | Open this | Native format |
|---|---|---|
| Any chat (paste once) | [STUDY-OS.md](../STUDY-OS.md) | System / first message |
| ChatGPT Custom GPT | [chatgpt](./chatgpt) | Name, description, instructions, starters, knowledge files |
| ChatGPT Project | [chatgpt](./chatgpt#chatgpt-project) | Project instructions + files |
| Claude Skill, Claude Code, Codex, Copilot, Cursor, Gemini CLI, and anything that reads `SKILL.md` | [agent-skill](./agent-skill) | [Agent Skills](https://agentskills.io) `SKILL.md` |
| Claude Project (claude.ai) | [claude-project](./claude-project) | Project instructions + files |
| Gemini Gem | [gemini-gem](./gemini-gem) | Gem name + instructions + knowledge |
| Grok | [grok](./grok) | Custom instructions / system |
| Perplexity Space | [perplexity](./perplexity) | Space instructions (search off by default) |
| Poe bot | [poe](./poe) | Bot prompt + greeting |
| Ollama / local models | [ollama](./ollama) | `Modelfile` SYSTEM |

If a new chat product appears and it has no skill format, paste [STUDY-OS.md](../STUDY-OS.md). If it supports Agent Skills, drop in [agent-skill](./agent-skill).

## What “native” means here

Each pack is rewritten for that product’s instruction box, not find-and-replaced.

| Product quirk | How the pack handles it |
|---|---|
| Custom GPTs do not keep memory across chats | Instructions say the **card** is memory; knowledge files hold the rulebook |
| Gems follow short, headed instructions better than a novel | Gem file is ROLE / TASK / FORMAT / CONSTRAINTS; rulebook is uploaded |
| Claude Skills load in three layers | `SKILL.md` = when + procedure; `references/` = math, card, example |
| Coding agents will try to write files | Skill may save `study-os-card.md` if the user is in a workspace; no other files |
| Perplexity wants to search | Space pack forbids search unless they hand you a syllabus URL |
| Local models have no file uploads | Ollama inlines the rulebook in `SYSTEM` |

## Edit path

1. Change behaviour in `core/`.
2. Re-upload knowledge files for GPT / Gem / Claude Project.
3. If you changed a hard rule, also update `agent-skill/SKILL.md` (it inlines the procedure) and the system-prompt packs (Grok, Poe, Ollama). Keep `agent-skill/references/` byte-identical to core — `eval/check_copies.py` checks.
