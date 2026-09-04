#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

EXPECTED = {
    'A': 'adf_a_boundary_scenarios.yaml',
    'B': 'adf_b_knowledge_scenarios.yaml',
    'C': 'adf_c_adapter_scenarios.yaml',
    'D': 'adf_d_workflow_scenarios.yaml',
    'E': 'adf_e_context_scenarios.yaml',
    'F': 'adf_f_conformance_scenarios.yaml',
    'G': 'adf_g_compatibility_scenarios.yaml',
    'H': 'adf_h_security_scenarios.yaml',
}
ADDENDA = (
    ('DBX', 'adf_databricks_skills_addendum_scenarios.yaml', 'databricks_agent_skills_addendum_execution_review.md'),
)
CKR = (
    ('CKR-A', 'docs/canonical_knowledge_retrofit/fixtures/ckr_a_authority_scenarios.yaml', 'docs/canonical_knowledge_retrofit/ckr_a_execution_review.md'),
    ('CKR-B', 'docs/canonical_knowledge_retrofit/fixtures/ckr_b_foundation_scenarios.yaml', 'docs/canonical_knowledge_retrofit/ckr_b_execution_review.md'),
)
ID_RE = re.compile(r'^\s*-\s+id:\s*["\']?([^"\'\s]+)', re.M)


def collect(path: Path, label: str, seen: dict[str, str], errors: list[str]) -> int:
    if not path.is_file():
        errors.append(f'missing {label} fixture catalog: {path.name}')
        return 0
    text = path.read_text(encoding='utf-8')
    if 'scenarios:' not in text:
        errors.append(f'{path.name}: missing scenarios collection')
    ids = ID_RE.findall(text)
    if not ids:
        errors.append(f'{path.name}: no scenario IDs found')
    for scenario_id in ids:
        if scenario_id in seen:
            errors.append(f'duplicate scenario id {scenario_id}: {seen[scenario_id]} and {path.name}')
        seen[scenario_id] = path.name
    return len(ids)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    root = repo / 'docs/agentic_development_foundation/fixtures'
    errors: list[str] = []
    seen: dict[str, str] = {}
    count = 0

    for letter, name in EXPECTED.items():
        count += collect(root / name, f'ADF-{letter}', seen, errors)
        review = repo / f'docs/agentic_development_foundation/adf_{letter.lower()}_execution_review.md'
        if not review.is_file():
            errors.append(f'ADF-{letter}: missing execution review')

    for label, name, review_name in ADDENDA:
        count += collect(root / name, f'ADF addendum {label}', seen, errors)
        review = repo / 'docs/agentic_development_foundation' / review_name
        if not review.is_file():
            errors.append(f'ADF addendum {label}: missing execution review {review_name}')

    for label, fixture_rel, review_rel in CKR:
        count += collect(repo / fixture_rel, label, seen, errors)
        review = repo / review_rel
        if not review.is_file():
            errors.append(f'{label}: missing execution review {review_rel}')

    for error in errors:
        print(f'ERROR {error}')
    print(f'Fixture catalog validation: {len(errors)} error(s), {count} scenario(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
