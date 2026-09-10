#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

VALIDATOR="validate_dptn_c_promotion.py"


def run(repo:Path)->int:
    return subprocess.run([sys.executable,str(repo/"scripts/agentic"/VALIDATOR),"--repo",str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode


def mutate_text(repo:Path,rel:str,transform,label:str,errors:list[str])->None:
    p=repo/rel; original=p.read_text(encoding="utf-8")
    try:
        changed=transform(original)
        if changed==original: errors.append(f"{label}: mutation was a no-op"); return
        p.write_text(changed,encoding="utf-8")
        if run(repo)==0: errors.append(f"{label}: DPTN-C validator unexpectedly passed")
        else: print(f"PASS negative control: {label}")
    finally: p.write_text(original,encoding="utf-8")


def jmut(fn):
    def t(text:str)->str:
        d=json.loads(text); fn(d); return json.dumps(d,indent=2)+"\n"
    return t


def path_hide(repo:Path,rel:str,label:str,errors:list[str])->None:
    p=repo/rel; hold=repo/(rel+".__guard_hold__")
    try:
        p.rename(hold)
        if run(repo)==0: errors.append(f"{label}: DPTN-C validator unexpectedly passed")
        else: print(f"PASS negative control: {label}")
    finally:
        if hold.exists(): hold.rename(p)


def create_collision(repo:Path,rel:str,label:str,errors:list[str])->None:
    p=repo/rel
    try:
        p.mkdir(parents=True); (p/"README.md").write_text("guard collision\n",encoding="utf-8")
        if run(repo)==0: errors.append(f"{label}: DPTN-C validator unexpectedly passed")
        else: print(f"PASS negative control: {label}")
    finally:
        if p.exists(): shutil.rmtree(p)


def toggle_c_state(text:str)->str:
    if "DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED" in text:
        return text.replace("DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED","DPTN-C — Canonical Knowledge Promotion: IN EXECUTION",1)
    return text.replace("DPTN-C — Canonical Knowledge Promotion: IN EXECUTION","DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED",1)


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default=".")
    src=Path(ap.parse_args().repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix="dmtz-dptnc-") as td:
        repo=Path(td)/"repo"; shutil.copytree(src,repo,ignore=shutil.ignore_patterns(".git","__pycache__",".pytest_cache"),symlinks=True)
        subprocess.run(["git","init","-q"],cwd=repo,check=True)
        subprocess.run(["git","config","user.email","dptnc@example.invalid"],cwd=repo,check=True)
        subprocess.run(["git","config","user.name","DPTN-C Guard"],cwd=repo,check=True)
        subprocess.run(["git","add","-A"],cwd=repo,check=True); subprocess.run(["git","commit","-qm","guard baseline"],cwd=repo,check=True)

        manifest="docs/documentation_topology_normalization/dptn_c_promotion_manifest.json"
        inventory="docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
        fixtures="docs/documentation_topology_normalization/fixtures/dptn_c_promotion_scenarios.yaml"
        readme="docs/documentation_topology_normalization/README.md"
        inv=json.loads((repo/inventory).read_text()); post=inv.get("canonical_layout")=="first_class_dptn_c" or inv.get("canonical_root")=="docs"

        mutate_text(repo,manifest,jmut(lambda d:d["authorized_move_ids"].append("MOVE-015")),"later-phase move authorization",errors)
        mutate_text(repo,manifest,jmut(lambda d:d["expected_counts"].__setitem__("stable_ids",1238)),"stable-ID expected count drift",errors)
        mutate_text(repo,manifest,jmut(lambda d:d["moves"][0].__setitem__("source_tree_sha","0"*40)),"MOVE-007 conservation tree drift",errors)
        mutate_text(repo,manifest,jmut(lambda d:d.__setitem__("status","candidate_ready" if d.get("status")=="accepted" else "accepted")),"DPTN-C lifecycle divergence",errors)
        mutate_text(repo,fixtures,lambda t:t.replace("DPTNC-32","DPTNC-99",1),"DPTN-C scenario identity drift",errors)
        mutate_text(repo,"docs/history/README.md",lambda t:t.replace("HISTORY / PROVENANCE ONLY","HISTORY ONLY",1),"history authority boundary removal",errors)
        mutate_text(repo,"docs/implementation/README.md",lambda t:t.replace("Implementation 001-A — BLOCKED / NOT STARTED","Implementation 001-A — NEXT / READY / NOT STARTED",1),"implementation gate bypass",errors)
        mutate_text(repo,inventory,jmut(lambda d:d.__setitem__("concept_count",25)),"concept-count conservation drift",errors)
        mutate_text(repo,inventory,jmut(lambda d:d["records"][0].__setitem__("target_owner","docs/canonical/reference/product-definition.md" if post else "docs/reference/product-definition.md")),"ownership-ledger target divergence",errors)

        if post:
            path_hide(repo,"docs/concepts","missing promoted concepts target",errors)
            path_hide(repo,"docs/canonical/concepts","missing legacy redirect",errors)
        else:
            create_collision(repo,"docs/concepts","premature occupied promotion target",errors)
            path_hide(repo,"docs/canonical/concepts","missing pre-cutover canonical source",errors)

        path_hide(repo,"docs/agentic_development_foundation","premature ADF decomposition/move",errors)
        mutate_text(repo,"docs/agentic_development_foundation/stable_id_registry.json",jmut(lambda d:d["families"]["ARCH"].__setitem__("max",501)),"accepted stable-ID registry drift",errors)
        mutate_text(repo,readme,toggle_c_state,"DPTN-C status/artifact divergence",errors)

    for e in errors: print("ERROR",e)
    print(f"DPTN-C promotion guard tests: {len(errors)} error(s), 14 negative control(s)")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
