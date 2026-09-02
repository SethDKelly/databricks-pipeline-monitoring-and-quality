#!/usr/bin/env python3
"""Dependency-free structural validator for the DMTZ OKF routing bundle.

ADF-B intentionally avoids adding a Python dependency stack before Implementation 001.
This validates the DMTZ producer profile, local resources, links, lifecycle warnings,
and root OKF version declaration. ADF-F may later replace/extend it with a full YAML
parser and CI integration without changing the profile semantics.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = ("type", "title", "description", "resource", "tags", "status")
VALID_STATUS = {"draft", "stable", "deprecated"}
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def scalar(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        return raw[1:-1]
    return raw


def parse_frontmatter(path: Path, text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter opening delimiter has no closing delimiter")
    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = scalar(match.group(2) or "")
    return data, "\n".join(lines[end + 1 :])


def local_target(source: Path, target: str, repo: Path) -> Path | None:
    target = target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    parsed = urlparse(target)
    if parsed.scheme:
        return None
    if target.startswith("/"):
        return (repo / target.lstrip("/")).resolve()
    return (source.parent / target).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    knowledge = repo / "knowledge"
    errors: list[str] = []
    warnings: list[str] = []

    if not knowledge.is_dir():
        print("ERROR knowledge/ directory is missing")
        return 1

    root_index = knowledge / "index.md"
    if not root_index.is_file():
        errors.append("knowledge/index.md is missing")
    else:
        try:
            root_meta, _ = parse_frontmatter(root_index, root_index.read_text(encoding="utf-8"))
            if scalar(root_meta.get("okf_version", "")) != "0.2":
                errors.append('knowledge/index.md must declare okf_version: "0.2"')
        except ValueError as exc:
            errors.append(f"knowledge/index.md: {exc}")

    today = dt.date.today()
    for path in sorted(knowledge.rglob("*.md")):
        rel = path.relative_to(repo)
        text = path.read_text(encoding="utf-8")
        try:
            meta, body = parse_frontmatter(path, text)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        if path.name not in {"index.md", "log.md"}:
            if not meta:
                errors.append(f"{rel}: concept document requires YAML frontmatter")
                continue
            missing = [key for key in REQUIRED if not meta.get(key, "").strip()]
            if missing:
                errors.append(f"{rel}: missing DMTZ profile fields: {', '.join(missing)}")
            status = scalar(meta.get("status", ""))
            if status and status not in VALID_STATUS:
                errors.append(f"{rel}: invalid status {status!r}")
            if status == "deprecated":
                warnings.append(f"{rel}: deprecated knowledge entry")
            tags = meta.get("tags", "").strip()
            if tags and not (tags.startswith("[") and tags.endswith("]")):
                errors.append(f"{rel}: DMTZ profile requires tags as an inline YAML list")

            resource = scalar(meta.get("resource", ""))
            target = local_target(path, resource, repo)
            if target is not None and not target.exists():
                errors.append(f"{rel}: resource target does not exist: {resource}")

            stale_after = scalar(meta.get("stale_after", ""))
            if stale_after:
                try:
                    stale_date = dt.date.fromisoformat(stale_after[:10])
                    if stale_date <= today:
                        warnings.append(f"{rel}: stale_after has been reached ({stale_after})")
                except ValueError:
                    errors.append(f"{rel}: stale_after must begin with ISO date YYYY-MM-DD")

        for link in MARKDOWN_LINK.findall(body):
            target = local_target(path, link, repo)
            if target is not None and not target.exists():
                errors.append(f"{rel}: local Markdown link target does not exist: {link}")

    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERROR {error}")

    print(f"OKF validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    if errors or (warnings and args.strict_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
