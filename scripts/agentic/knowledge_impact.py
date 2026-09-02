#!/usr/bin/env python3
"""Report OKF routing concepts whose canonical resource matches changed paths.

This is a review-impact helper only. A canonical change does not automatically mean
the routing concept is stale or must be rewritten.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data


def local_resource(concept: Path, resource: str, repo: Path) -> Path | None:
    if not resource or resource.startswith(("http://", "https://")) or urlparse(resource).scheme:
        return None
    return (concept.parent / resource).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--changed", action="append", default=[])
    parser.add_argument("--all", action="store_true", help="show complete reverse resource map")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    knowledge = repo / "knowledge"
    reverse: dict[Path, list[Path]] = {}

    for concept in sorted(knowledge.rglob("*.md")):
        if concept.name in {"index.md", "log.md"}:
            continue
        meta = frontmatter(concept)
        target = local_resource(concept, meta.get("resource", ""), repo)
        if target is not None:
            reverse.setdefault(target, []).append(concept)

    if args.all:
        for target, concepts in sorted(reverse.items(), key=lambda item: str(item[0])):
            rel_target = target.relative_to(repo) if target.is_relative_to(repo) else target
            print(f"{rel_target}")
            for concept in concepts:
                print(f"  REVIEW-ROUTE {concept.relative_to(repo)}")
        return 0

    if not args.changed:
        parser.error("provide --changed <repository-path> or --all")

    found = 0
    for raw in args.changed:
        changed = (repo / raw).resolve()
        concepts = reverse.get(changed, [])
        print(f"CHANGED {raw}")
        if not concepts:
            print("  no direct OKF resource routes; no automatic knowledge edit required")
        for concept in concepts:
            found += 1
            print(f"  REVIEW-CANDIDATE {concept.relative_to(repo)}")

    print(f"Knowledge impact: {found} direct routing review candidate(s). A candidate is not automatically stale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
