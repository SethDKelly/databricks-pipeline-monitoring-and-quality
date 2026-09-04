#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

OPS_DOCS=(
'docs/canonical/contracts/operations/lineage-topology.md',
'docs/canonical/contracts/operations/change-realization.md',
'docs/canonical/contracts/operations/prospective-review.md',
'docs/canonical/contracts/operations/execution-reconstruction.md',
'docs/canonical/contracts/operations/investigation-causality.md',
'docs/canonical/contracts/operations/impact-exposure-consequence.md',
'docs/canonical/contracts/operations/propagation-safeguard.md',
'docs/canonical/contracts/operations/execution-gate-control.md')
OPS_RE=re.compile(r'^### (OPS-\d{3}) —',re.M)
STATE_RE=re.compile(r'^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$',re.M)
LATER={'EXPL':'G','INTG':'H','ARCH':'I'}

def marker(text):
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:return 'candidate'
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8'))
    ops=inv['stable_families']['OPS']; state=ops.get('migration_state')
    if state not in {'candidate_ready','canonicalized'}: errors.append(f'OPS must be candidate_ready/canonicalized during/after CKR-F, found {state!r}')
    expected='candidate' if state=='candidate_ready' else 'canonical'
    if ops.get('migration_group')!='CKR-F': errors.append('OPS migration_group must remain CKR-F')
    if ops.get('target_documents')!=list(OPS_DOCS): errors.append('OPS target_documents do not match CKR-F canonical topology')
    ids=[]; corpus=[]
    for rel in OPS_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing OPS canonical target {rel}'); continue
        text=p.read_text(encoding='utf-8'); corpus.append(text); ids+=OPS_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if '**Migration record:** `stable_family.OPS`' not in text: errors.append(f'{rel}: missing stable-family migration record')
        if 'docs/concepts/phase_007/' not in text: errors.append(f'{rel}: missing Phase 007 provenance')
    expected_ids=[f'OPS-{i:03d}' for i in range(1,124)]
    if sorted(ids)!=expected_ids or len(ids)!=123: errors.append(f'OPS headings must cover OPS-001..OPS-123 exactly once; found {len(ids)}')
    joined='\n'.join(corpus)
    if 'OPS-124' in joined: errors.append('unaccepted OPS-124 present in canonical operations corpus')
    matrix=repo/'docs/canonical_knowledge_retrofit/ckr_f_semantic_conservation_matrix.md'
    if not matrix.is_file(): errors.append('missing CKR-F semantic conservation matrix')
    else:
        mt=matrix.read_text(encoding='utf-8')
        required=('Lineage ≠ causality','reachable ≠ operationally relevant ≠ exposed/affected','Change Intent ≠ Deployment ≠ Change','candidate ≠ exposure ≠ effect ≠ consequence ≠ cause','expected work ≠ opportunity ≠ Gate state ≠ actual execution','lead ≠ Causal Claim','confirmation requires REF-017 plus AUTH-034','exposed ≠ downstream effect ≠ consequence ≠ causal attribution','not exposed ≠ prevented by Safeguard','Propagation Safeguard ≠ Execution Gate','readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution','actual retained historical state ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation','no universal topology/completeness/risk/RCA/Impact/control/replay score')
        for phrase in required:
            if phrase not in mt: errors.append(f'CKR-F matrix missing boundary: {phrase}')
    for fam in ('SYN','REF','AUTH','HLTH'):
        if inv['stable_families'][fam]['migration_state']!='canonicalized': errors.append(f'{fam} must remain canonicalized during/after CKR-F')
    vocab=next(r for r in inv['records'] if r['record_id']=='reference.authority_vocabulary')
    if vocab['migration_state']!='canonicalized': errors.append('authority vocabulary must remain canonicalized during/after CKR-F')
    concepts=[r for r in inv['records'] if r.get('kind')=='concept']
    if len(concepts)!=24 or any(r['migration_state']!='canonicalized' for r in concepts): errors.append('all 24 concepts must remain canonicalized during/after CKR-F')
    states_by_group={k:v for k,v in STATE_RE.findall((repo/'docs/canonical_knowledge_retrofit/README.md').read_text(encoding='utf-8'))}
    for fam,letter in LATER.items():
        item=inv['stable_families'][fam]
        if item.get('migration_group')!=f'CKR-{letter}': errors.append(f'{fam}: migration ownership moved away from CKR-{letter}')
        if item.get('migration_state') not in {'legacy_authoritative','candidate_ready','canonicalized'}: errors.append(f'{fam}: invalid migration state')
        phase_state=states_by_group.get(letter,'')
        if phase_state in {'PLANNED','NEXT / READY'} and item.get('migration_state')!='legacy_authoritative': errors.append(f'{fam}: moved before CKR-{letter} entered execution')
    fixture=repo/'docs/canonical_knowledge_retrofit/fixtures/ckr_f_operations_scenarios.yaml'
    if not fixture.is_file(): errors.append('missing CKR-F fixture catalog')
    else:
        count=len(re.findall(r'^\s*- id: CKRF-\d{2}$',fixture.read_text(encoding='utf-8'),re.M))
        if count<40: errors.append(f'CKR-F fixture catalog too small; found {count}')
    for e in errors: print('ERROR',e)
    print(f'CKR-F operations validation: {len(errors)} error(s), OPS={len(ids)}/123, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
