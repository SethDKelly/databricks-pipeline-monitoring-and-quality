#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

REF_DOCS=(
'docs/canonical/contracts/evidence-time-causality/evidence-sufficiency-coverage.md',
'docs/canonical/contracts/evidence-time-causality/temporal-knowledge-correction.md',
'docs/canonical/contracts/evidence-time-causality/causal-epistemics-confirmation.md',
'docs/canonical/contracts/evidence-time-causality/exposure-readiness-control-proof.md')
AUTH_DOCS=(
'docs/canonical/authority/standing-conflict.md','docs/canonical/authority/governance-authority.md',
'docs/canonical/authority/normative-health-governance.md','docs/canonical/authority/capability-authorization.md',
'docs/canonical/authority/high-consequence-authority.md','docs/canonical/authority/disclosure-governance.md')
VOCAB='docs/canonical/authority/vocabulary.md'
REF_RE=re.compile(r'^### (REF-\d{3}) —',re.M); AUTH_RE=re.compile(r'^### (AUTH-\d{3}) —',re.M)

def marker(text):
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:return 'candidate'
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text())
    ref=inv['stable_families']['REF']; auth=inv['stable_families']['AUTH']; vocab=next(r for r in inv['records'] if r['record_id']=='reference.authority_vocabulary')
    states={ref['migration_state'],auth['migration_state'],vocab['migration_state']}
    if len(states)!=1 or next(iter(states)) not in {'candidate_ready','canonicalized'}: errors.append(f'CKR-D must move authority vocabulary, REF and AUTH atomically; states={sorted(states)}')
    state=next(iter(states)) if len(states)==1 else 'invalid'; expected='candidate' if state=='candidate_ready' else 'canonical'
    if ref.get('target_documents')!=list(REF_DOCS): errors.append('REF target_documents do not match CKR-D canonical topology')
    if auth.get('target_documents')!=list(AUTH_DOCS): errors.append('AUTH target_documents do not match CKR-D canonical topology')
    ref_ids=[]; auth_ids=[]
    for rel in REF_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing REF canonical target {rel}'); continue
        text=p.read_text(); ref_ids+=REF_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if 'docs/concepts/phase_004/' not in text: errors.append(f'{rel}: missing Phase 004 provenance')
    for rel in AUTH_DOCS:
        p=repo/rel
        if not p.is_file(): errors.append(f'missing AUTH canonical target {rel}'); continue
        text=p.read_text(); auth_ids+=AUTH_RE.findall(text)
        if marker(text)!=expected: errors.append(f'{rel}: authority marker does not match {state}')
        if 'docs/concepts/phase_005/' not in text: errors.append(f'{rel}: missing Phase 005 provenance')
    expected_ref=[f'REF-{i:03d}' for i in range(1,31)]; expected_auth=[f'AUTH-{i:03d}' for i in range(1,54)]
    if sorted(ref_ids)!=expected_ref: errors.append(f'REF headings must cover REF-001..REF-030 exactly once; found {len(ref_ids)}')
    if sorted(auth_ids)!=expected_auth: errors.append(f'AUTH headings must cover AUTH-001..AUTH-053 exactly once; found {len(auth_ids)}')
    vp=repo/VOCAB
    if not vp.is_file(): errors.append('missing canonical authority vocabulary')
    else:
        vt=vp.read_text()
        if marker(vt)!=expected: errors.append('authority vocabulary marker does not match CKR-D state')
        for phrase in ('Assertion Authority ≠ Capability Authorization','evidence sufficiency','authority-rule conflict','source count'):
            if phrase not in vt: errors.append(f'authority vocabulary missing separation/term: {phrase}')
        if 'docs/reference/authority_vocabulary.md' not in vt: errors.append('authority vocabulary missing legacy provenance')
    matrix=repo/'docs/canonical_knowledge_retrofit/ckr_d_semantic_conservation_matrix.md'
    if not matrix.is_file(): errors.append('missing CKR-D semantic conservation matrix')
    else:
        mt=matrix.read_text()
        for phrase in ('applicability ≠ coverage ≠ sufficiency','event/effective ≠ source availability ≠ framework knowledge','confirmation requires REF-017 plus AUTH-034','readiness ≠ Gate decision ≠ enforcement ≠ execution','authentication ≠ authorization ≠ Assertion Authority','safe abstraction cannot strengthen truth'):
            if phrase not in mt: errors.append(f'CKR-D matrix missing boundary: {phrase}')
    # Previous cutovers stay canonical; later families stay untouched.
    if inv['stable_families']['SYN']['migration_state']!='canonicalized': errors.append('SYN must remain canonicalized during CKR-D')
    for fam in ('HLTH','OPS','EXPL','INTG','ARCH'):
        if inv['stable_families'][fam]['migration_state']!='legacy_authoritative': errors.append(f'{fam} ownership moved early during CKR-D')
    concepts=[r for r in inv['records'] if r.get('kind')=='concept']
    if len(concepts)!=24 or any(r['migration_state']!='canonicalized' for r in concepts): errors.append('all 24 concepts must remain canonicalized during CKR-D')
    for e in errors: print('ERROR',e)
    print(f'CKR-D evidence/authority validation: {len(errors)} error(s), REF={len(ref_ids)}/30, AUTH={len(auth_ids)}/53, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
