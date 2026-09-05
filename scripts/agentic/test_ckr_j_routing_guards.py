#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,shutil,subprocess,sys,tempfile
from pathlib import Path
VALIDATOR="validate_ckr_j_routing.py"
def run(repo): return subprocess.run([sys.executable,str(repo/'scripts/agentic'/VALIDATOR),'--repo',str(repo)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
def mutate(repo,rel,transform,label,errors):
    path=repo/rel; original=path.read_text(encoding='utf-8')
    try:
        changed=transform(original)
        if changed==original: errors.append(f'{label}: mutation was a no-op'); return
        path.write_text(changed,encoding='utf-8')
        if run(repo)==0: errors.append(f'{label}: CKR-J validator unexpectedly passed')
        else: print(f'PASS negative control: {label}')
    finally: path.write_text(original,encoding='utf-8')
def json_transform(fn):
    def transform(text):
        data=json.loads(text); fn(data); return json.dumps(data,indent=2)+'\n'
    return transform
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); args=ap.parse_args(); src=Path(args.repo).resolve(); errors=[]
    with tempfile.TemporaryDirectory(prefix='dmtz-ckrj-guards-') as td:
        repo=Path(td)/'repo'; shutil.copytree(src,repo,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
        manifest=json.loads((repo/'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json').read_text(encoding='utf-8')); active=manifest.get('status')=='active'
        def drop_syn_target(d): d['stable_families']['SYN']['target_documents']=d['stable_families']['SYN']['target_documents'][:-1]
        def regress_family(d): d['stable_families']['ARCH']['migration_state']='candidate_ready'
        def bad_total(d): d['stable_reference']['accepted_total']=1238
        def first_match(d): d['stable_reference']['first_match_canonicality']=True
        def line_locator(d): d['stable_reference']['canonical_locator_format']='{owner_path}:{line}'
        def history_primary(d): d['okf_semantic_routes'][0]['primary_resource']='docs/concepts/phase_004/README.md'
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',json_transform(drop_syn_target),'stable-family target omission',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json',json_transform(regress_family),'stable-family ownership regression',errors)
        mutate(repo,'docs/canonical/architecture/frame-environment-decision-criteria.md',lambda t:t+'\n### ARCH-001 — duplicate routing definition\n','duplicate canonical stable definition across index/heading forms',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',json_transform(bad_total),'accepted stable-ID total drift',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',json_transform(first_match),'first-match canonicality regression',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',json_transform(line_locator),'line-number stable identity regression',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',json_transform(history_primary),'history path promoted as current OKF resource',errors)
        mutate(repo,'docs/canonical_knowledge_retrofit/fixtures/ckr_j_routing_scenarios.yaml',lambda t:t.replace('  - id: CKRJ-48\n','  - id: CKRJ-99\n',1),'CKR-J fixture identity drift',errors)
        if active:
            mutate(repo,'knowledge/domains/active-control.md',lambda t:t.replace('../../docs/canonical/architecture/active-control.md','../../docs/concepts/phase_010/07_execution_gate_propagation_safeguard_active_control_architecture/README.md',1),'active-control current route regression to Phase 010',errors)
            mutate(repo,'.agents/skills/resolve-contract/SKILL.md',lambda t:t.replace('--history','--old-history-mode'),'history/canonical resolver mode collapse',errors)
            mutate(repo,'scripts/agentic/resolve_stable_id.py',lambda t:t.replace('canonical_locator','legacy_locator'),'canonical resolver behavior marker removed',errors)
            mutate(repo,'scripts/agentic/knowledge_impact.py',lambda t:t.replace('BODY-LINK','SECONDARY'),'secondary OKF body-link impact coverage removed',errors)
        else:
            def premature_active(d): d['status']='active'
            mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',json_transform(premature_active),'premature CKR-J routing activation without atomic cutover',errors)
            mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',lambda t:t.replace('"history_discovery": "explicit_separate_on_demand"','"history_discovery": "mixed_with_default"',1),'default/history resolution collapse',errors)
            mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',lambda t:t.replace('"section_selector": "stable_id_token"','"section_selector": "line_number"',1),'unstable section selector',errors)
            mutate(repo,'docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json',lambda t:t.replace('"resolution_mode": "canonical_target_stable_definition"','"resolution_mode": "repository_first_match"',1),'repository search-order resolution regression',errors)
    for error in errors: print('ERROR',error)
    print(f'CKR-J routing guard tests: {len(errors)} error(s), 12 negative control(s)'); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
