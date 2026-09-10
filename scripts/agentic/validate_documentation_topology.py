#!/usr/bin/env python3
"""Validate the durable post-DPTN documentation topology.

This is the small operational guard retained after DPTN exit. It validates current
routing/ownership structure and preserved DPTN provenance; it does not make DPTN
history current authority and it does not freeze future semantic content.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SEMANTIC_ROOTS = (
    "docs/concepts",
    "docs/architecture",
    "docs/authority",
    "docs/contracts",
    "docs/experience",
    "docs/invariants",
    "docs/policies",
    "docs/reference",
)
FORBIDDEN_CURRENT_PATHS = (
    "docs/canonical",
    "docs/documentation_topology_normalization",
    "docs/design_history",
    "docs/foundation",
    "docs/planning",
    "docs/decisions",
)
ROUTING_SURFACES = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/index.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
    "docs/agentic_development_foundation/README.md",
    "docs/agentic_development_foundation/context_discovery_policy.md",
    "docs/agentic_development_foundation/conformance_policy.md",
    "docs/canonical_knowledge_retrofit/README.md",
)
RETIRED_DPTN_TOOLING = (
    "validate_dptn_a_topology.py",
    "test_dptn_a_topology_guards.py",
    "validate_dptn_b_history.py",
    "test_dptn_b_history_guards.py",
    "validate_dptn_c_promotion.py",
    "test_dptn_c_promotion_guards.py",
    "validate_dptn_d_decomposition.py",
    "test_dptn_d_decomposition_guards.py",
    "validate_dptn_e_convergence.py",
    "test_dptn_e_convergence_guards.py",
    "validate_dptn_f_rebinding.py",
    "test_dptn_f_rebinding_guards.py",
    "validate_dptn_status.py",
)
ARCHIVE = Path("docs/history/retrofits/dptn")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    repo = Path(ap.parse_args().repo).resolve()
    errors: list[str] = []

    required = (
        "docs/index.md",
        "docs/README.md",
        "docs/history/README.md",
        "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json",
        "docs/agentic_development_foundation/stable_id_registry.json",
        "docs/routing/okf_projection.json",
        "knowledge/index.md",
        "knowledge/project/documentation-topology.md",
        "docs/implementation/README.md",
        str(ARCHIVE / "README.md"),
        str(ARCHIVE / "dptn_g_exit_manifest.json"),
        str(ARCHIVE / "dptn_g_execution_review.md"),
        str(ARCHIVE / "fixtures/dptn_g_exit_scenarios.yaml"),
        "docs/history/routing/canonical-compatibility-pre-dptn-g/README.md",
    )
    for rel in required:
        if not (repo / rel).is_file():
            errors.append(f"missing final-topology artifact: {rel}")

    for rel in FORBIDDEN_CURRENT_PATHS:
        p = repo / rel
        if p.exists() or p.is_symlink():
            errors.append(f"retired current path still exists: {rel}")

    for rel in SEMANTIC_ROOTS:
        p = repo / rel
        if not p.is_dir() or p.is_symlink():
            errors.append(f"current semantic owner root missing or redirected: {rel}")

    inventory_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    registry_path = repo / "docs/agentic_development_foundation/stable_id_registry.json"
    if inventory_path.is_file() and registry_path.is_file():
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        roots = inventory.get("canonical_owner_roots")
        if roots != list(SEMANTIC_ROOTS):
            errors.append(f"canonical_owner_roots drifted: {roots!r}")
        if inventory.get("canonical_root") != "docs" or inventory.get("canonical_layout") != "first_class_dptn_c":
            errors.append("ownership inventory no longer selects first-class docs topology")
        if inventory.get("concept_count") != 24:
            errors.append(f"accepted concept count drifted: {inventory.get('concept_count')}")
        families = registry.get("families", {})
        total = sum(int(v["max"]) - int(v["min"]) + 1 for v in families.values())
        if len(families) != 8 or total != 1237 or families.get("ARCH", {}).get("max") != 500:
            errors.append(f"stable-ID baseline drifted: families={len(families)}, ids={total}, ARCH={families.get('ARCH')}")
        for record in inventory.get("records", []):
            if record.get("migration_state") == "canonicalized":
                target = record.get("target_owner", "")
                if not target.startswith("docs/") or target.startswith("docs/history/") or target.startswith("docs/canonical/"):
                    errors.append(f"canonicalized record has non-current target: {record.get('record_id')} -> {target}")
                elif not (repo / target).is_file():
                    errors.append(f"canonicalized record target missing: {target}")
        for family, owner in inventory.get("stable_families", {}).items():
            if owner.get("migration_state") != "canonicalized":
                errors.append(f"stable family not canonicalized: {family}")
            for target in owner.get("target_documents", []):
                if target.startswith("docs/history/") or target.startswith("docs/canonical/") or not (repo / target).is_file():
                    errors.append(f"{family}: invalid current target document {target}")

    history = repo / "docs/history/README.md"
    if history.is_file():
        text = history.read_text(encoding="utf-8")
        if "HISTORY / PROVENANCE ONLY" not in text or "history/retrofits/dptn" not in text:
            errors.append("history index does not preserve DPTN as provenance-only")

    archive_readme = repo / ARCHIVE / "README.md"
    if archive_readme.is_file():
        text = archive_readme.read_text(encoding="utf-8")
        for token in ("DPTN EXIT: ACCEPTED", "HISTORY / PROVENANCE ONLY", "DPTN-G"):
            if token not in text:
                errors.append(f"DPTN archive README missing exit token {token!r}")

    manifest_path = repo / ARCHIVE / "dptn_g_exit_manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("phase") != "DPTN-G" or manifest.get("status") != "accepted" or manifest.get("authorized_move_ids") != ["MOVE-020"]:
            errors.append("DPTN-G archive manifest phase/status/move contract drifted")
        if manifest.get("semantic_change") is not False or manifest.get("implementation_change") is not False:
            errors.append("DPTN-G archive manifest claims semantic or implementation change")
        if manifest.get("exit_decision") != "accepted":
            errors.append("DPTN-G exit decision is not accepted")

    review = repo / ARCHIVE / "dptn_g_execution_review.md"
    if review.is_file() and "**Status:** ACCEPTED — DPTN EXIT ACCEPTED" not in review.read_text(encoding="utf-8"):
        errors.append("DPTN-G execution review does not record accepted exit")

    for name in RETIRED_DPTN_TOOLING:
        live = repo / "scripts/agentic" / name
        archived = repo / ARCHIVE / "tooling" / name
        if live.exists() or live.is_symlink():
            errors.append(f"retired phase-specific DPTN tooling still live: scripts/agentic/{name}")
        if not archived.is_file():
            errors.append(f"retired DPTN tooling not preserved in history: {archived.relative_to(repo)}")

    forbidden_route_tokens = ("docs/documentation_topology_normalization/", "docs/canonical/")
    for rel in ROUTING_SURFACES:
        p = repo / rel
        if not p.is_file():
            errors.append(f"missing current routing surface: {rel}")
            continue
        text = p.read_text(encoding="utf-8")
        for token in forbidden_route_tokens:
            if token in text:
                errors.append(f"{rel}: retired current routing token remains: {token}")

    impl = repo / "docs/implementation/README.md"
    if impl.is_file():
        text = impl.read_text(encoding="utf-8")
        if "Implementation 001-A — NEXT / READY / NOT STARTED" not in text:
            errors.append("Implementation 001-A was not released to NEXT / READY / NOT STARTED")
        if "Implementation 001-A — BLOCKED / NOT STARTED" in text or "Implementation 001-A — IN PROGRESS" in text:
            errors.append("Implementation 001-A has an invalid post-DPTN status")

    spec_path = repo / "docs/routing/okf_projection.json"
    if spec_path.is_file():
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        route = next((x for x in spec.get("project", []) if x.get("name") == "documentation-topology"), None)
        if not route or route.get("resource") != "docs/index.md" or "active DPTN" in route.get("description", ""):
            errors.append("generated OKF documentation-topology route still depends on active DPTN")

    generated_route = repo / "knowledge/project/documentation-topology.md"
    if generated_route.is_file():
        text = generated_route.read_text(encoding="utf-8")
        if 'resource: "../../docs/index.md"' not in text or "documentation_topology_normalization" in text:
            errors.append("generated documentation-topology entry is not rebound to docs/index.md")

    runner = repo / "scripts/agentic/run_conformance.py"
    if runner.is_file():
        text = runner.read_text(encoding="utf-8")
        if "validate_documentation_topology.py" not in text:
            errors.append("conformance runner does not retain final documentation-topology validation")
        if "validate_dptn_" in text or "test_dptn_" in text:
            errors.append("conformance runner still invokes retired phase-specific DPTN tooling")

    generator = repo / "scripts/agentic/generate_okf_projection.py"
    if generator.is_file():
        p = subprocess.run(
            [sys.executable, str(generator), "--repo", str(repo), "--check"],
            cwd=repo,
            text=True,
            capture_output=True,
        )
        if p.returncode:
            errors.append("generated OKF projection is not deterministic/current: " + (p.stdout + p.stderr).strip())

    for e in errors:
        print("ERROR", e)
    print(f"Final documentation topology validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
