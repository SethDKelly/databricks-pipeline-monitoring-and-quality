#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path("docs/documentation_topology_normalization")
MIRRORS = (
    "AGENTS.md",
    "IMPLEMENTATION.md",
    "docs/implementation/README.md",
    "docs/implementation/AGENTS.md",
    "docs/implementation/agent_reference_index.md",
    ".cursor/rules/00-implementation-routing.mdc",
)
EXPECTED_CANONICAL = {
    "canonical.architecture": "docs/architecture/",
    "canonical.authority": "docs/authority/",
    "canonical.concepts": "docs/concepts/",
    "canonical.contracts": "docs/contracts/",
    "canonical.experience": "docs/experience/",
    "canonical.invariants": "docs/invariants/",
    "canonical.policies": "docs/policies/",
    "canonical.reference": "docs/reference/",
}
EXPECTED_PHASES = {f"history.phase-{n:03d}" for n in range(2, 11)}
EXPECTED_STABLE = {
    "SYN": "SYN-001..SYN-035",
    "REF": "REF-001..REF-030",
    "AUTH": "AUTH-001..AUTH-053",
    "HLTH": "HLTH-001..HLTH-066",
    "OPS": "OPS-001..OPS-123",
    "EXPL": "EXPL-001..EXPL-160",
    "INTG": "INTG-001..INTG-270",
    "ARCH": "ARCH-001..ARCH-500",
}
EXPECTED_FIXED = {
    "docs.root-index","docs.phase-status","canonical.index",
    "history.foundation","history.planning","history.reference-legacy",
    "decisions.current","history.logical-index","ckr.program","adf.program",
    "implementation.current","okf.domains","okf.implementation","okf.project",
    "okf.workflows","okf.index","okf.log","agent.root","implementation.root",
    "agent.skills","cursor.rules","claude.adapter","agentic.scripts",
}
FIXTURE_RE = re.compile(r"^\s*-\s+id:\s*(DPTNA-\d+)\s*$", re.M)
STATE_RE = re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$", re.M)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    root = repo / ROOT
    errors: list[str] = []

    required = (
        "README.md","topology_authority.md","topology_inventory.json",
        "move_map.json","target_topology.md","dptn_a_execution_review.md",
        "fixtures/dptn_a_topology_scenarios.yaml",
    )
    for name in required:
        if not (root / name).is_file():
            errors.append(f"missing DPTN-A artifact: {ROOT / name}")
    if errors:
        for e in errors: print("ERROR", e)
        return 1

    readme = (root / "README.md").read_text(encoding="utf-8")
    authority = (root / "topology_authority.md").read_text(encoding="utf-8")
    inventory = json.loads((root / "topology_inventory.json").read_text(encoding="utf-8"))
    move_map = json.loads((root / "move_map.json").read_text(encoding="utf-8"))
    review = (root / "dptn_a_execution_review.md").read_text(encoding="utf-8")
    fixtures = (root / "fixtures/dptn_a_topology_scenarios.yaml").read_text(encoding="utf-8")

    for marker in (
        "does not reopen any accepted semantic or architecture decision",
        "must not create a new permanent semantic registry",
        "DPTN-A physical-change prohibition",
    ):
        if marker not in authority:
            errors.append(f"topology authority missing invariant marker: {marker!r}")

    states = dict(STATE_RE.findall(readme))
    if states.get("A") not in {"IN EXECUTION", "COMPLETE / ACCEPTED"}:
        errors.append(f"DPTN-A state must be IN EXECUTION or COMPLETE / ACCEPTED; found {states.get('A')!r}")
    a_complete = states.get("A") == "COMPLETE / ACCEPTED"
    b_state = states.get("B")
    if a_complete and b_state != "NEXT / READY / NOT STARTED":
        errors.append(f"accepted DPTN-A must hand off to DPTN-B NEXT / READY / NOT STARTED; found {b_state!r}")
    if not a_complete and b_state != "PLANNED":
        errors.append(f"in-execution DPTN-A must leave DPTN-B PLANNED; found {b_state!r}")

    surfaces = inventory.get("surfaces", [])
    ids = [s.get("surface_id") for s in surfaces]
    if len(ids) != len(set(ids)):
        errors.append("topology inventory contains duplicate surface_id values")
    by_id = {s.get("surface_id"): s for s in surfaces}
    expected = set(EXPECTED_CANONICAL) | EXPECTED_PHASES | EXPECTED_FIXED
    missing = sorted(expected - set(by_id))
    if missing:
        errors.append(f"topology inventory missing required surfaces: {missing}")
    if len(surfaces) != 40:
        errors.append(f"topology inventory must contain exactly 40 file/root surfaces for DPTN-A baseline; found {len(surfaces)}")

    allowed_coverage = {"file","recursive_root"}
    for s in surfaces:
        sid = s.get("surface_id")
        if s.get("coverage") not in allowed_coverage:
            errors.append(f"{sid}: invalid coverage {s.get('coverage')!r}")
        source = str(s.get("source","")).rstrip("/")
        if source and not (repo / source).exists():
            errors.append(f"{sid}: baseline source missing during DPTN-A: {source}")

    for sid, target in EXPECTED_CANONICAL.items():
        s = by_id.get(sid, {})
        if s.get("current_role") != "current_semantic_authority":
            errors.append(f"{sid}: canonical family lost current_semantic_authority role")
        if s.get("planned_target") != target or s.get("planned_group") != "DPTN-C":
            errors.append(f"{sid}: unexpected first-class target/group")

    if by_id.get("canonical.concepts",{}).get("collision") != "target_occupied":
        errors.append("docs/concepts collision is not explicitly recorded")
    if by_id.get("canonical.reference",{}).get("collision") != "target_occupied":
        errors.append("docs/reference collision is not explicitly recorded")
    for sid in ("ckr.program","adf.program"):
        s = by_id.get(sid,{})
        if s.get("current_role") != "mixed_requires_split" or s.get("planned_target") != "SPLIT":
            errors.append(f"{sid}: mixed current/history directory must require explicit split")

    ckr_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    ckr = json.loads(ckr_path.read_text(encoding="utf-8"))
    if ckr.get("status") != "ckr_complete" or ckr.get("canonical_root") != "docs/canonical":
        errors.append("CKR authority baseline changed during DPTN-A")
    if ckr.get("concept_count") != 24:
        errors.append("accepted concept count changed during DPTN-A")
    stable = ckr.get("stable_families", {})
    for fam, accepted in EXPECTED_STABLE.items():
        if stable.get(fam, {}).get("accepted_range") != accepted:
            errors.append(f"{fam}: accepted stable range changed during DPTN-A")

    operations = move_map.get("operations", [])
    op_ids = [o.get("operation_id") for o in operations]
    if len(op_ids) != len(set(op_ids)):
        errors.append("move map contains duplicate operation_id values")
    if len(operations) != 33:
        errors.append(f"move map must contain exactly 33 DPTN-B–G operations; found {len(operations)}")
    for op in operations:
        oid = op.get("operation_id")
        for key in ("group","sources","targets","operation_kind","atomicity"):
            if not op.get(key):
                errors.append(f"{oid}: missing move-map field {key}")
    move_by_id = {o.get("operation_id"): o for o in operations}
    if "docs/concepts/ phase corpus has been relocated by DPTN-B" not in move_by_id.get("C-PROMOTE-CONCEPTS",{}).get("preconditions",[]):
        errors.append("concept promotion lacks history-first collision precondition")
    if "legacy docs/reference/ has been relocated by DPTN-B" not in move_by_id.get("C-PROMOTE-REFERENCE",{}).get("preconditions",[]):
        errors.append("reference promotion lacks history-first collision precondition")
    if move_by_id.get("D-CKR-HISTORY",{}).get("atomicity") != "root_filtered_atomic":
        errors.append("CKR history move must be filtered, never recursive bulk move")
    if move_by_id.get("D-ADF-HISTORY",{}).get("atomicity") != "explicit_set_atomic":
        errors.append("ADF history move must use an explicit set")

    b_started = b_state not in {None, "PLANNED", "NEXT / READY / NOT STARTED"}
    if not b_started:
        future_absent = (
            "docs/history","docs/index.md","docs/agentic",
            "docs/architecture","docs/contracts","docs/experience",
            "docs/invariants","docs/policies",
        )
        for rel in future_absent:
            if (repo / rel).exists():
                errors.append(f"premature DPTN physical target exists before DPTN-B execution: {rel}")
        if "NO OPERATIONS AUTHORIZED" not in str(move_map.get("status","")):
            errors.append("DPTN-A move map must explicitly keep operations unauthorized")

    fixture_ids = FIXTURE_RE.findall(fixtures)
    expected_fixture_ids = [f"DPTNA-{n:02d}" for n in range(1,25)]
    if fixture_ids != expected_fixture_ids:
        errors.append(f"DPTN-A fixture identities must be DPTNA-01..DPTNA-24 exactly; found {fixture_ids}")

    if a_complete:
        mirror = "DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT."
    else:
        mirror = "DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT."
    for rel in MIRRORS:
        p = repo / rel
        if not p.is_file():
            errors.append(f"missing DPTN live status surface: {rel}")
        elif mirror not in p.read_text(encoding="utf-8"):
            errors.append(f"{rel}: missing current DPTN status mirror {mirror!r}")
    impl = (repo / "docs/implementation/README.md").read_text(encoding="utf-8")
    if "Implementation 001-A — BLOCKED ON DPTN EXIT" not in impl:
        errors.append("implementation authority must block 001-A while DPTN is incomplete")

    if a_complete and "ACCEPTED — DPTN-A COMPLETE" not in review:
        errors.append("accepted DPTN-A requires accepted execution review marker")

    for e in errors:
        print("ERROR", e)
    print(f"DPTN-A topology validation: {len(errors)} error(s), surfaces={len(surfaces)}/40, operations={len(operations)}/33, fixtures={len(fixture_ids)}/24")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
