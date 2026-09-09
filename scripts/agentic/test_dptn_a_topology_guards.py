#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

VALIDATOR = "validate_dptn_a_topology.py"

def run(repo: Path) -> int:
    return subprocess.run([sys.executable, str(repo/"scripts/agentic"/VALIDATOR), "--repo", str(repo)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

def mutate(repo: Path, rel: str, transform, label: str, errors: list[str]) -> None:
    p = repo/rel
    original = p.read_text(encoding="utf-8")
    try:
        changed = transform(original)
        if changed == original:
            errors.append(f"{label}: mutation was a no-op")
            return
        p.write_text(changed, encoding="utf-8")
        if run(repo) == 0:
            errors.append(f"{label}: DPTN-A validator unexpectedly passed")
        else:
            print(f"PASS negative control: {label}")
    finally:
        p.write_text(original, encoding="utf-8")

def jmut(fn):
    def x(text):
        data=json.loads(text); fn(data); return json.dumps(data,indent=2)+"\n"
    return x

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default=".")
    a=ap.parse_args(); src=Path(a.repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix="dmtz-dptna-guards-") as td:
        repo=Path(td)/"repo"
        shutil.copytree(src,repo,ignore=shutil.ignore_patterns(".git","__pycache__",".pytest_cache"))

        def drop_arch(d): d["surfaces"]=[s for s in d["surfaces"] if s["surface_id"]!="canonical.architecture"]
        def demote_ckr(d): next(s for s in d["surfaces"] if s["surface_id"]=="ckr.program").update(current_role="historical_provenance")
        def bulk_adf(d): next(s for s in d["surfaces"] if s["surface_id"]=="adf.program").update(planned_target="docs/history/foundations/adf/")
        def erase_collision(d): next(s for s in d["surfaces"] if s["surface_id"]=="canonical.concepts").update(collision="none")
        def remove_precondition(d):
            o=next(o for o in d["operations"] if o["operation_id"]=="C-PROMOTE-CONCEPTS")
            o["preconditions"]=[p for p in o["preconditions"] if "phase corpus" not in p]
        def authorize_early(d): d["status"]="DPTN-A AUTHORIZED FOR PHYSICAL MOVE"
        def drift_arch(d): d["stable_families"]["ARCH"]["accepted_range"]="ARCH-001..ARCH-501"

        mutate(repo,"docs/documentation_topology_normalization/topology_inventory.json",jmut(drop_arch),"canonical family omitted from topology inventory",errors)
        mutate(repo,"docs/documentation_topology_normalization/topology_inventory.json",jmut(demote_ckr),"CKR mixed-directory role collapsed to history",errors)
        mutate(repo,"docs/documentation_topology_normalization/topology_inventory.json",jmut(bulk_adf),"ADF recursive bulk-move shortcut",errors)
        mutate(repo,"docs/documentation_topology_normalization/topology_inventory.json",jmut(erase_collision),"concept target collision omitted",errors)
        mutate(repo,"docs/documentation_topology_normalization/move_map.json",jmut(remove_precondition),"concept promotion history-first precondition removed",errors)
        mutate(repo,"docs/documentation_topology_normalization/move_map.json",jmut(authorize_early),"DPTN-A premature physical-move authorization",errors)
        mutate(repo,"docs/documentation_topology_normalization/fixtures/dptn_a_topology_scenarios.yaml",lambda t:t.replace("DPTNA-24","DPTNA-99",1),"DPTN-A fixture identity drift",errors)
        mutate(repo,"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json",jmut(drift_arch),"DPTN-A stable-ID semantic baseline drift",errors)
        mutate(repo,"AGENTS.md",lambda t:re.sub(r"^DPTN status mirror:.*$","DPTN status mirror: STALE.",t,count=1,flags=re.M),"stale DPTN live status mirror",errors)
        mutate(repo,"docs/implementation/README.md",lambda t:t.replace("Implementation 001-A — BLOCKED ON DPTN EXIT","Implementation 001-A — NEXT / READY / NOT STARTED",1),"premature implementation release during DPTN",errors)

        readme=(repo/"docs/documentation_topology_normalization/README.md").read_text(encoding="utf-8")
        b_not_started=("DPTN-B — Historical Namespace Preparation & Collision Removal: PLANNED." in readme or "DPTN-B — Historical Namespace Preparation & Collision Removal: NEXT / READY / NOT STARTED." in readme)
        if b_not_started:
            p=repo/"docs/history"
            p.mkdir(parents=True,exist_ok=True)
            if run(repo)==0: errors.append("premature history-root creation: DPTN-A validator unexpectedly passed")
            else: print("PASS negative control: premature history-root creation")
            shutil.rmtree(p)

    for e in errors: print("ERROR",e)
    print(f"DPTN-A guard tests: {len(errors)} error(s), 11 negative control(s)")
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())
