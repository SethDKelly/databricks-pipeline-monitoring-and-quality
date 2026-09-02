#!/usr/bin/env python3
"""Report availability/version of supported coding-agent runtimes.

This probe is deliberately non-authenticating and non-semantic. Finding a binary is not
ADF-G runtime acceptance; the representative bounded task must still be performed and
recorded in runtime_compatibility_evidence.json.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

TOOL_COMMANDS = {
    "cursor": ("agent", "cursor-agent", "cursor"),
    "claude_code": ("claude",),
    "codex": ("codex",),
}


def version(command: str) -> str | None:
    try:
        proc = subprocess.run(
            [command, "--version"],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = (proc.stdout or proc.stderr).strip()
    return output.splitlines()[0] if output else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--require", choices=sorted(TOOL_COMMANDS))
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    required_surfaces = {
        "AGENTS.md": repo / "AGENTS.md",
        "knowledge/index.md": repo / "knowledge/index.md",
        ".agents/skills": repo / ".agents/skills",
        ".claude/CLAUDE.md": repo / ".claude/CLAUDE.md",
        ".cursor/rules": repo / ".cursor/rules",
    }
    result: dict[str, object] = {
        "repository_surfaces": {
            name: path.exists() for name, path in required_surfaces.items()
        },
        "tools": {},
        "note": "Binary availability/version is environment evidence only, not ADF-G runtime acceptance.",
    }

    tools: dict[str, dict[str, object]] = {}
    for tool, candidates in TOOL_COMMANDS.items():
        found = None
        for candidate in candidates:
            path = shutil.which(candidate)
            if path:
                found = (candidate, path)
                break
        tools[tool] = {
            "available": found is not None,
            "command": found[0] if found else None,
            "path": found[1] if found else None,
            "version": version(found[0]) if found else None,
        }
    result["tools"] = tools

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for tool, data in tools.items():
            state = "AVAILABLE" if data["available"] else "UNAVAILABLE"
            detail = f" ({data['version']})" if data.get("version") else ""
            print(f"{tool}: {state}{detail}")
        missing = [name for name, exists in result["repository_surfaces"].items() if not exists]
        print(f"repository surfaces: {'PASS' if not missing else 'FAIL'}")
        for name in missing:
            print(f"MISSING {name}")

    if args.require and not tools[args.require]["available"]:
        return 2
    return 1 if not all(result["repository_surfaces"].values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
