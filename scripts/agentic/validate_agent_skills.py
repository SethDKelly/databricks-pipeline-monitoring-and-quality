#!/usr/bin/env python3
"""Dependency-free structural validator for DMTZ ADF-D portable workflows."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKILLS = (
    "resolve-context",
    "implement-group",
    "resolve-contract",
    "run-conformance",
    "review-change",
    "update-traceability",
    "exit-review",
)
ALLOWED_FRONTMATTER = {"name", "description"}
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
MAX_SKILL_BYTES = 7000
MAX_BRIDGE_BYTES = 900


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data: dict[str, str] = {}
    for line in lines[1:end]:
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data, "\n".join(lines[end + 1 :])


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    warnings: list[str] = []

    canonical = repo / ".agents" / "skills"
    if not canonical.is_dir():
        errors.append("canonical .agents/skills directory is missing")

    for name in SKILLS:
        skill = canonical / name / "SKILL.md"
        if not skill.is_file():
            errors.append(f"missing canonical skill: {skill.relative_to(repo)}")
            continue
        text = skill.read_text(encoding="utf-8")
        if len(text.encode("utf-8")) > MAX_SKILL_BYTES:
            errors.append(f"{skill.relative_to(repo)} exceeds {MAX_SKILL_BYTES} byte focused-workflow budget")
        try:
            meta, body = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{skill.relative_to(repo)}: {exc}")
            continue
        if meta.get("name") != name:
            errors.append(f"{skill.relative_to(repo)} name must equal directory name {name!r}")
        if not meta.get("description"):
            errors.append(f"{skill.relative_to(repo)} requires description")
        extras = sorted(set(meta) - ALLOWED_FRONTMATTER)
        if extras:
            errors.append(f"{skill.relative_to(repo)} has provider-specific/unapproved frontmatter: {', '.join(extras)}")
        for heading in ("Human-directed boundary", "Workflow", "Stop conditions"):
            if heading not in body:
                errors.append(f"{skill.relative_to(repo)} missing required section marker: {heading}")
        if "autonom" not in body.lower() and name == "implement-group":
            warnings.append("implement-group does not contain an explicit autonomy-boundary term")

        bridge = repo / ".claude" / "commands" / f"{name}.md"
        if not bridge.is_file():
            errors.append(f"missing Claude bridge: {bridge.relative_to(repo)}")
        else:
            bridge_text = bridge.read_text(encoding="utf-8")
            expected = f".agents/skills/{name}/SKILL.md"
            if expected not in bridge_text:
                errors.append(f"{bridge.relative_to(repo)} does not point to {expected}")
            if len(bridge_text.encode("utf-8")) > MAX_BRIDGE_BYTES:
                errors.append(f"{bridge.relative_to(repo)} exceeds thin-bridge budget")

        duplicate = repo / ".claude" / "skills" / name / "SKILL.md"
        if duplicate.exists():
            errors.append(f"duplicate Claude skill would create a second workflow source: {duplicate.relative_to(repo)}")

        route = repo / "knowledge" / "workflows" / f"{name}.md"
        if not route.is_file():
            errors.append(f"missing OKF workflow route: {route.relative_to(repo)}")
        else:
            route_text = route.read_text(encoding="utf-8")
            if 'status: "stable"' not in route_text:
                errors.append(f"{route.relative_to(repo)} must be stable after ADF-D")
            if f"../../.agents/skills/{name}/SKILL.md" not in route_text:
                errors.append(f"{route.relative_to(repo)} does not route to canonical skill")

    manifest = repo / "docs" / "agentic_development_foundation" / "tool_compatibility.json"
    if not manifest.is_file():
        errors.append("tool compatibility manifest is missing")
    else:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            for tool in ("cursor", "claude_code", "codex"):
                mechanism = data["tools"][tool].get("workflow_mechanism", "")
                if not mechanism or ("ADF-D" in mechanism and "deferred" in mechanism.lower()):
                    errors.append(f"tool compatibility manifest still defers ADF-D workflow mechanism for {tool}")
        except (json.JSONDecodeError, KeyError) as exc:
            errors.append(f"invalid tool compatibility manifest: {exc}")

    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"Agent skill validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
