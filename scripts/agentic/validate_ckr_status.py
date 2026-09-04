#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

MIRRORS = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
)
STATE_RE = re.compile(r"^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$", re.M)
LETTERS = "ABCDEFGHIJK"


def complete_label(complete: list[str]) -> str:
    if not complete:
        return ""
    if len(complete) == 1:
        return f"CKR-{complete[0]}"
    return f"CKR-{complete[0]}–CKR-{complete[-1]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    authority = repo / "docs/canonical_knowledge_retrofit/README.md"
    errors: list[str] = []

    if not authority.is_file():
        print("ERROR missing CKR authority README")
        return 1

    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding="utf-8"))}
    if set(states) != set(LETTERS):
        errors.append(f"CKR authority must declare CKR-A..CKR-K exactly once; found {sorted(states)}")

    complete = [c for c in LETTERS if str(states.get(c, "")).startswith("COMPLETE / ACCEPTED")]
    nexts = [c for c in LETTERS if states.get(c) == "NEXT / READY"]
    in_progress = [c for c in LETTERS if states.get(c) == "IN EXECUTION"]

    if complete:
        expected = list(LETTERS[: len(complete)])
        if complete != expected:
            errors.append(f"CKR completed groups are not contiguous from A: {complete}")

    active = nexts + in_progress
    if len(complete) < len(LETTERS):
        expected_active = LETTERS[len(complete)]
        if len(active) != 1:
            errors.append(f"CKR must declare exactly one NEXT / READY or IN EXECUTION group; found next={nexts}, in_progress={in_progress}")
        elif active[0] != expected_active:
            errors.append(f"CKR active group {active[0]} does not follow completed groups {complete}")
    elif active:
        errors.append(f"all CKR groups are complete; no CKR group may remain active: {active}")

    if nexts and in_progress:
        errors.append("CKR cannot declare NEXT / READY and IN EXECUTION simultaneously")

    mirror: str | None = None
    if len(complete) == len(LETTERS):
        mirror = "CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT."
    elif in_progress:
        prefix = f"COMPLETE {complete_label(complete)}; " if complete else ""
        mirror = f"CKR status mirror: {prefix}IN EXECUTION CKR-{in_progress[0]}; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT."
    elif nexts:
        prefix = f"COMPLETE {complete_label(complete)}; " if complete else ""
        mirror = f"CKR status mirror: {prefix}NEXT CKR-{nexts[0]}; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT."

    if mirror:
        for rel in MIRRORS:
            path = repo / rel
            if not path.is_file():
                errors.append(f"missing live CKR status mirror surface: {rel}")
                continue
            if mirror not in path.read_text(encoding="utf-8"):
                errors.append(f"{rel}: missing current CKR status mirror {mirror!r}")
        print(mirror)

    implementation = (repo / "docs/implementation/README.md").read_text(encoding="utf-8") if (repo / "docs/implementation/README.md").is_file() else ""
    if len(complete) < len(LETTERS) and "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT" not in implementation:
        errors.append("implementation authority must block 001-A while CKR is incomplete")

    for error in errors:
        print(f"ERROR {error}")
    print(f"CKR status drift validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
