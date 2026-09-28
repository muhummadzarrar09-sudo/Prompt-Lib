#!/usr/bin/env python3
"""
Copy-sync check — native/agent-skill/references/*.md must be exact copies of core/*.md.

core/ is the source of truth. These files exist only because the Claude Skill
format wants flat reference files; hand-editing a copy is how drift happens.
If this fails: copy core/<name>.md over the references copy. Never edit both.

Usage: python check_copies.py   (exit 0 = in sync, 1 = drift)
No deps.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPIES = [
    "card-schema.md",
    "diagnostics.md",
    "metrics.md",
    "output-spec.md",
    "priority-and-time.md",
    "profile.md",
]

def main():
    drifted = []
    for name in COPIES:
        src = ROOT / "core" / name
        dst = ROOT / "native" / "agent-skill" / "references" / name
        if not src.exists():
            drifted.append(f"{name}: core source missing")
            continue
        if not dst.exists():
            drifted.append(f"{name}: references copy missing")
            continue
        if src.read_bytes() != dst.read_bytes():
            drifted.append(f"{name}: references copy differs from core — copy core/{name} over it")
    if drifted:
        print("DRIFT DETECTED — core/ is source of truth:")
        for d in drifted:
            print(f"  ✗ {d}")
        sys.exit(1)
    print(f"✓ all {len(COPIES)} reference copies match core/")

if __name__ == "__main__":
    main()
