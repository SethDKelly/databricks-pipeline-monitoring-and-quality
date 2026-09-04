#!/usr/bin/env python3
"""Resolve exact DMTZ stable-ID occurrences without manufacturing canonicality."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})$")


def load_registry(repo: Path) -> dict:
    path = repo / "docs" / "agentic_development_foundation" / "stable_id_registry.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_ckr_family(repo: Path, registry: dict, family: str) -> dict | None:
    rel = registry.get("ownership_inventory")
    if not rel:
        return None
    path = repo / rel
    if not path.is_file():
        return None
    try:
        inventory = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return inventory.get("stable_families", {}).get(family)


def classify(line: str, stable_id: str) -> str:
    stripped = line.strip()
    escaped = re.escape(stable_id)
    patterns = (
        rf"^#+\s+(?:\*\*)?{escaped}(?:\*\*)?(?:\b|\s|[:—-])",
        rf"^(?:[-*]\s+)?(?:\*\*)?{escaped}(?:\*\*)?(?:\b|\s|[:—-])",
    )
    return "definition_candidate" if any(re.search(p, stripped) for p in patterns) else "reference"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("stable_id")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    token = args.stable_id.strip().upper()
    match = ID_RE.match(token)
    if not match:
        print(f"ERROR invalid stable ID format: {args.stable_id}")
        return 2

    registry = load_registry(repo)
    family, number_text = match.groups()
    number = int(number_text)
    limits = registry["families"].get(family)
    if not limits or number < limits["min"] or number > limits["max"]:
        if limits:
            accepted = f"{family}-{limits['min']:03d}..{family}-{limits['max']:03d}"
        else:
            accepted = "no accepted range"
        print(f"ERROR {token} is outside {accepted}")
        return 2

    family_authority = load_ckr_family(repo, registry, family)

    root = repo / registry.get("search_root", "docs")
    occurrence_pattern = re.compile(rf"(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])")
    results: list[dict[str, object]] = []

    for path in sorted(root.rglob("*.md")):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for index, line in enumerate(lines, start=1):
            if occurrence_pattern.search(line):
                results.append(
                    {
                        "path": str(path.relative_to(repo)),
                        "line": index,
                        "role": classify(line, token),
                        "text": line.strip(),
                    }
                )

    authority_hint = None
    if family_authority:
        authority_hint = {
            "migration_state": family_authority.get("migration_state"),
            "current_owner_root": family_authority.get("current_owner_root"),
            "target_owner_root": family_authority.get("target_owner_root"),
            "note": "Family-level CKR hint only. CKR-J will add deterministic exact canonical owner/anchor resolution after migration.",
        }

    payload = {
        "stable_id": token,
        "accepted_range": f"{family}-{limits['min']:03d}..{family}-{limits['max']:03d}",
        "ckr_authority": authority_hint,
        "occurrences": results,
        "canonicality_note": "Occurrences are retrieval candidates. definition_candidate is mechanical only. During CKR, use the ownership inventory to determine whether current authority is still legacy or has canonicalized; do not infer ownership from search order.",
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"{token}: {len(results)} exact occurrence(s)")
        if authority_hint:
            print(
                "CKR family state: "
                f"{authority_hint['migration_state']} | current root={authority_hint['current_owner_root']} "
                f"| target root={authority_hint['target_owner_root']}"
            )
        for item in results:
            print(f"{item['role']:20} {item['path']}:{item['line']}  {item['text']}")
        print(payload["canonicality_note"])

    if not results:
        print("ERROR no exact stable-ID occurrence found; do not infer semantics from memory", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
