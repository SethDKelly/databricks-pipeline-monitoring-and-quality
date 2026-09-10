#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

LIVE_SURFACES = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
)
STATE_RE = re.compile(r"^- \*\*ADF-([A-H]) — .*?: (.+?)\.\*\*$", re.M)
EXIT_ACCEPTED = "**Status:** ACCEPTED — AGENTIC DEVELOPMENT FOUNDATION EXECUTION EXIT COMPLETE"
CURRENT_HANDOFF = "Implementation 001-A — NEXT / READY / NOT STARTED"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    repo = Path(ap.parse_args().repo).resolve()
    errors: list[str] = []

    authority = repo / "docs/agentic_development_foundation/README.md"
    if not authority.is_file():
        print("ERROR missing ADF authority README")
        return 1

    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding="utf-8"))}
    expected_letters = set("ABCDEFGH")
    if set(states) != expected_letters:
        errors.append(f"ADF authority must retain ADF-A..ADF-H exit states; found {sorted(states)}")

    incomplete = [letter for letter in "ABCDEFGH" if not str(states.get(letter, "")).startswith("COMPLETE / ACCEPTED")]
    if incomplete:
        errors.append(f"ADF exit regression: groups no longer complete/accepted: {incomplete}")

    deferred = [letter for letter in "ABCDEFGH" if "DEFERRED VERIFICATION" in str(states.get(letter, ""))]
    if deferred != ["G"]:
        errors.append(f"only the bounded ADF-G runtime verification exception may remain deferred; found {deferred}")

    candidates = (
        repo / "docs/agentic_development_foundation/execution_exit_review.md",
        repo / "docs/history/foundations/adf/execution_exit_review.md",
    )
    exit_review = next((p for p in candidates if p.is_file()), None)
    if not exit_review or EXIT_ACCEPTED not in exit_review.read_text(encoding="utf-8"):
        errors.append("ADF execution-exit evidence is missing or no longer accepted")

    for rel in LIVE_SURFACES:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing current implementation/agent surface: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "ADF status mirror:" in text:
            errors.append(f"{rel}: completed ADF phase mirror should not be duplicated in current implementation guidance")
        if "NEXT ADF-" in text or "IN EXECUTION ADF-" in text:
            errors.append(f"{rel}: stale active-ADF progression wording remains")

    implementation = repo / "docs/implementation/README.md"
    if not implementation.is_file() or CURRENT_HANDOFF not in implementation.read_text(encoding="utf-8"):
        errors.append("current implementation handoff must remain Implementation 001-A — NEXT / READY / NOT STARTED")

    for error in errors:
        print("ERROR", error)
    print(f"ADF exit/status validation: {len(errors)} error(s); ADF exit accepted, ADF-EX-17 deferred")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
