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

POST_EXIT_REQUIRED = {
    "docs/README.md": (
        "**CKR state:** CKR-A–CKR-K COMPLETE / ACCEPTED — CKR EXIT ACCEPTED — IMPLEMENTATION 001-A NEXT / READY / NOT STARTED.",
        "Implementation 001-A is NEXT / READY / NOT STARTED",
    ),
    "docs/canonical/README.md": (
        "**Authority state:** CANONICALIZATION COMPLETE — CKR EXIT ACCEPTED",
    ),
    "docs/agentic_development_foundation/README.md": (
        "**Current handoff:** CKR COMPLETE / EXIT ACCEPTED — IMPLEMENTATION 001-A NEXT / READY / NOT STARTED.",
        "CKR has subsequently completed and exited successfully",
    ),
    "knowledge/index.md": (
        "CKR-A–K is complete/accepted",
        "Implementation 001-A is NEXT / READY / NOT STARTED",
    ),
    "knowledge/project/agentic-foundation.md": (
        "CKR is complete/accepted",
        "Implementation 001-A is NEXT / READY / NOT STARTED",
    ),
    "docs/phase_status.md": (
        "Phase 010 — Technical Architecture: COMPLETE",
    ),
}

POST_EXIT_FORBIDDEN = (
    "CKR MIGRATION IN PROGRESS",
    "CKR is the active pre-implementation documentation-authority retrofit",
    "Implementation 001-A is blocked until CKR-K",
    "Implementation 001-A remains blocked until CKR-K",
    "blocks product implementation until CKR-K",
    "All accepted semantic families are canonicalized through CKR-I.",
    "CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory is the current post-ADF work.",
    "reference.authority_vocabulary` and REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain with their inventory-selected legacy owners",
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
            text = path.read_text(encoding="utf-8")
            if mirror not in text:
                errors.append(f"{rel}: missing current CKR status mirror {mirror!r}")
            if len(complete) == len(LETTERS) and "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT" in text:
                errors.append(f"{rel}: stale CKR implementation-blocked marker remains after accepted exit")
        print(mirror)

    implementation_path = repo / "docs/implementation/README.md"
    implementation = implementation_path.read_text(encoding="utf-8") if implementation_path.is_file() else ""
    if len(complete) < len(LETTERS) and "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT" not in implementation:
        errors.append("implementation authority must block 001-A while CKR is incomplete")
    if len(complete) == len(LETTERS) and "Implementation 001-A — NEXT / READY / NOT STARTED" not in implementation:
        errors.append("accepted CKR exit requires Implementation 001-A NEXT / READY / NOT STARTED")

    if len(complete) == len(LETTERS):
        for rel, required_tokens in POST_EXIT_REQUIRED.items():
            path = repo / rel
            if not path.is_file():
                errors.append(f"missing post-CKR living orientation surface: {rel}")
                continue
            text = path.read_text(encoding="utf-8")
            for token in required_tokens:
                if token not in text:
                    errors.append(f"{rel}: missing accepted post-CKR orientation marker {token!r}")
            for token in POST_EXIT_FORBIDDEN:
                if token in text:
                    errors.append(f"{rel}: stale transitional CKR wording remains after accepted exit: {token!r}")

    for error in errors:
        print(f"ERROR {error}")
    print(f"CKR status drift validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
