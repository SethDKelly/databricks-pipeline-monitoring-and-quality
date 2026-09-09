#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = "docs/documentation_topology_normalization"
PHASES = ["DPTN-B", "DPTN-C", "DPTN-D", "DPTN-E", "DPTN-F", "DPTN-G"]
CURRENT_CANONICAL = {
    "docs/canonical/concepts/**": "docs/concepts/**",
    "docs/canonical/architecture/**": "docs/architecture/**",
    "docs/canonical/authority/**": "docs/authority/**",
    "docs/canonical/contracts/**": "docs/contracts/**",
    "docs/canonical/experience/**": "docs/experience/**",
    "docs/canonical/invariants/**": "docs/invariants/**",
    "docs/canonical/policies/**": "docs/policies/**",
    "docs/canonical/reference/**": "docs/reference/**",
}
HISTORY_SOURCES = {
    "docs/concepts/**",
    "docs/foundation/**",
    "docs/reference/**",
    "docs/planning/**",
    "docs/decisions/**",
    "docs/design_history/**",
}
MIXED = {"docs/canonical_knowledge_retrofit/**", "docs/agentic_development_foundation/**"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    required = [
        f"{ROOT}/README.md",
        f"{ROOT}/topology_authority.md",
        f"{ROOT}/topology_inventory.json",
        f"{ROOT}/move_map.json",
        f"{ROOT}/collision_register.md",
        f"{ROOT}/dptn_a_execution_review.md",
        f"{ROOT}/fixtures/dptn_a_topology_scenarios.yaml",
    ]
    for rel in required:
        if not (repo / rel).is_file():
            errors.append(f"missing DPTN-A artifact: {rel}")

    if errors:
        for e in errors: print("ERROR", e)
        return 1

    readme = (repo / ROOT / "README.md").read_text(encoding="utf-8")
    inventory = load_json(repo / ROOT / "topology_inventory.json")
    moves = load_json(repo / ROOT / "move_map.json")
    collisions = (repo / ROOT / "collision_register.md").read_text(encoding="utf-8")
    fixtures = (repo / ROOT / "fixtures/dptn_a_topology_scenarios.yaml").read_text(encoding="utf-8")
    ckr = load_json(repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json")
    stable = load_json(repo / "docs/agentic_development_foundation/stable_id_registry.json")

    if ckr.get("status") != "ckr_complete" or ckr.get("canonical_root") not in {"docs/canonical","docs"}:
        errors.append("DPTN-A requires accepted CKR completion with a recognized pre/post-normalization canonical root")
    if ckr.get("canonical_root")=="docs" and ckr.get("canonical_layout")!="first_class_dptn_c":
        errors.append("normalized CKR root requires the DPTN-C first-class layout marker")

    total = sum(int(v["max"]) - int(v["min"]) + 1 for v in stable.get("families", {}).values())
    counts = inventory.get("accepted_counts", {})
    if total != 1237 or counts.get("stable_ids") != 1237:
        errors.append(f"accepted stable-ID total must remain 1237; registry={total}, inventory={counts.get('stable_ids')}")
    if counts.get("concepts") != 24 or ckr.get("concept_count") != 24:
        errors.append("accepted concept count must remain 24")
    if counts.get("architecture_ids") != 500:
        errors.append("accepted architecture-ID count must remain 500")

    rows = inventory.get("inventory", [])
    by_source = {r.get("source"): r for r in rows}
    if len(by_source) != len(rows):
        errors.append("topology inventory source rules must be unique")

    for src, target in CURRENT_CANONICAL.items():
        row = by_source.get(src)
        if not row:
            errors.append(f"missing current canonical inventory rule: {src}")
        elif row.get("target") != target or row.get("phase") != "DPTN-C" or row.get("role") != "current_semantic_authority":
            errors.append(f"invalid current canonical promotion rule: {src}")

    for src in HISTORY_SOURCES:
        row = by_source.get(src)
        if not row or row.get("role") != "history_provenance" or row.get("phase") != "DPTN-B":
            errors.append(f"history source must be explicitly assigned to DPTN-B: {src}")

    for src in MIXED:
        row = by_source.get(src)
        if not row or row.get("role") != "mixed_lifecycle" or row.get("phase") != "DPTN-D" or row.get("action") != "file_level_decomposition_required":
            errors.append(f"mixed lifecycle source must require DPTN-D file-level decomposition: {src}")

    if inventory.get("explicit_exclusions") is None or "semantic contract content changes" not in inventory.get("explicit_exclusions", []):
        errors.append("inventory must explicitly exclude semantic contract changes")

    if moves.get("physical_moves_authorized") is not False:
        errors.append("DPTN-A move map must remain a planning ledger rather than general physical-move authorization")
    if moves.get("dependency_order") != PHASES:
        errors.append(f"DPTN dependency order must be {PHASES}")

    move_rows = moves.get("moves", [])
    ids = [m.get("id") for m in move_rows]
    expected_ids = [f"MOVE-{i:03d}" for i in range(1, 21)]
    if ids != expected_ids:
        errors.append("move map must contain ordered MOVE-001..MOVE-020 exactly once")

    move_by_source = {m.get("source"): m for m in move_rows}
    if move_by_source.get("docs/canonical/concepts/**", {}).get("requires") != ["MOVE-001"]:
        errors.append("canonical concepts promotion must require historical concepts relocation")
    if move_by_source.get("docs/canonical/reference/**", {}).get("requires") != ["MOVE-002"]:
        errors.append("canonical reference promotion must require legacy reference relocation")
    if move_by_source.get("docs/canonical_knowledge_retrofit/**", {}).get("action") != "decompose_file_by_file":
        errors.append("CKR bulk move must remain forbidden")
    if move_by_source.get("docs/agentic_development_foundation/**", {}).get("action") != "decompose_file_by_file":
        errors.append("ADF bulk move must remain forbidden")

    collision_ids = re.findall(r"COL-\d{3}", collisions)
    if sorted(set(collision_ids)) != [f"COL-{i:03d}" for i in range(1, 14)]:
        errors.append("collision register must contain COL-001..COL-013")

    fixture_ids = re.findall(r"id: (DPTNA-\d{2})", fixtures)
    if fixture_ids != [f"DPTNA-{i:02d}" for i in range(1, 25)]:
        errors.append("DPTN-A fixture catalog must contain DPTNA-01..DPTNA-24 in order")

    a_complete = "DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED" in readme
    later_active = bool(re.search(r"DPTN-[B-G].*?(IN EXECUTION|COMPLETE / ACCEPTED)", readme))
    if not later_active:
        for src in CURRENT_CANONICAL:
            path = repo / src[:-3]
            if not path.is_dir():
                errors.append(f"DPTN-A planning phase may not move current canonical subtree: {src}")
        if (repo / "docs/history").exists():
            errors.append("docs/history must not be physically created during DPTN-A planning-only execution")

    if "Implementation 001-A remains blocked until DPTN-G" not in readme:
        errors.append("DPTN authority must block Implementation 001-A until DPTN-G exit")

    status = inventory.get("status")
    move_status = moves.get("status")
    fixture_status = re.search(r"^status: (\S+)", fixtures, re.M)
    fixture_status = fixture_status.group(1) if fixture_status else None
    if a_complete:
        if (status, move_status, fixture_status) != ("accepted", "accepted", "accepted"):
            errors.append("accepted DPTN-A requires accepted inventory, move map and fixture statuses")
    else:
        if (status, move_status, fixture_status) != ("candidate_ready", "candidate_ready", "candidate_ready"):
            errors.append("in-execution DPTN-A requires candidate_ready artifact statuses")

    for error in errors:
        print("ERROR", error)
    print(f"DPTN-A topology validation: {len(errors)} error(s), inventory_rules={len(rows)}, moves={len(move_rows)}, collisions=13, scenarios=24, stable_ids={total}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
