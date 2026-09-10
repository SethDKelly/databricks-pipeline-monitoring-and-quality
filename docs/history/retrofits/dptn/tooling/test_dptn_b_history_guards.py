#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, shutil, subprocess, sys, tempfile
from pathlib import Path

VALIDATOR = "validate_dptn_b_history.py"


def run(repo: Path) -> int:
    return subprocess.run([sys.executable,str(repo/"scripts/agentic"/VALIDATOR),"--repo",str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode


def text_mutate(repo: Path, rel: str, transform, label: str, errors: list[str]) -> None:
    p=repo/rel; original=p.read_text(encoding="utf-8")
    try:
        changed=transform(original)
        if changed==original: errors.append(f"{label}: mutation was a no-op"); return
        p.write_text(changed,encoding="utf-8")
        if run(repo)==0: errors.append(f"{label}: DPTN-B validator unexpectedly passed")
        else: print(f"PASS negative control: {label}")
    finally: p.write_text(original,encoding="utf-8")


def json_mutate(fn):
    def t(text: str) -> str:
        d=json.loads(text); fn(d); return json.dumps(d,indent=2)+"\n"
    return t


def path_move(repo: Path, rel: str, label: str, errors: list[str]) -> None:
    p=repo/rel; hold=repo/(rel+".__guard_hold__")
    try:
        p.rename(hold)
        if run(repo)==0: errors.append(f"{label}: DPTN-B validator unexpectedly passed")
        else: print(f"PASS negative control: {label}")
    finally:
        if hold.exists(): hold.rename(p)


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default=".")
    src=Path(ap.parse_args().repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix="dmtz-dptnb-") as td:
        repo=Path(td)/"repo"
        shutil.copytree(src,repo,ignore=shutil.ignore_patterns(".git","__pycache__",".pytest_cache"),symlinks=True)
        subprocess.run(["git","init","-q"],cwd=repo,check=True)
        subprocess.run(["git","config","user.email","dptn@example.invalid"],cwd=repo,check=True)
        subprocess.run(["git","config","user.name","DPTN Guard"],cwd=repo,check=True)
        subprocess.run(["git","add","-A"],cwd=repo,check=True)
        subprocess.run(["git","commit","-qm","guard baseline"],cwd=repo,check=True)

        manifest="docs/documentation_topology_normalization/dptn_b_relocation_manifest.json"
        text_mutate(repo,manifest,json_mutate(lambda d:d["authorized_move_ids"].append("MOVE-007")),"later-phase move authorization",errors)
        text_mutate(repo,manifest,json_mutate(lambda d:d["expected_counts"].__setitem__("stable_ids",1238)),"stable-ID count drift",errors)
        text_mutate(repo,manifest,json_mutate(lambda d:d["moves"][1].__setitem__("source_tree_sha","0"*40)),"MOVE-002 preservation-tree drift",errors)
        text_mutate(repo,manifest,json_mutate(lambda d:d["moves"][0].__setitem__("source_tree_sha","0"*40)),"MOVE-001 preservation-tree drift",errors)
        text_mutate(repo,manifest,json_mutate(lambda d:d.__setitem__("status","candidate_ready" if d.get("status")=="accepted" else "accepted")),"DPTN-B artifact/status divergence",errors)
        text_mutate(repo,"docs/history/README.md",lambda t:t.replace("**Authority:** HISTORY / PROVENANCE ONLY — NOT CURRENT SEMANTIC AUTHORITY","**Authority:** HISTORY"),"history role marker removal",errors)
        text_mutate(repo,"docs/history/README.md",lambda t:t.replace("# DMTZ Documentation History","# DMTZ Documentation History\n\n**Authority:** CANONICAL CURRENT AUTHORITY",1),"history claims current authority",errors)
        text_mutate(repo,"docs/documentation_topology_normalization/fixtures/dptn_b_history_scenarios.yaml",lambda t:t.replace("DPTNB-24","DPTNB-99",1),"DPTN-B scenario identity drift",errors)
        text_mutate(repo,"docs/implementation/README.md",lambda t:t.replace("Implementation 001-A — BLOCKED / NOT STARTED","Implementation 001-A — NEXT / READY / NOT STARTED",1),"implementation gate bypass",errors)
        path_move(repo,"docs/history/reference-legacy","missing relocated reference tree",errors)
        text_mutate(repo,"docs/documentation_topology_normalization/collision_register.md",lambda t:t.replace("COL-001 — RESOLVED BY DPTN-B","COL-001 — RESOLUTION LOST",1),"DPTN-B collision-resolution regression",errors)
        path_move(repo,"docs/agentic_development_foundation","premature ADF bulk move",errors)

    for e in errors: print("ERROR",e)
    print(f"DPTN-B history guard tests: {len(errors)} error(s), 12 negative control(s)")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
