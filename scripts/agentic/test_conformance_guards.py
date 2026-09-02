#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil, subprocess, sys, tempfile
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
        mutate_and_expect_failure(repo, 'IMPLEMENTATION.md', lambda t: t.replace('COMPLETE ADF-A–ADF-F; NEXT ADF-G.', 'COMPLETE ADF-A–ADF-E; NEXT ADF-F.', 1), 'validate_status_drift.py', 'stale implementation status mirror', errors)
        mutate_and_expect_failure(repo, 'knowledge/project/authority.md', lambda t: t.replace('resource:', 'resource: "../../definitely-missing.md"\nold_resource:', 1), 'validate_okf.py', 'broken canonical resource route', errors)
        mutate_and_expect_failure(repo, 'AGENTS.md', lambda t: t + '\nARCH-501\n', 'validate_agentic_references.py', 'unaccepted stable ID citation', errors)

    for error in errors:
        print(f'ERROR {error}')
    print(f'Conformance guard tests: {len(errors)} error(s), 7 negative control(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
