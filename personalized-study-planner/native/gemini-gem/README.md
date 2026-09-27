# Gemini Gem

Gems are not Skills. They are a name + standing instructions + up to 10 knowledge files. Gemini follows **short headed instructions** better than a long essay. Put the operating law in the instruction box; put math, schema, and the worked example in Knowledge.

## Create the Gem

1. [gemini.google.com](https://gemini.google.com) → Gems → New Gem.
2. **Name:** `Study OS`
3. Paste [instructions.md](./instructions.md) into Instructions.
4. Knowledge — upload:
   - `../../core/RULEBOOK.md`
   - `../../core/output-spec.md`
   - `../../core/card-schema.md`
   - `../../core/priority-and-time.md`
   - `../../examples/maya-26-days-out.md`
5. Default tool: **none** (not Deep Research, not image, not Guided Learning).
6. Preview: *“I have an exam in 3 weeks, 1 hour a day, I’ll paste topics.”* It must ask for missing pieces in one batch.
7. Save.

## Gemini CLI / Code Assist

If you are in Gemini CLI, do **not** use this Gem file. Install the Agent Skill:

- [`../agent-skill`](../agent-skill) → `.gemini/skills/study-os/`

Optional project briefing: copy [GEMINI.md](./GEMINI.md) to a study workspace root if you want CLI to treat that folder as a Study OS workspace.

## Quirks this pack accounts for

- Gems ignore buried rules in a wall of prose — instructions are ROLE / TASK / FORMAT / CONSTRAINTS.
- Uploaded files are not used unless the instructions name them.
- Do not set Deep Research as default or it will wander off the syllabus.
