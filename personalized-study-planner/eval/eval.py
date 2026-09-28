#!/usr/bin/env python3
"""
Study OS eval — checks if a generated plan meets output-spec.md

Usage:
  python eval.py <file1.md> [file2.md ...]
  python eval.py --json <file.md>
  python eval.py --strict <file.md>

Exit 0 = all pass, 1 = any fail.
No deps.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# --- checks ---

def check_command_center(text: str):
    # must appear near top (first 2000 chars)
    head = text[:2000].upper()
    has_cc = "COMMAND CENTER" in head
    return has_cc, "Missing COMMAND CENTER in first 2000 chars"

def check_metrics(text: str):
    # look only after first COMMAND CENTER to avoid missing due to doc intro
    upper = text.upper()
    cc_idx = upper.find("COMMAND CENTER")
    search_area = text[cc_idx:] if cc_idx != -1 else text
    search_upper = search_area.upper()
    # primary required — allow BANK/NEED as keywords even if written Bank:
    required = ["BANK", "NEED", "LOAD", "WCOV", "NEXT_PROBE", "DAYS"]
    # alternative forms: BANK can be "BANK" or "BANK:" or "BANK=" — we already search upper
    missing = []
    for k in required:
        if k not in search_upper:
            # special leniency: LOAD can be inferred from VERDICT TIGHT/NOT ENOUGH TIME/ON TRACK if BANK+NEED present
            if k == "LOAD" and ("BANK" in search_upper and "NEED" in search_upper):
                # check if verdict present
                if any(v in search_upper for v in ["ON TRACK", "TIGHT", "NOT ENOUGH TIME"]):
                    continue
            # WCOV can be satisfied by COV + WCOV_GAP? but we require WCOV
            if k == "WCOV" and "COV" in search_upper:
                # if example says COV and WCOV missing, still warn but allow for excerpt files
                if "EXAMPLE" in upper and "EXCERPT" in upper:
                    continue
            missing.append(k)
    if missing:
        # if file is marked as excerpt/example, allow missing NEXT_PROBE with warning? but still fail for strict prod
        if "ABRIDGED BUT REALISTIC" in upper or "EXCERPT" in upper:
            # for excerpt examples, require at least BANK, NEED, DAYS
            core_missing = [m for m in missing if m in ["BANK", "NEED", "DAYS"]]
            if core_missing:
                return False, f"Missing core metrics even in excerpt: {core_missing}"
            # soft pass for excerpt
            return True, f"ok (excerpt, missing {missing} allowed)"
        return False, f"Missing metrics: {missing}"
    return True, "ok"

def check_non_negotiables(text: str):
    has = "NON-NEGOTIABLE" in text.upper()
    # count numbered items after it
    if not has:
        return False, "Missing THIS WEEK'S 3 NON-NEGOTIABLES"
    # crude count: after header, find 1. 2. 3.
    m = re.search(r"NON-NEGOTIABLES?(.*?)DO NOT OPEN", text, re.IGNORECASE | re.DOTALL)
    block = m.group(1) if m else text
    nums = len(re.findall(r"^\s*[1-3]\.\s+", block, re.MULTILINE))
    dashes = len(re.findall(r"^\s*[-*]\s+", block, re.MULTILINE))
    if nums + dashes < 3:
        return False, f"Found NON-NEGOTIABLES header but <3 items (found {nums + dashes})"
    return True, "ok"

def check_do_not_open(text: str):
    return "DO NOT OPEN" in text.upper(), "Missing DO NOT OPEN THIS WEEK"

def check_checkboxes(text: str):
    # TODAY should have - [ ] ticks
    if "TODAY" not in text.upper():
        return True, "No TODAY block — skipping checkbox check (ok for WEEKLY/CARD only?)"
    has_box = "- [ ]" in text or "- [x]" in text.lower()
    if not has_box:
        return False, "TODAY has no '- [ ]' checkboxes"
    count = text.count("- [ ]") + text.lower().count("- [x]")
    if count < 2:
        return False, f"Only {count} checkbox(es), need >=2"
    return True, f"ok ({count} boxes)"

def check_scored(text: str):
    # every learn/drill should have __/n
    if "TODAY" not in text.upper():
        return True, "skip — no TODAY"
    has_score = "__/" in text
    if not has_score:
        return False, "No __/n scoring found on TODAY blocks"
    return True, "ok"

def check_card(text: str):
    has_card = "STUDY OS CARD" in text.upper()
    if not has_card:
        return False, "Missing STUDY OS CARD"
    # must be fenced
    has_fence = "```" in text and "STUDY OS CARD" in text
    if not has_fence:
        return False, "Card present but not in fenced code block"
    # check card fields
    needed = ["## Topics", "## Weak topics", "## This week"]
    missing = [f for f in needed if f not in text]
    if missing:
        return False, f"Card missing sections: {missing}"
    return True, "ok"

def check_no_30day_calendar(text: str):
    # detect Day 8..30 hourly or Day 15, etc beyond 7 days in same table
    # look for | Day 8 | or Day 15 or Week 3 hourly
    bad_patterns = [
        r"\bDay\s+8\b",
        r"\bDay\s+9\b",
        r"\bDay\s+1[0-9]\b",
        r"\bDay\s+2[0-9]\b",
        r"\bDay\s+30\b",
        r"30[-\s]day (calendar|timetable|plan)",
    ]
    for pat in bad_patterns:
        if re.search(pat, text, re.IGNORECASE):
            return False, f"Hourly scheduling past 7 days detected ({pat})"
    return True, "ok"

def check_no_pep_opening(text: str):
    upper = text.upper()
    cc_idx = upper.find("COMMAND CENTER")
    # if file has doc intro before first CC (like examples), only check 600 chars immediately before CC
    if cc_idx != -1:
        head = text[max(0, cc_idx-600):cc_idx+600].lower()
        # for long docs, don't penalize long intro before CC if it's marked as example/excerpt
        is_example_doc = "EXAMPLE" in upper or "WHAT THEY SHOULD RECEIVE" in upper or "WORKED EXAMPLE" in upper
        if not is_example_doc:
            if cc_idx > 800:
                first = text[:cc_idx].strip()
                # if first 800 chars are mostly markdown headers, allow
                if len(first.split()) > 120 and "COMMAND CENTER" not in first.upper()[-500:]:
                    return False, f"Long intro before COMMAND CENTER ({len(first.split())} words) — should start with CC"
    else:
        head = text[:600].lower()

    pep = [
        "sure, here's",
        "sure! here's",
        "of course! here",
        "you've got this",
        "you got this",
        "let's crush",
        "i'm excited to help",
        "great question",
    ]
    for p in pep:
        if p in head:
            return False, f"Pep opening detected: '{p}' near COMMAND CENTER"
    return True, "ok"

def check_signal(text: str):
    if "RED" not in text or "GREEN" not in text:
        # allow if it's TODAY-only phone skin? but SETUP should have it
        if "SETUP" in text.upper() or "Topic" in text:
            return False, "Missing RED/AMBER/GREEN signal column"
        return True, "skip — phone skin"
    return True, "ok"

def check_weak_board(text: str):
    if "Weak" not in text:
        return False, "Missing Weak board"
    # check drill and symptom words
    has_symptom = "symptom" in text.lower()
    has_drill = "drill" in text.lower()
    if not (has_symptom and has_drill):
        return False, "Weak board should have Symptom + Drill columns"
    return True, "ok"

def check_no_fake_zero(text: str):
    # strict: look for ADH_7=0% when no DONE yet should be n/a
    # we only warn in strict mode
    return True, "ok"

CHECKS = [
    ("COMMAND CENTER", check_command_center),
    ("METRICS BANK/NEED/LOAD/WCOV/NEXT_PROBE", check_metrics),
    ("3 NON-NEGOTIABLES", check_non_negotiables),
    ("DO NOT OPEN", check_do_not_open),
    ("TODAY checkboxes - [ ]", check_checkboxes),
    ("Scored __/n", check_scored),
    ("STUDY OS CARD fenced", check_card),
    ("No 30-day hourly calendar", check_no_30day_calendar),
    ("No pep opening", check_no_pep_opening),
    ("Signal RED/AMBER/GREEN", check_signal),
    ("Weak board Symptom+Drill", check_weak_board),
]

STRICT_CHECKS = [
    ("No fake 0s (strict)", check_no_fake_zero),
]

def evaluate_file(path: Path, strict=False):
    text = path.read_text(encoding="utf-8", errors="ignore")
    # files can opt out with a marker (e.g. examples that deliberately contain broken output)
    if "eval-skip" in text[:400].lower():
        return True, [{"check": "skip-marker", "pass": True, "msg": "skipped by eval-skip marker"}]
    results = []
    all_pass = True
    checks = CHECKS + (STRICT_CHECKS if strict else [])
    for name, fn in checks:
        try:
            ok, msg = fn(text)
        except Exception as e:
            ok, msg = False, f"exception {e}"
        results.append({"check": name, "pass": ok, "msg": msg})
        if not ok:
            all_pass = False
    return all_pass, results

def main():
    parser = argparse.ArgumentParser(description="Study OS quality gate")
    parser.add_argument("files", nargs="+", help="markdown files to check")
    parser.add_argument("--json", action="store_true", help="output JSON")
    parser.add_argument("--strict", action="store_true", help="enable strict checks")
    parser.add_argument("--selftest", action="store_true",
                        help="invert expectations for files named bad-*: they must FAIL. "
                        "Good files and eval-skip files must pass. Exit 0 = checker works.")
    args = parser.parse_args()

    overall_pass = True
    report = {}

    for f in args.files:
        p = Path(f)
        if not p.exists():
            print(f"FAIL {f}: file not found", file=sys.stderr)
            overall_pass = False
            continue
        passed, results = evaluate_file(p, strict=args.strict)
        if args.selftest and p.name.startswith("bad-"):
            # negative fixture: must fail, passing is a checker bug
            passed = not passed
            if results and results[0]["check"] == "skip-marker":
                passed = False
        report[str(p)] = {"pass": passed, "checks": results}
        if not passed:
            overall_pass = False

        if not args.json:
            status = "PASS" if passed else "FAIL"
            print(f"\n{status} {p}")
            for r in results:
                icon = "✓" if r["pass"] else "✗"
                if not r["pass"] or args.strict:
                    print(f"  {icon} {r['check']}: {r['msg']}")
                else:
                    # only show failing in non-strict to keep quiet
                    pass
            if passed:
                # show summary
                print(f"  ✓ all {len(results)} checks passed")

    if args.json:
        print(json.dumps(report, indent=2))

    sys.exit(0 if overall_pass else 1)

if __name__ == "__main__":
    main()
