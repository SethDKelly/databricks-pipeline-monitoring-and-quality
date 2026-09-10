#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,shutil,subprocess,sys,tempfile
from pathlib import Path
VALIDATOR="validate_dptn_d_decomposition.py"
def run(repo:Path)->int:
    return subprocess.run([sys.executable,str(repo/"scripts/agentic"/VALIDATOR),"--repo",str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
def mutate(repo:Path,rel:str,fn,label:str,errors:list[str]):
    p=repo/rel; old=p.read_text(encoding="utf-8")
    try:
        new=fn(old)
        if new==old: errors.append(f"{label}: no-op mutation"); return
        p.write_text(new,encoding="utf-8")
        if run(repo)==0: errors.append(f"{label}: validator unexpectedly passed")
        else: print("PASS negative control:",label)
    finally: p.write_text(old,encoding="utf-8")
def hide(repo:Path,rel:str,label:str,errors:list[str]):
    p=repo/rel; hold=p.with_name(p.name+".__guard__")
    try:
        p.rename(hold)
        if run(repo)==0: errors.append(f"{label}: validator unexpectedly passed")
        else: print("PASS negative control:",label)
    finally:
        if hold.exists(): hold.rename(p)
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default="."); src=Path(ap.parse_args().repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix="dmtz-dptnd-") as td:
        repo=Path(td)/"repo"; shutil.copytree(src,repo,ignore=shutil.ignore_patterns(".git","__pycache__",".pytest_cache"),symlinks=True)
        hide(repo,"docs/history/retrofits/ckr/ckr_k_execution_review.md","missing CKR exit provenance",errors)
        hide(repo,"docs/history/foundations/adf/execution_exit_review.md","missing ADF exit provenance",errors)
        hide(repo,"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json","durable CKR ledger moved to history",errors)
        hide(repo,"docs/agentic_development_foundation/authority_scope_policy.md","durable ADF authority policy moved to history",errors)
        hide(repo,"docs/agentic_development_foundation/adf_g_runtime_probe.md","live deferred runtime procedure lost",errors)
        mutate(repo,"docs/history/README.md",lambda t:t.replace("HISTORY / PROVENANCE ONLY","HISTORY ONLY",1),"history authority boundary weakened",errors)
        mutate(repo,"docs/implementation/README.md",lambda t:t.replace("Implementation 001-A — BLOCKED / NOT STARTED","Implementation 001-A — NEXT / READY / NOT STARTED",1),"implementation gate bypass",errors)
        manifest="docs/documentation_topology_normalization/dptn_d_decomposition_manifest.json"
        mutate(repo,manifest,lambda t:t.replace('"MOVE-016"','"MOVE-017"',1),"later-phase move authorization",errors)
        mutate(repo,manifest,lambda t:t.replace('"stable_ids": 1237','"stable_ids": 1238',1),"stable-ID conservation drift",errors)
        mutate(repo,"docs/documentation_topology_normalization/fixtures/dptn_d_decomposition_scenarios.yaml",lambda t:t.replace("DPTND-18","DPTND-99",1),"scenario identity drift",errors)
    for e in errors: print("ERROR",e)
    print(f"DPTN-D decomposition guard tests: {len(errors)} error(s), 10 negative control(s)")
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
