#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, os, re, subprocess, sys
from pathlib import Path

ROOT = "docs/documentation_topology_normalization"
STATE_RE = re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$", re.M)
FIXTURE_RE = re.compile(r"^\s*-\s+id:\s+(DPTNC-\d{2})\s*$", re.M)
CURRENT_ROOTS = (
    "docs/concepts", "docs/architecture", "docs/authority", "docs/contracts",
    "docs/experience", "docs/invariants", "docs/policies", "docs/reference",
)
REPRESENTATIVE = {
    "SYN-001": "docs/contracts/",
    "REF-030": "docs/contracts/",
    "AUTH-053": "docs/authority/",
    "HLTH-066": "docs/contracts/",
    "OPS-123": "docs/contracts/",
    "EXPL-160": "docs/experience/",
    "INTG-270": "docs/contracts/",
    "ARCH-500": "docs/architecture/",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_object(repo: Path, spec: str) -> str | None:
    p = subprocess.run(["git", "rev-parse", spec], cwd=repo, text=True, capture_output=True)
    return p.stdout.strip() if p.returncode == 0 else None


def resolve(repo: Path, token: str, history: bool = False) -> tuple[int, dict | None, str]:
    cmd=[sys.executable,str(repo/"scripts/agentic/resolve_stable_id.py"),token,"--repo",str(repo),"--json"]
    if history: cmd.append("--history")
    p=subprocess.run(cmd,cwd=repo,text=True,capture_output=True)
    if p.returncode: return p.returncode,None,(p.stdout+p.stderr).strip()
    try: return 0,json.loads(p.stdout),""
    except json.JSONDecodeError as exc: return 99,None,str(exc)


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default=".")
    repo=Path(ap.parse_args().repo).resolve(); errors=[]
    required=(
        f"{ROOT}/README.md", f"{ROOT}/move_map.json", f"{ROOT}/collision_register.md",
        f"{ROOT}/dptn_c_promotion_manifest.json", f"{ROOT}/dptn_c_execution_review.md",
        f"{ROOT}/fixtures/dptn_c_promotion_scenarios.yaml",
        "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json",
        "docs/agentic_development_foundation/stable_id_registry.json", "docs/history/README.md",
    )
    for rel in required:
        if not (repo/rel).is_file(): errors.append(f"missing DPTN-C artifact/dependency: {rel}")
    if errors:
        for e in errors: print("ERROR",e)
        return 1

    readme=(repo/ROOT/"README.md").read_text(encoding="utf-8")
    states={k:v for k,v in STATE_RE.findall(readme)}
    c_state=states.get("C")
    if states.get("A")!="COMPLETE / ACCEPTED" or states.get("B")!="COMPLETE / ACCEPTED" or c_state not in {"IN EXECUTION","COMPLETE / ACCEPTED"}:
        errors.append(f"DPTN-C requires A/B complete and C active/complete; A={states.get('A')!r}, B={states.get('B')!r}, C={c_state!r}")

    manifest=load_json(repo/ROOT/"dptn_c_promotion_manifest.json")
    expected_status="accepted" if c_state=="COMPLETE / ACCEPTED" else "candidate_ready"
    if manifest.get("status")!=expected_status: errors.append(f"DPTN-C manifest status must be {expected_status!r}")
    if manifest.get("phase")!="DPTN-C" or manifest.get("schema_version")!="1.0": errors.append("DPTN-C manifest schema/phase drifted")
    if "does not own or change dmtz product semantics" not in manifest.get("purpose","").lower(): errors.append("DPTN-C manifest must remain explicitly non-semantic")
    expected_ids=[f"MOVE-{i:03d}" for i in range(7,15)]
    if manifest.get("authorized_move_ids")!=expected_ids: errors.append("DPTN-C may authorize MOVE-007..MOVE-014 only")
    counts=manifest.get("expected_counts",{})
    expected_counts={"moves":8,"concepts":24,"stable_ids":1237,"stable_families":8,"architecture_ids":500,"architecture_inventory_records":9,"scenarios":32,"negative_controls":14}
    if counts!=expected_counts: errors.append(f"DPTN-C expected counts drifted: {counts}")
    moves=manifest.get("moves",[])
    if [m.get("id") for m in moves]!=expected_ids: errors.append("DPTN-C move evidence must contain MOVE-007..MOVE-014 exactly once/in order")

    inventory=load_json(repo/"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json")
    registry=load_json(repo/"docs/agentic_development_foundation/stable_id_registry.json")
    total=sum(int(x["max"])-int(x["min"])+1 for x in registry.get("families",{}).values())
    if total!=1237 or len(registry.get("families",{}))!=8: errors.append(f"stable-ID baseline changed: families={len(registry.get('families',{}))}, ids={total}")
    if inventory.get("concept_count")!=24 or inventory.get("status")!="ckr_complete": errors.append("CKR completion/concept baseline changed")
    if inventory.get("stable_families",{}).get("ARCH",{}).get("accepted_range")!="ARCH-001..ARCH-500": errors.append("ARCH accepted range changed")
    if len(inventory.get("architecture_segments",[]))!=9: errors.append("architecture inventory must remain 9 records")

    post = inventory.get("canonical_layout")=="first_class_dptn_c" or inventory.get("canonical_root")=="docs"
    pre = not post
    if pre:
        if inventory.get("canonical_root")!="docs/canonical": errors.append("pre-cutover DPTN-C must retain CKR canonical_root docs/canonical")
        blob=git_object(repo,"HEAD:docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json") if (repo/".git").exists() else None
        if blob and blob!=manifest.get("ownership_inventory_baseline_blob"): errors.append("ownership inventory changed before atomic DPTN-C cutover")
        for m in moves:
            src,target,sha=m.get("source"),m.get("target"),m.get("source_tree_sha")
            if not (repo/src).is_dir() or (repo/src).is_symlink(): errors.append(f"{m.get('id')}: pre-cutover source tree missing/non-tree: {src}")
            if (repo/target).exists() or (repo/target).is_symlink(): errors.append(f"{m.get('id')}: target occupied before atomic cutover: {target}")
            if (repo/".git").exists() and git_object(repo,f"HEAD:{src}")!=sha: errors.append(f"{m.get('id')}: source tree differs from accepted baseline")
        for token in REPRESENTATIVE:
            code,payload,msg=resolve(repo,token)
            if code or not payload: errors.append(f"{token}: pre-cutover resolver failure {msg}")
            elif not payload["canonical_owner"]["path"].startswith("docs/canonical/"): errors.append(f"{token}: pre-cutover owner escaped docs/canonical")
    else:
        if inventory.get("canonical_root")!="docs" or inventory.get("canonical_layout")!="first_class_dptn_c": errors.append("post-cutover inventory must declare first_class_dptn_c under docs")
        if inventory.get("canonical_owner_roots")!=list(CURRENT_ROOTS): errors.append("canonical_owner_roots must enumerate the eight normalized first-class roots in accepted order")
        if inventory.get("design_history_index")!="docs/history/design-history/README.md": errors.append("design_history_index must resolve to normalized history")

        for m in moves:
            src,target,sha=m.get("source"),m.get("target"),m.get("source_tree_sha")
            tp=repo/target; sp=repo/src
            if not tp.is_dir() or tp.is_symlink(): errors.append(f"{m.get('id')}: promoted target is not a substantive directory: {target}")
            if (repo/".git").exists() and git_object(repo,f"HEAD:{target}")!=sha: errors.append(f"{m.get('id')}: promoted target tree differs from accepted source tree")
            if not sp.is_symlink(): errors.append(f"{m.get('id')}: legacy canonical path must be a redirect symlink, not a substantive owner: {src}")
            else:
                expected="../"+Path(target).name
                if os.readlink(sp)!=expected: errors.append(f"{m.get('id')}: redirect target must be {expected!r}; found {os.readlink(sp)!r}")

        # No substantive current owner in the ledger may remain under docs/canonical or docs/history.
        for rec in inventory.get("records",[]):
            target=rec.get("target_owner","")
            if target.startswith("docs/canonical/") or target.startswith("docs/history/") or not target.startswith("docs/"):
                errors.append(f"{rec.get('record_id')}: normalized target_owner invalid: {target}")
            if not (repo/target).is_file(): errors.append(f"{rec.get('record_id')}: normalized target_owner missing: {target}")
            origin=rec.get("current_owner","")
            if not origin.startswith("docs/history/"): errors.append(f"{rec.get('record_id')}: historical source pointer must live under docs/history after path reclaim: {origin}")

        for fam,data in inventory.get("stable_families",{}).items():
            root=data.get("target_owner_root","")
            if root.startswith("docs/canonical/") or root.startswith("docs/history/"): errors.append(f"{fam}: target_owner_root not normalized current path: {root}")
            for rel in data.get("target_documents",[]):
                if rel.startswith("docs/canonical/") or rel.startswith("docs/history/") or not (repo/rel).is_file(): errors.append(f"{fam}: invalid/missing normalized target document: {rel}")
            origin=data.get("current_owner_root","")
            if not origin.startswith("docs/history/"): errors.append(f"{fam}: historical source root must live under docs/history: {origin}")

        for rec in inventory.get("architecture_segments",[]):
            target=rec.get("target_owner",""); origin=rec.get("current_owner","")
            if not target.startswith("docs/architecture/") or not (repo/target).is_file(): errors.append(f"{rec.get('record_id')}: architecture target not normalized/missing: {target}")
            if not origin.startswith("docs/history/"): errors.append(f"{rec.get('record_id')}: architecture provenance not normalized to history: {origin}")

        for item in inventory.get("history_sources",[]):
            if not item.get("path","").startswith("docs/history/"): errors.append(f"history source pointer escaped normalized history: {item.get('path')}")

        canonical=repo/"docs/canonical"
        if not (canonical/"README.md").is_file(): errors.append("docs/canonical/README.md must remain through DPTN-E")
        else:
            ctext=(canonical/"README.md").read_text(encoding="utf-8")
            for marker in ("ROUTING / COMPATIBILITY ONLY","not a substantive semantic owner","DPTN-E"):
                if marker not in ctext: errors.append(f"docs/canonical/README.md missing post-promotion boundary marker {marker!r}")

        for token,prefix in REPRESENTATIVE.items():
            code,payload,msg=resolve(repo,token)
            if code or not payload: errors.append(f"{token}: normalized resolver failure {msg}")
            else:
                path=payload["canonical_owner"]["path"]
                if not path.startswith(prefix) or path.startswith("docs/canonical/") or path.startswith("docs/history/"):
                    errors.append(f"{token}: normalized owner incorrect: {path}")
                if payload.get("canonical_locator")!=f"{path}::{token}": errors.append(f"{token}: locator/path mismatch")

        code,payload,msg=resolve(repo,"OPS-123",history=True)
        if code or not payload: errors.append(f"OPS-123 --history failed after promotion: {msg}")
        else:
            h=payload.get("history_occurrences",[])
            if not h or not any(x.get("path","").startswith("docs/history/") for x in h): errors.append("--history must still discover preserved history after promotion")
            for x in h:
                if any(x.get("path","").startswith(root+"/") for root in CURRENT_ROOTS): errors.append(f"--history misclassified current owner as history: {x.get('path')}")

    # Historical namespace and later-phase boundaries remain intact in either cutover state.
    htext=(repo/"docs/history/README.md").read_text(encoding="utf-8")
    if "HISTORY / PROVENANCE ONLY" not in htext or "NOT CURRENT SEMANTIC AUTHORITY" not in htext: errors.append("history authority boundary weakened")
    for rel in ("docs/agentic_development_foundation","docs/canonical_knowledge_retrofit","knowledge"):
        if not (repo/rel).is_dir(): errors.append(f"later-phase source moved prematurely: {rel}")
    impl=(repo/"docs/implementation/README.md").read_text(encoding="utf-8")
    if "Implementation 001-A — BLOCKED / NOT STARTED" not in impl: errors.append("Implementation 001-A gate released during DPTN-C")

    fixtures=(repo/ROOT/"fixtures/dptn_c_promotion_scenarios.yaml").read_text(encoding="utf-8")
    ids=FIXTURE_RE.findall(fixtures)
    if ids!=[f"DPTNC-{i:02d}" for i in range(1,33)]: errors.append("DPTN-C fixtures must contain DPTNC-01..DPTNC-32 exactly once/in order")
    fm=re.search(r"^status:\s+(\S+)",fixtures,re.M)
    if not fm or fm.group(1)!=expected_status: errors.append(f"DPTN-C fixture status must be {expected_status}")
    review=(repo/ROOT/"dptn_c_execution_review.md").read_text(encoding="utf-8")
    marker="**Status:** ACCEPTED — DPTN-C COMPLETE" if c_state=="COMPLETE / ACCEPTED" else "**Status:** IN EXECUTION"
    if marker not in review: errors.append(f"DPTN-C execution review missing state marker {marker!r}")

    for e in errors: print("ERROR",e)
    print(f"DPTN-C promotion validation: {len(errors)} error(s), moves={len(moves)}/8, scenarios={len(ids)}/32, stable_ids={total}, state={c_state}, layout={'post' if post else 'pre'}")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
