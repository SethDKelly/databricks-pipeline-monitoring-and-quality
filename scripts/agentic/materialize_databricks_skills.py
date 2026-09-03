#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

PROFILE = 'docs/agentic_development_foundation/databricks_vendor_skills_profile.json'
NAME_RE = re.compile(r'^name:\s*["\']?([^"\'\s]+)', re.M)
VERSION_RE = re.compile(r'^\s*version:\s*["\']?([^"\'\s]+)', re.M)
CLI_VERSION_RE = re.compile(r'(\d+)\.(\d+)\.(\d+)')


def load_profile(repo: Path) -> dict:
    return json.loads((repo / PROFILE).read_text(encoding='utf-8'))


def parse_semver(text: str) -> tuple[int, int, int] | None:
    match = CLI_VERSION_RE.search(text)
    return tuple(map(int, match.groups())) if match else None


def discover(root: Path) -> dict[str, tuple[str, Path]]:
    found: dict[str, tuple[str, Path]] = {}
    if not root.is_dir():
        return found
    for skill in root.rglob('SKILL.md'):
        text = skill.read_text(encoding='utf-8')
        name = NAME_RE.search(text)
        version = VERSION_RE.search(text)
        if name and version and name.group(1).startswith('databricks-'):
            found[name.group(1)] = (version.group(1), skill)
    return found


def validate_materialized(root: Path, profile: dict) -> list[str]:
    expected = {item['name']: item['version'] for item in profile['selected_skills']}
    found = discover(root)
    errors: list[str] = []
    for name, version in expected.items():
        if name not in found:
            errors.append(f'missing materialized skill {name}')
        elif found[name][0] != version:
            errors.append(f'{name}: materialized version {found[name][0]} != reviewed {version}')
    extras = sorted(set(found) - set(expected))
    if extras:
        errors.append(f'unreviewed materialized Databricks skills present: {extras}')
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    ap.add_argument('--execute', action='store_true', help='Run the reviewed aitools --path materialization command.')
    ap.add_argument('--replace', action='store_true', help='Remove only the configured ignored materialization directory before executing.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    profile = load_profile(repo)
    rel = Path(profile['materialization']['path'])
    if rel != Path('.databricks/agent-skills'):
        print('ERROR materialization path must remain .databricks/agent-skills')
        return 1
    dest = (repo / rel).resolve()
    if repo not in dest.parents:
        print('ERROR materialization path escaped repository')
        return 1

    selected = [item['name'] for item in profile['selected_skills']]
    cmd = ['databricks', 'aitools', 'install', '--path', str(dest), '--skills', ','.join(selected)]
    print('Reviewed materialization command:')
    print(' '.join(shlex.quote(part) for part in cmd))

    if not args.execute:
        if dest.exists():
            errors = validate_materialized(dest, profile)
            for error in errors:
                print(f'ERROR {error}')
            print(f'Local Databricks skill materialization: {len(errors)} error(s)')
            return 1 if errors else 0
        print('INFO local vendor-skill materialization is absent; execute during Implementation 001-A or an explicitly authorized developer setup task.')
        return 0

    binary = shutil.which('databricks')
    if not binary:
        print('ERROR databricks CLI is not installed or not on PATH')
        return 1
    version_proc = subprocess.run([binary, '--version'], cwd=repo, text=True, capture_output=True)
    version_text = (version_proc.stdout + version_proc.stderr).strip()
    print(f'Databricks CLI: {version_text}')
    actual = parse_semver(version_text)
    required = parse_semver(profile['minimum_databricks_cli'])
    if version_proc.returncode != 0 or not actual or not required or actual < required:
        print(f'ERROR selected profile requires Databricks CLI >= {profile["minimum_databricks_cli"]}')
        return 1

    if dest.exists() and any(dest.iterdir()):
        if not args.replace:
            print(f'ERROR {rel} is not empty; rerun with --replace only after reviewing the selected profile/upstream change')
            return 1
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, cwd=repo)
    if proc.returncode != 0:
        return proc.returncode
    errors = validate_materialized(dest, profile)
    for error in errors:
        print(f'ERROR {error}')
    print(f'Local Databricks skill materialization: {len(errors)} error(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
