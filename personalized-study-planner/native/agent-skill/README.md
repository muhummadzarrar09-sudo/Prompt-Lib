# Agent Skill (open `SKILL.md`)

This pack is the [Agent Skills](https://agentskills.io) standard: a folder with `SKILL.md` plus optional `references/`. One folder runs anywhere that standard is implemented.

Confirmed consumers of this format include Claude (claude.ai Skills + Claude Code), GitHub Copilot, Cursor, OpenAI Codex, Gemini CLI, and other coding agents that load `SKILL.md`.

## Install

Copy the whole `agent-skill` folder and rename it `study-os`.

| Product | Put it here |
|---|---|
| Claude Code (this project) | `.claude/skills/study-os/` |
| Claude Code (your user) | `~/.claude/skills/study-os/` |
| claude.ai custom Skill | Zip `SKILL.md` + `references/` and upload in Skills settings |
| GitHub Copilot | `.github/skills/study-os/` |
| Cursor | `.cursor/skills/study-os/` or `~/.cursor/skills/study-os/` |
| Codex | `~/.codex/skills/study-os/` (or the project skills dir your Codex build uses) |
| Gemini CLI | `.gemini/skills/study-os/` or the skills path in Gemini CLI docs |

The folder must contain:

```text
study-os/
├── SKILL.md
└── references/
    ├── output-spec.md
    ├── card-schema.md
    ├── priority-and-time.md
    ├── session-builder.md
    ├── metrics.md
    ├── diagnostics.md
    └── profile.md
```

`references/` in this pack are the files the skill should load on demand. They match `core/` (plus `session-builder.md`). If you edit core, copy `output-spec.md`, `card-schema.md`, and `priority-and-time.md` here before you re-install.

## How it should trigger

The YAML `description` is the trigger. Students should be able to say any of:

- “make me a study plan”
- “exam on 23 Oct, here’s my syllabus”
- “TODAY 45 minutes” + paste a card
- “track my weak topics”
- “I fell behind”

If it does not trigger, start the message with `Use the study-os skill` (Claude Code) or `@study-os`.

## Workspace behaviour

If you can write files and the user is studying inside this repo (or they ask you to save):

- Update / create `study-os-card.md` in the working directory when the card changes
- Do not create other notes, timetables, or scripts unless asked
