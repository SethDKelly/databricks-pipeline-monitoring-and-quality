#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

SPEC = "docs/routing/okf_projection.json"
GENERATED = "scripts/agentic/generate_okf_projection.py"


def pretty(name: str) -> str:
    words = []
    for part in name.replace("_", "-").split("-"):
        words.append("DMTZ" if part.lower() == "dmtz" else part.capitalize())
    return " ".join(words)


def rel_link(output: str, target: str) -> str:
    start = Path(output).parent.as_posix() or "."
    return os.path.relpath(target, start=start).replace(os.sep, "/")


def frontmatter(route_type: str, title: str, description: str, resource: str, tags: list[str], output: str) -> str:
    tags_text = ", ".join(json.dumps(tag) for tag in tags)
    return (
        "---\n"
        f"type: {json.dumps(route_type)}\n"
        f"title: {json.dumps(title)}\n"
        f"description: {json.dumps(description)}\n"
        f"resource: {json.dumps(rel_link(output, resource))}\n"
        f"tags: [{tags_text}]\n"
        'status: "stable"\n'
        f'generated: "{GENERATED}"\n'
        "---\n"
    )


def render_concept(kind: str, route: dict, output: str) -> str:
    route_type = "Domain Routing Reference" if kind == "domains" else "Project Authority"
    body = frontmatter(route_type, route["title"], route["description"], route["resource"], ["dmtz", kind.rstrip("s"), "generated"], output)
    body += "# Use\n\n"
    body += "**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.** Source: `docs/routing/okf_projection.json`.\n\n"
    body += f"Primary route: [{route['title']}]({rel_link(output, route['resource'])}).\n"
    related = route.get("related", [])
    if related:
        body += "\nRelated current routes:\n\n"
        for target in related:
            body += f"- [{Path(target).name}]({rel_link(output, target)})\n"
    body += "\nThis projection is routing only. It does not establish semantic, authorization, evidence, health, causal, implementation, or deployment authority.\n"
    return body


def concept_index(kind: str, heading: str, routes: dict[str, tuple[str, dict]]) -> str:
    body = f"# {heading}\n\n**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**\n\n"
    for rel, (route_kind, route) in sorted(routes.items()):
        if route_kind == kind:
            body += f"- [{route['title']}]({rel.split('/', 1)[1]})\n"
    return body


def catalog_index(heading: str, output: str, entries: list[tuple[str, str]]) -> str:
    body = f"# {heading}\n\n**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.** Entries derive directly from repository-owned catalogs.\n\n"
    for title, target in entries:
        body += f"- [{title}]({rel_link(output, target)})\n"
    return body


def render_all(repo: Path) -> dict[str, str]:
    spec = json.loads((repo / SPEC).read_text(encoding="utf-8"))
    if spec.get("status") != "active" or spec.get("authority") != "DERIVED ROUTING ONLY — NOT SEMANTIC AUTHORITY":
        raise RuntimeError("OKF projection specification authority/status is invalid")
    if spec.get("discovery_root") != "docs/index.md" or spec.get("generated_root") != "knowledge":
        raise RuntimeError("OKF projection root contract drifted")

    routes: dict[str, tuple[str, dict]] = {}
    for route in spec["domains"]:
        routes[f"domains/{route['name']}.md"] = ("domains", route)
    for route in spec["project"]:
        routes[f"project/{route['name']}.md"] = ("project", route)

    skill_paths = sorted(repo.glob(spec["workflow_source"]))
    workflow_entries = [(pretty(path.parent.name), path.relative_to(repo).as_posix()) for path in skill_paths]
    implementation_paths = sorted(repo.glob(spec["implementation_source"]))
    implementation_entries = []
    for path in implementation_paths:
        dirname = path.parent.name
        implementation_entries.append((f"Implementation {dirname[:3]} — {pretty(dirname[4:])}", path.relative_to(repo).as_posix()))

    expected = spec["expected_counts"]
    actual = {
        "domains": sum(1 for kind, _ in routes.values() if kind == "domains"),
        "project": sum(1 for kind, _ in routes.values() if kind == "project"),
        "workflow_catalog_entries": len(workflow_entries),
        "implementation_catalog_entries": len(implementation_entries),
        "concept_documents": len(routes),
    }
    for key, value in actual.items():
        if expected.get(key) != value:
            raise RuntimeError(f"OKF projection count drift for {key}: expected {expected.get(key)}, found {value}")

    files: dict[str, str] = {}
    for rel, (kind, route) in routes.items():
        files[rel] = render_concept(kind, route, f"knowledge/{rel}")
    files["domains/index.md"] = concept_index("domains", "Domain routing", routes)
    files["project/index.md"] = concept_index("project", "Project routing", routes)
    files["workflows/index.md"] = catalog_index("Workflow routing", "knowledge/workflows/index.md", workflow_entries)
    files["implementation/index.md"] = catalog_index("Implementation routing", "knowledge/implementation/index.md", implementation_entries)
    files["index.md"] = '''---
okf_version: "0.2"
generated: "scripts/agentic/generate_okf_projection.py"
---
# DMTZ OKF Routing Projection

**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**

The authored discovery root is [`docs/index.md`](../docs/index.md). This `knowledge/` tree exists only as an OKF v0.2 compatibility projection and cannot establish DMTZ semantic authority.

- [Domain routes](domains/index.md)
- [Project routes](project/index.md)
- [Implementation routes](implementation/index.md)
- [Development workflow routes](workflows/index.md)

For a known stable ID, use `python3 scripts/agentic/resolve_stable_id.py <ID>` directly. Use `--history` only for explicit provenance work.
'''
    files["log.md"] = '''# OKF Projection Log

**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**

The pre-DPTN-E authored knowledge log and full routing tree are preserved under `docs/history/routing/okf-pre-dptn-e/`.

Current projection source: `docs/routing/okf_projection.json`.
Current discovery root: `docs/index.md`.
'''
    if expected.get("total_markdown_files") != len(files):
        raise RuntimeError(f"OKF projection file-count drift: expected {expected.get('total_markdown_files')}, found {len(files)}")
    return files


def check(repo: Path, files: dict[str, str]) -> int:
    root = repo / "knowledge"
    errors: list[str] = []
    expected = {Path(rel).as_posix() for rel in files}
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*.md")} if root.is_dir() else set()
    for rel in sorted(expected - actual):
        errors.append(f"missing generated OKF file: knowledge/{rel}")
    for rel in sorted(actual - expected):
        errors.append(f"unexpected non-generated OKF file: knowledge/{rel}")
    for rel in sorted(expected & actual):
        if (root / rel).read_text(encoding="utf-8") != files[rel]:
            errors.append(f"generated OKF drift: knowledge/{rel}")
    for error in errors:
        print("ERROR", error)
    print(f"OKF projection generation check: {len(errors)} error(s), {len(files)} tracked markdown file(s)")
    return 1 if errors else 0


def write(repo: Path, files: dict[str, str]) -> int:
    root = repo / "knowledge"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    for rel, content in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(files)} OKF projection markdown file(s) under knowledge/")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    try:
        files = render_all(repo)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1
    return write(repo, files) if args.write else check(repo, files)


if __name__ == "__main__":
    raise SystemExit(main())
