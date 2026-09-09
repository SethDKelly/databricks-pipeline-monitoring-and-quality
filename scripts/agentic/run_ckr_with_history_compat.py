#!/usr/bin/env python3
"""Run completed CKR checks against their accepted-era path view during DPTN.

DPTN-B moved historical design sources, DPTN-C moved substantive current owners to
first-class docs/<family> paths, and DPTN-D moved completed CKR execution evidence to
history. Completed CKR checks intentionally retain the topology/evidence view accepted
at CKR exit. This wrapper reconstructs only that bounded view for one completed check.

The projection is ephemeral, never committed, never participates in current owner
selection, and cannot authorize semantic or implementation changes.
"""
from __future__ import annotations
import argparse,json,os,shutil,subprocess,sys
from pathlib import Path

LEGACY_HISTORY={
"docs/concepts":"history/phases","docs/reference":"history/reference-legacy","docs/foundation":"history/foundation",
"docs/planning":"history/planning","docs/decisions":"history/decisions","docs/design_history":"history/design-history"}
FAMILIES=("concepts","architecture","authority","contracts","experience","invariants","policies","reference")
LITERAL_CKR_ROUTE_CHECKS={"validate_ckr_j_routing.py","validate_ckr_status.py"}

def back_history(path:str)->str:
    for new,old in (("docs/history/phases","docs/concepts"),("docs/history/reference-legacy","docs/reference"),("docs/history/foundation","docs/foundation"),("docs/history/planning","docs/planning"),("docs/history/decisions","docs/decisions"),("docs/history/design-history","docs/design_history")):
        if path==new or path.startswith(new+"/"): return old+path[len(new):]
    return path

def back_current(path:str)->str:
    for fam in FAMILIES:
        new=f"docs/{fam}"
        if path==new or path.startswith(new+"/"): return f"docs/canonical/{fam}"+path[len(new):]
    return path

def legacy_inventory_view(data:dict)->dict:
    d=json.loads(json.dumps(data)); d["canonical_root"]="docs/canonical"; d.pop("canonical_layout",None); d.pop("canonical_owner_roots",None); d["design_history_index"]="docs/design_history/README.md"
    for rec in d.get("records",[]): rec["current_owner"]=back_history(rec.get("current_owner","")); rec["target_owner"]=back_current(rec.get("target_owner",""))
    for fam in d.get("stable_families",{}).values():
        fam["current_owner_root"]=back_history(fam.get("current_owner_root","")); fam["target_owner_root"]=back_current(fam.get("target_owner_root","")); fam["target_documents"]=[back_current(x) for x in fam.get("target_documents",[])]
    for rec in d.get("architecture_segments",[]): rec["current_owner"]=back_history(rec.get("current_owner","")); rec["target_owner"]=back_current(rec.get("target_owner",""))
    for item in d.get("history_sources",[]): item["path"]=back_history(item.get("path",""))
    return d

def project_ckr_evidence(repo:Path)->list[Path]:
    """Rehydrate DPTN-D-retired CKR evidence at accepted-era paths for completed checks."""
    hist=repo/"docs/history/retrofits/ckr"; cur=repo/"docs/canonical_knowledge_retrofit"; created=[]
    if not hist.is_dir(): return created
    for child in hist.iterdir():
        target=cur/child.name
        if target.exists() or target.is_symlink(): continue
        rel=os.path.relpath(child,target.parent)
        os.symlink(rel,target,target_is_directory=child.is_dir()); created.append(target)
    return created

def pre_c_history_projection(repo:Path)->list[Path]:
    created=[]
    for rel,target in LEGACY_HISTORY.items():
        p=repo/rel
        if p.exists() or p.is_symlink(): continue
        p.parent.mkdir(parents=True,exist_ok=True); os.symlink(target,p,target_is_directory=True); created.append(p)
    return created

def accepted_routing_projection(repo:Path,inventory_path:Path):
    original_inventory=inventory_path.read_text(encoding="utf-8"); data=json.loads(original_inventory)
    readme=repo/"docs/canonical/README.md"; original_readme=readme.read_text(encoding="utf-8"); saved_redirects={}
    try:
        for fam in FAMILIES:
            current=repo/f"docs/{fam}"; legacy=repo/f"docs/canonical/{fam}"
            if not current.is_dir() or current.is_symlink(): raise RuntimeError(f"missing normalized current root {current}")
            if legacy.is_symlink(): saved_redirects[fam]=os.readlink(legacy); legacy.unlink()
            elif legacy.exists(): raise RuntimeError(f"legacy canonical route is not a redirect: {legacy}")
            shutil.copytree(current,legacy,symlinks=True)
        inventory_path.write_text(json.dumps(legacy_inventory_view(data),indent=2)+"\n",encoding="utf-8")
        readme.write_text("**Authority state:** CANONICALIZATION COMPLETE — CKR EXIT ACCEPTED\n\n"+original_readme,encoding="utf-8"); yield
    finally:
        inventory_path.write_text(original_inventory,encoding="utf-8"); readme.write_text(original_readme,encoding="utf-8")
        for fam in reversed(FAMILIES):
            legacy=repo/f"docs/canonical/{fam}"
            if legacy.is_dir() and not legacy.is_symlink(): shutil.rmtree(legacy)
            elif legacy.is_symlink(): legacy.unlink()
            os.symlink(saved_redirects.get(fam,f"../{fam}"),legacy,target_is_directory=True)

def post_c_projection(repo:Path,inventory_path:Path):
    original_inventory=inventory_path.read_text(encoding="utf-8"); data=json.loads(original_inventory); hidden=repo/"docs/.dptn_ckr_current"; created_history=[]; saved_redirects={}
    if hidden.exists() or hidden.is_symlink(): raise RuntimeError("reserved CKR compatibility path already exists")
    hidden.mkdir()
    try:
        for fam in FAMILIES:
            current=repo/f"docs/{fam}"; legacy=repo/f"docs/canonical/{fam}"; parked=hidden/fam
            if not current.is_dir() or current.is_symlink(): raise RuntimeError(f"missing normalized current root {current}")
            if legacy.is_symlink(): saved_redirects[fam]=os.readlink(legacy); legacy.unlink()
            elif legacy.exists(): raise RuntimeError(f"legacy canonical route is not a redirect: {legacy}")
            current.rename(parked); os.symlink(f"../.dptn_ckr_current/{fam}",legacy,target_is_directory=True)
        for fam,target in (("concepts","history/phases"),("reference","history/reference-legacy")):
            p=repo/f"docs/{fam}"; os.symlink(target,p,target_is_directory=True); created_history.append(p)
        for rel,target in (("docs/foundation","history/foundation"),("docs/planning","history/planning"),("docs/decisions","history/decisions"),("docs/design_history","history/design-history")):
            p=repo/rel
            if not p.exists() and not p.is_symlink(): os.symlink(target,p,target_is_directory=True); created_history.append(p)
        inventory_path.write_text(json.dumps(legacy_inventory_view(data),indent=2)+"\n",encoding="utf-8"); yield
    finally:
        inventory_path.write_text(original_inventory,encoding="utf-8")
        for p in reversed(created_history):
            try:p.unlink()
            except FileNotFoundError:pass
        for fam in reversed(FAMILIES):
            legacy=repo/f"docs/canonical/{fam}"; current=repo/f"docs/{fam}"; parked=hidden/fam
            if legacy.is_symlink(): legacy.unlink()
            if parked.exists(): parked.rename(current)
            os.symlink(saved_redirects.get(fam,f"../{fam}"),legacy,target_is_directory=True)
        try:hidden.rmdir()
        except OSError:pass

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("script"); ap.add_argument("args",nargs=argparse.REMAINDER); ns=ap.parse_args()
    repo=Path(__file__).resolve().parents[2]; inventory=repo/"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    evidence=project_ckr_evidence(repo)
    try:
        data=json.loads(inventory.read_text(encoding="utf-8")); post=data.get("canonical_layout")=="first_class_dptn_c" or data.get("canonical_root")=="docs"
        if not post:
            created=pre_c_history_projection(repo)
            try:return subprocess.run([sys.executable,str(repo/ns.script),*ns.args],cwd=repo).returncode
            finally:
                for p in reversed(created):
                    try:p.unlink()
                    except FileNotFoundError:pass
        projection=accepted_routing_projection if Path(ns.script).name in LITERAL_CKR_ROUTE_CHECKS else post_c_projection
        gen=projection(repo,inventory); next(gen)
        try:return subprocess.run([sys.executable,str(repo/ns.script),*ns.args],cwd=repo).returncode
        finally:
            try:next(gen)
            except StopIteration:pass
    finally:
        for p in reversed(evidence):
            try:p.unlink()
            except FileNotFoundError:pass
if __name__=="__main__": raise SystemExit(main())
