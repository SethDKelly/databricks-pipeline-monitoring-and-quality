#!/usr/bin/env python3
"""Validate DMTZ coding-agent adapters without requiring vendor CLIs.

ADF-C validates repository configuration and authority topology. ADF-G later owns
runtime/tool-in-the-loop smoke verification and ADF-F owns CI integration.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_TOOLS = {"cursor", "claude_code", "codex"}
ALWAYS_TRUE = re.compile(r"^\s*alwaysApply\s*:\s*true\s*$", re.MULTILINE | re.IGNORECASE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    warnings: list[str] = []

    agents = repo / "AGENTS.md"
    knowledge = repo / "knowledge" / "index.md"
    scope_policy = repo / "docs" / "agentic_development_foundation" / "authority_scope_policy.md"
    claude = repo / ".claude" / "CLAUDE.md"
    root_claude = repo / "CLAUDE.md"
    manifest_path = repo / "docs" / "agentic_development_foundation" / "tool_compatibility.json"
    cursor_rules = repo / ".cursor" / "rules"

    for required in (agents, knowledge, scope_policy, manifest_path):
        if not required.is_file():
            fail(errors, f"missing required shared artifact: {required.relative_to(repo)}")

    if root_claude.exists():
        fail(errors, "root CLAUDE.md is intentionally disallowed: Cursor also loads it as persistent context; use .claude/CLAUDE.md")

    if not claude.is_file():
        fail(errors, "missing .claude/CLAUDE.md")
    else:
        text = claude.read_text(encoding="utf-8")
        if "@../AGENTS.md" not in text:
            fail(errors, ".claude/CLAUDE.md must import ../AGENTS.md")
        if "knowledge/index.md" not in text:
            fail(errors, ".claude/CLAUDE.md must route discovery to knowledge/index.md")
        if len(text.splitlines()) > 60:
            fail(errors, ".claude/CLAUDE.md exceeds the ADF-C thin-adapter budget of 60 lines")

    if not cursor_rules.is_dir():
        fail(errors, "missing .cursor/rules directory")
    else:
        rules = sorted(cursor_rules.rglob("*.mdc"))
        if not rules:
            fail(errors, "no Cursor .mdc project rules found")
        for rule in rules:
            text = rule.read_text(encoding="utf-8")
            rel = rule.relative_to(repo)
            if ALWAYS_TRUE.search(text):
                fail(errors, f"{rel}: alwaysApply true violates current scoped-rule policy")
            if len(text.splitlines()) > 500:
                fail(errors, f"{rel}: exceeds 500-line focused-rule budget")
        routing = cursor_rules / "00-implementation-routing.mdc"
        if not routing.is_file():
            fail(errors, "missing Cursor routing rule")
        else:
            text = routing.read_text(encoding="utf-8")
            for expected in ("knowledge/index.md", "authority_scope_policy.md", "AGENTS.md"):
                if expected not in text:
                    fail(errors, f"Cursor routing rule must reference {expected}")

    for forbidden in (repo / "CODEX.md", repo / ".codex" / "AGENTS.md"):
        if forbidden.exists():
            fail(errors, f"unexpected Codex semantic adapter: {forbidden.relative_to(repo)}; root AGENTS.md is canonical")

    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(errors, f"tool_compatibility.json is invalid JSON: {exc}")
        else:
            tools = manifest.get("tools", {})
            missing = REQUIRED_TOOLS - set(tools)
            if missing:
                fail(errors, f"tool compatibility manifest missing: {', '.join(sorted(missing))}")
            authority = manifest.get("authority", {})
            expected_authority = {
                "shared_instructions": "AGENTS.md",
                "scope_policy": "docs/agentic_development_foundation/authority_scope_policy.md",
                "knowledge_entry": "knowledge/index.md",
                "implementation_status": "docs/implementation/README.md",
            }
            for key, value in expected_authority.items():
                if authority.get(key) != value:
                    fail(errors, f"manifest authority.{key} must equal {value!r}")
            for name, tool in tools.items():
                if tool.get("knowledge_entry") != "knowledge/index.md":
                    fail(errors, f"manifest tool {name}: knowledge_entry must be knowledge/index.md")
                if "runtime_smoke_pending" in tool.get("support_status", ""):
                    warnings.append(f"{name}: runtime smoke verification remains pending ADF-G")

    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"Agent adapter validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
