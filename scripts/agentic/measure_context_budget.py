#!/usr/bin/env python3
"""Measure deterministic repository byte budgets for DMTZ agent-facing context surfaces."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def size(path: Path) -> int:
    return len(path.read_bytes()) if path.is_file() else 0


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    cfg_path = repo / "docs" / "agentic_development_foundation" / "context_budget.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))["limits"]
    errors: list[str] = []

    agents = repo / "AGENTS.md"
    claude = repo / ".claude" / "CLAUDE.md"
    root_claude = repo / "CLAUDE.md"
    rules = sorted((repo / ".cursor" / "rules").glob("*.mdc"))

    measurements: list[tuple[str, int, int]] = []
    measurements.append(("AGENTS.md", size(agents), cfg["agents_md"]))
    measurements.append((".claude/CLAUDE.md", size(claude), cfg["claude_md"]))

    cursor_total = sum(size(path) for path in rules)
    measurements.append(("cursor rules aggregate", cursor_total, cfg["cursor_rules_aggregate"]))
    for path in rules:
        measurements.append((str(path.relative_to(repo)), size(path), cfg["cursor_rule_each"]))

    always_bytes = 0
    for path in rules:
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?m)^alwaysApply:\s*true\s*$", text):
            always_bytes += size(path)

    cursor_baseline = size(agents) + always_bytes + size(root_claude)
    claude_baseline = size(agents) + size(claude)
    codex_baseline = size(agents)
    measurements.extend(
        [
            ("cursor root baseline", cursor_baseline, cfg["cursor_root_baseline"]),
            ("claude root baseline", claude_baseline, cfg["claude_root_baseline"]),
            ("codex root baseline", codex_baseline, cfg["codex_root_baseline"]),
        ]
    )

    for path in sorted((repo / ".agents" / "skills").glob("*/SKILL.md")):
        measurements.append((str(path.relative_to(repo)), size(path), cfg["skill_each"]))
    for path in sorted((repo / ".claude" / "commands").glob("*.md")):
        measurements.append((str(path.relative_to(repo)), size(path), cfg["claude_command_each"]))

    knowledge = repo / "knowledge"
    root_index = knowledge / "index.md"
    measurements.append(("knowledge/index.md", size(root_index), cfg["knowledge_root_index"]))
    for path in sorted(knowledge.rglob("*.md")):
        if path == root_index or path.name == "log.md":
            continue
        limit = cfg["knowledge_nested_index_each"] if path.name == "index.md" else cfg["knowledge_concept_each"]
        measurements.append((str(path.relative_to(repo)), size(path), limit))

    for name, actual, limit in measurements:
        state = "PASS" if actual <= limit else "FAIL"
        print(f"{state:4} {actual:6}/{limit:6} bytes  {name}")
        if actual > limit:
            errors.append(f"{name} exceeds context budget by {actual - limit} bytes")

    if root_claude.is_file():
        errors.append("root CLAUDE.md exists and contributes duplicate persistent Cursor context")

    for error in errors:
        print(f"ERROR {error}")
    print(f"Context budget validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
