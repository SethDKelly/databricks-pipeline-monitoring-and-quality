#!/usr/bin/env python3
from __future__ import annotations
import argparse,re
from pathlib import Path
ID_RE=re.compile(r'^\s*-\s+id:\s*["\']?([^"\'\s]+)',re.M)
CATALOG=(
('ADF-A','docs/history/foundations/adf/fixtures/adf_a_boundary_scenarios.yaml','docs/history/foundations/adf/adf_a_execution_review.md'),('ADF-B','docs/history/foundations/adf/fixtures/adf_b_knowledge_scenarios.yaml','docs/history/foundations/adf/adf_b_execution_review.md'),('ADF-C','docs/history/foundations/adf/fixtures/adf_c_adapter_scenarios.yaml','docs/history/foundations/adf/adf_c_execution_review.md'),('ADF-D','docs/history/foundations/adf/fixtures/adf_d_workflow_scenarios.yaml','docs/history/foundations/adf/adf_d_execution_review.md'),('ADF-E','docs/history/foundations/adf/fixtures/adf_e_context_scenarios.yaml','docs/history/foundations/adf/adf_e_execution_review.md'),('ADF-F','docs/history/foundations/adf/fixtures/adf_f_conformance_scenarios.yaml','docs/history/foundations/adf/adf_f_execution_review.md'),('ADF-G','docs/history/foundations/adf/fixtures/adf_g_compatibility_scenarios.yaml','docs/history/foundations/adf/adf_g_execution_review.md'),('ADF-H','docs/history/foundations/adf/fixtures/adf_h_security_scenarios.yaml','docs/history/foundations/adf/adf_h_execution_review.md'),('ADF-DBX','docs/history/foundations/adf/fixtures/adf_databricks_skills_addendum_scenarios.yaml','docs/history/foundations/adf/databricks_agent_skills_addendum_execution_review.md'),
('CKR-A','docs/history/retrofits/ckr/fixtures/ckr_a_authority_scenarios.yaml','docs/history/retrofits/ckr/ckr_a_execution_review.md'),('CKR-B','docs/history/retrofits/ckr/fixtures/ckr_b_foundation_scenarios.yaml','docs/history/retrofits/ckr/ckr_b_execution_review.md'),('CKR-C','docs/history/retrofits/ckr/fixtures/ckr_c_concept_scenarios.yaml','docs/history/retrofits/ckr/ckr_c_execution_review.md'),('CKR-D','docs/history/retrofits/ckr/fixtures/ckr_d_evidence_authority_scenarios.yaml','docs/history/retrofits/ckr/ckr_d_execution_review.md'),('CKR-E','docs/history/retrofits/ckr/fixtures/ckr_e_health_quality_scenarios.yaml','docs/history/retrofits/ckr/ckr_e_execution_review.md'),('CKR-F','docs/history/retrofits/ckr/fixtures/ckr_f_operations_scenarios.yaml','docs/history/retrofits/ckr/ckr_f_execution_review.md'),('CKR-G','docs/history/retrofits/ckr/fixtures/ckr_g_experience_scenarios.yaml','docs/history/retrofits/ckr/ckr_g_execution_review.md'),('CKR-H','docs/history/retrofits/ckr/fixtures/ckr_h_integration_scenarios.yaml','docs/history/retrofits/ckr/ckr_h_execution_review.md'),('CKR-I','docs/history/retrofits/ckr/fixtures/ckr_i_architecture_scenarios.yaml','docs/history/retrofits/ckr/ckr_i_execution_review.md'),('CKR-J','docs/history/retrofits/ckr/fixtures/ckr_j_routing_scenarios.yaml','docs/history/retrofits/ckr/ckr_j_execution_review.md'),('CKR-K','docs/history/retrofits/ckr/fixtures/ckr_k_exit_scenarios.yaml','docs/history/retrofits/ckr/ckr_k_execution_review.md'),
('DPTN-A','docs/history/retrofits/dptn/fixtures/dptn_a_topology_scenarios.yaml','docs/history/retrofits/dptn/dptn_a_execution_review.md'),('DPTN-B','docs/history/retrofits/dptn/fixtures/dptn_b_history_scenarios.yaml','docs/history/retrofits/dptn/dptn_b_execution_review.md'),('DPTN-C','docs/history/retrofits/dptn/fixtures/dptn_c_promotion_scenarios.yaml','docs/history/retrofits/dptn/dptn_c_execution_review.md'),('DPTN-D','docs/history/retrofits/dptn/fixtures/dptn_d_decomposition_scenarios.yaml','docs/history/retrofits/dptn/dptn_d_execution_review.md'),('DPTN-E','docs/history/retrofits/dptn/fixtures/dptn_e_convergence_scenarios.yaml','docs/history/retrofits/dptn/dptn_e_execution_review.md'),('DPTN-F','docs/history/retrofits/dptn/fixtures/dptn_f_rebinding_scenarios.yaml','docs/history/retrofits/dptn/dptn_f_execution_review.md'),('DPTN-G','docs/history/retrofits/dptn/fixtures/dptn_g_exit_scenarios.yaml','docs/history/retrofits/dptn/dptn_g_execution_review.md'))
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--repo',default='.');repo=Path(ap.parse_args().repo).resolve();errors=[];seen={};count=0
    for label,fixture,review in CATALOG:
        fp=repo/fixture;rp=repo/review
        if not fp.is_file():errors.append(f'missing {label} fixture catalog: {fixture}');continue
        if not rp.is_file():errors.append(f'{label}: missing execution review {review}')
        text=fp.read_text(encoding='utf-8')
        if 'scenarios:' not in text:errors.append(f'{fixture}: missing scenarios collection')
        ids=ID_RE.findall(text)
        if not ids:errors.append(f'{fixture}: no scenario IDs found')
        for sid in ids:
            if sid in seen:errors.append(f'duplicate scenario id {sid}: {seen[sid]} and {fixture}')
            seen[sid]=fixture
        count+=len(ids)
    for e in errors:print('ERROR',e)
    print(f'Fixture catalog validation: {len(errors)} error(s), {count} scenario(s)');return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
