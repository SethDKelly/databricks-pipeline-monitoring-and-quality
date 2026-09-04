#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CKR_B_IDS = (
    "foundation.product_definition",
    "foundation.actors_stakeholders",
    "foundation.terminology",
    "foundation.concept_design_method",
    "foundation.architectural_principles",
    "foundation.security_governance_policy",
    "foundation.ecosystem_lifecycles",
    "foundation.mvp_boundary",
    "reference.glossary",
)

HISTORY_ONLY = (
    "docs/foundation/009_initial_roadmap.md",
    "docs/foundation/010_open_questions.md",
    "docs/foundation/011_phase_006_exit_phase_007_handoff.md",
)

REQUIRED_ACTORS = (
    "Data engineer / pipeline maintainer",
    "Data platform engineer / platform operator",
    "Business analyst / data consumer",
    "Data owner",
    "Data steward / governance steward",
    "Security / privacy / compliance stakeholder",
    "Incident responder / on-call engineer",
    "Monitoring framework administrator",
)

REQUIRED_CONCEPT_DESIGN = (
    "Purpose",
    "Operational principle",
    "State",
    "Actions",
    "Invariants / behavioral expectations",
    "Synchronizations",
    "Failure / ambiguity behavior",
    "Vendor-shaped design",
    "Architecture-shaped design",
    "UI-shaped design",
    "Overconfident reasoning",
)

REQUIRED_NON_EQUIVALENCES = (
    "Observation ≠ Assessment",
    "Expectation ≠ Baseline",
    "Lineage ≠",
    "Capability Authorization",
    "Assertion Authority",
    "missing evidence",
    "current state ≠ historical",
    "passive monitoring ≠ active",
    "Execution Gate ≠ Propagation Safeguard",
)


def occurrences(text: str, token: str) -> int:
    return len(re.findall(rf"(?<![A-Za-z0-9-]){re.escape(token)}(?![A-Za-z0-9-])", text))


def require_sequence_headings(text: str, prefix: str, start: int, end: int, label: str, errors: list[str]) -> None:
    for number in range(start, end + 1):
        if not re.search(rf"^{re.escape(prefix)}\s+{number}\.\s", text, re.M):
            errors.append(f"{label}: missing numbered heading {number}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    inv_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    records = {r["record_id"]: r for r in inv.get("records", [])}

    actual = tuple(rid for rid, rec in records.items() if rec.get("migration_group") == "CKR-B")
    if set(actual) != set(CKR_B_IDS) or len(actual) != 9:
        errors.append(f"CKR-B must own exactly the nine accepted foundation/glossary records; found {sorted(actual)}")

    for rid in CKR_B_IDS:
        rec = records.get(rid)
        if not rec:
            errors.append(f"missing CKR-B record {rid}")
            continue
        state = rec.get("migration_state")
        if state not in {"candidate_ready", "canonicalized"}:
            errors.append(f"{rid}: CKR-B active/complete state must be candidate_ready or canonicalized, found {state!r}")
        legacy = repo / rec["current_owner"]
        target = repo / rec["target_owner"]
        if not legacy.is_file():
            errors.append(f"{rid}: legacy owner missing")
        if not target.is_file():
            errors.append(f"{rid}: canonical candidate/target missing")
            continue
        text = target.read_text(encoding="utf-8")
        expected_marker = "**Authority:** CANDIDATE / NOT CURRENT AUTHORITY" if state == "candidate_ready" else "**Authority:** CANONICAL CURRENT AUTHORITY"
        if expected_marker not in text:
            errors.append(f"{rid}: target authority marker does not match inventory state {state}")
        for required in (
            f"**Canonical key:** `{rid}`",
            f"**Migration record:** `{rid}`",
            "**Kind:**",
            "**Owns current question:**",
            "## Provenance",
        ):
            if required not in text:
                errors.append(f"{rid}: missing canonical metadata/section {required!r}")
        legacy_rel = rec["current_owner"]
        legacy_name = Path(legacy_rel).name
        if legacy_name not in text:
            errors.append(f"{rid}: provenance does not reference inventoried legacy owner {legacy_rel}")

    principles = (repo / records["foundation.architectural_principles"]["target_owner"]).read_text(encoding="utf-8")
    for number in range(1, 33):
        token = f"AP-{number:02d}"
        if occurrences(principles, token) != 1:
            errors.append(f"architectural principles: {token} must appear exactly once")

    security = (repo / records["foundation.security_governance_policy"]["target_owner"]).read_text(encoding="utf-8")
    for number in range(1, 16):
        token = f"SP-{number:02d}"
        if occurrences(security, token) != 1:
            errors.append(f"security governance: {token} must appear exactly once")

    lifecycles = (repo / records["foundation.ecosystem_lifecycles"]["target_owner"]).read_text(encoding="utf-8")
    require_sequence_headings(lifecycles, "##", 1, 14, "ecosystem lifecycles", errors)
    if "non-rewriting" not in lifecycles.lower() or "bitemporal" not in lifecycles.lower():
        errors.append("ecosystem lifecycles: must preserve non-rewriting and bitemporal history principles")

    mvp = (repo / records["foundation.mvp_boundary"]["target_owner"]).read_text(encoding="utf-8")
    require_sequence_headings(mvp, "###", 1, 13, "MVP required capabilities", errors)
    for letter in "ABCDEFGHIJK":
        if not re.search(rf"^### Scenario {letter} —", mvp, re.M):
            errors.append(f"MVP boundary: missing Scenario {letter}")
    for term in ("Collibra", "Immuta", "LLM", "graph database", "active control"):
        if term.lower() not in mvp.lower():
            errors.append(f"MVP boundary: optional/non-required boundary missing {term}")

    actors = (repo / records["foundation.actors_stakeholders"]["target_owner"]).read_text(encoding="utf-8")
    for actor in REQUIRED_ACTORS:
        if actor not in actors:
            errors.append(f"actors/stakeholders: missing actor role {actor}")

    method = (repo / records["foundation.concept_design_method"]["target_owner"]).read_text(encoding="utf-8")
    for phrase in REQUIRED_CONCEPT_DESIGN:
        if phrase not in method:
            errors.append(f"Concept Design method: missing required element {phrase}")

    terminology = (repo / records["foundation.terminology"]["target_owner"]).read_text(encoding="utf-8")
    glossary = (repo / records["reference.glossary"]["target_owner"]).read_text(encoding="utf-8")
    combined_terms = terminology + "\n" + glossary
    for phrase in REQUIRED_NON_EQUIVALENCES:
        if phrase.lower() not in combined_terms.lower():
            errors.append(f"terminology/glossary: missing critical boundary {phrase!r}")

    product = (repo / records["foundation.product_definition"]["target_owner"]).read_text(encoding="utf-8")
    if "understandable over time" not in product or "not" not in product.lower():
        errors.append("product definition: core purpose/product stance coverage missing")
    for phrase in ("Evidence", "Historical", "Lineage", "Governance", "Investigation", "Business analysis"):
        if phrase.lower() not in product.lower():
            errors.append(f"product definition: capability-family coverage missing {phrase}")

    for rel in HISTORY_ONLY:
        if not (repo / rel).is_file():
            errors.append(f"CKR-B historical source missing: {rel}")
    history_paths = {item.get("path") for item in inv.get("history_sources", [])}
    for rel in HISTORY_ONLY:
        if rel not in history_paths:
            errors.append(f"CKR-B history source not retained in ownership inventory: {rel}")

    # CKR-B must not preempt later semantic domains.
    for rid, rec in records.items():
        if rec.get("migration_group") == "CKR-C" and rec.get("migration_state") != "legacy_authoritative":
            errors.append(f"{rid}: CKR-C concept must remain legacy_authoritative during CKR-B")
    for family, item in inv.get("stable_families", {}).items():
        if item.get("migration_state") != "legacy_authoritative":
            errors.append(f"{family}: stable-ID family must remain legacy_authoritative during CKR-B")

    matrix = repo / "docs/canonical_knowledge_retrofit/ckr_b_semantic_conservation_matrix.md"
    review = repo / "docs/canonical_knowledge_retrofit/ckr_b_execution_review.md"
    fixture = repo / "docs/canonical_knowledge_retrofit/fixtures/ckr_b_foundation_scenarios.yaml"
    for path, label in ((matrix, "semantic conservation matrix"), (review, "execution review"), (fixture, "scenario fixture")):
        if not path.is_file():
            errors.append(f"missing CKR-B {label}")

    for error in errors:
        print(f"ERROR {error}")
    states = {records[rid].get("migration_state") for rid in CKR_B_IDS if rid in records}
    print(f"CKR-B foundation validation: {len(errors)} error(s), 9 record(s), states={sorted(states)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
