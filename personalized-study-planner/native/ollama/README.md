# Ollama / local models

Local models have no GPT / Gem / Skill UI and no file uploads. The rulebook has to live in the **Modelfile `SYSTEM`** (or the equivalent system prompt in LM Studio, llama.cpp, Jan, Open WebUI).

## Quick start

From this folder:

```bash
ollama create study-os -f Modelfile
ollama run study-os
```

Then paste exam details. Say `TODAY` / `DONE` / `STUCK` as usual.

## Which base model? VRAM vs quant table

| VRAM | Recommended base | GGUF quant | Expected quality |
|---|---|---|---|
| 24GB+ | `llama3.1:70b-instruct` or `qwen2.5:32b-instruct` | Q4_K_M or Q5_K_M | Best — full card + metrics stable |
| 16GB | `llama3.1:8b-instruct`, `qwen2.5:14b-instruct`, `phi4:14b`, `mistral-nemo:12b` | Q5_K_M / Q6_K | Great — use main `Modelfile` |
| 8GB | `llama3.1:8b-instruct-Q4_K_M`, `qwen2.5:7b-instruct-Q5_K_M`, `gemma2:9b-Q4_K_M` | Q4_K_M | Good — use `Modelfile` with `num_ctx 8192` |
| 4-6GB | `qwen2.5:3b`, `phi3.5:3.8b`, `llama3.2:3b` | Q4_K_M / Q5 | Lite — use `Modelfile.7b` variant, ask `CARD` second turn if truncated |
| CPU only | `qwen2.5:7b-instruct-Q4_0` via llama.cpp | Q4_0 | Lite only, temp 0.2 |

**Change `FROM` in the Modelfile to whatever you have pulled.** Example:

```bash
ollama pull qwen2.5:14b-instruct
# edit Modelfile FROM line
ollama create study-os -f Modelfile
```

**Quant guide (llama.cpp / LM Studio):**

- `Q4_K_M` — default, good balance, ~4.5GB for 8B
- `Q5_K_M` — better reasoning, ~5.5GB for 8B, recommended for Study OS metrics
- `Q6_K` — near fp16, ~6.5GB for 8B, best for card schema
- `Q8_0` — almost no loss, needs 8GB+
- Avoid `Q2`, `Q3` — they break the card table and forget LOAD/WCOV

If the card collapses or LOAD disappears, go up one quant or switch to 14B.

## Two Modelfiles

- `Modelfile` — full Study OS, 8B+ tuned, `temperature 0.3`, `num_ctx 8192`, repeat penalty 1.1. Use for daily driver.
- `Modelfile.7b` — lite, 3-7B, `temperature 0.2`, `num_ctx 4096`, shorter output. It prints minimal SETUP + TODAY + card. If it truncates, type `CARD` and it will print only the card.

```bash
ollama create study-os-lite -f Modelfile.7b
ollama run study-os-lite
```

## LM Studio / Open WebUI / Jan / llama.cpp

1. Copy the `SYSTEM` string out of `Modelfile` (or `Modelfile.7b`) into the system prompt box.
2. Set temperature 0.3 (0.2 for 7b), top_p 0.9, repeat_penalty 1.1
3. Context length 8192 (4096 for lite)
4. Disable web tools / browsing
5. Save preset as "Study OS"

## Troubleshooting

| Problem | Fix |
|---|---|
| Card truncated after Topics | Type `CARD` — second turn prints only card. Or switch to `Modelfile.7b` |
| LOAD/WCOV missing | Model too small / quant too low. Use Q5_K_M or 14B |
| 30-day calendar appears | New chat, paste system again, keep temp 0.3. Check you didn't use a creative preset |
| No checkboxes | Same — temp too high or instruction-following weak. Use qwen2.5:14b or llama3.1:8b |
| Too slow on CPU | Use `Modelfile.7b` + Q4_K_M, or `phi3.5:3.8b` |

## Eval

Test your local model output:

```bash
ollama run study-os "Exam: FSc Physics Date: 15 Oct ... Today 60 min" > /tmp/out.md
python ../../eval/eval.py /tmp/out.md
```

If eval fails, try larger model or higher quant.

## Honesty

A 7B Q4 model will not reliably keep the full topic table + weak board + week strip + TODAY + card in one reply. That's why `Modelfile.7b` exists — it deliberately prints a shorter SETUP and relies on `CARD` second turn. If you need full output in one shot, use 14B+ Q5_K_M.
