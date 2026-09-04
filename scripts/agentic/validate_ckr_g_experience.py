#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

EXPL_DOCS=(
'docs/canonical/experience/question-scope-temporal.md',
'docs/canonical/experience/answer-structure-traceability.md',
'docs/canonical/experience/health-change-execution-questions.md',
'docs/canonical/experience/investigation-impact-control-governance-questions.md',
'docs/canonical/experience/epistemic-language.md',
'docs/canonical/experience/audience-authorization-safe-abstraction.md',
'docs/canonical/experience/progressive-maturity-retention.md',
'docs/canonical/experience/historical-comparative-explanation.md')
EXPL_RE=re.compile(r'^### (EXPL-\d{3}) —',re.M)
STATE_RE=re.compile(r'^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$',re.M)
LATER={'INTG':'H','ARCH':'I'}

def marker(text):
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:return 'candidate'
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8'))
    expl=inv['stable_families']['EXPL']; state=expl.get('migration_state')
    if state not in {'candidate_ready','canonicalized'}: errors.append(f'EXPL must be candidate_ready/canonicalized during/after CKR-G, found {state!r}')
    expected='candidate' if state=='candidate_ready' else 'canonical'
    if expl.get('migration_group')!='CKR-G': errors.append('EXPL migration_group must remain CKR-G')
    if expl.get('target_documents')!=list(EXPL_DOCS): errors.append('EXPL target_documents do not match CKR-G canonical topology')
    ids=[]; corpus=[]
    for rel in EXPL_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing EXPL canonical target {rel}'); continue
        text=p.read_text(encoding='utf-8'); corpus.append(text); ids+=EXPL_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if '**Migration record:** `stable_family.EXPL`' not in text: errors.append(f'{rel}: missing stable-family migration record')
        if 'docs/concepts/phase_008/' not in text: errors.append(f'{rel}: missing Phase 008 provenance')
    expected_ids=[f'EXPL-{i:03d}' for i in range(1,161)]
    if sorted(ids)!=expected_ids or len(ids)!=160: errors.append(f'EXPL headings must cover EXPL-001..EXPL-160 exactly once; found {len(ids)}')
    joined='\n'.join(corpus)
    if re.search(r'^### EXPL-161 —',joined,re.M): errors.append('unaccepted EXPL-161 heading present in canonical experience corpus')
    matrix=repo/'docs/canonical_knowledge_retrofit/ckr_g_semantic_conservation_matrix.md'
    if not matrix.is_file(): errors.append('missing CKR-G semantic conservation matrix')
    else:
        mt=matrix.read_text(encoding='utf-8')
        required=('question ≠ truth ≠ authorization','answer statement ≠ independent truth','basis count ≠ confidence','one supported sibling does not strengthen an unresolved sibling','ran ≠ succeeded ≠ produced output ≠ current/fresh output ≠ healthy','Change Intent ≠ Deployment ≠ activation ≠ realized Change','Investigation/localization ≠ Causal Claim','candidate/reachable ≠ opportunity ≠ exposure ≠ effect ≠ consequence ≠ causal attribution','Safeguard administration ≠ enforcement ≠ prevented exposure ≠ recovery','readiness ≠ Gate decision ≠ enforcement ≠ execution','unknown/unresolved ≠ false/absent/safe','safe abstraction can reduce detail but cannot strengthen truth','elapsed time/rewording ≠ evidence or maturity','retained actual communication ≠ timeless truth','historical source state ≠ as-known-at-cut Explanation ≠ retained actual communication ≠ current retrospective Explanation','no universal Explanation confidence, completeness, maturity, RCA, Impact, control-effectiveness, answer-quality or replay score')
        for phrase in required:
            if phrase not in mt: errors.append(f'CKR-G matrix missing boundary: {phrase}')
    for fam in ('SYN','REF','AUTH','HLTH','OPS'):
        if inv['stable_families'][fam]['migration_state']!='canonicalized': errors.append(f'{fam} must remain canonicalized during/after CKR-G')
    vocab=next(r for r in inv['records'] if r['record_id']=='reference.authority_vocabulary')
    if vocab['migration_state']!='canonicalized': errors.append('authority vocabulary must remain canonicalized during/after CKR-G')
    concepts=[r for r in inv['records'] if r.get('kind')=='concept']
    if len(concepts)!=24 or any(r['migration_state']!='canonicalized' for r in concepts): errors.append('all 24 concepts must remain canonicalized during/after CKR-G')
    states_by_group={k:v for k,v in STATE_RE.findall((repo/'docs/canonical_knowledge_retrofit/README.md').read_text(encoding='utf-8'))}
    for fam,letter in LATER.items():
        item=inv['stable_families'][fam]
        if item.get('migration_group')!=f'CKR-{letter}': errors.append(f'{fam}: migration ownership moved away from CKR-{letter}')
        if item.get('migration_state') not in {'legacy_authoritative','candidate_ready','canonicalized'}: errors.append(f'{fam}: invalid migration state')
        phase_state=states_by_group.get(letter,'')
        if phase_state in {'PLANNED','NEXT / READY'} and item.get('migration_state')!='legacy_authoritative': errors.append(f'{fam}: moved before CKR-{letter} entered execution')
    fixture=repo/'docs/canonical_knowledge_retrofit/fixtures/ckr_g_experience_scenarios.yaml'
    if not fixture.is_file(): errors.append('missing CKR-G fixture catalog')
    else:
        count=len(re.findall(r'^\s*- id: CKRG-\d{2}$',fixture.read_text(encoding='utf-8'),re.M))
        if count<40: errors.append(f'CKR-G fixture catalog too small; found {count}')
    for e in errors: print('ERROR',e)
    print(f'CKR-G experience validation: {len(errors)} error(s), EXPL={len(ids)}/160, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
