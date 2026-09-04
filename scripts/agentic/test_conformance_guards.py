#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path


def run(repo: Path, script: str) -> int:
    return subprocess.run([sys.executable, str(repo/'scripts/agentic'/script), '--repo', str(repo)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode


def mutate_and_expect_failure(repo: Path, rel: str, transform, script: str, label: str, errors: list[str]) -> None:
    path = repo / rel
    original = path.read_text(encoding='utf-8')
    try:
        path.write_text(transform(original), encoding='utf-8')
        if run(repo, script) == 0:
            errors.append(f'{label}: validator unexpectedly passed')
        else:
            print(f'PASS negative control: {label}')
    finally:
        path.write_text(original, encoding='utf-8')


def stale_status(text: str) -> str:
    return re.sub(
        r'ADF status mirror: .*?$',
        'ADF status mirror: COMPLETE ADF-A–ADF-E; NEXT ADF-F.',
        text,
        count=1,
        flags=re.MULTILINE,
    )


def stale_ckr_status(text: str) -> str:
    return re.sub(
        r'CKR status mirror: .*?$',
        'CKR status mirror: COMPLETE CKR-A; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.',
        text,
        count=1,
        flags=re.MULTILINE,
    )


def enable_vendor_auto_expansion(text: str) -> str:
    data = json.loads(text)
    data['materialization']['automatic_new_skills'] = True
    return json.dumps(data, indent=2) + '\n'


def add_deferred_model_skill(text: str) -> str:
    data = json.loads(text)
    data['selected_skills'].append({'name': 'databricks-model-serving', 'version': '0.4.0'})
    return json.dumps(data, indent=2) + '\n'


def fabricate_lineage_canonicalization(text: str) -> str:
    data = json.loads(text)
    for rec in data['records']:
        if rec['record_id'] == 'concept.lineage':
            rec['migration_state'] = 'canonicalized'
            break
    return json.dumps(data, indent=2) + '\n'


def move_lineage_target_outside_canonical(text: str) -> str:
    data = json.loads(text)
    for rec in data['records']:
        if rec['record_id'] == 'concept.lineage':
            rec['target_owner'] = 'docs/design_history/lineage.md'
            break
    return json.dumps(data, indent=2) + '\n'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    source = Path(args.repo).resolve()
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix='dmtz-adff-') as td:
        repo = Path(td) / 'repo'
        shutil.copytree(source, repo, ignore=shutil.ignore_patterns('.git', '__pycache__', '.pytest_cache'))

        mutate_and_expect_failure(repo, 'knowledge/project/authority.md', lambda t: t.replace('type:', 'missing_type:', 1), 'validate_okf.py', 'malformed OKF metadata', errors)
        mutate_and_expect_failure(repo, '.agents/skills/implement-group/SKILL.md', lambda t: t.replace('description:', 'model: forbidden\ndescription:', 1), 'validate_agent_skills.py', 'provider-specific skill metadata', errors)
        mutate_and_expect_failure(repo, '.cursor/rules/00-implementation-routing.mdc', lambda t: t.replace('alwaysApply: false', 'alwaysApply: true', 1), 'validate_agent_adapters.py', 'always-applied Cursor rule regression', errors)
        mutate_and_expect_failure(repo, 'AGENTS.md', lambda t: t + '\n' + ('x' * 20000), 'measure_context_budget.py', 'persistent-context overflow', errors)
        mutate_and_expect_failure(repo, 'IMPLEMENTATION.md', stale_status, 'validate_status_drift.py', 'stale ADF status mirror', errors)
        mutate_and_expect_failure(repo, 'knowledge/project/authority.md', lambda t: t.replace('resource:', 'resource: "../../definitely-missing.md"\nold_resource:', 1), 'validate_okf.py', 'broken canonical resource route', errors)
        mutate_and_expect_failure(repo, 'AGENTS.md', lambda t: t + '\nARCH-501\n', 'validate_agentic_references.py', 'unaccepted stable ID citation', errors)
        mutate_and_expect_failure(repo, 'docs/agentic_development_foundation/runtime_compatibility_evidence.json', lambda t: t.replace('"runtime_status": "unverified"', '"runtime_status": "supported"', 1), 'validate_adf_g_compatibility.py', 'fabricated provider runtime support', errors)
        mutate_and_expect_failure(repo, '.claude/CLAUDE.md', lambda t: t + '\ncredential: ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n', 'scan_agentic_secrets.py', 'checked-in high-confidence secret', errors)
        mutate_and_expect_failure(repo, 'docs/agentic_development_foundation/tool_lifecycle_review.json', lambda t: t.replace('"security_reviewed_on": "2026-09-02"', '"security_reviewed_on": "2020-01-01"', 1), 'validate_adf_h_governance.py', 'expired provider security review horizon', errors)
        mutate_and_expect_failure(repo, 'docs/agentic_development_foundation/databricks_vendor_skills_profile.json', enable_vendor_auto_expansion, 'validate_databricks_agent_skills.py', 'automatic Databricks vendor-skill expansion', errors)
        mutate_and_expect_failure(repo, 'docs/agentic_development_foundation/databricks_vendor_skills_profile.json', add_deferred_model_skill, 'validate_databricks_agent_skills.py', 'deferred model skill added to initial Databricks set', errors)
        mutate_and_expect_failure(repo, 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json', fabricate_lineage_canonicalization, 'validate_canonical_knowledge.py', 'canonicalization without canonical target evidence', errors)
        mutate_and_expect_failure(repo, 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json', move_lineage_target_outside_canonical, 'validate_canonical_knowledge.py', 'canonical target outside docs/canonical', errors)
        mutate_and_expect_failure(repo, 'IMPLEMENTATION.md', stale_ckr_status, 'validate_ckr_status.py', 'stale CKR implementation status mirror', errors)
        mutate_and_expect_failure(repo, 'docs/canonical/invariants/architectural-principles.md', lambda t: t.replace('### AP-32 —', '### AP-XX —', 1), 'validate_ckr_b_foundation.py', 'omitted CKR-B AP-32 identity', errors)
        mutate_and_expect_failure(repo, 'docs/canonical/policies/security-governance.md', lambda t: t.replace('### SP-15 —', '### SP-XX —', 1), 'validate_ckr_b_foundation.py', 'omitted CKR-B SP-15 identity', errors)
        mutate_and_expect_failure(repo, 'docs/canonical/policies/mvp-boundary.md', lambda t: t.replace('### Scenario K —', '### Scenario Z —', 1), 'validate_ckr_b_foundation.py', 'omitted CKR-B MVP Scenario K', errors)
        mutate_and_expect_failure(repo, 'docs/canonical/reference/product-definition.md', lambda t: t.replace('001_product_definition.md', 'missing-product-origin.md'), 'validate_ckr_b_foundation.py', 'broken CKR-B legacy provenance', errors)

    for error in errors:
        print(f'ERROR {error}')
    print(f'Conformance guard tests: {len(errors)} error(s), 19 negative control(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
