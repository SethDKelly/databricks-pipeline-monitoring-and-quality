#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

PROFILE = 'docs/agentic_development_foundation/databricks_vendor_skills_profile.json'
EXPECTED_SELECTED = {
    'databricks-core',
    'databricks-dabs',
    'databricks-jobs',
    'databricks-pipelines',
    'databricks-data-discovery',
    'databricks-dbsql',
    'databricks-unity-catalog',
    'databricks-lakeflow-connect',
}
OVERLAYS = {
    'dmtz-databricks-environment-discovery',
    'dmtz-databricks-acquisition',
    'dmtz-databricks-persistence',
    'dmtz-databricks-lineage',
    'dmtz-databricks-runtime-provenance',
    'dmtz-databricks-governance',
}
DEFERRED_MODELS = {
    'databricks-model-serving',
    'databricks-ml-training',
    'databricks-mlflow-evaluation',
    'databricks-agent-bricks',
    'databricks-ai-functions',
    'databricks-ai-runtime',
    'databricks-vector-search',
}
SEMVER = re.compile(r'^\d+\.\d+\.\d+$')
SHA40 = re.compile(r'^[0-9a-f]{40}$')
NAME_RE = re.compile(r'^name:\s*["\']?([^"\'\s]+)', re.M)
VERSION_RE = re.compile(r'^\s*version:\s*["\']?([^"\'\s]+)', re.M)


def local_materialization_errors(root: Path, expected: dict[str, str]) -> list[str]:
    if not root.is_dir():
        return []
    found: dict[str, str] = {}
    for path in root.rglob('SKILL.md'):
        text = path.read_text(encoding='utf-8')
        n = NAME_RE.search(text)
        v = VERSION_RE.search(text)
        if n and v and n.group(1).startswith('databricks-'):
            found[n.group(1)] = v.group(1)
    errors: list[str] = []
    for name, version in expected.items():
        if name not in found:
            errors.append(f'local materialization missing {name}')
        elif found[name] != version:
            errors.append(f'local {name} version {found[name]} != reviewed {version}')
    extras = sorted(set(found) - set(expected))
    if extras:
        errors.append(f'local materialization contains unreviewed skills: {extras}')
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    path = repo / PROFILE
    if not path.is_file():
        print(f'ERROR missing {PROFILE}')
        return 1
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        print(f'ERROR invalid Databricks vendor profile JSON: {exc}')
        return 1

    upstream = data.get('upstream', {})
    if upstream.get('repository') != 'databricks/databricks-agent-skills':
        errors.append('upstream repository must be databricks/databricks-agent-skills')
    if not SHA40.match(str(upstream.get('commit', ''))):
        errors.append('reviewed upstream commit must be a 40-character Git SHA')
    sources = upstream.get('official_docs', [])
    if len(sources) < 2 or any(not str(s).startswith('https://docs.databricks.com/') for s in sources):
        errors.append('official Databricks documentation references are required')
    try:
        reviewed = dt.date.fromisoformat(data.get('reviewed_on', ''))
    except ValueError:
        errors.append('reviewed_on must be ISO date')
        reviewed = None
    horizon = data.get('review_horizon_days')
    if not isinstance(horizon, int) or horizon <= 0 or horizon > 90:
        errors.append('review_horizon_days must be between 1 and 90')
    elif reviewed:
        age = (dt.date.today() - reviewed).days
        if age < 0:
            errors.append('reviewed_on cannot be in the future')
        elif age > horizon:
            errors.append(f'Databricks vendor skill review exceeds {horizon}-day horizon ({age} days old)')

    selected = data.get('selected_skills', [])
    if not isinstance(selected, list):
        selected = []
        errors.append('selected_skills must be a list')
    names = [item.get('name') for item in selected if isinstance(item, dict)]
    if set(names) != EXPECTED_SELECTED or len(names) != len(EXPECTED_SELECTED):
        errors.append(f'initial selected skill set drifted; expected {sorted(EXPECTED_SELECTED)}, got {sorted(n for n in names if n)}')
    for item in selected:
        if not isinstance(item, dict) or not SEMVER.match(str(item.get('version', ''))):
            errors.append(f'invalid reviewed vendor skill entry: {item!r}')
    if set(names) & DEFERRED_MODELS:
        errors.append('deferred model/AI skill entered the initial selected set')
    deferred = set(data.get('deferred_model_ai_skills', []))
    if not DEFERRED_MODELS.issubset(deferred):
        errors.append('deferred model/AI list lost a required initial exclusion')

    material = data.get('materialization', {})
    if material.get('mode') != 'aitools_path' or material.get('path') != '.databricks/agent-skills':
        errors.append('vendor materialization must use controlled aitools_path under .databricks/agent-skills')
    if material.get('agent_configuration_modified') is not False or material.get('install_state_written') is not False:
        errors.append('reviewed materialization must not modify agent configuration or write aitools install state')
    if material.get('automatic_new_skills') is not False:
        errors.append('automatic new Databricks skill installation must remain disabled')
    mcp = data.get('managed_mcp_servers', {})
    if mcp.get('status') != 'not_configured_by_addendum':
        errors.append('managed MCP servers must remain outside this addendum')

    if not (repo / '.gitignore').read_text(encoding='utf-8').find('.databricks/') >= 0:
        errors.append('.databricks/ must remain ignored')
    for vendor_copy in (repo / '.agents' / 'skills').glob('databricks-*'):
        if vendor_copy.is_dir():
            errors.append(f'vendor skill copied into canonical DMTZ skill directory: {vendor_copy.relative_to(repo)}')
    for overlay in OVERLAYS:
        if not (repo / '.agents/skills' / overlay / 'SKILL.md').is_file():
            errors.append(f'missing DMTZ Databricks overlay: {overlay}')
        if not (repo / '.claude/commands' / f'{overlay}.md').is_file():
            errors.append(f'missing Claude bridge for DMTZ Databricks overlay: {overlay}')
        if not (repo / 'knowledge/workflows' / f'{overlay}.md').is_file():
            errors.append(f'missing OKF route for DMTZ Databricks overlay: {overlay}')

    addendum = repo / 'docs/agentic_development_foundation/databricks_agent_skills_addendum.md'
    if not addendum.is_file():
        errors.append('missing Databricks Agent Skills addendum')
    else:
        text = addendum.read_text(encoding='utf-8')
        for phrase in ('Databricks skills know how Databricks works', 'Unity Catalog', 'Lakeflow Connect', 'A vendor skill recommendation never grants A3/A4 permission', 'Managed MCP servers'):
            if phrase not in text:
                errors.append(f'addendum missing required boundary: {phrase!r}')

    expected_versions = {item['name']: item['version'] for item in selected if isinstance(item, dict) and item.get('name') and item.get('version')}
    local = repo / '.databricks/agent-skills'
    local_errors = local_materialization_errors(local, expected_versions)
    errors.extend(local_errors)
    if not local.exists():
        warnings.append('local Databricks vendor-skill materialization not present; expected until Implementation 001-A environment setup')

    for warning in warnings:
        print(f'WARN {warning}')
    for error in errors:
        print(f'ERROR {error}')
    print(f'Databricks Agent Skills addendum validation: {len(errors)} error(s), {len(warnings)} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
