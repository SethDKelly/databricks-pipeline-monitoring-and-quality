#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LIVE_SURFACES = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
    "docs/index.md",
)
STATE_RE = re.compile(r"^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$", re.M)
CURRENT_HANDOFF = "Implementation 001-A — NEXT / READY / NOT STARTED"
FORBIDDEN = (
    "CKR MIGRATION IN PROGRESS",
    "CKR is the active pre-implementation documentation-authority retrofit",
    "Implementation 001-A is blocked until CKR-K",
    "Implementation 001-A remains blocked until CKR-K",
    "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT",
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    repo = Path(ap.parse_args().repo).resolve()
    errors: list[str] = []

    authority = repo / "docs/canonical_knowledge_retrofit/README.md"
    if not authority.is_file():
        print("ERROR missing CKR authority README")
        return 1

    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding="utf-8"))}
    expected_letters = set("ABCDEFGHIJK")
    if set(states) != expected_letters:
        errors.append(f"CKR authority must retain CKR-A..CKR-K exit states; found {sorted(states)}")

    incomplete = [letter for letter in "ABCDEFGHIJK" if not str(states.get(letter, "")).startswith("COMPLETE / ACCEPTED")]
    if incomplete:
        errors.append(f"CKR exit regression: groups no longer complete/accepted: {incomplete}")

    inventory_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    if not inventory_path.is_file():
        errors.append("missing CKR ownership inventory")
    else:
        try:
            inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
            if inventory.get("status") != "ckr_complete":
                errors.append(f"CKR ownership inventory status drifted: {inventory.get('status')!r}")
            if inventory.get("canonical_root") != "docs" or inventory.get("canonical_layout") != "first_class_dptn_c":
                errors.append("CKR ownership inventory no longer selects the normalized first-class docs topology")
            if inventory.get("concept_count") != 24:
                errors.append(f"CKR concept count drifted: {inventory.get('concept_count')!r}")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid CKR ownership inventory JSON: {exc}")

    for rel in LIVE_SURFACES:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing current implementation/routing surface: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "CKR status mirror:" in text:
            errors.append(f"{rel}: completed CKR phase mirror should not be duplicated in current implementation guidance")
        for token in FORBIDDEN:
            if token in text:
                errors.append(f"{rel}: stale CKR transition wording remains: {token!r}")

    implementation = repo / "docs/implementation/README.md"
    if not implementation.is_file() or CURRENT_HANDOFF not in implementation.read_text(encoding="utf-8"):
        errors.append("current implementation handoff must remain Implementation 001-A — NEXT / READY / NOT STARTED")

    for error in errors:
        print("ERROR", error)
    print(f"CKR exit/status validation: {len(errors)} error(s); CKR exit accepted")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
