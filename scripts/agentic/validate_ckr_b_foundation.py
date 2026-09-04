#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
CKR_B_IDS=("foundation.product_definition","foundation.actors_stakeholders","foundation.terminology","foundation.concept_design_method","foundation.architectural_principles","foundation.security_governance_policy","foundation.ecosystem_lifecycles","foundation.mvp_boundary","reference.glossary")
HISTORY_ONLY=("docs/foundation/009_initial_roadmap.md","docs/foundation/010_open_questions.md","docs/foundation/011_phase_006_exit_phase_007_handoff.md")
REQUIRED_ACTORS=("Data engineer / pipeline maintainer","Data platform engineer / platform operator","Business analyst / data consumer","Data owner","Data steward / governance steward","Security / privacy / compliance stakeholder","Incident responder / on-call engineer","Monitoring framework administrator")
REQUIRED_CONCEPT_DESIGN=("Purpose","Operational principle","State","Actions","Invariants / behavioral expectations","Synchronizations","Failure / ambiguity behavior","Vendor-shaped design","Architecture-shaped design","UI-shaped design","Overconfident reasoning")
REQUIRED_NON_EQUIVALENCES=("Observation ≠ Assessment","Expectation ≠ Baseline","Lineage ≠","Capability Authorization","Assertion Authority","missing evidence","current state ≠ historical","passive monitoring ≠ active","Execution Gate ≠ Propagation Safeguard")

def numbered(text,prefix,start,end,label,errors):
    for n in range(start,end+1):
        if not re.search(rf'^{re.escape(prefix)}\s+{n}\.\s',text,re.M): errors.append(f'{label}: missing numbered heading {n}')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    inv=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text()); records={r['record_id']:r for r in inv['records']}
    owned=[rid for rid,r in records.items() if r.get('migration_group')=='CKR-B']
    if set(owned)!=set(CKR_B_IDS) or len(owned)!=9: errors.append(f'CKR-B must own exactly nine accepted records; found {sorted(owned)}')
    for rid in CKR_B_IDS:
        rec=records.get(rid)
        if not rec: errors.append(f'missing CKR-B record {rid}'); continue
        if rec.get('migration_state')!='canonicalized': errors.append(f'{rid}: accepted CKR-B record must remain canonicalized')
        legacy=repo/rec['current_owner']; target=repo/rec['target_owner']
        if not legacy.is_file(): errors.append(f'{rid}: legacy provenance owner missing')
        if not target.is_file(): errors.append(f'{rid}: canonical owner missing'); continue
        text=target.read_text(encoding='utf-8')
        for required in ('**Authority:** CANONICAL CURRENT AUTHORITY',f'**Canonical key:** `{rid}`',f'**Migration record:** `{rid}`','**Kind:**','**Owns current question:**','## Provenance'):
            if required not in text: errors.append(f'{rid}: missing accepted canonical metadata {required!r}')
        if Path(rec['current_owner']).name not in text: errors.append(f'{rid}: canonical provenance no longer references legacy owner')
    principles=(repo/records['foundation.architectural_principles']['target_owner']).read_text()
    for n in range(1,33):
        tok=f'AP-{n:02d}'
        if len(re.findall(rf'^###\s+{tok}\s+—',principles,re.M))!=1: errors.append(f'architectural principles: {tok} must appear exactly once')
    security=(repo/records['foundation.security_governance_policy']['target_owner']).read_text()
    for n in range(1,16):
        tok=f'SP-{n:02d}'
        if len(re.findall(rf'^###\s+{tok}\s+—',security,re.M))!=1: errors.append(f'security governance: {tok} must appear exactly once')
    lifecycles=(repo/records['foundation.ecosystem_lifecycles']['target_owner']).read_text(); numbered(lifecycles,'##',1,14,'ecosystem lifecycles',errors)
    if 'non-rewriting' not in lifecycles.lower() or 'bitemporal' not in lifecycles.lower(): errors.append('ecosystem lifecycles must preserve non-rewriting/bitemporal semantics')
    mvp=(repo/records['foundation.mvp_boundary']['target_owner']).read_text(); numbered(mvp,'###',1,13,'MVP required capabilities',errors)
    for letter in 'ABCDEFGHIJK':
        if not re.search(rf'^### Scenario {letter} —',mvp,re.M): errors.append(f'MVP boundary: missing Scenario {letter}')
    for term in ('Collibra','Immuta','LLM','graph database','active control'):
        if term.lower() not in mvp.lower(): errors.append(f'MVP boundary: missing optional/non-required boundary {term}')
    actors=(repo/records['foundation.actors_stakeholders']['target_owner']).read_text()
    for actor in REQUIRED_ACTORS:
        if actor not in actors: errors.append(f'actors/stakeholders: missing {actor}')
    method=(repo/records['foundation.concept_design_method']['target_owner']).read_text()
    for phrase in REQUIRED_CONCEPT_DESIGN:
        if phrase not in method: errors.append(f'Concept Design method: missing {phrase}')
    combined=(repo/records['foundation.terminology']['target_owner']).read_text()+'\n'+(repo/records['reference.glossary']['target_owner']).read_text()
    for phrase in REQUIRED_NON_EQUIVALENCES:
        if phrase.lower() not in combined.lower(): errors.append(f'terminology/glossary: missing boundary {phrase!r}')
    product=(repo/records['foundation.product_definition']['target_owner']).read_text()
    if 'understandable over time' not in product: errors.append('product definition core purpose missing')
    for phrase in ('Evidence','Historical','Lineage','Governance','Investigation','Business analysis'):
        if phrase.lower() not in product.lower(): errors.append(f'product definition: missing capability family {phrase}')
    history_paths={x.get('path') for x in inv.get('history_sources',[])}
    for rel in HISTORY_ONLY:
        if not (repo/rel).is_file(): errors.append(f'CKR-B historical source missing: {rel}')
        if rel not in history_paths: errors.append(f'CKR-B history source removed from inventory: {rel}')
    # Later groups may legitimately progress after CKR-B. Guard against ownership theft, not progression.
    for rid,rec in records.items():
        if rid not in CKR_B_IDS and rec.get('migration_group')=='CKR-B': errors.append(f'{rid}: later record was incorrectly reassigned to CKR-B')
    expected_groups={'SYN':'CKR-C','REF':'CKR-D','AUTH':'CKR-D','HLTH':'CKR-E','OPS':'CKR-F','EXPL':'CKR-G','INTG':'CKR-H','ARCH':'CKR-I'}
    for family,group in expected_groups.items():
        if inv.get('stable_families',{}).get(family,{}).get('migration_group')!=group: errors.append(f'{family}: stable family migration ownership changed from {group}')
    for rel in ('docs/canonical_knowledge_retrofit/ckr_b_semantic_conservation_matrix.md','docs/canonical_knowledge_retrofit/ckr_b_execution_review.md','docs/canonical_knowledge_retrofit/fixtures/ckr_b_foundation_scenarios.yaml'):
        if not (repo/rel).is_file(): errors.append(f'missing accepted CKR-B evidence {rel}')
    for e in errors: print('ERROR',e)
    print(f'CKR-B foundation validation: {len(errors)} error(s), 9 canonicalized record(s); later-group progression permitted under assigned ownership')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
