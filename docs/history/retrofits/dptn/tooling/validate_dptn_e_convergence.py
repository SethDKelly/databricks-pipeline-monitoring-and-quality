#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess,sys
from pathlib import Path

ROOT=Path('docs/documentation_topology_normalization')
STATE_RE=re.compile(r'^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$',re.M)
FIXTURE_RE=re.compile(r'^\s*-\s+id:\s+(DPTNE-\d{2})\s*$',re.M)
ARCHIVE_SHA='7e4e6bf6c5f57316beb98f511b8ee078de8c55a8'
GENERATED_SHA='8a8ac74f7eb5afcd7245043501103b0b691101f6'

def git_object(repo:Path,spec:str)->str|None:
    p=subprocess.run(['git','rev-parse',spec],cwd=repo,text=True,capture_output=True)
    return p.stdout.strip() if p.returncode==0 else None

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); repo=Path(ap.parse_args().repo).resolve(); errors=[]
    required=(ROOT/'README.md',ROOT/'dptn_e_convergence_manifest.json',ROOT/'dptn_e_execution_review.md',ROOT/'fixtures/dptn_e_convergence_scenarios.yaml',Path('docs/index.md'),Path('docs/routing/okf_projection.json'),Path('scripts/agentic/generate_okf_projection.py'),Path('docs/history/routing/okf-pre-dptn-e'),Path('docs/canonical/README.md'),Path('docs/history/README.md'),Path('docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json'),Path('docs/agentic_development_foundation/stable_id_registry.json'))
    for rel in required:
        if not (repo/rel).exists(): errors.append(f'missing DPTN-E artifact/dependency: {rel}')
    if errors:
        for e in errors: print('ERROR',e)
        return 1
    states={k:v for k,v in STATE_RE.findall((repo/ROOT/'README.md').read_text(encoding='utf-8'))}; e_state=states.get('E')
    if any(states.get(c)!='COMPLETE / ACCEPTED' for c in 'ABCD') or e_state not in {'IN EXECUTION','COMPLETE / ACCEPTED'}:
        errors.append(f'DPTN-E requires A-D complete and E active/complete; states={states}')
    manifest=json.loads((repo/ROOT/'dptn_e_convergence_manifest.json').read_text(encoding='utf-8'))
    expected_status='accepted' if e_state=='COMPLETE / ACCEPTED' else 'candidate_ready'
    if manifest.get('status')!=expected_status: errors.append(f'DPTN-E manifest status must be {expected_status}')
    if manifest.get('phase')!='DPTN-E' or manifest.get('authorized_move_ids')!=['MOVE-017','MOVE-018']: errors.append('DPTN-E may authorize MOVE-017/MOVE-018 only')
    if manifest.get('authority_change') is not False or manifest.get('implementation_change') is not False: errors.append('DPTN-E may not change semantic/implementation authority')
    if manifest.get('discovery_root')!='docs/index.md' or manifest.get('knowledge_mode')!='generated_okf_v0.2_compatibility_projection': errors.append('DPTN-E discovery/projection contract drifted')
    spec=json.loads((repo/'docs/routing/okf_projection.json').read_text(encoding='utf-8'))
    if spec.get('authority')!='DERIVED ROUTING ONLY — NOT SEMANTIC AUTHORITY' or spec.get('discovery_root')!='docs/index.md' or spec.get('generated_root')!='knowledge': errors.append('OKF projection specification authority/root contract drifted')
    counts=spec.get('expected_counts',{})
    if counts!={'domains':7,'project':9,'workflow_catalog_entries':13,'implementation_catalog_entries':11,'concept_documents':16,'total_markdown_files':22}: errors.append(f'OKF projection expected counts drifted: {counts}')
    for route in spec.get('domains',[])+spec.get('project',[]):
        resource=route.get('resource','')
        if not resource or not (repo/resource).exists(): errors.append(f'projection route resource missing: {resource!r}')
        for related in route.get('related',[]):
            if not (repo/related).exists(): errors.append(f'projection related route missing: {related}')
    dindex=(repo/'docs/index.md').read_text(encoding='utf-8')
    for token in ('ROUTING / DISCOVERY ROOT — NOT A SEMANTIC OWNER','single authored human/tool-neutral discovery root','generated compatibility projection','DPTN-F'):
        if token not in dindex: errors.append(f'docs/index.md missing discovery boundary token {token!r}')
    ctext=(repo/'docs/canonical/README.md').read_text(encoding='utf-8')
    for token in ('ROUTING / COMPATIBILITY ONLY','not a substantive semantic owner','docs/index.md','DPTN-E'):
        if token not in ctext: errors.append(f'docs/canonical/README.md missing compatibility marker {token!r}')
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in ctext: errors.append('docs/canonical/README.md may not regain substantive semantic authority')
    htext=(repo/'docs/history/README.md').read_text(encoding='utf-8')
    if 'HISTORY / PROVENANCE ONLY' not in htext or 'okf-pre-dptn-e' not in htext: errors.append('history index must preserve DPTN-E authored-routing provenance')
    if (repo/'.git').exists():
        archive=git_object(repo,'HEAD:docs/history/routing/okf-pre-dptn-e'); generated=git_object(repo,'HEAD:knowledge')
        if archive!=ARCHIVE_SHA: errors.append(f'pre-DPTN-E authored knowledge tree was not preserved exactly: {archive}')
        if e_state=='COMPLETE / ACCEPTED' and generated!=GENERATED_SHA: errors.append(f'generated knowledge tree differs from accepted DPTN-E tree: {generated}')
    p=subprocess.run([sys.executable,str(repo/'scripts/agentic/generate_okf_projection.py'),'--repo',str(repo),'--check'],cwd=repo,text=True,capture_output=True)
    if p.returncode: errors.append('generated OKF projection check failed: '+(p.stdout+p.stderr).strip())
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8')); reg=json.loads((repo/'docs/agentic_development_foundation/stable_id_registry.json').read_text(encoding='utf-8'))
    total=sum(int(x['max'])-int(x['min'])+1 for x in reg.get('families',{}).values())
    if inv.get('concept_count')!=24: errors.append(f'concept count changed: {inv.get("concept_count")}')
    if total!=1237 or len(reg.get('families',{}))!=8: errors.append(f'stable-ID baseline changed: families={len(reg.get("families",{}))}, ids={total}')
    impl=(repo/'docs/implementation/README.md').read_text(encoding='utf-8')
    if 'Implementation 001-A — BLOCKED / NOT STARTED' not in impl: errors.append('Implementation 001-A gate released during DPTN-E')
    fixtures=(repo/ROOT/'fixtures/dptn_e_convergence_scenarios.yaml').read_text(encoding='utf-8'); ids=FIXTURE_RE.findall(fixtures)
    if ids!=[f'DPTNE-{i:02d}' for i in range(1,25)]: errors.append('DPTN-E fixtures must contain DPTNE-01..DPTNE-24 exactly once/in order')
    review=(repo/ROOT/'dptn_e_execution_review.md').read_text(encoding='utf-8'); marker='**Status:** ACCEPTED — DPTN-E COMPLETE' if e_state=='COMPLETE / ACCEPTED' else '**Status:** IN EXECUTION'
    if marker not in review: errors.append(f'DPTN-E execution review missing state marker {marker!r}')
    for e in errors: print('ERROR',e)
    print(f'DPTN-E convergence validation: {len(errors)} error(s), scenarios={len(ids)}/24, stable_ids={total}, state={e_state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
