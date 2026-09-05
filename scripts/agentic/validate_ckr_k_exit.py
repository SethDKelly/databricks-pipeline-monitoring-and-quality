#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

STATE_RE = re.compile(r"^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$", re.M)
ID_RE = re.compile(r"^(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})$")
FIXTURE_RE = re.compile(r"^\s*-\s+id:\s+(CKRK-\d{2})\s*$", re.M)
PHASE_RE = re.compile(r"phase_(\d{3})")
MIRRORS = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def state_map(repo: Path) -> dict[str, str]:
    text = (repo / "docs/canonical_knowledge_retrofit/README.md").read_text(encoding="utf-8")
    return {letter: state for letter, state in STATE_RE.findall(text)}


def canonical_marker(path: Path) -> bool:
    return path.is_file() and "**Authority:** CANONICAL CURRENT AUTHORITY" in path.read_text(encoding="utf-8", errors="ignore")


def provenance_mentions(text: str, source: str) -> bool:
    if source in text or Path(source).name in text:
        return True
    match = PHASE_RE.search(source)
    return bool(match and f"phase_{match.group(1)}" in text)


def run_resolver(repo: Path, stable_id: str) -> tuple[int, dict | None, str]:
    cmd = [sys.executable, str(repo / "scripts/agentic/resolve_stable_id.py"), stable_id, "--repo", str(repo), "--json"]
    proc = subprocess.run(cmd, cwd=repo, text=True, capture_output=True)
    if proc.returncode != 0:
        return proc.returncode, None, (proc.stdout + proc.stderr).strip()
    try:
        return 0, json.loads(proc.stdout), ""
    except json.JSONDecodeError as exc:
        return 1, None, f"invalid resolver JSON: {exc}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    manifest_path = repo / "docs/canonical_knowledge_retrofit/ckr_k_exit_manifest.json"
    inventory_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    registry_path = repo / "docs/agentic_development_foundation/stable_id_registry.json"
    routing_path = repo / "docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json"
    fixture_path = repo / "docs/canonical_knowledge_retrofit/fixtures/ckr_k_exit_scenarios.yaml"
    matrix_path = repo / "docs/canonical_knowledge_retrofit/ckr_k_consolidation_provenance_matrix.md"
    review_path = repo / "docs/canonical_knowledge_retrofit/ckr_k_execution_review.md"

    for path, label in (
        (manifest_path, "CKR-K exit manifest"),
        (inventory_path, "ownership inventory"),
        (registry_path, "stable-ID registry"),
        (routing_path, "CKR-J routing manifest"),
        (fixture_path, "CKR-K fixtures"),
        (matrix_path, "CKR-K conservation matrix"),
        (review_path, "CKR-K execution review"),
    ):
        if not path.is_file():
            errors.append(f"missing {label}: {path.relative_to(repo)}")
    if errors:
        for error in errors: print("ERROR", error)
        return 1

    try:
        manifest = load_json(manifest_path)
        inventory = load_json(inventory_path)
        registry = load_json(registry_path)
        routing = load_json(routing_path)
    except json.JSONDecodeError as exc:
        print(f"ERROR invalid CKR-K JSON input: {exc}")
        return 1

    states = state_map(repo)
    k_state = states.get("K")
    if k_state not in {"IN EXECUTION", "COMPLETE / ACCEPTED"}:
        errors.append(f"CKR-K validator requires CKR-K IN EXECUTION or COMPLETE / ACCEPTED; found {k_state!r}")
    for letter in "ABCDEFGHIJ":
        if states.get(letter) != "COMPLETE / ACCEPTED":
            errors.append(f"CKR-{letter} must remain COMPLETE / ACCEPTED during CKR-K; found {states.get(letter)!r}")

    status = manifest.get("status")
    expected_status = "accepted" if k_state == "COMPLETE / ACCEPTED" else "candidate_ready"
    if status != expected_status:
        errors.append(f"CKR-K manifest status must be {expected_status!r} for state {k_state!r}; found {status!r}")
    if manifest.get("schema_version") != "1.0" or manifest.get("phase") != "CKR-K":
        errors.append("CKR-K manifest schema/phase drifted")
    purpose = manifest.get("purpose", "").lower()
    if "does not own dmtz product semantics" not in purpose:
        errors.append("CKR-K manifest must remain explicitly non-semantic")

    counts = manifest.get("expected_counts", {})
    expected_counts = {
        "ownership_records": 34, "concept_records": 24, "stable_families": 8,
        "stable_ids": 1237, "architecture_segments": 9, "okf_semantic_routes": 7,
        "prior_ckr_groups": 10, "ckr_k_scenarios": 36, "ckr_k_negative_controls": 14,
    }
    if counts != expected_counts:
        errors.append(f"CKR-K expected_counts drifted: {counts}")

    records = inventory.get("records", [])
    concepts = [r for r in records if r.get("kind") == "concept"]
    families = inventory.get("stable_families", {})
    segments = inventory.get("architecture_segments", [])
    if len(records) != 34: errors.append(f"ownership record count must remain 34; found {len(records)}")
    if len(concepts) != 24: errors.append(f"concept record count must remain 24; found {len(concepts)}")
    if len(families) != 8: errors.append(f"stable family count must remain 8; found {len(families)}")
    if len(segments) != 9: errors.append(f"architecture inventory record count must remain 9; found {len(segments)}")

    for record in records:
        rid = record.get("record_id", "<unknown>")
        if record.get("migration_state") != "canonicalized":
            errors.append(f"{rid}: CKR exit requires canonicalized record state")
        source = record.get("current_owner")
        target = record.get("target_owner")
        if not source or not (repo / source).is_file():
            errors.append(f"{rid}: historical source missing: {source!r}")
            continue
        if not target or not target.startswith("docs/canonical/") or not canonical_marker(repo / target):
            errors.append(f"{rid}: canonical target missing/current-authority marker invalid: {target!r}")
            continue
        source_text = (repo / source).read_text(encoding="utf-8", errors="ignore")
        if "**Authority:** CANONICAL CURRENT AUTHORITY" in source_text:
            errors.append(f"{rid}: legacy source claims canonical current authority")
        target_text = (repo / target).read_text(encoding="utf-8", errors="ignore")
        if "## Provenance" not in target_text:
            errors.append(f"{rid}: canonical target lacks explicit Provenance section")
        elif not provenance_mentions(target_text, source):
            errors.append(f"{rid}: canonical provenance does not retain original source identity {source}")

    total_ids = 0
    for family, limits in registry.get("families", {}).items():
        low, high = int(limits.get("min", 0)), int(limits.get("max", -1))
        total_ids += max(0, high - low + 1)
        item = families.get(family, {})
        if item.get("migration_state") != "canonicalized":
            errors.append(f"{family}: CKR exit requires canonicalized stable family")
        source_root = item.get("current_owner_root")
        if not source_root or not (repo / source_root).exists():
            errors.append(f"{family}: historical stable-family root missing: {source_root!r}")
        phase = PHASE_RE.search(source_root or "")
        phase_token = f"phase_{phase.group(1)}" if phase else None
        for target in item.get("target_documents", []):
            path = repo / target
            if not canonical_marker(path):
                errors.append(f"{family}: canonical target invalid: {target}")
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "## Provenance" not in text:
                errors.append(f"{family}: {target} lacks explicit Provenance section")
            elif phase_token and phase_token not in text:
                errors.append(f"{family}: {target} does not retain {phase_token} provenance")
    if total_ids != 1237:
        errors.append(f"accepted stable-ID total must remain 1237; found {total_ids}")

    for segment in segments:
        rid = segment.get("record_id", "<unknown-architecture>")
        if segment.get("migration_state") != "canonicalized":
            errors.append(f"{rid}: CKR exit requires canonicalized architecture inventory state")
        source = segment.get("current_owner")
        target = segment.get("target_owner")
        if not source or not (repo / source).is_file():
            errors.append(f"{rid}: historical architecture source missing")
        if not target or not canonical_marker(repo / target):
            errors.append(f"{rid}: canonical architecture target invalid")
        else:
            text = (repo / target).read_text(encoding="utf-8", errors="ignore")
            if "## Provenance" not in text or "phase_010" not in text:
                errors.append(f"{rid}: architecture target must retain explicit Phase 010 provenance")

    prior = manifest.get("prior_execution_reviews", [])
    if len(prior) != 10:
        errors.append(f"CKR-K must bind exactly ten prior CKR execution reviews; found {len(prior)}")
    for rel in prior:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing prior CKR execution review {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "ACCEPTED" not in text:
            errors.append(f"prior CKR execution review is not accepted: {rel}")

    design_history = repo / manifest.get("design_history_index", "")
    if not design_history.is_file():
        errors.append("design-history index missing")
    else:
        history_text = design_history.read_text(encoding="utf-8", errors="ignore")
        for token in ("PROVENANCE / RATIONALE / HISTORICAL DESIGN RECORD", "Current-truth rule", "Preservation rule"):
            if token not in history_text:
                errors.append(f"design-history index lost required role marker {token!r}")

    if registry.get("status") != "accepted_canonical_resolution":
        errors.append("stable-ID registry must remain accepted_canonical_resolution")
    resolution = registry.get("resolution", {})
    if resolution.get("mode") != "canonical_target_stable_definition" or resolution.get("history_discovery") != "explicit_separate_on_demand":
        errors.append("stable-ID canonical/history resolution boundary drifted")

    if routing.get("status") != "active":
        errors.append("CKR-J routing manifest must remain active at CKR exit")
    routes = routing.get("okf_semantic_routes", [])
    if len(routes) != 7:
        errors.append(f"CKR exit requires seven semantic OKF routes; found {len(routes)}")
    for route in routes:
        primary = route.get("primary_resource", "")
        if not primary.startswith("docs/canonical/") or not (repo / primary).exists():
            errors.append(f"noncanonical/missing current OKF primary route: {route.get('path')} -> {primary}")

    for rel in manifest.get("representative_current_resources", []):
        if not canonical_marker(repo / rel):
            errors.append(f"representative current resource is not canonical current authority: {rel}")

    for stable_id in manifest.get("representative_stable_ids", []):
        if not ID_RE.match(stable_id):
            errors.append(f"invalid representative stable ID {stable_id!r}")
            continue
        code, payload, detail = run_resolver(repo, stable_id)
        if code != 0 or payload is None:
            errors.append(f"{stable_id}: representative canonical resolution failed: {detail}")
            continue
        locator = payload.get("canonical_locator", "")
        owner = payload.get("canonical_owner", {}).get("path", "")
        if not locator.endswith(f"::{stable_id}") or not owner.startswith("docs/canonical/"):
            errors.append(f"{stable_id}: representative lookup did not terminate in canonical owner: {locator!r}")
        if "history_occurrences" in payload:
            errors.append(f"{stable_id}: default canonical lookup unexpectedly mixed history occurrences")

    scan_paths = [repo / route.get("path", "") for route in routes]
    scan_paths += [repo / rel for rel in MIRRORS]
    for path in scan_paths:
        if not path.is_file():
            errors.append(f"missing live routing/status surface {path.relative_to(repo)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in manifest.get("forbidden_live_patterns", []):
            if pattern in text:
                errors.append(f"{path.relative_to(repo)} retains forbidden pre-cutover current-routing text {pattern!r}")

    inventory_status = inventory.get("status")
    matrix_text = matrix_path.read_text(encoding="utf-8", errors="ignore")
    review_text = review_path.read_text(encoding="utf-8", errors="ignore")
    if k_state == "IN EXECUTION":
        if inventory_status == manifest.get("inventory_final_status"):
            errors.append("inventory lifecycle cannot become ckr_complete before CKR-K acceptance")
        if "**Status:** CANDIDATE — CKR-K IN EXECUTION" not in matrix_text:
            errors.append("CKR-K matrix must remain candidate while CKR-K is in execution")
        if "**Status:** IN EXECUTION" not in review_text:
            errors.append("CKR-K execution review must remain in execution before acceptance")
        for rel in MIRRORS:
            text = (repo / rel).read_text(encoding="utf-8", errors="ignore")
            if "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT" not in text:
                errors.append(f"{rel}: Implementation 001-A was released before CKR-K acceptance")
    elif k_state == "COMPLETE / ACCEPTED":
        if inventory_status != manifest.get("inventory_final_status"):
            errors.append(f"accepted CKR-K requires inventory status {manifest.get('inventory_final_status')!r}; found {inventory_status!r}")
        if "**Status:** ACCEPTED — CKR-K COMPLETE" not in matrix_text:
            errors.append("accepted CKR-K requires accepted conservation matrix")
        if "**Status:** ACCEPTED — CKR-K COMPLETE" not in review_text:
            errors.append("accepted CKR-K requires accepted execution review")
        implementation = (repo / "docs/implementation/README.md").read_text(encoding="utf-8", errors="ignore")
        if "Implementation 001-A — NEXT / READY / NOT STARTED" not in implementation:
            errors.append("accepted CKR-K must release Implementation 001-A to NEXT / READY / NOT STARTED")
        for rel in MIRRORS:
            text = (repo / rel).read_text(encoding="utf-8", errors="ignore")
            if "IMPLEMENTATION 001-A BLOCKED ON CKR EXIT" in text:
                errors.append(f"{rel}: stale implementation block remains after CKR exit acceptance")

    fixture_ids = FIXTURE_RE.findall(fixture_path.read_text(encoding="utf-8"))
    expected_fixture_ids = [f"CKRK-{i:02d}" for i in range(1, 37)]
    if fixture_ids != expected_fixture_ids:
        errors.append("CKR-K fixture catalog must contain CKRK-01..CKRK-36 exactly once and in order")

    for error in errors: print("ERROR", error)
    print(
        f"CKR-K exit validation: {len(errors)} error(s), records={len(records)}/34, concepts={len(concepts)}/24, "
        f"families={len(families)}/8, stable_ids={total_ids}/1237, architecture_records={len(segments)}/9, "
        f"routes={len(routes)}/7, representative_ids={len(manifest.get('representative_stable_ids', []))}, state={status}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
