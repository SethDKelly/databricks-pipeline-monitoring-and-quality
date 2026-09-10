#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess
from pathlib import Path

ROOT="docs/documentation_topology_normalization"
STATE_RE=re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$",re.M)
FIXTURE_RE=re.compile(r"^\s*-\s+id:\s+(DPTNF-\d{2})\s*$",re.M)
MIRROR="DPTN status mirror: COMPLETE DPTN-A–DPTN-F; NEXT DPTN-G; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT."
SEMANTIC_TREES={
"architecture":"0f1564882f1c8d142c0eb4e5d77eb9ab56e43415","authority":"c3f7a1436294dff05729d81edbabcbac180833f5","concepts":"67d418f9d71ca9c64169c813853da514a37166ad","contracts":"b01663426ff83a79e09a0a05a218638587f86905","experience":"6e7b89390426ba651c2735baf6d441fc39dafd9c","invariants":"3e2f3ac5f6b201200fd6bce9cb9cbba92243c8ed","policies":"4acc2b064198d0a3725d4ff4bdda30e2cb139dff","reference":"6a3a361d1275f23c601710ba62089f790ae9f3f8"}
CURRENT_SURFACES=("AGENTS.md","IMPLEMENTATION.md",".claude/CLAUDE.md",".cursor/rules/00-implementation-routing.mdc",".agents/skills/resolve-context/SKILL.md","docs/agentic_development_foundation/developer_onboarding.md","docs/agentic_development_foundation/tool_compatibility_matrix.md","docs/agentic_development_foundation/adf_g_runtime_probe.md","docs/agentic_development_foundation/compatibility_smoke_checklist.md","docs/agentic_development_foundation/stable_reference_policy.md")
RULE_SURFACES=(".cursor/rules/10-design-change-control.mdc",".cursor/rules/20-contracts-evidence-temporal.mdc",".cursor/rules/30-identity-governance-authorization.mdc",".cursor/rules/40-acquisition-integrations.mdc",".cursor/rules/50-health-lineage-impact.mdc",".cursor/rules/60-investigation-reasoning-explanation.mdc",".cursor/rules/70-serving-security.mdc",".cursor/rules/95-active-control.mdc")

def tree_sha(repo:Path,rel:str)->str|None:
    if not (repo/".git").exists(): return None
    p=subprocess.run(["git","-C",str(repo),"rev-parse",f"HEAD:{rel}"],text=True,capture_output=True)
    return p.stdout.strip() if p.returncode==0 else None

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--repo",default=".");repo=Path(ap.parse_args().repo).resolve();errors=[]
    required=(f"{ROOT}/README.md",f"{ROOT}/dptn_f_rebinding_manifest.json",f"{ROOT}/dptn_f_execution_review.md",f"{ROOT}/fixtures/dptn_f_rebinding_scenarios.yaml","docs/index.md","knowledge/index.md","docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json","docs/agentic_development_foundation/stable_id_registry.json","docs/implementation/README.md")
    for rel in required:
        if not (repo/rel).is_file(): errors.append(f"missing DPTN-F artifact/dependency: {rel}")
    if errors:
        for e in errors: print("ERROR",e)
        return 1
    readme=(repo/ROOT/"README.md").read_text(encoding="utf-8");states=dict(STATE_RE.findall(readme));state=states.get("F")
    if any(states.get(c)!="COMPLETE / ACCEPTED" for c in "ABCDE") or state not in {"IN EXECUTION","COMPLETE / ACCEPTED"}: errors.append(f"invalid DPTN-F progression state: {states}")
    manifest=json.loads((repo/ROOT/"dptn_f_rebinding_manifest.json").read_text(encoding="utf-8"));expected_status="accepted" if state=="COMPLETE / ACCEPTED" else "candidate_ready"
    if manifest.get("phase")!="DPTN-F" or manifest.get("status")!=expected_status: errors.append("DPTN-F manifest phase/status divergence")
    if manifest.get("authorized_move_ids")!=["MOVE-019"]: errors.append("DPTN-F may authorize MOVE-019 only")
    if manifest.get("semantic_change") is not False or manifest.get("implementation_change") is not False: errors.append("DPTN-F must remain non-semantic and non-implementation")
    discovery=manifest.get("discovery",{});stable=manifest.get("stable_reference",{})
    if discovery.get("repository_native_entry")!="docs/index.md" or discovery.get("okf_compatibility_entry")!="knowledge/index.md" or discovery.get("knowledge_role")!="generated_compatibility_only": errors.append("DPTN-F discovery routing contract drifted")
    if stable.get("resolver")!="scripts/agentic/resolve_stable_id.py" or stable.get("locator_format")!="{owner_path}::{stable_id}" or stable.get("default_scope")!="canonical_owner_only" or stable.get("history_mode")!="explicit_--history" or stable.get("first_match_canonicality") is not False or stable.get("current_link_history_fallback") is not False: errors.append("DPTN-F stable-reference contract drifted")
    expected={"concepts":24,"stable_ids":1237,"stable_families":8,"architecture_ids":500,"implementation_001_a":"blocked_not_started"}
    if manifest.get("conservation")!=expected: errors.append(f"DPTN-F conservation baseline drifted: {manifest.get('conservation')}")
    inv=json.loads((repo/"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json").read_text());reg=json.loads((repo/"docs/agentic_development_foundation/stable_id_registry.json").read_text());total=sum(int(v["max"])-int(v["min"])+1 for v in reg.get("families",{}).values())
    if inv.get("concept_count")!=24 or total!=1237 or len(reg.get("families",{}))!=8 or inv.get("canonical_root")!="docs" or inv.get("canonical_layout")!="first_class_dptn_c": errors.append("semantic/current-owner conservation baseline changed")
    for fam,expected_sha in SEMANTIC_TREES.items():
        actual=tree_sha(repo,f"docs/{fam}")
        if actual is not None and actual!=expected_sha: errors.append(f"semantic owner tree drifted: docs/{fam} {actual} != {expected_sha}")
    docs_index=(repo/"docs/index.md").read_text(encoding="utf-8");knowledge=(repo/"knowledge/index.md").read_text(encoding="utf-8")
    if "AUTHORITY: CURRENT ROUTING / DISCOVERY ROOT ONLY" not in docs_index or "knowledge/index.md" not in docs_index: errors.append("docs/index.md discovery/compatibility boundary missing")
    if "GENERATED OKF PROJECTION — DO NOT HAND-EDIT." not in knowledge or "docs/index.md" not in knowledge: errors.append("knowledge/index.md generated-compatibility boundary missing")
    for rel in CURRENT_SURFACES:
        p=repo/rel
        if not p.is_file(): errors.append(f"missing current routing surface: {rel}");continue
        if "docs/index.md" not in p.read_text(encoding="utf-8"): errors.append(f"{rel}: repository-native docs/index.md route missing")
    tool=json.loads((repo/"docs/agentic_development_foundation/tool_compatibility.json").read_text());auth=tool.get("authority",{})
    if auth.get("knowledge_entry")!="docs/index.md" or auth.get("okf_compatibility_entry")!="knowledge/index.md": errors.append("tool compatibility authority discovery entries are not rebound")
    for name,data in tool.get("tools",{}).items():
        if data.get("knowledge_entry")!="docs/index.md" or data.get("okf_compatibility_entry")!="knowledge/index.md": errors.append(f"{name}: discovery entries are not rebound")
    forbidden=("docs/concepts/phase_","docs/foundation/","docs/canonical/contracts/","docs/canonical/architecture/","docs/canonical/authority/","docs/canonical/experience/")
    for rel in RULE_SURFACES:
        p=repo/rel
        if not p.is_file(): errors.append(f"missing scoped routing rule: {rel}");continue
        text=p.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text: errors.append(f"{rel}: stale pre-normalization route remains: {token}")
    link_validator=(repo/"scripts/agentic/validate_agentic_references.py").read_text(encoding="utf-8")
    if "dptn_d_history_fallback" in link_validator: errors.append("current reference validator still contains DPTN-D history fallback")
    impact=(repo/"scripts/agentic/knowledge_impact.py").read_text(encoding="utf-8")
    if "docs/canonical/" in impact or "canonical_owner_roots" not in impact: errors.append("knowledge impact routing is not normalized to current owner roots")
    compat=(repo/"scripts/agentic/run_ckr_with_history_compat.py").read_text(encoding="utf-8")
    if "accepted_routing_projection" not in compat or "project_ckr_knowledge" not in compat: errors.append("completed CKR accepted-era compatibility projection missing")
    if "Implementation 001-A — BLOCKED / NOT STARTED" not in (repo/"docs/implementation/README.md").read_text(encoding="utf-8"): errors.append("Implementation 001-A gate released during DPTN-F")
    fixtures=(repo/ROOT/"fixtures/dptn_f_rebinding_scenarios.yaml").read_text(encoding="utf-8");ids=FIXTURE_RE.findall(fixtures)
    if ids!=[f"DPTNF-{i:02d}" for i in range(1,25)]: errors.append("DPTN-F fixtures must contain DPTNF-01..DPTNF-24 exactly once/in order")
    if f"status: {expected_status}" not in fixtures: errors.append(f"DPTN-F fixture status must be {expected_status}")
    review=(repo/ROOT/"dptn_f_execution_review.md").read_text(encoding="utf-8");marker="**Status:** ACCEPTED — DPTN-F COMPLETE" if state=="COMPLETE / ACCEPTED" else "**Status:** IN EXECUTION"
    if marker not in review: errors.append("DPTN-F execution review state mismatch")
    if state=="COMPLETE / ACCEPTED":
        if states.get("G")!="NEXT / READY": errors.append("DPTN-G must be NEXT / READY after DPTN-F acceptance")
        for rel in ("AGENTS.md","IMPLEMENTATION.md","docs/implementation/README.md","docs/implementation/AGENTS.md","docs/implementation/agent_reference_index.md",".cursor/rules/00-implementation-routing.mdc"):
            if MIRROR not in (repo/rel).read_text(encoding="utf-8"): errors.append(f"{rel}: DPTN-F accepted status mirror missing")
    for e in errors: print("ERROR",e)
    print(f"DPTN-F rebinding validation: {len(errors)} error(s), scenarios={len(ids)}/24, stable_ids={total}, state={state}")
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
