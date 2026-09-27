# Poe bot

Poe bots are a prompt + greeting + optional knowledge. They are not Skills. Create a bot with [prompt.md](./prompt.md) as the Prompt, [greeting.md](./greeting.md) as the Greeting.

## Setup

1. Poe → Create bot.
2. Name: `Study OS`
3. Prompt: paste [prompt.md](./prompt.md)
4. Greeting: paste [greeting.md](./greeting.md)
5. Knowledge (if your Poe plan allows): upload `core/RULEBOOK.md`, `core/card-schema.md`, `examples/maya-26-days-out.md`
6. Temperature: low (~0.3) if the bot has a slider
7. Suggest replies / follow-ups: off if they add fluff

Poe often switches underlying models. The prompt is written so a cheaper model still emits the card and the 7-day cap.
