# Start here

You were given a study coach. Not another “30-day timetable” prompt. Two minutes.

## What you will actually get

Not a speech. A screen you can screenshot:

```text
COMMAND CENTER
Exam: Chemistry + Bio  |  23 Oct  |  26 days left
Clock: 75 min weeknights  /  Sat 3h
Bank: 24h available  ·  32h to cover well  ·  TIGHT
THIS WEEK'S 3 NON-NEGOTIABLES
1. 8-reaction organic map from memory, 6/8
2. Nephron labelled without notes
3. Hormones 12-row table closed-book
DO NOT OPEN THIS WEEK
- Ecology notes
- Rewriting bonding
```

Then a **tick list for today** with a score on every block (`__/8`), a fallback if the evening dies, and a **Study OS Card** you paste back tomorrow. Weak topics stay on a drill list until you can actually do them.

If your assistant returns “Day 1–30: revise all chapters”, it ignored the coach. New chat, paste the prompt again.

## Do this now

**60 seconds, no questions (phone):**

1. Open any chat.
2. Copy everything in [`60-SECOND.md`](./60-SECOND.md) (4-line intake only).
3. Paste, fill 4 lines, send. You get a screenshot-able plan + TODAY ticks + card. Save card. Done.

**2 minutes, better plan (any app):**

1. Open ChatGPT, Claude, Gemini, or whatever you already use.
2. Copy everything between `START PROMPT` and `END PROMPT` in [`STUDY-OS.md`](./STUDY-OS.md) — or the short version in [`QUICK-PROMPT.md`](./QUICK-PROMPT.md).
3. Under it, paste:

```text
Exam:
Date:
Weekdays: ___ min    Weekends: ___
Topics / syllabus:
Done so far:
Weak topics (and what goes wrong):
Hardest part of studying + what I do when it actually works:
Timed papers: freeze / rush / fine
Block I can finish: 15 / 25 / 40 / 60
State today: low / ok / wired / fried / anxious
Today I can study: ___ minutes from ___
```

4. If it sends a numbered question batch, answer it. That is interrogation — it is how the metrics (LOAD, WCOV, next probe) get real. Two rounds max.
5. Save the **Study OS Card** it prints. That is your save file. Notes app is fine.

**If you will use this until the exam** (better): open [`native/README.md`](./native/README.md) and install the pack for *your* app so you stop re-pasting the rulebook.

| App | Open |
|---|---|
| ChatGPT | [`native/chatgpt`](./native/chatgpt) |
| Claude | [`native/agent-skill`](./native/agent-skill) or [`native/claude-project`](./native/claude-project) |
| Gemini | [`native/gemini-gem`](./native/gemini-gem) |
| Anything else | [`native/README.md`](./native/README.md) |

## Every study day after that

Paste the card, then one line:

```text
TODAY — I have ___ minutes from ___
```

When you stop:

```text
DONE — minutes:    scores:    shaky:
```

If it prints `PROBE`, close the notes, answer, then:

```text
PROBE RESULT · topic · __/5 · minutes · which were wrong
```

Once a week: `WEEKLY`. Ten days out: it should switch to papers by itself. Fell off: `STUCK`. Type `METRICS` if you only want the numbers.

## What “good” looks like

[`examples/output-gallery.md`](./examples/output-gallery.md) — garbage plan vs this.  
[`examples/maya-26-days-out.md`](./examples/maya-26-days-out.md) — a full first reply.

## Sending this to someone else

Use [`SHARE.md`](./SHARE.md). Don’t dump the whole git tree in their DMs — send START-HERE + the prompt.
