# Custom GPT — Configure tab

Paste these into the matching fields. Instructions live in [instructions.md](./instructions.md).

## Name

```
Study OS
```

## Description

```
Personalized exam study plans from your syllabus, exam date, daily time, and progress. Tracks weak topics. Paste your card back each session.
```

## Conversation starters

```
Build my study plan — I’ll paste syllabus, exam date, and daily time
TODAY — I have minutes. Here’s my Study OS Card
DONE — here’s what I finished and what felt shaky
I fell behind, or my exam is in 10 days or less
I’m fried / I freeze on timed papers / I can’t start — build around that
```

## Knowledge (upload, in this order)

1. `core/RULEBOOK.md`
2. `core/metrics.md`
3. `core/interrogation.md`
4. `core/diagnostics.md`
5. `core/profile.md`
6. `core/output-spec.md`
7. `core/card-schema.md`
8. `core/priority-and-time.md`
9. `examples/maya-26-days-out.md`

In Instructions they are referred to by filename. Keep the names if you rename on upload, or edit Instructions to match.

## Capabilities

| Capability | Setting | Why |
|---|---|---|
| Web search | On | Only for an official syllabus URL / exam-board spec the user gives you |
| Code interpreter / data analysis | On | Optional time-budget arithmetic |
| Canvas | Off | Tables in markdown are enough; canvas splits the card |
| Image generation | Off | Not a study-plan job |
| Memory | N/A for GPTs | GPTs do not use ChatGPT memory. The card is memory. |

## Recommended model

Whatever the workspace default is. Prefer a reasoning-capable model if the picker has one.
