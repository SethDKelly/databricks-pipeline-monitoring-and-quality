#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

CONCEPTS = {
'monitoring_scope': ('monitoring-scope.md', ['include','exclude','resolveAt'], ['missing assertion','not an exclusion','authorization']),
'entity_identity': ('entity-identity.md', ['establish','recognize','associateReference','separate','endReference'], ['replacement','not identity','ambiguous']),
'semantic_definition': ('semantic-definition.md', ['define','revise','resolveAt'], ['schema meaning','Expectation','Observation/Change']),
'responsibility_assignment': ('responsibility-assignment.md', ['assign','transfer','end','resolveAt'], ['Responsibility','Assertion Authority','Capability Authorization']),
'classification': ('classification.md', ['classify','reclassify','resolveAt'], ['Classification','Policy Context','universal criticality score']),
'policy_context': ('policy-context.md', ['associate','supersede','resolveAt'], ['does not grant/deny access','compliance','unknown']),
'expectation': ('expectation.md', ['establish','revise','exceptFor','retire','resolveApplicable'], ['normative','Baseline is descriptive','Missing Expectation']),
'baseline': ('baseline.md', ['derive','refresh','registerProspectiveBreak','markNonComparable','resolveComparable'], ['descriptive','not normative','Typical']),
'observation': ('observation.md', ['record','correct','retrieve'], ['Observation is evidence','Missing evidence','observed absence']),
'assessment': ('assessment.md', ['assess','reassess','explainBasis'], ['dimension-scoped','Typical','No implicit']),
'change_intent': ('change-intent.md', ['register','revise','withdraw','resolvePlannedAt'], ['planned','Deployment','realized Change']),
'execution_history': ('execution-history.md', ['recordState','associateExecution','associateImplementationState','associateInputVersion','associateOutputVersion','correctState','resolveAt'], ['Execution success','output existence','Missing telemetry']),
'deployment': ('deployment.md', ['recordAttempt','recordActivation','supersede','associateIntent','resolveActiveAt'], ['attempt','activation','causality']),
'lineage': ('lineage.md', ['assertRelationship','observeRelationship','supersedeRelationship','correctRelationship','traverseAt'], ['reachability','exposure','cause']),
'change': ('change.md', ['derive','recordOccurred','correct','resolveWindow'], ['realized','Change Intent','not automatically']),
'investigation': ('investigation.md', ['open','linkEvidence','linkClaim','linkImpact','refineScope','close','reopen'], ['closure','never confirms','localization']),
'causal_claim': ('causal-claim.md', ['propose','support','contradict','reviseStatus','confirm','reject'], ['proposed','supported','weakened','unresolved','rejected','confirmed','REF-017','AUTH-034']),
'impact': ('impact.md', ['identifyCandidates','evaluateExposure','linkDownstreamEffect','recordConsequence','revise'], ['reachability','exposure','effect','consequence','causal attribution']),
'annotation': ('annotation.md', ['add','revise','withdraw','dispute'], ['human context','structured','owning concept']),
'explanation': ('explanation.md', ['compose','composeAt','inspectBasis','refresh'], ['projection','cannot manufacture','as-known']),
'propagation_safeguard': ('propagation-safeguard.md', ['propose','activate','release','cancel','resolveAt'], ['proposal','effective enforcement','prevented exposure','Release']),
'capability_authorization': ('capability-authorization.md', ['recordDecision','supersedeDecision','resolveFor','explainBasis'], ['Authentication','Assertion Authority','enforcement']),
'execution_gate': ('execution-gate.md', ['register','evaluate','hold','admit','override','retire','resolveAt'], ['readiness','Gate decision','effective enforcement','actual execution','Propagation Safeguard']),
'assertion_authority': ('assertion-authority.md', ['establishRule','reviseRule','correctRule','resolveStanding','explainAuthorityBasis'], ['factual','Capability Authorization','evidence sufficiency','enforcement']),
}
SYNC_DOCS = [
'subject-scope-governance.md','planned-change-reference-transition.md','runtime-evidence-health-control.md',
'investigation-causality.md','impact-annotation-explanation.md','historical-replay.md']
LATER = {'REF':'CKR-D','AUTH':'CKR-D','HLTH':'CKR-E','OPS':'CKR-F','EXPL':'CKR-G','INTG':'CKR-H','ARCH':'CKR-I'}


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); args=ap.parse_args()
    repo=Path(args.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text())
    records={r['record_id']:r for r in inv['records']}
    c_records={k:v for k,v in records.items() if k.startswith('concept.')}
    if set(c_records) != {f'concept.{k}' for k in CONCEPTS}: errors.append('concept inventory must match exact accepted 24-concept catalog')
    states={r.get('migration_state') for r in c_records.values()}
    syn=inv['stable_families']['SYN']; states.add(syn.get('migration_state'))
    if len(states)!=1 or next(iter(states),None) not in {'candidate_ready','canonicalized'}:
        errors.append(f'CKR-C concepts + SYN must share one candidate_ready/canonicalized state; found {sorted(states)}')
    state=next(iter(states),None); marker='CANDIDATE / NOT CURRENT AUTHORITY' if state=='candidate_ready' else 'CANONICAL CURRENT AUTHORITY'
    required_sections=['## Current semantics','## Actions','## Invariants / boundaries','## Ambiguity / evidence','## Synchronizations / related canonical resources','## Non-goals','## Provenance']
    for key,(name,actions,tokens) in CONCEPTS.items():
        rid=f'concept.{key}'; rec=records.get(rid,{})
        path=repo/rec.get('target_owner','')
        if path.name!=name or not path.is_file(): errors.append(f'{rid}: missing expected target {name}'); continue
        text=path.read_text(encoding='utf-8')
        if f'**Authority:** {marker}' not in text: errors.append(f'{rid}: authority marker does not match {state}')
        if f'**Migration record:** `{rid}`' not in text: errors.append(f'{rid}: migration record header mismatch')
        for section in required_sections:
            if section not in text: errors.append(f'{rid}: missing section {section}')
        for action in actions:
            if f'`{action}`' not in text: errors.append(f'{rid}: missing accepted action {action}')
        for token in tokens:
            if token.lower() not in text.lower(): errors.append(f'{rid}: missing boundary token {token!r}')
        if '## Deferred questions' in text: errors.append(f'{rid}: stale deferred-question section promoted into current canonical resource')
        current=rec.get('current_owner')
        if not current or not (repo/current).is_file(): errors.append(f'{rid}: missing legacy provenance owner')
        elif current not in text: errors.append(f'{rid}: canonical provenance does not name legacy owner')
    if syn.get('accepted_range')!='SYN-001..SYN-035': errors.append('SYN accepted range changed')
    target_docs=syn.get('target_documents',[])
    expected=[f'docs/canonical/contracts/synchronization/{n}' for n in SYNC_DOCS]
    if target_docs != expected: errors.append('SYN target_documents must exactly match six bounded canonical synchronization documents')
    sync_text='\n'.join((repo/p).read_text(encoding='utf-8') for p in expected if (repo/p).is_file())
    ids=re.findall(r'^### (SYN-\d{3}) —',sync_text,re.M)
    expected_ids=[f'SYN-{i:03d}' for i in range(1,36)]
    if sorted(ids)!=expected_ids or len(ids)!=35: errors.append(f'SYN coverage must contain SYN-001..SYN-035 exactly once; found {len(ids)} headings')
    for p in expected:
        path=repo/p
        if not path.is_file(): errors.append(f'missing SYN target {p}'); continue
        text=path.read_text(encoding='utf-8')
        if f'**Authority:** {marker}' not in text: errors.append(f'{p}: SYN authority marker mismatch')
        if '**Migration record:** `stable_family.SYN`' not in text: errors.append(f'{p}: missing stable-family migration record')
    for phrase in ['Synchronization order is never','not an umbrella concept','Unknown','concept state remains owned']:
        if phrase.lower() not in sync_text.lower(): errors.append(f'SYN corpus missing cross-cutting synchronization boundary {phrase!r}')
    if not (repo/'docs/concepts/phase_002').exists() or not (repo/'docs/concepts/phase_003').exists(): errors.append('Phase 002/003 provenance roots must remain preserved')
    # CKR-C owns only concepts + SYN. Later families must retain their assigned migration group,
    # but their state may legitimately advance when that later CKR group is human-selected.
    # Later-group validators enforce their own atomicity and progression isolation.
    for fam,group in LATER.items():
        item=inv['stable_families'][fam]
        if item.get('migration_group')!=group:
            errors.append(f'{fam}: migration ownership moved away from assigned {group}')
        if item.get('migration_state') not in {'legacy_authoritative','candidate_ready','canonicalized'}:
            errors.append(f'{fam}: invalid later-family migration state {item.get("migration_state")!r}')
    for e in errors: print('ERROR',e)
    print(f'CKR-C concept validation: {len(errors)} error(s), {len(c_records)} concept(s), SYN headings={len(ids)}, state={state}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
