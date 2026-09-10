#!/usr/bin/env python3
"""Run completed CKR checks against their accepted-era path/routing view.

DPTN moved historical design sources, promoted first-class current semantic owners,
archived completed CKR evidence, replaced the hand-authored OKF plane with generated
compatibility output, and finally retired the live docs/canonical compatibility
namespace. Completed CKR checks retain the exact topology/evidence/routing view
accepted at CKR exit through an ephemeral projection only.

All compatibility projection is temporary, never committed, never participates in
current owner selection, and cannot authorize semantic or implementation changes.
"""
from __future__ import annotations
import argparse,json,os,shutil,subprocess,sys
from pathlib import Path

LEGACY_HISTORY={"docs/concepts":"history/phases","docs/reference":"history/reference-legacy","docs/foundation":"history/foundation","docs/planning":"history/planning","docs/decisions":"history/decisions","docs/design_history":"history/design-history"}
FAMILIES=("concepts","architecture","authority","contracts","experience","invariants","policies","reference")
LITERAL_CKR_ROUTE_CHECKS={"validate_ckr_j_routing.py","validate_ckr_status.py"}

def back_history(path:str)->str:
    for new,old in (("docs/history/phases","docs/concepts"),("docs/history/reference-legacy","docs/reference"),("docs/history/foundation","docs/foundation"),("docs/history/planning","docs/planning"),("docs/history/decisions","docs/decisions"),("docs/history/design-history","docs/design_history")):
        if path==new or path.startswith(new+"/"):return old+path[len(new):]
    return path

def back_current(path:str)->str:
    for fam in FAMILIES:
        new=f"docs/{fam}"
        if path==new or path.startswith(new+"/"):return f"docs/canonical/{fam}"+path[len(new):]
    return path

def legacy_inventory_view(data:dict)->dict:
    d=json.loads(json.dumps(data));d["canonical_root"]="docs/canonical";d.pop("canonical_layout",None);d.pop("canonical_owner_roots",None);d["design_history_index"]="docs/design_history/README.md"
    for rec in d.get("records",[]):rec["current_owner"]=back_history(rec.get("current_owner",""));rec["target_owner"]=back_current(rec.get("target_owner",""))
    for fam in d.get("stable_families",{}).values():
        fam["current_owner_root"]=back_history(fam.get("current_owner_root",""));fam["target_owner_root"]=back_current(fam.get("target_owner_root",""));fam["target_documents"]=[back_current(x) for x in fam.get("target_documents",[])]
    for rec in d.get("architecture_segments",[]):rec["current_owner"]=back_history(rec.get("current_owner",""));rec["target_owner"]=back_current(rec.get("target_owner",""))
    for item in d.get("history_sources",[]):item["path"]=back_history(item.get("path",""))
    return d

def project_ckr_evidence(repo:Path)->list[Path]:
    hist=repo/"docs/history/retrofits/ckr";cur=repo/"docs/canonical_knowledge_retrofit";created=[]
    if not hist.is_dir():return created
    for child in hist.iterdir():
        target=cur/child.name
        if target.exists() or target.is_symlink():continue
        os.symlink(os.path.relpath(child,target.parent),target,target_is_directory=child.is_dir());created.append(target)
    return created

def project_ckr_knowledge(repo:Path):
    """Restore the pre-DPTN-E authored OKF tree only while completed CKR checks run."""
    archive=repo/"docs/history/routing/okf-pre-dptn-e";live=repo/"knowledge";parked=repo/".dptn_e_generated_knowledge"
    if not archive.is_dir():
        yield;return
    if parked.exists() or parked.is_symlink():raise RuntimeError("reserved DPTN-E compatibility path already exists")
    if not live.is_dir():raise RuntimeError("current generated knowledge tree missing")
    live.rename(parked);shutil.copytree(archive,live,symlinks=True)
    try:yield
    finally:
        if live.exists():shutil.rmtree(live)
        parked.rename(live)

def pre_c_history_projection(repo:Path)->list[Path]:
    created=[]
    for rel,target in LEGACY_HISTORY.items():
        p=repo/rel
        if p.exists() or p.is_symlink():continue
        p.parent.mkdir(parents=True,exist_ok=True);os.symlink(target,p,target_is_directory=True);created.append(p)
    return created

def ensure_legacy_root(repo:Path):
    """Create docs/canonical only for the lifetime of a completed-CKR projection.

    Returns whether the root was created here and, when the root existed, the set of
    preexisting family symlinks so cleanup can faithfully restore only prior state.
    """
    root=repo/"docs/canonical";created_root=False;preexisting={}
    if root.is_symlink():raise RuntimeError("docs/canonical may not be a symlink during CKR compatibility projection")
    if not root.exists():root.mkdir(parents=True);created_root=True
    elif not root.is_dir():raise RuntimeError("docs/canonical compatibility path is not a directory")
    for fam in FAMILIES:
        p=root/fam
        if p.is_symlink():preexisting[fam]=os.readlink(p)
        elif p.exists():raise RuntimeError(f"legacy canonical family path is not a redirect: {p}")
    return root,created_root,preexisting

def cleanup_legacy_root(root:Path,created_root:bool,preexisting:dict[str,str])->None:
    for fam in FAMILIES:
        p=root/fam
        if p.is_dir() and not p.is_symlink():shutil.rmtree(p)
        elif p.is_symlink() or p.exists():p.unlink()
        if fam in preexisting:os.symlink(preexisting[fam],p,target_is_directory=True)
    if created_root:
        # A completed-CKR check may have temporarily rewritten/created README.md.
        for child in list(root.iterdir()):
            if child.is_dir() and not child.is_symlink():shutil.rmtree(child)
            else:child.unlink()
        root.rmdir()

def accepted_routing_projection(repo:Path,inventory_path:Path):
    original_inventory=inventory_path.read_text(encoding="utf-8");data=json.loads(original_inventory);root,created_root,saved=ensure_legacy_root(repo);readme=root/"README.md";readme_existed=readme.is_file();original_readme=readme.read_text(encoding="utf-8") if readme_existed else ""
    try:
        for fam in FAMILIES:
            legacy=root/fam
            if legacy.is_symlink():legacy.unlink()
            shutil.copytree(repo/f"docs/{fam}",legacy,symlinks=True)
        inventory_path.write_text(json.dumps(legacy_inventory_view(data),indent=2)+"\n",encoding="utf-8")
        readme.write_text("**Authority state:** CANONICALIZATION COMPLETE — CKR EXIT ACCEPTED\n\n"+original_readme,encoding="utf-8")
        yield
    finally:
        inventory_path.write_text(original_inventory,encoding="utf-8")
        if readme_existed:readme.write_text(original_readme,encoding="utf-8")
        elif readme.exists():readme.unlink()
        cleanup_legacy_root(root,created_root,saved)

def post_c_projection(repo:Path,inventory_path:Path):
    original_inventory=inventory_path.read_text(encoding="utf-8");data=json.loads(original_inventory);hidden=repo/"docs/.dptn_ckr_current";created=[];root,created_root,saved=ensure_legacy_root(repo)
    if hidden.exists() or hidden.is_symlink():raise RuntimeError("reserved CKR compatibility path already exists")
    hidden.mkdir()
    try:
        for fam in FAMILIES:
            current=repo/f"docs/{fam}";legacy=root/fam;parked=hidden/fam
            if not current.is_dir() or current.is_symlink():raise RuntimeError(f"missing normalized current root {current}")
            if legacy.is_symlink():legacy.unlink()
            current.rename(parked);os.symlink(f"../.dptn_ckr_current/{fam}",legacy,target_is_directory=True)
        for fam,target in (("concepts","history/phases"),("reference","history/reference-legacy")):
            p=repo/f"docs/{fam}";os.symlink(target,p,target_is_directory=True);created.append(p)
        for rel,target in (("docs/foundation","history/foundation"),("docs/planning","history/planning"),("docs/decisions","history/decisions"),("docs/design_history","history/design-history")):
            p=repo/rel
            if not p.exists() and not p.is_symlink():os.symlink(target,p,target_is_directory=True);created.append(p)
        inventory_path.write_text(json.dumps(legacy_inventory_view(data),indent=2)+"\n",encoding="utf-8");yield
    finally:
        inventory_path.write_text(original_inventory,encoding="utf-8")
        for p in reversed(created):
            try:p.unlink()
            except FileNotFoundError:pass
        for fam in reversed(FAMILIES):
            legacy=root/fam;current=repo/f"docs/{fam}";parked=hidden/fam
            if legacy.is_symlink():legacy.unlink()
            if parked.exists():parked.rename(current)
        try:hidden.rmdir()
        except OSError:pass
        cleanup_legacy_root(root,created_root,saved)

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("script");ap.add_argument("args",nargs=argparse.REMAINDER);ns=ap.parse_args();repo=Path(__file__).resolve().parents[2];inventory=repo/"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    evidence=project_ckr_evidence(repo);kg=project_ckr_knowledge(repo);next(kg)
    try:
        data=json.loads(inventory.read_text(encoding="utf-8"));post=data.get("canonical_layout")=="first_class_dptn_c" or data.get("canonical_root")=="docs"
        if not post:
            created=pre_c_history_projection(repo)
            try:return subprocess.run([sys.executable,str(repo/ns.script),*ns.args],cwd=repo).returncode
            finally:
                for p in reversed(created):
                    try:p.unlink()
                    except FileNotFoundError:pass
        projection=accepted_routing_projection if Path(ns.script).name in LITERAL_CKR_ROUTE_CHECKS else post_c_projection;gen=projection(repo,inventory);next(gen)
        try:return subprocess.run([sys.executable,str(repo/ns.script),*ns.args],cwd=repo).returncode
        finally:
            try:next(gen)
            except StopIteration:pass
    finally:
        try:next(kg)
        except StopIteration:pass
        for p in reversed(evidence):
            try:p.unlink()
            except FileNotFoundError:pass
if __name__=="__main__":raise SystemExit(main())
