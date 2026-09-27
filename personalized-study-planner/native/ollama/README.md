# Ollama / local models

Local models have no GPT / Gem / Skill UI and no file uploads. The rulebook has to live in the **Modelfile `SYSTEM`** (or the equivalent system prompt in LM Studio, llama.cpp, Jan, Open WebUI).

## Create the model

From this folder:

```bash
ollama create study-os -f Modelfile
ollama run study-os
```

Then paste exam details. Say `TODAY` / `DONE` / `STUCK` as usual.

Change `FROM` in the Modelfile to whatever you have pulled (`llama3.1`, `qwen2.5`, `mistral`, `phi4`, …). Smaller models drift: if the card schema collapses, switch to a larger instruct model and keep `temperature 0.3`.

## LM Studio / Open WebUI / llama.cpp

Copy the `SYSTEM` string out of `Modelfile` into the system prompt box. Set temperature 0.3. Disable web tools.

## Honesty

A 7B model will not reliably keep the full topic table and the card in one reply. If output truncates, ask `CARD` as a second turn, or use [QUICK-PROMPT](../../QUICK-PROMPT.md) instead of this full system.
