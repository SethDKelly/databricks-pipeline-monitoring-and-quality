#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path

VALIDATOR='validate_dptn_e_convergence.py'
def run(repo:Path)->int:return subprocess.run([sys.executable,str(repo/'scripts/agentic'/VALIDATOR),'--repo',str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
def mutate(repo:Path,rel:str,fn,label:str,errors:list[str]):
    p=repo/rel; old=p.read_text(encoding='utf-8')
    try:
        new=fn(old)
        if new==old: errors.append(f'{label}: mutation was a no-op'); return
        p.write_text(new,encoding='utf-8')
        if run(repo)==0: errors.append(f'{label}: DPTN-E validator unexpectedly passed')
        else: print('PASS negative control:',label)
    finally:p.write_text(old,encoding='utf-8')
def hide(repo:Path,rel:str,label:str,errors:list[str]):
    p=repo/rel; hold=repo/(rel+'.__guard__')
    try:
        p.rename(hold)
        if run(repo)==0: errors.append(f'{label}: DPTN-E validator unexpectedly passed')
        else: print('PASS negative control:',label)
    finally:
        if hold.exists():hold.rename(p)
def jmut(fn):
    def t(text):
        d=json.loads(text);fn(d);return json.dumps(d,indent=2)+'\n'
    return t
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--repo',default='.');src=Path(ap.parse_args().repo).resolve();errors=[]
    with tempfile.TemporaryDirectory(prefix='dmtz-dptne-') as td:
        repo=Path(td)/'repo';shutil.copytree(src,repo,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'),symlinks=True)
        hide(repo,'docs/index.md','missing authored discovery root',errors)
        mutate(repo,'docs/routing/okf_projection.json',jmut(lambda d:d.__setitem__('authority','SEMANTIC AUTHORITY')),'projection authority inflation',errors)
        mutate(repo,'knowledge/domains/acquisition.md',lambda t:t+'\nhand edit\n','generated knowledge hand edit',errors)
        hide(repo,'docs/history/routing/okf-pre-dptn-e','lost pre-convergence authored knowledge archive',errors)
        mutate(repo,'docs/canonical/README.md',lambda t:t+'\n**Authority:** CANONICAL CURRENT AUTHORITY\n','canonical compatibility authority inflation',errors)
        mutate(repo,'knowledge/index.md',lambda t:t+'\nextra\n','generated root drift',errors)
        mutate(repo,'docs/agentic_development_foundation/stable_id_registry.json',jmut(lambda d:d['families']['ARCH'].__setitem__('max',501)),'stable-ID baseline drift',errors)
        mutate(repo,'docs/implementation/README.md',lambda t:t.replace('Implementation 001-A — BLOCKED / NOT STARTED','Implementation 001-A — NEXT / READY / NOT STARTED',1),'implementation gate bypass',errors)
        mutate(repo,'docs/documentation_topology_normalization/README.md',lambda t:t.replace('DPTN-E — OKF / Documentation Root Convergence: COMPLETE / ACCEPTED','DPTN-E — OKF / Documentation Root Convergence: IN EXECUTION',1),'DPTN-E lifecycle divergence',errors)
        mutate(repo,'docs/routing/okf_projection.json',jmut(lambda d:d.__setitem__('discovery_root','knowledge/index.md')),'discovery root drift',errors)
        mutate(repo,'docs/routing/okf_projection.json',jmut(lambda d:d.__setitem__('generated_root','docs/knowledge')),'generated root drift',errors)
        hide(repo,'knowledge/project/authority.md','missing generated concept file',errors)
    for e in errors:print('ERROR',e)
    print(f'DPTN-E convergence guard tests: {len(errors)} error(s), 12 negative control(s)');return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
