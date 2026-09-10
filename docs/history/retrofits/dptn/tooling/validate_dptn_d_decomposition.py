#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

ROOT="docs/documentation_topology_normalization"
STATE_RE=re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$",re.M)
FIXTURE_RE=re.compile(r"^\s*-\s+id:\s+(DPTND-\d{2})\s*$",re.M)
ADF_HISTORY=(
"01_adf_a_authority_scope_boundary.md","02_adf_b_okf_knowledge_plane.md","03_adf_c_instruction_tool_adapters.md","04_adf_d_portable_skills_workflows.md",
"05_adf_e_context_reference_maintenance.md","06_adf_f_conformance_validation_ci.md","07_adf_g_tool_compatibility_operating_model.md","08_adf_h_security_trust_lifecycle_governance.md",
"adf_a_execution_review.md","adf_b_execution_review.md","adf_c_execution_review.md","adf_d_execution_review.md","adf_e_execution_review.md","adf_f_execution_review.md",
"adf_g_execution_review.md","adf_h_execution_review.md","databricks_agent_skills_addendum_execution_review.md","design_exit_review.md","execution_exit_criteria.md","execution_exit_review.md")
ADF_LIVE=("README.md","authority_scope_policy.md","agentic_change_governance.md","conformance_policy.md","context_discovery_policy.md","stable_reference_policy.md","stable_id_registry.json","security_trust_lifecycle_policy.md","adf_g_progression_exception.md","adf_g_runtime_probe.md","adf_h_security_baseline.md","runtime_compatibility_evidence.json","tool_lifecycle_review.json")
CKR_LIVE=("README.md","authority_model.md","canonical_document_template.md","canonical_ownership_inventory.json","canonical_ownership_inventory.md","migration_contract.md")

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default="."); repo=Path(ap.parse_args().repo).resolve(); errors=[]
    required=(f"{ROOT}/README.md",f"{ROOT}/dptn_d_decomposition_manifest.json",f"{ROOT}/dptn_d_execution_review.md",f"{ROOT}/fixtures/dptn_d_decomposition_scenarios.yaml","docs/history/README.md","docs/implementation/README.md")
    for rel in required:
        if not (repo/rel).is_file(): errors.append(f"missing DPTN-D artifact/dependency: {rel}")
    if errors:
        for e in errors: print("ERROR",e)
        return 1
    readme=(repo/ROOT/"README.md").read_text(encoding="utf-8"); states=dict(STATE_RE.findall(readme)); d=states.get("D")
    if states.get("A")!="COMPLETE / ACCEPTED" or states.get("B")!="COMPLETE / ACCEPTED" or states.get("C")!="COMPLETE / ACCEPTED" or d not in {"IN EXECUTION","COMPLETE / ACCEPTED"}: errors.append(f"invalid DPTN-D progression state: {states}")
    manifest=json.loads((repo/ROOT/"dptn_d_decomposition_manifest.json").read_text(encoding="utf-8"))
    expected_status="accepted" if d=="COMPLETE / ACCEPTED" else "candidate_ready"
    if manifest.get("phase")!="DPTN-D" or manifest.get("status")!=expected_status: errors.append("DPTN-D manifest phase/status divergence")
    if manifest.get("authorized_move_ids")!=["MOVE-015","MOVE-016"]: errors.append("DPTN-D may authorize MOVE-015 and MOVE-016 only")
    if manifest.get("semantic_change") is not False or manifest.get("implementation_change") is not False: errors.append("DPTN-D must remain non-semantic and non-implementation")
    c=manifest.get("conservation",{}); expected={"concepts":24,"stable_ids":1237,"stable_families":8,"architecture_ids":500,"implementation_001_a":"blocked_not_started"}
    if c!=expected: errors.append(f"DPTN-D conservation baseline drifted: {c}")
    ckr=repo/"docs/canonical_knowledge_retrofit"; ch=repo/"docs/history/retrofits/ckr"
    for name in CKR_LIVE:
        if not (ckr/name).is_file(): errors.append(f"missing durable CKR current artifact: {name}")
    for p in ckr.iterdir():
        if p.name.startswith("ckr_") or p.name=="fixtures": errors.append(f"completed CKR evidence remains in current root: {p.name}")
    if not ch.is_dir(): errors.append("missing CKR retrofit history root")
    else:
        if not (ch/"ckr_k_execution_review.md").is_file() or not (ch/"fixtures/ckr_k_exit_scenarios.yaml").is_file(): errors.append("CKR history is incomplete")
    adf=repo/"docs/agentic_development_foundation"; ah=repo/"docs/history/foundations/adf"
    for name in ADF_LIVE:
        if not (adf/name).is_file(): errors.append(f"missing durable/live ADF artifact: {name}")
    for name in ADF_HISTORY:
        if (adf/name).exists(): errors.append(f"completed ADF evidence remains in current root: {name}")
        if not (ah/name).is_file(): errors.append(f"missing preserved ADF history artifact: {name}")
    if (adf/"fixtures").exists(): errors.append("ADF accepted scenario fixtures remain in current root")
    if not (ah/"fixtures/adf_h_security_scenarios.yaml").is_file(): errors.append("ADF historical fixture corpus incomplete")
    hist=(repo/"docs/history/README.md").read_text(encoding="utf-8")
    for marker in ("HISTORY / PROVENANCE ONLY","NOT CURRENT SEMANTIC AUTHORITY","history/retrofits/ckr","history/foundations/adf"):
        if marker not in hist: errors.append(f"history boundary/index missing {marker!r}")
    inv=json.loads((ckr/"canonical_ownership_inventory.json").read_text(encoding="utf-8")); reg=json.loads((adf/"stable_id_registry.json").read_text(encoding="utf-8"))
    total=sum(int(x["max"])-int(x["min"])+1 for x in reg.get("families",{}).values())
    if inv.get("concept_count")!=24 or total!=1237 or len(reg.get("families",{}))!=8: errors.append("semantic/stable-ID conservation baseline changed")
    if inv.get("canonical_root")!="docs" or inv.get("canonical_layout")!="first_class_dptn_c": errors.append("DPTN-C current-owner topology was reopened")
    impl=(repo/"docs/implementation/README.md").read_text(encoding="utf-8")
    if "Implementation 001-A — BLOCKED / NOT STARTED" not in impl: errors.append("Implementation 001-A gate released during DPTN-D")
    fixtures=(repo/ROOT/"fixtures/dptn_d_decomposition_scenarios.yaml").read_text(encoding="utf-8"); ids=FIXTURE_RE.findall(fixtures)
    if ids!=[f"DPTND-{i:02d}" for i in range(1,19)]: errors.append("DPTN-D fixtures must contain DPTND-01..DPTND-18 exactly once/in order")
    if f"status: {expected_status}" not in fixtures: errors.append(f"DPTN-D fixture status must be {expected_status}")
    review=(repo/ROOT/"dptn_d_execution_review.md").read_text(encoding="utf-8"); marker="**Status:** ACCEPTED — DPTN-D COMPLETE" if d=="COMPLETE / ACCEPTED" else "**Status:** IN EXECUTION"
    if marker not in review: errors.append("DPTN-D execution review state mismatch")
    for e in errors: print("ERROR",e)
    print(f"DPTN-D decomposition validation: {len(errors)} error(s), scenarios={len(ids)}/18, stable_ids={total}, state={d}")
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
