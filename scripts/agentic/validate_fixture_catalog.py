#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path
EXPECTED={'A':'adf_a_boundary_scenarios.yaml','B':'adf_b_knowledge_scenarios.yaml','C':'adf_c_adapter_scenarios.yaml','D':'adf_d_workflow_scenarios.yaml','E':'adf_e_context_scenarios.yaml','F':'adf_f_conformance_scenarios.yaml','G':'adf_g_compatibility_scenarios.yaml','H':'adf_h_security_scenarios.yaml'}
ADDENDA=(('DBX','adf_databricks_skills_addendum_scenarios.yaml','databricks_agent_skills_addendum_execution_review.md'),)
CKR=(
('CKR-A','docs/canonical_knowledge_retrofit/fixtures/ckr_a_authority_scenarios.yaml','docs/canonical_knowledge_retrofit/ckr_a_execution_review.md'),
('CKR-B','docs/canonical_knowledge_retrofit/fixtures/ckr_b_foundation_scenarios.yaml','docs/canonical_knowledge_retrofit/ckr_b_execution_review.md'),
('CKR-C','docs/canonical_knowledge_retrofit/fixtures/ckr_c_concept_scenarios.yaml','docs/canonical_knowledge_retrofit/ckr_c_execution_review.md'),
('CKR-D','docs/canonical_knowledge_retrofit/fixtures/ckr_d_evidence_authority_scenarios.yaml','docs/canonical_knowledge_retrofit/ckr_d_execution_review.md'),
('CKR-E','docs/canonical_knowledge_retrofit/fixtures/ckr_e_health_quality_scenarios.yaml','docs/canonical_knowledge_retrofit/ckr_e_execution_review.md'))
ID_RE=re.compile(r'^\s*-\s+id:\s*["\']?([^"\'\s]+)',re.M)
def collect(path,label,seen,errors):
    if not path.is_file(): errors.append(f'missing {label} fixture catalog: {path.name}'); return 0
    text=path.read_text(encoding='utf-8')
    if 'scenarios:' not in text: errors.append(f'{path.name}: missing scenarios collection')
    ids=ID_RE.findall(text)
    if not ids: errors.append(f'{path.name}: no scenario IDs found')
    for sid in ids:
        if sid in seen: errors.append(f'duplicate scenario id {sid}: {seen[sid]} and {path.name}')
        seen[sid]=path.name
    return len(ids)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); root=repo/'docs/agentic_development_foundation/fixtures'; errors=[]; seen={}; count=0
    for letter,name in EXPECTED.items():
        count+=collect(root/name,f'ADF-{letter}',seen,errors)
        if not (repo/f'docs/agentic_development_foundation/adf_{letter.lower()}_execution_review.md').is_file(): errors.append(f'ADF-{letter}: missing execution review')
    for label,name,review in ADDENDA:
        count+=collect(root/name,f'ADF addendum {label}',seen,errors)
        if not (repo/'docs/agentic_development_foundation'/review).is_file(): errors.append(f'ADF addendum {label}: missing execution review {review}')
    for label,fixture,review in CKR:
        count+=collect(repo/fixture,label,seen,errors)
        if not (repo/review).is_file(): errors.append(f'{label}: missing execution review {review}')
    for e in errors: print('ERROR',e)
    print(f'Fixture catalog validation: {len(errors)} error(s), {count} scenario(s)'); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
