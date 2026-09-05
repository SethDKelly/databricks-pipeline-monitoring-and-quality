#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VALIDATOR = 'validate_ckr_i_architecture.py'


def run(repo: Path) -> int:
    return subprocess.run(
        [sys.executable, str(repo / 'scripts/agentic' / VALIDATOR), '--repo', str(repo)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode


def mutate(repo: Path, rel: str, transform, label: str, errors: list[str]) -> None:
    path = repo / rel
    original = path.read_text(encoding='utf-8')
    try:
        path.write_text(transform(original), encoding='utf-8')
        if run(repo) == 0:
            errors.append(f'{label}: CKR-I validator unexpectedly passed')
        else:
            print(f'PASS negative control: {label}')
    finally:
        path.write_text(original, encoding='utf-8')


def json_transform(fn):
    def transform(text: str) -> str:
        data = json.loads(text)
        fn(data)
        return json.dumps(data, indent=2) + '\n'
    return transform


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    src = Path(args.repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix='dmtz-ckri-guards-') as td:
        repo = Path(td) / 'repo'
        shutil.copytree(src, repo, ignore=shutil.ignore_patterns('.git', '__pycache__', '.pytest_cache'))

        def drop_target(d):
            d['stable_families']['ARCH']['target_documents'] = d['stable_families']['ARCH']['target_documents'][:-1]

        def split_segment_state(d):
            d['architecture_segments'][0]['migration_state'] = 'legacy_authoritative'

        def move_reference_early(d):
            next(x for x in d['architecture_segments'] if x['record_id'] == 'architecture.reference_architecture')['migration_state'] = 'canonicalized'

        mutate(repo, 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json', json_transform(drop_target), 'partial CKR-I target topology', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json', json_transform(split_segment_state), 'partial CKR-I segment cutover', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json', json_transform(move_reference_early), 'reference architecture moves before ARCH family', errors)
        mutate(repo, 'docs/canonical/architecture/frame-environment-decision-criteria.md', lambda t: t.replace('ARCH-032', 'ARCH-999'), 'omitted CKR-I ARCH-032 identity', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('documented capability ≠ deployment presence ≠ entitlement ≠ enablement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability', 'documented capability = deployment support'), 'vendor capability/deployment collapse regression', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('framework retention authority ≠ source Assertion Authority', 'framework retention authority = source Assertion Authority'), 'retention/source-authority collapse regression', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('GitHub Actions success ≠ Databricks activation; deployment ≠ activation ≠ run', 'GitHub Actions success = Databricks activation = run'), 'runtime activation/join overclaim regression', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('current state/config/policy ≠ historical state; Delta transaction-log time travel ≠ DMTZ historical replay contract', 'current state/config/policy = historical state; Delta time travel = historical replay'), 'historical replay collapse regression', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('evidence suitability ≠ readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution', 'evidence suitability = readiness = Gate decision = enforcement = execution'), 'Gate lifecycle collapse regression', errors)
        mutate(repo, 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md', lambda t: t.replace('Safeguard active + not exposed ≠ REF-028 prevention without opportunity/path/alternate-path evidence', 'Safeguard active + not exposed = REF-028 prevention'), 'Safeguard prevention overclaim regression', errors)
        mutate(repo, 'docs/canonical/architecture/reference-architecture.md', lambda t: t.replace('No ARCH-501 is required', 'ARCH-501 is required'), 'unaccepted ARCH-501 reference architecture expansion', errors)

    for error in errors:
        print('ERROR', error)
    print(f'CKR-I architecture guard tests: {len(errors)} error(s), 11 negative control(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
