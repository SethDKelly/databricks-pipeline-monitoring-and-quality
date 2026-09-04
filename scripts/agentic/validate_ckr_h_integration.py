#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

INTG_DOCS=(
'docs/canonical/contracts/integration/integration-contract-vocabulary.md',
'docs/canonical/contracts/integration/identity-governance-authority-sources.md',
'docs/canonical/contracts/integration/change-deployment-runtime-evidence.md',
'docs/canonical/contracts/integration/health-quality-measurement-sources.md',
'docs/canonical/contracts/integration/lineage-exposure-impact-sources.md',
'docs/canonical/contracts/integration/investigation-causality-control-sources.md',
'docs/canonical/contracts/integration/explanation-replay-disclosure-sources.md',
'docs/canonical/contracts/integration/cross-source-feasibility-retention-cost.md')
INTG_RE=re.compile(r'^### (INTG-\d{3}) —',re.M)
STATE_RE=re.compile(r'^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$',re.M)
LATER={'ARCH':'I'}

def marker(text):
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:return 'candidate'
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8'))
    intg=inv['stable_families']['INTG']; state=intg.get('migration_state')
    if state not in {'candidate_ready','canonicalized'}: errors.append(f'INTG must be candidate_ready/canonicalized during/after CKR-H, found {state!r}')
    expected='candidate' if state=='candidate_ready' else 'canonical'
    if intg.get('migration_group')!='CKR-H': errors.append('INTG migration_group must remain CKR-H')
    if intg.get('target_documents')!=list(INTG_DOCS): errors.append('INTG target_documents do not match CKR-H canonical topology')
    ids=[]; corpus=[]
    for rel in INTG_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing INTG canonical target {rel}'); continue
        text=p.read_text(encoding='utf-8'); corpus.append(text); ids+=INTG_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if '**Migration record:** `stable_family.INTG`' not in text: errors.append(f'{rel}: missing stable-family migration record')
        if 'docs/concepts/phase_009/' not in text: errors.append(f'{rel}: missing Phase 009 provenance')
    expected_ids=[f'INTG-{i:03d}' for i in range(1,271)]
    if sorted(ids)!=expected_ids or len(ids)!=270: errors.append(f'INTG headings must cover INTG-001..INTG-270 exactly once; found {len(ids)}')
    joined='\n'.join(corpus)
    if re.search(r'^### INTG-271 —',joined,re.M): errors.append('unaccepted INTG-271 heading present in canonical integration corpus')
    matrix=repo/'docs/canonical_knowledge_retrofit/ckr_h_semantic_conservation_matrix.md'
    if not matrix.is_file(): errors.append('missing CKR-H semantic conservation matrix')
    else:
        mt=matrix.read_text(encoding='utf-8')
        required=(
        'available ≠ relevant ≠ eligible ≠ authoritative ≠ sufficient ≠ authorized',
        'source-local identifier/name ≠ ecosystem Entity Identity',
        'timestamp proximity ≠ exact cross-system association',
        'positive-event support ≠ negative-evidence capability',
        'no returned record ≠ absence',
        'current-state availability ≠ historical replay capability',
        'late/backfilled evidence now ≠ evidence available at an earlier knowledge cut',
        'multiple endpoints ≠ independent corroboration when commonly derived',
        'fallback availability ≠ inherited authority',
        'integration failure ≠ monitored-product negative',
        'GitHub Actions success ≠ Databricks activation',
        'configured dependency ≠ actual precedence ≠ waiting ≠ version consumption',
        'execution success ≠ output existence ≠ freshness/currentness ≠ health',
        'profile metric ≠ Baseline membership ≠ drift Assessment ≠ normative health',
        'captured lineage event ≠ encounter ≠ exposure',
        'exposure ≠ effect ≠ consequence ≠ causal attribution',
        'localization ≠ Causal Claim',
        'Safeguard enforcement ≠ prevented exposure',
        'HOLD/ADMIT ≠ execution outcome',
        'historical source state ≠ as-known-at-cut Explanation ≠ retained actual communication ≠ current retrospective Explanation',
        'support classification ≠ truth/confidence/completeness',
        'latency ≠ event/effective truth',
        'quota/cost ≠ evidence authority',
        'no universal source-support/confidence/completeness/health/Impact/control/replay score')
        for phrase in required:
            if phrase not in mt: errors.append(f'CKR-H matrix missing boundary: {phrase}')
    for fam in ('SYN','REF','AUTH','HLTH','OPS','EXPL'):
        if inv['stable_families'][fam]['migration_state']!='canonicalized': errors.append(f'{fam} must remain canonicalized during/after CKR-H')
    vocab=next(r for r in inv['records'] if r['record_id']=='reference.authority_vocabulary')
    if vocab['migration_state']!='canonicalized': errors.append('authority vocabulary must remain canonicalized during/after CKR-H')
    concepts=[r for r in inv['records'] if r.get('kind')=='concept']
    if len(concepts)!=24 or any(r['migration_state']!='canonicalized' for r in concepts): errors.append('all 24 concepts must remain canonicalized during/after CKR-H')
    states_by_group={k:v for k,v in STATE_RE.findall((repo/'docs/canonical_knowledge_retrofit/README.md').read_text(encoding='utf-8'))}
    for fam,letter in LATER.items():
        item=inv['stable_families'][fam]
        if item.get('migration_group')!=f'CKR-{letter}': errors.append(f'{fam}: migration ownership moved away from CKR-{letter}')
        if item.get('migration_state') not in {'legacy_authoritative','candidate_ready','canonicalized'}: errors.append(f'{fam}: invalid migration state')
        phase_state=states_by_group.get(letter,'')
        if phase_state in {'PLANNED','NEXT / READY'} and item.get('migration_state')!='legacy_authoritative': errors.append(f'{fam}: moved before CKR-{letter} entered execution')
    phase9=next((x for x in inv.get('history_sources',[]) if x.get('path')=='docs/concepts/phase_009'),None)
    if state=='candidate_ready':
        if not phase9 or phase9.get('classification_during_migration')!='mixed_legacy_authority_and_design_history': errors.append('Phase 009 must remain mixed legacy authority/design history while INTG is candidate_ready')
    if state=='canonicalized':
        if not phase9 or phase9.get('classification_during_migration')!='design_history_and_provenance_for_canonicalized_INTG': errors.append('Phase 009 must become design history/provenance after INTG cutover')
    fixture=repo/'docs/canonical_knowledge_retrofit/fixtures/ckr_h_integration_scenarios.yaml'
    if not fixture.is_file(): errors.append('missing CKR-H fixture catalog')
    else:
        count=len(re.findall(r'^\s*- id: CKRH-\d{2}$',fixture.read_text(encoding='utf-8'),re.M))
        if count<60: errors.append(f'CKR-H fixture catalog too small; found {count}')
    for e in errors: print('ERROR',e)
    print(f'CKR-H integration validation: {len(errors)} error(s), INTG={len(ids)}/270, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
