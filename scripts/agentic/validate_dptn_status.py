#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

LETTERS = "ABCDEFG"
MIRRORS = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
)
ORIENTATION = (
    "docs/README.md",
    "docs/agentic_development_foundation/README.md",
    "docs/canonical_knowledge_retrofit/README.md",
    "knowledge/index.md",
    "knowledge/project/agentic-foundation.md",
)
STATE_RE = re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$", re.M)


def label(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return f"DPTN-{items[0]}"
    return f"DPTN-{items[0]}–DPTN-{items[-1]}"


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=".")
    repo = Path(ap.parse_args().repo).resolve(); errors: list[str] = []
    authority = repo / "docs/documentation_topology_normalization/README.md"
    if not authority.is_file():
        print("ERROR missing DPTN authority README")
        return 1

    text = authority.read_text(encoding="utf-8")
    states = {k: v for k, v in STATE_RE.findall(text)}
    if set(states) != set(LETTERS):
        errors.append(f"DPTN authority must declare DPTN-A..DPTN-G exactly once; found {sorted(states)}")

    complete = [c for c in LETTERS if states.get(c) == "COMPLETE / ACCEPTED"]
    in_progress = [c for c in LETTERS if states.get(c) == "IN EXECUTION"]
    nexts = [c for c in LETTERS if states.get(c) == "NEXT / READY"]
    planned = [c for c in LETTERS if states.get(c) == "PLANNED"]

    if complete != list(LETTERS[:len(complete)]):
        errors.append(f"DPTN completed groups must be contiguous from A: {complete}")

    if len(complete) < len(LETTERS):
        expected = LETTERS[len(complete)]
        active = in_progress + nexts
        if len(active) != 1 or active[0] != expected:
            errors.append(f"DPTN must have exactly one active group {expected}; in_progress={in_progress}, next={nexts}")
        expected_planned = list(LETTERS[len(complete)+1:])
        if planned != expected_planned:
            errors.append(f"remaining DPTN groups must be PLANNED in order {expected_planned}; found {planned}")
    elif in_progress or nexts or planned:
        errors.append("all DPTN groups complete; no active/planned group may remain")

    if in_progress:
        prefix = f"COMPLETE {label(complete)}; " if complete else ""
        mirror = f"DPTN status mirror: {prefix}IN EXECUTION DPTN-{in_progress[0]}; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT."
    elif nexts:
        prefix = f"COMPLETE {label(complete)}; " if complete else ""
        mirror = f"DPTN status mirror: {prefix}NEXT DPTN-{nexts[0]}; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT."
    else:
        mirror = "DPTN status mirror: COMPLETE DPTN-A–DPTN-G; DPTN EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT."

    for rel in MIRRORS:
        p = repo / rel
        if not p.is_file():
            errors.append(f"missing DPTN mirror surface: {rel}")
            continue
        body = p.read_text(encoding="utf-8")
        if mirror not in body:
            errors.append(f"{rel}: missing current DPTN mirror {mirror!r}")

    impl = (repo / "docs/implementation/README.md").read_text(encoding="utf-8")
    if len(complete) < len(LETTERS):
        if "Implementation 001-A — BLOCKED / NOT STARTED" not in impl:
            errors.append("implementation authority must block 001-A while DPTN is incomplete")
        if "**CKR exit baseline:**" not in impl or "Implementation 001-A — NEXT / READY / NOT STARTED" not in impl:
            errors.append("implementation authority must preserve the historical CKR release baseline while DPTN owns current blocking")
    else:
        if "Implementation 001-A — NEXT / READY / NOT STARTED" not in impl:
            errors.append("accepted DPTN exit must restore Implementation 001-A NEXT / READY / NOT STARTED")

    if len(complete) < len(LETTERS):
        required = ("DPTN", "Implementation 001-A")
        for rel in ORIENTATION:
            p = repo / rel
            if not p.is_file():
                errors.append(f"missing DPTN orientation surface: {rel}")
                continue
            body = p.read_text(encoding="utf-8")
            for token in required:
                if token not in body:
                    errors.append(f"{rel}: missing active DPTN orientation token {token!r}")

    print(mirror)
    for e in errors: print("ERROR", e)
    print(f"DPTN status drift validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
