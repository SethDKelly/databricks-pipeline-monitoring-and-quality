#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path

def run(repo,script): return subprocess.run([sys.executable,str(repo/'scripts/agentic'/script),'--repo',str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
def mutate(repo,rel,transform,script,label,errors):
    p=repo/rel; original=p.read_text(encoding='utf-8')
    try:
        p.write_text(transform(original),encoding='utf-8')
        if run(repo,script)==0: errors.append(f'{label}: validator unexpectedly passed')
        else: print(f'PASS negative control: {label}')
    finally:p.write_text(original,encoding='utf-8')
def stale_status(t): return re.sub(r'ADF status mirror: .*?$','ADF status mirror: COMPLETE ADF-A–ADF-E; NEXT ADF-F.',t,count=1,flags=re.M)
def stale_ckr(t): return re.sub(r'CKR status mirror: .*?$','CKR status mirror: COMPLETE CKR-A; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.',t,count=1,flags=re.M)
def vendor_auto(t): d=json.loads(t); d['materialization']['automatic_new_skills']=True; return json.dumps(d,indent=2)+'\n'
def model_skill(t): d=json.loads(t); d['selected_skills'].append({'name':'databricks-model-serving','version':'0.4.0'}); return json.dumps(d,indent=2)+'\n'
def misassign_hlth(t): d=json.loads(t); d['stable_families']['HLTH']['migration_group']='CKR-F'; return json.dumps(d,indent=2)+'\n'
def move_lineage(t): d=json.loads(t); next(r for r in d['records'] if r['record_id']=='concept.lineage')['target_owner']='docs/design_history/lineage.md'; return json.dumps(d,indent=2)+'\n'
def partial_ckrc(t): d=json.loads(t); next(r for r in d['records'] if r['record_id']=='concept.observation')['migration_state']='candidate_ready'; return json.dumps(d,indent=2)+'\n'
def partial_ckrd(t): d=json.loads(t); d['stable_families']['AUTH']['migration_state']='legacy_authoritative'; return json.dumps(d,indent=2)+'\n'
def remove_hlth_target(t): d=json.loads(t); d['stable_families']['HLTH']['target_documents']=d['stable_families']['HLTH']['target_documents'][:-1]; return json.dumps(d,indent=2)+'\n'
def future_ops(t): d=json.loads(t); d['stable_families']['OPS']['migration_state']='canonicalized'; return json.dumps(d,indent=2)+'\n'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); src=Path(a.repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix='dmtz-conformance-') as td:
        repo=Path(td)/'repo'; shutil.copytree(src,repo,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
        mutate(repo,'knowledge/project/authority.md',lambda t:t.replace('type:','missing_type:',1),'validate_okf.py','malformed OKF metadata',errors)
        mutate(repo,'.agents/skills/implement-group/SKILL.md',lambda t:t.replace('description:','model: forbidden\ndescription:',1),'validate_agent_skills.py','provider-specific skill metadata',errors)
        mutate(repo,'.cursor/rules/00-implementation-routing.mdc',lambda t:t.replace('alwaysApply: false','alwaysApply: true',1),'validate_agent_adapters.py','always-applied Cursor rule regression',errors)
        mutate(repo,'AGENTS.md',lambda t:t+'\n'+('x'*20000),'measure_context_budget.py','persistent-context overflow',errors)
        mutate(repo,'IMPLEMENTATION.md',stale_status,'validate_status_drift.py','stale ADF status mirror',errors)
        mutate(repo,'knowledge/project/authority.md',lambda t:t.replace('resource:','resource: "../../definitely-missing.md"\nold_resource:',1),'validate_okf.py','broken canonical resource route',errors)
        mutate(repo,'AGENTS.md',lambda t:t+'\nARCH-501\n','validate_agentic_references.py','unaccepted stable ID citation',errors)
        mutate(repo,'docs/agentic_development_foundation/runtime_compatibility_evidence.json',lambda t:t.replace('"runtime_status": "unverified"','"runtime_status": "supported"',1),'validate_adf_g_compatibility.py','fabricated provider runtime support',errors)
        mutate(repo,'.claude/CLAUDE.md',lambda t:t+'\ncredential: ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n','scan_agentic_secrets.py','checked-in high-confidence secret',errors)
        mutate(repo,'docs/agentic_development_foundation/tool_lifecycle_review.json',lambda t:t.replace('"security_reviewed_on": "2026-09-02"','"security_reviewed_on": "2020-01-01"',1),'validate_adf_h_governance.py','expired provider security review horizon',errors)
        mutate(repo,'docs/agentic_development_foundation/databricks_vendor_skills_profile.json',vendor_auto,'validate_databricks_agent_skills.py','automatic Databricks vendor-skill expansion',errors)
        mutate(repo,'docs/agentic_development_foundation/databricks_vendor_skills_profile.json',model_skill,'validate_databricks_agent_skills.py','deferred model skill added to initial Databricks set',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',misassign_hlth,'validate_ckr_d_evidence_authority.py','later-family migration ownership drift after CKR-D',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',move_lineage,'validate_canonical_knowledge.py','canonical target outside docs/canonical',errors)
        mutate(repo,'IMPLEMENTATION.md',stale_ckr,'validate_ckr_status.py','stale CKR implementation status mirror',errors)
        mutate(repo,'docs/canonical/invariants/architectural-principles.md',lambda t:t.replace('### AP-32 —','### AP-XX —',1),'validate_ckr_b_foundation.py','omitted CKR-B AP-32 identity',errors)
        mutate(repo,'docs/canonical/policies/security-governance.md',lambda t:t.replace('### SP-15 —','### SP-XX —',1),'validate_ckr_b_foundation.py','omitted CKR-B SP-15 identity',errors)
        mutate(repo,'docs/canonical/policies/mvp-boundary.md',lambda t:t.replace('### Scenario K —','### Scenario Z —',1),'validate_ckr_b_foundation.py','omitted CKR-B MVP Scenario K',errors)
        mutate(repo,'docs/canonical/reference/product-definition.md',lambda t:t.replace('001_product_definition.md','missing-product-origin.md'),'validate_ckr_b_foundation.py','broken CKR-B legacy provenance',errors)
        mutate(repo,'docs/canonical/concepts/observation.md',lambda t:t.replace('`retrieve`','`missingRetrieve`',1),'validate_ckr_c_concepts.py','omitted CKR-C Observation action',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',partial_ckrc,'validate_ckr_c_concepts.py','partial CKR-C concept cutover',errors)
        mutate(repo,'docs/canonical/contracts/synchronization/historical-replay.md',lambda t:t.replace('### SYN-035 —','### SYN-999 —',1),'validate_ckr_c_concepts.py','omitted CKR-C SYN-035 identity',errors)
        mutate(repo,'docs/canonical/concepts/entity-identity.md',lambda t:t.replace('docs/concepts/phase_002/01_scope_and_identity/entity_identity.md','docs/concepts/missing-identity.md'),'validate_ckr_c_concepts.py','broken CKR-C concept provenance',errors)
        mutate(repo,'docs/canonical/concepts/baseline.md',lambda t:t.replace('not normative','normative',1),'validate_ckr_c_concepts.py','Expectation/Baseline non-collapse regression',errors)
        mutate(repo,'docs/canonical/contracts/evidence-time-causality/exposure-readiness-control-proof.md',lambda t:t.replace('### REF-030 —','### REF-999 —',1),'validate_ckr_d_evidence_authority.py','omitted CKR-D REF-030 identity',errors)
        mutate(repo,'docs/canonical/authority/disclosure-governance.md',lambda t:t.replace('### AUTH-053 —','### AUTH-999 —',1),'validate_ckr_d_evidence_authority.py','omitted CKR-D AUTH-053 identity',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',partial_ckrd,'validate_ckr_d_evidence_authority.py','partial CKR-D authority cutover',errors)
        mutate(repo,'docs/canonical/authority/vocabulary.md',lambda t:t.replace('Assertion Authority ≠ Capability Authorization','Assertion Authority = Capability Authorization',1),'validate_ckr_d_evidence_authority.py','authority versus authorization collapse',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_d_semantic_conservation_matrix.md',lambda t:t.replace('safe abstraction cannot strengthen truth','safe abstraction may strengthen truth',1),'validate_ckr_d_evidence_authority.py','disclosure overstatement regression',errors)
        mutate(repo,'docs/canonical/contracts/health-quality-timing/composite-health-readiness-timing.md',lambda t:t.replace('### HLTH-066 —','### HLTH-999 —',1),'validate_ckr_e_health_quality.py','omitted CKR-E HLTH-066 identity',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',remove_hlth_target,'validate_ckr_e_health_quality.py','partial CKR-E target topology',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_e_semantic_conservation_matrix.md',lambda t:t.replace('Lineage does not propagate status','Lineage propagates status',1),'validate_ckr_e_health_quality.py','blind health propagation regression',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',future_ops,'validate_ckr_e_health_quality.py','future OPS ownership theft during CKR-E',errors)
    for e in errors: print('ERROR',e)
    print(f'Conformance guard tests: {len(errors)} error(s), 33 negative control(s)'); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
