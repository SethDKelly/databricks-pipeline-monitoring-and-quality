#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path

def run(repo:Path)->int:
    return subprocess.run([sys.executable,str(repo/'scripts/agentic/validate_dptn_f_rebinding.py'),'--repo',str(repo)],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode

def mutate(repo:Path,rel:str,fn,label:str,errors:list[str]):
    p=repo/rel;old=p.read_text(encoding='utf-8')
    try:
        new=fn(old)
        if new==old: errors.append(f'{label}: no-op mutation');return
        p.write_text(new,encoding='utf-8')
        if run(repo)==0: errors.append(f'{label}: validator unexpectedly passed')
        else: print('PASS negative control:',label)
    finally:p.write_text(old,encoding='utf-8')

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--repo',default='.');src=Path(ap.parse_args().repo).resolve();errors=[]
    with tempfile.TemporaryDirectory(prefix='dptn-f-guards-') as td:
        repo=Path(td)/'repo';shutil.copytree(src,repo,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'),symlinks=True)
        mutate(repo,'docs/agentic_development_foundation/tool_compatibility.json',lambda t:t.replace('"knowledge_entry": "docs/index.md"','"knowledge_entry": "knowledge/index.md"',1),'tool primary discovery regression',errors)
        mutate(repo,'.agents/skills/resolve-context/SKILL.md',lambda t:t.replace('docs/index.md','knowledge/index.md',1),'resolve-context discovery regression',errors)
        mutate(repo,'.cursor/rules/10-design-change-control.mdc',lambda t:t.replace('docs/architecture/reference-architecture.md','docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md',1),'Phase 010 rule regression',errors)
        mutate(repo,'.cursor/rules/10-design-change-control.mdc',lambda t:t.replace('docs/reference/concept-design-method.md','docs/foundation/004_concept_design_method.md',1),'foundation rule regression',errors)
        mutate(repo,'scripts/agentic/knowledge_impact.py',lambda t:t.replace('canonical_owner_roots','docs/canonical/',1),'impact routing compatibility regression',errors)
        mutate(repo,'scripts/agentic/validate_agentic_references.py',lambda t:t+'\n# dptn_d_history_fallback\n','current-link history fallback regression',errors)
        mutate(repo,'docs/documentation_topology_normalization/dptn_f_rebinding_manifest.json',lambda t:t.replace('"first_match_canonicality": false','"first_match_canonicality": true',1),'first-match canonicality regression',errors)
        mutate(repo,'knowledge/index.md',lambda t:t.replace('GENERATED OKF PROJECTION — DO NOT HAND-EDIT.','HAND AUTHORED KNOWLEDGE',1),'generated OKF authority regression',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',lambda t:t.replace('"concept_count":24','"concept_count":25',1),'concept conservation drift',errors)
        mutate(repo,'docs/agentic_development_foundation/stable_id_registry.json',lambda t:t.replace('"max": 500','"max": 501',1),'stable-ID conservation drift',errors)
        mutate(repo,'docs/implementation/README.md',lambda t:t.replace('Implementation 001-A — BLOCKED / NOT STARTED','Implementation 001-A — NEXT / READY / NOT STARTED',1),'implementation gate bypass',errors)
        mutate(repo,'docs/documentation_topology_normalization/dptn_f_rebinding_manifest.json',lambda t:t.replace('"authorized_move_ids": ["MOVE-019"]','"authorized_move_ids": ["MOVE-019", "MOVE-020"]',1),'premature DPTN-G move authorization',errors)
    for e in errors: print('ERROR',e)
    print(f'DPTN-F rebinding guards: {len(errors)} error(s), 12 negative control(s)')
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
