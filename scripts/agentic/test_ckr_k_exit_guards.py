#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VALIDATOR = "validate_ckr_k_exit.py"


def run(repo: Path) -> int:
    return subprocess.run(
        [sys.executable, str(repo / "scripts/agentic" / VALIDATOR), "--repo", str(repo)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode


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
            errors.append(f"{label}: CKR-K validator unexpectedly passed")
        else:
            print(f"PASS negative control: {label}")
    finally:
        path.write_text(original, encoding="utf-8")


def mutate_pair(repo: Path, first: tuple[str, object], second: tuple[str, object], label: str, errors: list[str]) -> None:
    paths = [(repo / first[0], first[1]), (repo / second[0], second[1])]
    originals = [(path, path.read_text(encoding="utf-8"), transform) for path, transform in paths]
    try:
        changed_any = False
        for path, original, transform in originals:
            changed = transform(original)
            changed_any = changed_any or changed != original
            path.write_text(changed, encoding="utf-8")
        if not changed_any:
            errors.append(f"{label}: mutation was a no-op")
            return
        if run(repo) == 0:
            errors.append(f"{label}: CKR-K validator unexpectedly passed")
        else:
            print(f"PASS negative control: {label}")
    finally:
        for path, original, _ in originals:
            path.write_text(original, encoding="utf-8")


def json_transform(fn):
    def transform(text: str) -> str:
        data = json.loads(text)
        fn(data)
        return json.dumps(data, indent=2) + "\n"
    return transform


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    src = Path(args.repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="dmtz-ckrk-guards-") as td:
        repo = Path(td) / "repo"
        shutil.copytree(src, repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"))
        manifest = json.loads((repo / "docs/canonical_knowledge_retrofit/ckr_k_exit_manifest.json").read_text(encoding="utf-8"))
        accepted = manifest.get("status") == "accepted"

        def regress_record(data): data["records"][0]["migration_state"] = "candidate_ready"
        def regress_family(data): data["stable_families"]["OPS"]["migration_state"] = "candidate_ready"
        def regress_segment(data): data["architecture_segments"][0]["migration_state"] = "candidate_ready"
        def routing_inactive(data): data["status"] = "candidate_ready"
        def route_to_history(data): data["okf_semantic_routes"][0]["primary_resource"] = "docs/concepts/phase_004/README.md"
        def registry_drift(data): data["families"]["ARCH"]["max"] = 501

        mutate(repo, "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json", json_transform(regress_record), "record migration regression after CKR exit review", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json", json_transform(regress_family), "stable-family migration regression after CKR exit review", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json", json_transform(regress_segment), "architecture-segment migration regression after CKR exit review", errors)
        mutate(repo, "docs/canonical/reference/product-definition.md", lambda t: t.replace("**Authority:** CANONICAL CURRENT AUTHORITY", "**Authority:** HISTORY ONLY", 1), "canonical target authority loss", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/ckr_j_execution_review.md", lambda t: t.replace("ACCEPTED", "REVIEWED"), "prior CKR acceptance evidence loss", errors)
        mutate(repo, "docs/canonical/reference/product-definition.md", lambda t: t.replace("## Provenance", "## Source notes", 1), "record-level canonical provenance loss", errors)
        mutate(repo, "docs/canonical/contracts/operations/lineage-topology.md", lambda t: t.replace("phase_007", "phase_history"), "stable-family phase provenance loss", errors)
        mutate(repo, "docs/design_history/README.md", lambda t: t.replace("PROVENANCE / RATIONALE / HISTORICAL DESIGN RECORD", "REFERENCE MATERIAL", 1), "design-history role collapse", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json", json_transform(routing_inactive), "canonical-first routing deactivation", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json", json_transform(route_to_history), "current OKF route regression to phase history", errors)
        mutate(repo, "docs/agentic_development_foundation/stable_id_registry.json", json_transform(registry_drift), "accepted stable-ID range drift", errors)
        mutate(repo, "scripts/agentic/resolve_stable_id.py", lambda t: t.replace("canonical_locator", "legacy_locator"), "deterministic canonical locator behavior removed", errors)
        mutate(repo, "docs/canonical_knowledge_retrofit/fixtures/ckr_k_exit_scenarios.yaml", lambda t: t.replace("  - id: CKRK-36\n", "  - id: CKRK-99\n", 1), "CKR-K fixture identity drift", errors)

        if accepted:
            inv_transform = json_transform(lambda d: d.__setitem__("status", "ckr_i_cutover"))
            impl_transform = lambda t: t.replace("CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.", "CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.", 1)
            label = "accepted exit lifecycle and implementation release regression"
        else:
            inv_transform = json_transform(lambda d: d.__setitem__("status", "ckr_complete"))
            impl_transform = lambda t: t.replace("IMPLEMENTATION 001-A BLOCKED ON CKR EXIT", "IMPLEMENTATION 001-A NEXT", 1)
            label = "premature exit lifecycle and implementation release"
        mutate_pair(
            repo,
            ("docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json", inv_transform),
            ("AGENTS.md", impl_transform),
            label,
            errors,
        )

    for error in errors: print("ERROR", error)
    print(f"CKR-K exit guard tests: {len(errors)} error(s), 14 negative control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
