# Eval — quality gate for Study OS output

If a reply does not pass this gate, it is broken. Throw away, new chat, paste prompt as message 1.

This mirrors `core/output-spec.md` and `examples/output-gallery.md`.

## What it checks

| Check | Source |
|---|---|
| COMMAND CENTER first | output-spec.md §1 |
| Has BANK, NEED, LOAD, WCOV, NEXT_PROBE | metrics.md |
| THIS WEEK'S 3 NON-NEGOTIABLES | output-spec.md broken list |
| DO NOT OPEN THIS WEEK | output-spec.md |
| TODAY has `- [ ]` checkboxes | output-spec.md §4 |
| Every learn/drill block has `__/n` | diagnostics.md |
| Has Study OS Card fenced block | RULEBOOK hard rule 7 |
| No hourly schedule past 7 days | RULEBOOK hard rule 4 |
| No pep opening | output-spec.md broken list |
| Topic table has RED/AMBER/GREEN and RED first | output-spec.md §2 |
| Weak board has Symptom + Drill + Next due | output-spec.md |

## Run

```bash
# check a file you saved from ChatGPT/Claude
python eval/eval.py examples/maya-26-days-out.md

# check your own output (paste into /tmp/out.md first)
python eval/eval.py /tmp/out.md

# check all examples
python eval/eval.py examples/maya-26-days-out.md examples/ahmed-fsc-18-days.md

# full suite: fixtures + examples. bad-* fixtures must fail, good must pass
python eval/eval.py --selftest eval/fixtures/*.md examples/*.md

# drift guard: agent-skill references/ must be exact copies of core/
python eval/check_copies.py

# strict mode — also fails on ASSUMED without label, fake 0s
python eval/eval.py --strict /tmp/out.md

# JSON for CI
python eval/eval.py --json examples/maya-26-days-out.md
```

Exit code 0 = PASS, 1 = FAIL.

## Fixtures

- `fixtures/good-minimal.md` — minimal passing SETUP (should PASS)
- `fixtures/bad-pep-calendar.md` — 30-day calendar + pep + no checkboxes (should FAIL)
- `fixtures/bad-no-metrics.md` — missing LOAD/WCOV (should FAIL)

```bash
python eval/eval.py --selftest eval/fixtures/*.md examples/*.md
```

A file can opt out of the gate with `eval-skip` in its first lines — used by `examples/output-gallery.md`, which deliberately contains broken output as a reference.

## Use in other Prompt-Lib use cases

Copy this folder, edit `CHECKS` in `eval.py`. Same pattern: command center + tick list + card = memory.

## CI idea

```yaml
# .github/workflows/study-os.yml
- run: python personalized-study-planner/eval/eval.py --selftest personalized-study-planner/eval/fixtures/*.md personalized-study-planner/examples/*.md
- run: python personalized-study-planner/eval/check_copies.py
```

## Use in other Prompt-Lib use cases

Copy this folder, edit `CHECKS` in `eval.py`. Same pattern: command center + tick list + card = memory.

## CI idea

```yaml
# .github/workflows/study-os.yml
- run: python personalized-study-planner/eval/eval.py personalized-study-planner/examples/*.md
```

If this fails, the prompt regressed.
