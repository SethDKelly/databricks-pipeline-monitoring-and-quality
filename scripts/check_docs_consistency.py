#!/usr/bin/env python3
"""Check and optionally render canonical documentation phase status.

`docs/README.md` remains the living authority for the completed design-phase
progression rendered into `docs/phase_status.md`. Current repository entry points
and implementation guidance should reference authoritative documentation rather
than independently re-declaring a current design phase.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "docs" / "README.md"
RENDERED = ROOT / "docs" / "phase_status.md"

BEGIN = "<!-- PHASE_STATUS:BEGIN -->"
END = "<!-- PHASE_STATUS:END -->"

LIVING_DOCS = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "IMPLEMENTATION.md",
    ROOT / "docs" / "index.md",
    ROOT / "docs" / "concepts" / "README.md",
    ROOT / "docs" / "implementation" / "README.md",
    ROOT / "docs" / "implementation" / "AGENTS.md",
)

# Current entry points should route to the appropriate authority rather than
# independently maintaining a design-phase status. Historical documents are
# intentionally outside LIVING_DOCS and may retain status-at-the-time wording.
FORBIDDEN_CURRENT_STATUS = (
    re.compile(r"repository is currently in \*\*Phase \d{3}", re.IGNORECASE),
    re.compile(r"Phase \d{3}[^\n]*\bis next and has not started\b", re.IGNORECASE),
    re.compile(r"Phase \d{3}[^\n]*\bNEXT\s+—\s+not started\b", re.IGNORECASE),
)


def canonical_phase_lines(text: str) -> list[str]:
    match = re.search(r"^## Current state\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.MULTILINE)
    if not match:
        raise ValueError("docs/README.md has no '## Current state' section")
    lines = [line.rstrip() for line in match.group(1).splitlines() if line.startswith("- **Phase ")]
    if not lines:
        raise ValueError("docs/README.md current-state section has no phase declarations")
    return lines


def render_text(lines: list[str]) -> str:
    return (
        "# Documentation Phase Status\n\n"
        "This file is generated from the canonical `## Current state` section in `docs/README.md` "
        "by `scripts/check_docs_consistency.py --render`.\n\n"
        "Do not edit the phase lines below directly.\n\n"
        f"{BEGIN}\n"
        + "\n".join(lines)
        + f"\n{END}\n"
    )


def check() -> list[str]:
    errors: list[str] = []
    canonical = CANONICAL.read_text(encoding="utf-8")
    try:
        phase_lines = canonical_phase_lines(canonical)
    except ValueError as exc:
        return [str(exc)]

    expected = render_text(phase_lines)
    if not RENDERED.exists():
        errors.append("docs/phase_status.md is missing; run with --render")
    elif RENDERED.read_text(encoding="utf-8") != expected:
        errors.append("docs/phase_status.md is out of sync with docs/README.md; run with --render")

    for path in LIVING_DOCS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_CURRENT_STATUS:
            match = pattern.search(text)
            if match:
                rel = path.relative_to(ROOT)
                errors.append(
                    f"{rel}: independently maintained current-phase wording: {match.group(0)!r}; "
                    "route through docs/index.md/docs/README.md instead"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--render",
        action="store_true",
        help="regenerate docs/phase_status.md from docs/README.md before checking",
    )
    args = parser.parse_args()

    canonical = CANONICAL.read_text(encoding="utf-8")
    try:
        phase_lines = canonical_phase_lines(canonical)
    except ValueError as exc:
        print(f"documentation consistency error: {exc}", file=sys.stderr)
        return 1

    if args.render:
        RENDERED.write_text(render_text(phase_lines), encoding="utf-8")

    errors = check()
    if errors:
        print("Documentation consistency check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Documentation phase status is consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
