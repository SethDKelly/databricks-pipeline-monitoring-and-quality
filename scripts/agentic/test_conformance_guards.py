#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path

def run(repo:Path,script:str)->int:
    target=repo/'scripts/agentic'/script; compat=repo/'scripts/agentic/run_ckr_with_history_compat.py'
    if script.startswith(('validate_ckr_','test_ckr_')) or script in {'validate_canonical_knowledge.py','validate_agentic_references.py'}:
        cmd=[sys.executable,str(compat),f'scripts/agentic/{script}','--repo',str(repo)]
    else: cmd=[sys.executable,str(target),'--repo',str(repo)]
    return subprocess.run(cmd,cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode

def mutate(repo:Path,rel:str,fn,script:str,label:str,errors:list[str]):
    p=repo/rel; old=p.read_text(encoding='utf-8')
    try:
        new=fn(old)
        if new==old: errors.append(f'{label}: no-op mutation'); return
        p.write_text(new,encoding='utf-8')
        if run(repo,script)==0: errors.append(f'{label}: validator unexpectedly passed')
        else: print('PASS negative control:',label)
    finally:p.write_text(old,encoding='utf-8')

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); src=Path(ap.parse_args().repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix='dmtz-conformance-') as td:
        repo=Path(td)/'repo'; shutil.copytree(src,repo,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'),symlinks=True)
        mutate(repo,'IMPLEMENTATION.md',lambda t:re.sub(r'DPTN status mirror: .*?$','DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.',t,count=1,flags=re.M),'validate_dptn_status.py','stale DPTN status mirror',errors)
        mutate(repo,'IMPLEMENTATION.md',lambda t:re.sub(r'ADF status mirror: .*?$','ADF status mirror: COMPLETE ADF-A–ADF-E; NEXT ADF-F.',t,count=1,flags=re.M),'validate_status_drift.py','stale ADF status mirror',errors)
        mutate(repo,'IMPLEMENTATION.md',lambda t:re.sub(r'CKR status mirror: .*?$','CKR status mirror: COMPLETE CKR-A; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.',t,count=1,flags=re.M),'validate_ckr_status.py','stale CKR status mirror',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',lambda t:t.replace('"concept_count": 24','"concept_count": 25',1),'validate_dptn_d_decomposition.py','concept conservation drift',errors)
        mutate(repo,'docs/agentic_development_foundation/stable_id_registry.json',lambda t:t.replace('"max": 500','"max": 501',1),'validate_dptn_d_decomposition.py','stable-ID registry drift',errors)
        mutate(repo,'docs/history/README.md',lambda t:t.replace('HISTORY / PROVENANCE ONLY','HISTORY ONLY',1),'validate_dptn_d_decomposition.py','history authority weakening',errors)
        mutate(repo,'docs/implementation/README.md',lambda t:t.replace('Implementation 001-A — BLOCKED / NOT STARTED','Implementation 001-A — NEXT / READY / NOT STARTED',1),'validate_dptn_d_decomposition.py','implementation gate bypass',errors)
        mutate(repo,'docs/agentic_development_foundation/runtime_compatibility_evidence.json',lambda t:t.replace('"runtime_status": "unverified"','"runtime_status": "supported"',1),'validate_adf_g_compatibility.py','fabricated provider runtime support',errors)
        mutate(repo,'docs/agentic_development_foundation/databricks_vendor_skills_profile.json',lambda t:t.replace('"automatic_new_skills": false','"automatic_new_skills": true',1),'validate_databricks_agent_skills.py','automatic vendor skill expansion',errors)
        mutate(repo,'knowledge/project/authority.md',lambda t:t.replace('type:','missing_type:',1),'validate_okf.py','malformed OKF metadata',errors)
        mutate(repo,'.cursor/rules/00-implementation-routing.mdc',lambda t:t.replace('alwaysApply: false','alwaysApply: true',1),'validate_agent_adapters.py','always-applied Cursor routing rule',errors)
        mutate(repo,'AGENTS.md',lambda t:t+'\nARCH-501\n','validate_agentic_references.py','unaccepted stable ID citation',errors)
    for e in errors: print('ERROR',e)
    print(f'Cross-cutting conformance guards: {len(errors)} error(s), 12 negative control(s)'); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
