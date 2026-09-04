#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

HLTH_DOCS=(
'docs/canonical/contracts/health-quality-timing/measurement-applicability.md',
'docs/canonical/contracts/health-quality-timing/structural-compatibility.md',
'docs/canonical/contracts/health-quality-timing/baseline-comparability.md',
'docs/canonical/contracts/health-quality-timing/normative-assessment.md',
'docs/canonical/contracts/health-quality-timing/transformation-reconciliation.md',
'docs/canonical/contracts/health-quality-timing/composite-health-readiness-timing.md')
HLTH_RE=re.compile(r'^### (HLTH-\d{3}) —',re.M)
LATER=('OPS','EXPL','INTG','ARCH')

def marker(text):
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:return 'candidate'
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text())
    hlth=inv['stable_families']['HLTH']; state=hlth.get('migration_state')
    if state not in {'candidate_ready','canonicalized'}: errors.append(f'HLTH must be candidate_ready/canonicalized during CKR-E, found {state!r}')
    expected='candidate' if state=='candidate_ready' else 'canonical'
    if hlth.get('migration_group')!='CKR-E': errors.append('HLTH migration_group must remain CKR-E')
    if hlth.get('target_documents')!=list(HLTH_DOCS): errors.append('HLTH target_documents do not match CKR-E canonical topology')
    ids=[]; corpus=[]
    for rel in HLTH_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing HLTH canonical target {rel}'); continue
        text=p.read_text(encoding='utf-8'); corpus.append(text); ids+=HLTH_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if '**Migration record:** `stable_family.HLTH`' not in text: errors.append(f'{rel}: missing stable-family migration record')
        if 'docs/concepts/phase_006/' not in text: errors.append(f'{rel}: missing Phase 006 provenance')
    expected_ids=[f'HLTH-{i:03d}' for i in range(1,67)]
    if sorted(ids)!=expected_ids or len(ids)!=66: errors.append(f'HLTH headings must cover HLTH-001..HLTH-066 exactly once; found {len(ids)}')
    joined='\n'.join(corpus)
    if 'HLTH-067' in joined: errors.append('unaccepted HLTH-067 present in canonical health corpus')
    matrix=repo/'docs/canonical_knowledge_retrofit/ckr_e_semantic_conservation_matrix.md'
    if not matrix.is_file(): errors.append('missing CKR-E semantic conservation matrix')
    else:
        mt=matrix.read_text(encoding='utf-8')
        required=(
        'metric definition ≠ Observation ≠ Assessment',
        'semantic applicability ≠ profile selection ≠ computability ≠ current availability ≠ Assessment outcome',
        'declared/governed schema meaning ≠ structural Expectation ≠ proposed/planned state ≠ realized Observation/Change ≠ compatibility Assessment',
        'Observation ≠ reference membership ≠ Baseline ≠ comparative Assessment ≠ normative Expectation',
        'Lineage does not propagate status',
        'component Assessment ≠ bounded composite health',
        'eligible ≠ suitable ≠ ready ≠ control authorization ≠ Gate decision ≠ enforcement ≠ execution',
        'no universal health, confidence, anomaly or comparability score')
        for phrase in required:
            if phrase not in mt: errors.append(f'CKR-E matrix missing boundary: {phrase}')
    # Prior cutovers remain canonical.
    for fam in ('SYN','REF','AUTH'):
        if inv['stable_families'][fam]['migration_state']!='canonicalized': errors.append(f'{fam} must remain canonicalized during CKR-E')
    vocab=next(r for r in inv['records'] if r['record_id']=='reference.authority_vocabulary')
    if vocab['migration_state']!='canonicalized': errors.append('authority vocabulary must remain canonicalized during CKR-E')
    concepts=[r for r in inv['records'] if r.get('kind')=='concept']
    if len(concepts)!=24 or any(r['migration_state']!='canonicalized' for r in concepts): errors.append('all 24 concepts must remain canonicalized during CKR-E')
    for fam in LATER:
        item=inv['stable_families'][fam]
        if item.get('migration_state')!='legacy_authoritative': errors.append(f'{fam} ownership moved early during CKR-E')
    fixture=repo/'docs/canonical_knowledge_retrofit/fixtures/ckr_e_health_quality_scenarios.yaml'
    if not fixture.is_file(): errors.append('missing CKR-E fixture catalog')
    else:
        count=len(re.findall(r'^\s*- id: CKRE-\d{2}$',fixture.read_text(encoding='utf-8'),re.M))
        if count<36: errors.append(f'CKR-E fixture catalog too small; found {count}')
    for e in errors: print('ERROR',e)
    print(f'CKR-E health/quality validation: {len(errors)} error(s), HLTH={len(ids)}/66, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
