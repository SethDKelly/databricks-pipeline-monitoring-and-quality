#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ALLOWED_STATES = {"legacy_authoritative", "candidate_ready", "canonicalized", "history_only"}
REQUIRED_CANONICAL_INDEXES = (
    "docs/canonical/README.md",
    "docs/canonical/concepts/README.md",
    "docs/canonical/contracts/README.md",
    "docs/canonical/policies/README.md",
    "docs/canonical/invariants/README.md",
    "docs/canonical/authority/README.md",
    "docs/canonical/experience/README.md",
    "docs/canonical/architecture/README.md",
    "docs/canonical/reference/README.md",
)
RANGE_RE = re.compile(r"^([A-Z]+)-(\d{3})\.\.\1-(\d{3})$")


def is_under(path: str, root: str) -> bool:
    p = Path(path)
    r = Path(root)
    try:
        p.relative_to(r)
        return True
    except ValueError:
        return False


def authority_marker(path: Path) -> str | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "**Authority:** CANONICAL CURRENT AUTHORITY" in text:
        return "canonical"
    if "**Authority:** CANDIDATE / NOT CURRENT AUTHORITY" in text:
        return "candidate"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    inv_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    if not inv_path.is_file():
        print("ERROR missing canonical ownership inventory")
        return 1

    try:
        inv = json.loads(inv_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR invalid canonical ownership inventory JSON: {exc}")
        return 1

    if inv.get("schema_version") != "1.0":
        errors.append("canonical ownership inventory schema_version must be 1.0")
    if set(inv.get("allowed_states", [])) != ALLOWED_STATES:
        errors.append("canonical ownership inventory allowed_states does not match CKR migration contract")
    if inv.get("canonical_root") != "docs/canonical":
        errors.append("canonical_root must be docs/canonical")

    for rel in REQUIRED_CANONICAL_INDEXES:
        if not (repo / rel).is_file():
            errors.append(f"missing canonical structural index: {rel}")

    for rel in (
        "docs/design_history/README.md",
        "docs/canonical_knowledge_retrofit/authority_model.md",
        "docs/canonical_knowledge_retrofit/migration_contract.md",
        "docs/canonical_knowledge_retrofit/canonical_document_template.md",
    ):
        if not (repo / rel).is_file():
            errors.append(f"missing CKR authority artifact: {rel}")

    records = inv.get("records", [])
    seen_ids: set[str] = set()
    seen_targets: set[str] = set()
    concept_records = 0

    for rec in records:
        rid = rec.get("record_id")
        state = rec.get("migration_state")
        current = rec.get("current_owner")
        target = rec.get("target_owner")
        if not rid or rid in seen_ids:
            errors.append(f"invalid or duplicate ownership record_id: {rid!r}")
            continue
        seen_ids.add(rid)
        if state not in ALLOWED_STATES:
            errors.append(f"{rid}: invalid migration_state {state!r}")
        if rec.get("kind") == "concept":
            concept_records += 1
        if state in {"legacy_authoritative", "candidate_ready", "canonicalized"}:
            if not current or not (repo / current).is_file():
                errors.append(f"{rid}: current_owner missing or not a file: {current!r}")
            if not target or not is_under(target, "docs/canonical"):
                errors.append(f"{rid}: target_owner must be under docs/canonical: {target!r}")
            elif target in seen_targets:
                errors.append(f"{rid}: duplicate target_owner {target}")
            else:
                seen_targets.add(target)

        target_path = repo / target if target else None
        marker = authority_marker(target_path) if target_path else None
        if state == "legacy_authoritative" and marker == "canonical":
            errors.append(f"{rid}: legacy_authoritative record has target claiming canonical authority")
        elif state == "candidate_ready":
            if not target_path or not target_path.is_file():
                errors.append(f"{rid}: candidate_ready target is missing")
            elif marker != "candidate":
                errors.append(f"{rid}: candidate_ready target must declare CANDIDATE / NOT CURRENT AUTHORITY")
        elif state == "canonicalized":
            if not target_path or not target_path.is_file():
                errors.append(f"{rid}: canonicalized target is missing")
            elif marker != "canonical":
                errors.append(f"{rid}: canonicalized target must declare CANONICAL CURRENT AUTHORITY")

    if concept_records != inv.get("concept_count") or concept_records != 24:
        errors.append(f"concept inventory must contain exactly 24 concepts; found {concept_records}")

    registry_path = repo / "docs/agentic_development_foundation/stable_id_registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    families = inv.get("stable_families", {})
    if set(families) != set(registry.get("families", {})):
        errors.append("stable_families must cover exactly the accepted stable-ID registry families")
    for family, limits in registry.get("families", {}).items():
        item = families.get(family, {})
        expected_range = f"{family}-{limits['min']:03d}..{family}-{limits['max']:03d}"
        if item.get("accepted_range") != expected_range:
            errors.append(f"{family}: accepted_range must be {expected_range}")
        if item.get("migration_state") not in ALLOWED_STATES:
            errors.append(f"{family}: invalid migration_state")
        current_root = item.get("current_owner_root")
        target_root = item.get("target_owner_root")
        if not current_root or not (repo / current_root).exists():
            errors.append(f"{family}: current_owner_root missing: {current_root!r}")
        if not target_root or not is_under(target_root, "docs/canonical"):
            errors.append(f"{family}: target_owner_root must be under docs/canonical")

    arch_segments = inv.get("architecture_segments", [])
    covered: list[tuple[int, int]] = []
    for segment in arch_segments:
        state = segment.get("migration_state")
        if state not in ALLOWED_STATES:
            errors.append(f"{segment.get('record_id')}: invalid architecture migration_state")
        current = segment.get("current_owner")
        target = segment.get("target_owner")
        if not current or not (repo / current).is_file():
            errors.append(f"{segment.get('record_id')}: missing architecture current_owner")
        if not target or not is_under(target, "docs/canonical/architecture"):
            errors.append(f"{segment.get('record_id')}: architecture target must be under docs/canonical/architecture")
        raw_range = segment.get("range")
        if raw_range:
            match = RANGE_RE.match(raw_range)
            if not match or match.group(1) != "ARCH":
                errors.append(f"{segment.get('record_id')}: invalid ARCH range {raw_range!r}")
            else:
                covered.append((int(match.group(2)), int(match.group(3))))

    if sorted(covered) != [(1, 32), (33, 80), (81, 132), (133, 190), (191, 274), (275, 350), (351, 420), (421, 500)]:
        errors.append(f"architecture segment coverage must exactly partition ARCH-001..ARCH-500; found {sorted(covered)}")

    for item in inv.get("history_sources", []):
        path = item.get("path")
        if not path or not (repo / path).exists():
            errors.append(f"design-history source missing: {path!r}")

    canonical_root = repo / "docs/canonical"
    structural = {(repo / rel).resolve() for rel in REQUIRED_CANONICAL_INDEXES}
    declared_targets = {(repo / p).resolve() for p in seen_targets}
    declared_targets.update((repo / seg.get("target_owner")).resolve() for seg in arch_segments if seg.get("target_owner"))
    for path in canonical_root.rglob("*.md"):
        resolved = path.resolve()
        if resolved in structural:
            continue
        if resolved not in declared_targets:
            errors.append(f"unregistered substantive canonical document: {path.relative_to(repo)}")

    for error in errors:
        print(f"ERROR {error}")
    canonicalized = sum(1 for r in records if r.get("migration_state") == "canonicalized")
    candidates = sum(1 for r in records if r.get("migration_state") == "candidate_ready")
    print(
        "Canonical knowledge validation: "
        f"{len(errors)} error(s), {len(records)} ownership record(s), "
        f"{concept_records} concept(s), {canonicalized} canonicalized, {candidates} candidate(s)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
