#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, json, subprocess, sys
from pathlib import Path

CHECKS = (
    ('documentation consistency', 'scripts/check_docs_consistency.py', []),
    ('OKF structure/resources', 'scripts/agentic/validate_okf.py', []),
    ('tool adapters', 'scripts/agentic/validate_agent_adapters.py', []),
    ('portable skills', 'scripts/agentic/validate_agent_skills.py', []),
    ('agentic references', 'scripts/agentic/validate_agentic_references.py', ['--repo', '{repo}']),
    ('ADF status drift', 'scripts/agentic/validate_status_drift.py', ['--repo', '{repo}']),
    ('canonical knowledge authority', 'scripts/agentic/validate_canonical_knowledge.py', ['--repo', '{repo}']),
    ('CKR-B foundation semantic coverage', 'scripts/agentic/validate_ckr_b_foundation.py', ['--repo', '{repo}']),
    ('CKR status drift', 'scripts/agentic/validate_ckr_status.py', ['--repo', '{repo}']),
    ('fixture catalog', 'scripts/agentic/validate_fixture_catalog.py', ['--repo', '{repo}']),
    ('context budgets', 'scripts/agentic/measure_context_budget.py', ['{repo}']),
    ('ADF-G compatibility evidence', 'scripts/agentic/validate_adf_g_compatibility.py', ['--repo', '{repo}']),
    ('Databricks Agent Skills addendum', 'scripts/agentic/validate_databricks_agent_skills.py', ['--repo', '{repo}']),
    ('agentic secret scan', 'scripts/agentic/scan_agentic_secrets.py', ['--repo', '{repo}']),
    ('ADF-H security/lifecycle governance', 'scripts/agentic/validate_adf_h_governance.py', ['--repo', '{repo}']),
)


def knowledge_lifecycle(repo: Path) -> tuple[int, int]:
    deprecated = stale = 0
    today = dt.date.today()
    for path in (repo/'knowledge').rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        if 'status: "deprecated"' in text or 'status: deprecated' in text:
            deprecated += 1
        for line in text.splitlines():
            if line.startswith('stale_after:'):
                raw = line.split(':', 1)[1].strip().strip("\"'")[:10]
                try:
                    if dt.date.fromisoformat(raw) <= today:
                        stale += 1
                except ValueError:
                    pass
    return deprecated, stale


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    ap.add_argument('--report')
    ap.add_argument('--skip-negative-controls', action='store_true')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    results: list[tuple[str, int, str]] = []

    for name, rel, extra in CHECKS:
        cmd = [sys.executable, str(repo/rel)] + [x.format(repo=str(repo)) for x in extra]
        proc = subprocess.run(cmd, cwd=repo, text=True, capture_output=True)
        output = (proc.stdout + proc.stderr).strip()
        results.append((name, proc.returncode, output))
        print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} {name}")
        if output:
            print(output)

    if not args.skip_negative_controls:
        proc = subprocess.run([sys.executable, str(repo/'scripts/agentic/test_conformance_guards.py'), '--repo', str(repo)], cwd=repo, text=True, capture_output=True)
        output = (proc.stdout + proc.stderr).strip()
        results.append(('negative controls', proc.returncode, output))
        print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} negative controls")
        if output:
            print(output)

    compat = json.loads((repo/'docs/agentic_development_foundation/tool_compatibility.json').read_text(encoding='utf-8'))['tools']
    deprecated, stale = knowledge_lifecycle(repo)
    overall = 'PASS' if all(code == 0 for _, code, _ in results) else 'FAIL'
    lines = [
        '# Agentic Conformance Report',
        '',
        f'**Agentic configuration conformance:** {overall}',
        '',
        '> This report describes repository agentic/documentation-authority configuration health only. It is not DMTZ domain health, data quality, source health, or production readiness.',
        '',
        '## Checks',
        '',
        '| Check | Result |',
        '|---|---|',
    ]
    lines += [f'| {name} | {"PASS" if code == 0 else "FAIL"} |' for name, code, _ in results]
    lines += ['', '## Tool compatibility state', '']
    for tool, data in compat.items():
        runtime = data.get('runtime_status', 'unknown')
        lines.append(f'- **{tool}:** `{data.get("support_status", "unknown")}` / runtime `{runtime}`')
    lines += [
        '',
        '## Knowledge lifecycle',
        '',
        f'- Deprecated knowledge entries: **{deprecated}**',
        f'- Stale knowledge entries: **{stale}**',
        '',
        '## Notes',
        '',
        '- Provider tool-in-the-loop runtime verification remains independent per tool; ADF-EX-17 is currently deferred under the bounded progression exception.',
        '- CKR changes documentation authority/routing, not accepted DMTZ semantics; Implementation 001-A remains blocked until CKR exit.',
        '- CKR-B semantic coverage checks protect the first substantive foundation/glossary migration from silent omission of accepted principles, lifecycles or MVP scenarios.',
        '- `docs/canonical/` becomes current semantic authority only record-by-record through the CKR migration inventory and atomic cutover contract.',
        '- Databricks vendor skills are reviewed operational dependencies; local `aitools --path` materialization remains an Implementation 001-A environment verification after CKR unlocks implementation.',
        '- Managed Databricks MCP servers are not configured by the Databricks Agent Skills addendum and require separate security/integration review.',
        '- Agentic secret scanning is a high-confidence repository guard, not a replacement for organization-wide secret scanning.',
        '- A tool may be degraded/unverified without converting another tool or DMTZ domain status to failure.',
        '',
    ]
    report = '\n'.join(lines)
    if args.report:
        out = Path(args.report)
        if not out.is_absolute():
            out = repo / out
        out.write_text(report, encoding='utf-8')
    print(report)
    return 0 if overall == 'PASS' else 1

if __name__ == '__main__':
    raise SystemExit(main())
