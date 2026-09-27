# ChatGPT — Custom GPT and Projects

ChatGPT does not read `SKILL.md`. Teach it through the **Configure** tab (Custom GPT) or **Project instructions** (Projects). Put rules in Instructions. Put the rulebook, card schema, and worked example in Knowledge. Do not bury behaviour only in files — GPT knowledge retrieval is lossy.

## Custom GPT (best)

1. Go to [chatgpt.com/gpts](https://chatgpt.com/gpts) → Create → **Configure**.
2. Copy each field from [CONFIG.md](./CONFIG.md).
3. Paste [instructions.md](./instructions.md) into **Instructions**.
4. Upload these as **Knowledge** (markdown, not screenshots):
   - `../../core/RULEBOOK.md`
   - `../../core/output-spec.md`
   - `../../core/card-schema.md`
   - `../../core/priority-and-time.md`
   - `../../examples/maya-26-days-out.md`
5. Capabilities: see CONFIG.md. Image generation **off**.
6. Preview with: *“Exam 23 Oct, I have 75 min/day, I’ll paste topics next.”* It should ask for the rest in **one** batch, not start a fake syllabus.
7. Create. Share the GPT link if you want other students on it.

Each new chat with the GPT starts empty. Students paste the Study OS Card every time. That is by design.

## ChatGPT Project

Use a Project if you don’t want a GPT in the store.

1. New Project → name it `Study OS`.
2. Project instructions: paste [instructions.md](./instructions.md). Skip the “You are a Custom GPT named…” line if you want; the rest stays.
3. Add the same four knowledge files as above.
4. Keep **one** Project chat per exam (or per student). Projects hold files; they still need the card for progress.

## Not this

Do not put Study OS in **global** Custom Instructions. That would infect every unrelated chat.
