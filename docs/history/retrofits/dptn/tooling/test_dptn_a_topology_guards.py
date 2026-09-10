#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VALIDATOR = "validate_dptn_a_topology.py"


def run(repo: Path) -> int:
    return subprocess.run([sys.executable, str(repo / "scripts/agentic" / VALIDATOR), "--repo", str(repo)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode


def mutate(repo: Path, rel: str, transform, label: str, errors: list[str]) -> None:
    path = repo / rel
    original = path.read_text(encoding="utf-8")
    try:
        changed = transform(original)
        if changed == original:
            errors.append(f"{label}: mutation was a no-op")
            return
        path.write_text(changed, encoding="utf-8")
        if run(repo) == 0:
            errors.append(f"{label}: DPTN-A validator unexpectedly passed")
        else:
            print(f"PASS negative control: {label}")
    finally:
        path.write_text(original, encoding="utf-8")


def json_transform(fn):
    def transform(text: str) -> str:
        data = json.loads(text)
        fn(data)
        return json.dumps(data, indent=2) + "\n"
    return transform


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=".")
    src = Path(ap.parse_args().repo).resolve(); errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="dmtz-dptna-") as td:
        repo = Path(td) / "repo"
        shutil.copytree(src, repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"))

        mutate(repo, "docs/documentation_topology_normalization/topology_inventory.json", json_transform(lambda d: d["accepted_counts"].__setitem__("stable_ids", 1238)), "stable-ID baseline drift", errors)
        mutate(repo, "docs/documentation_topology_normalization/topology_inventory.json", json_transform(lambda d: d["accepted_counts"].__setitem__("concepts", 25)), "concept-count baseline drift", errors)
        mutate(repo, "docs/documentation_topology_normalization/move_map.json", json_transform(lambda d: d.__setitem__("physical_moves_authorized", True)), "premature physical-move authorization", errors)
        mutate(repo, "docs/documentation_topology_normalization/move_map.json", json_transform(lambda d: d["moves"][6].pop("requires", None)), "concept collision dependency removal", errors)
        mutate(repo, "docs/documentation_topology_normalization/move_map.json", json_transform(lambda d: d["moves"][13].pop("requires", None)), "reference collision dependency removal", errors)
        mutate(repo, "docs/documentation_topology_normalization/topology_inventory.json", json_transform(lambda d: next(r for r in d["inventory"] if r["source"] == "docs/canonical_knowledge_retrofit/**").__setitem__("action", "relocate")), "CKR mixed-lifecycle bulk move", errors)
        mutate(repo, "docs/documentation_topology_normalization/topology_inventory.json", json_transform(lambda d: next(r for r in d["inventory"] if r["source"] == "docs/agentic_development_foundation/**").__setitem__("action", "relocate")), "ADF mixed-lifecycle bulk move", errors)
        mutate(repo, "docs/documentation_topology_normalization/collision_register.md", lambda t: t.replace("COL-013", "COL-099", 1), "collision-register identity drift", errors)
        mutate(repo, "docs/documentation_topology_normalization/fixtures/dptn_a_topology_scenarios.yaml", lambda t: t.replace("DPTNA-24", "DPTNA-99", 1), "scenario identity drift", errors)
        mutate(repo, "docs/documentation_topology_normalization/README.md", lambda t: t.replace("Implementation 001-A remains blocked until DPTN-G", "Implementation 001-A may begin during DPTN"), "implementation gate bypass", errors)

    for e in errors: print("ERROR", e)
    print(f"DPTN-A topology guard tests: {len(errors)} error(s), 10 negative control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
