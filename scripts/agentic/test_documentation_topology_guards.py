#!/usr/bin/env python3
"""Negative controls for the durable post-DPTN documentation topology guard."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VALIDATOR = "scripts/agentic/validate_documentation_topology.py"


def run(repo: Path) -> int:
    return subprocess.run(
        [sys.executable, str(repo / VALIDATOR), "--repo", str(repo)],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode


def expect_failure(repo: Path, label: str, mutate, restore, errors: list[str]) -> None:
    try:
        mutate()
        if run(repo) == 0:
            errors.append(f"{label}: validator unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        restore()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    src = Path(ap.parse_args().repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="dmtz-topology-guards-") as td:
        repo = Path(td) / "repo"
        shutil.copytree(src, repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"), symlinks=True)

        # 1. Reintroduce the retired canonical compatibility namespace.
        p = repo / "docs/canonical/README.md"
        expect_failure(
            repo,
            "retired docs/canonical namespace restored",
            lambda: (p.parent.mkdir(parents=True, exist_ok=True), p.write_text("legacy\n", encoding="utf-8")),
            lambda: shutil.rmtree(p.parent, ignore_errors=True),
            errors,
        )

        # 2. Reintroduce the retired live DPTN program root.
        p = repo / "docs/documentation_topology_normalization/README.md"
        expect_failure(
            repo,
            "live DPTN program root restored",
            lambda: (p.parent.mkdir(parents=True, exist_ok=True), p.write_text("active\n", encoding="utf-8")),
            lambda: shutil.rmtree(p.parent, ignore_errors=True),
            errors,
        )

        # 3. Lose the final accepted DPTN exit manifest.
        p = repo / "docs/history/retrofits/dptn/dptn_g_exit_manifest.json"
        saved = p.read_bytes()
        expect_failure(repo, "DPTN-G exit manifest missing", p.unlink, lambda: p.write_bytes(saved), errors)

        # 4. Drift accepted concept count.
        p = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
        original = p.read_text(encoding="utf-8")
        data = json.loads(original)
        data["concept_count"] = 25
        expect_failure(
            repo,
            "accepted concept count drift",
            lambda: p.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 5. Extend the frozen ARCH range.
        p = repo / "docs/agentic_development_foundation/stable_id_registry.json"
        original = p.read_text(encoding="utf-8")
        data = json.loads(original)
        data["families"]["ARCH"]["max"] = 501
        expect_failure(
            repo,
            "stable-ID range drift",
            lambda: p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 6. Weaken the history authority boundary.
        p = repo / "docs/history/README.md"
        original = p.read_text(encoding="utf-8")
        expect_failure(
            repo,
            "history authority weakened",
            lambda: p.write_text(original.replace("HISTORY / PROVENANCE ONLY", "HISTORY ONLY", 1), encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 7. Start implementation as a side effect of DPTN exit.
        p = repo / "docs/implementation/README.md"
        original = p.read_text(encoding="utf-8")
        expect_failure(
            repo,
            "implementation started by topology exit",
            lambda: p.write_text(original.replace("Implementation 001-A — NEXT / READY / NOT STARTED", "Implementation 001-A — IN PROGRESS", 1), encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 8. Remove the authored discovery root.
        p = repo / "docs/index.md"
        saved = p.read_bytes()
        expect_failure(repo, "authored discovery root missing", p.unlink, lambda: p.write_bytes(saved), errors)

        # 9. Rebind generated OKF topology routing to history instead of current discovery.
        p = repo / "docs/routing/okf_projection.json"
        original = p.read_text(encoding="utf-8")
        data = json.loads(original)
        for route in data["project"]:
            if route["name"] == "documentation-topology":
                route["resource"] = "docs/history/retrofits/dptn/README.md"
        expect_failure(
            repo,
            "OKF topology route points to history",
            lambda: p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 10. Restore one retired phase-specific DPTN validator to live tooling.
        source = repo / "docs/history/retrofits/dptn/tooling/validate_dptn_status.py"
        target = repo / "scripts/agentic/validate_dptn_status.py"
        expect_failure(
            repo,
            "retired phase tooling restored live",
            lambda: shutil.copy2(source, target),
            lambda: target.unlink(missing_ok=True),
            errors,
        )

        # 11. Reintroduce a current routing dependency on docs/canonical.
        p = repo / "AGENTS.md"
        original = p.read_text(encoding="utf-8")
        expect_failure(
            repo,
            "current agent routing points to retired canonical path",
            lambda: p.write_text(original + "\nUse docs/canonical/architecture for current routing.\n", encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

        # 12. Revoke the archived exit decision.
        p = repo / "docs/history/retrofits/dptn/dptn_g_exit_manifest.json"
        original = p.read_text(encoding="utf-8")
        data = json.loads(original)
        data["exit_decision"] = "rejected"
        expect_failure(
            repo,
            "archived DPTN exit decision changed",
            lambda: p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8"),
            lambda: p.write_text(original, encoding="utf-8"),
            errors,
        )

    for e in errors:
        print("ERROR", e)
    print(f"Final documentation topology guards: {len(errors)} error(s), 12 negative control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
