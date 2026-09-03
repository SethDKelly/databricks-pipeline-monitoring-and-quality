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
ID_RE = re.compile(r'^\s*-\s+id:\s*["\']?([^"\'\s]+)', re.M)


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
        path = root / name
        if not path.is_file():
            errors.append(f'missing ADF-{letter} fixture catalog: {name}')
            continue
        text = path.read_text(encoding='utf-8')
        if 'scenarios:' not in text:
            errors.append(f'{name}: missing scenarios collection')
        ids = ID_RE.findall(text)
        if not ids:
            errors.append(f'{name}: no scenario IDs found')
        for scenario_id in ids:
            count += 1
            if scenario_id in seen:
                errors.append(f'duplicate scenario id {scenario_id}: {seen[scenario_id]} and {name}')
            seen[scenario_id] = name
        review = repo / f'docs/agentic_development_foundation/adf_{letter.lower()}_execution_review.md'
        if not review.is_file():
            errors.append(f'ADF-{letter}: missing execution review')
    for error in errors:
        print(f'ERROR {error}')
    print(f'Fixture catalog validation: {len(errors)} error(s), {count} scenario(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
