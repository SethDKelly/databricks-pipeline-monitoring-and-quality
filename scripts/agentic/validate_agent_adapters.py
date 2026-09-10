#!/usr/bin/env python3
"""Validate DMTZ coding-agent adapters against current repository routing."""
from __future__ import annotations
import json,re,sys
from pathlib import Path

REQUIRED_TOOLS={"cursor","claude_code","codex"}
ALWAYS_TRUE=re.compile(r"^\s*alwaysApply\s*:\s*true\s*$",re.M|re.I)

def main()->int:
    repo=Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve();errors=[];warnings=[]
    agents=repo/"AGENTS.md";docs_index=repo/"docs/index.md";okf=repo/"knowledge/index.md";scope=repo/"docs/agentic_development_foundation/authority_scope_policy.md";claude=repo/".claude/CLAUDE.md";root_claude=repo/"CLAUDE.md";manifest_path=repo/"docs/agentic_development_foundation/tool_compatibility.json";cursor_rules=repo/".cursor/rules"
    for p in (agents,docs_index,okf,scope,manifest_path):
        if not p.is_file():errors.append(f"missing required shared artifact: {p.relative_to(repo)}")
    if root_claude.exists():errors.append("root CLAUDE.md is intentionally disallowed: use .claude/CLAUDE.md")
    if okf.is_file():
        text=okf.read_text(encoding="utf-8")
        if "GENERATED OKF PROJECTION — DO NOT HAND-EDIT." not in text or "docs/index.md" not in text:errors.append("knowledge/index.md must remain generated compatibility routing to docs/index.md")
    if not claude.is_file():errors.append("missing .claude/CLAUDE.md")
    else:
        text=claude.read_text(encoding="utf-8")
        if "@../AGENTS.md" not in text:errors.append(".claude/CLAUDE.md must import ../AGENTS.md")
        for token in ("docs/index.md","knowledge/index.md"):
            if token not in text:errors.append(f".claude/CLAUDE.md must reference {token}")
        if "compatib" not in text.lower():errors.append(".claude/CLAUDE.md must distinguish generated OKF compatibility")
        if len(text.splitlines())>60:errors.append(".claude/CLAUDE.md exceeds the thin-adapter budget of 60 lines")
    if not cursor_rules.is_dir():errors.append("missing .cursor/rules directory")
    else:
        rules=sorted(cursor_rules.rglob("*.mdc"))
        if not rules:errors.append("no Cursor .mdc project rules found")
        for rule in rules:
            text=rule.read_text(encoding="utf-8");rel=rule.relative_to(repo)
            if ALWAYS_TRUE.search(text):errors.append(f"{rel}: alwaysApply true violates current scoped-rule policy")
            if len(text.splitlines())>500:errors.append(f"{rel}: exceeds 500-line focused-rule budget")
        routing=cursor_rules/"00-implementation-routing.mdc"
        if not routing.is_file():errors.append("missing Cursor routing rule")
        else:
            text=routing.read_text(encoding="utf-8")
            for token in ("docs/index.md","knowledge/index.md","authority_scope_policy.md","AGENTS.md"):
                if token not in text:errors.append(f"Cursor routing rule must reference {token}")
    for forbidden in (repo/"CODEX.md",repo/".codex/AGENTS.md"):
        if forbidden.exists():errors.append(f"unexpected Codex semantic adapter: {forbidden.relative_to(repo)}; root AGENTS.md is canonical")
    if manifest_path.is_file():
        try:manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:errors.append(f"tool_compatibility.json is invalid JSON: {exc}");manifest={}
        tools=manifest.get("tools",{});missing=REQUIRED_TOOLS-set(tools)
        if missing:errors.append(f"tool compatibility manifest missing: {', '.join(sorted(missing))}")
        authority=manifest.get("authority",{});expected={"shared_instructions":"AGENTS.md","scope_policy":"docs/agentic_development_foundation/authority_scope_policy.md","knowledge_entry":"docs/index.md","okf_compatibility_entry":"knowledge/index.md","implementation_status":"docs/implementation/README.md"}
        for key,value in expected.items():
            if authority.get(key)!=value:errors.append(f"manifest authority.{key} must equal {value!r}")
        for name,tool in tools.items():
            if tool.get("knowledge_entry")!="docs/index.md":errors.append(f"manifest tool {name}: knowledge_entry must be docs/index.md")
            if tool.get("okf_compatibility_entry")!="knowledge/index.md":errors.append(f"manifest tool {name}: okf_compatibility_entry must be knowledge/index.md")
            if "runtime_smoke_pending" in tool.get("support_status",""):warnings.append(f"{name}: runtime smoke verification remains pending ADF-G-XT01")
    for w in warnings:print("WARN",w)
    for e in errors:print("ERROR",e)
    print(f"Agent adapter validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
