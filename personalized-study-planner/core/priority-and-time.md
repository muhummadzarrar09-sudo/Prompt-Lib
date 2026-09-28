# Priority scoring and time budget

Load this when you are ranking topics, writing a time budget, or deciding ON TRACK / TIGHT / NOT ENOUGH TIME.

## Priority (use silently unless asked)

For each topic:

- **Weight** 1–5 from exam importance. Default 3 if unknown. Use official weighting when given.
- **Gap** = 6 − confidence
- **Confidence is evidence-capped first** (RULEBOOK 19): a ≤50% graded score on the topic means Gap is computed from confidence 2, whatever they claimed; ≥80% floors at 3
- **Freshness** = 1 if practiced in last 7 days, 2 if 8–21 days, 3 if never practiced or > 21 days
- **Weak multiplier** = 1.5 if on the weak list, else 1.0

`Priority = Weight × Gap × Freshness × Weak multiplier`

Work order = highest priority first. Constraint: do not put three heavy new topics on the same weekday. Mix learn / drill / paper.

## Time budget

Remaining calendar days = exam date − today.  
Subtract 1 lighter day per week.  
If ≥ 21 days left, also subtract 2 buffer days.

`Usable hours = remaining study days × real daily average × 0.85 − ASGN` (slippage, minus assignments / labs due inside the window — `metrics.md`).

Hours needed (adjust if they are clearly faster/slower):

| Kind of topic | Hours to exam-ready |
|---|---|
| New, never studied | 1.5–3 |
| Seen in class, not revised | 1–1.5 |
| Revised, needs exam practice | 0.75–1 |
| Weak / repeatedly failed | ×1.4 on top of the row above |
| Full past-paper block | 1–1.5 |

Verdict:

- **ON TRACK** — usable ≥ needed
- **TIGHT** — usable is within ~25% below needed; triage low-weight topics
- **NOT ENOUGH TIME** — say so in one sentence, then name full coverage / skim / drop

## Phases

- **> 21 days:** 50% close remaining gaps, 30% weak + questions, 20% recap
- **10–21 days:** 25% remaining gaps, 50% questions + weaks, 25% mixed papers
- **≤ 10 days:** 10% patch holes, 70% papers / mixed questions, 20% weak lightning drills. Auto COUNTDOWN.
- **≤ 3 days:** papers, mark schemes, weak flash drills, sleep. No new topics.
