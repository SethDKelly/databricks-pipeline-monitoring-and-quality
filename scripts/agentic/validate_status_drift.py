#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

MIRRORS = (
    'AGENTS.md',
    'IMPLEMENTATION.md',
    'docs/implementation/README.md',
    'docs/implementation/AGENTS.md',
    'docs/implementation/agent_reference_index.md',
    '.cursor/rules/00-implementation-routing.mdc',
)
STATE_RE = re.compile(r'^- \*\*ADF-([A-H]) — .*?: (.+?)\.\*\*$', re.M)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    authority = repo / 'docs/agentic_development_foundation/README.md'
    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding='utf-8'))}
    complete = [c for c in 'ABCDEFGH' if states.get(c) == 'COMPLETE / ACCEPTED']
    nexts = [c for c in 'ABCDEFGH' if states.get(c) == 'NEXT / READY']
    in_progress = [c for c in 'ABCDEFGH' if str(states.get(c, '')).startswith('IN EXECUTION')]
    errors: list[str] = []

    if complete:
        expected_complete = list('ABCDEFGH'[:len(complete)])
        if complete != expected_complete:
            errors.append(f'ADF completed groups are not contiguous from A: {complete}')

    active = nexts + in_progress
    if len(active) != 1 and len(complete) < 8:
        errors.append(f'ADF authority must declare exactly one NEXT / READY or IN EXECUTION group; found next={nexts}, in_progress={in_progress}')
    if active and len(complete) < 8 and active[0] != 'ABCDEFGH'[len(complete)]:
        errors.append(f'ADF active group {active[0]} does not follow completed groups {complete}')
    if nexts and in_progress:
        errors.append('ADF authority cannot declare NEXT / READY and IN EXECUTION groups simultaneously')

    mirror = None
    if complete and in_progress:
        mirror = f"ADF status mirror: COMPLETE ADF-A–ADF-{complete[-1]}; IN EXECUTION ADF-{in_progress[0]}."
    elif complete and nexts:
        mirror = f"ADF status mirror: COMPLETE ADF-A–ADF-{complete[-1]}; NEXT ADF-{nexts[0]}."

    if mirror:
        for rel in MIRRORS:
            path = repo / rel
            if not path.is_file():
                errors.append(f'missing live ADF status mirror surface: {rel}')
                continue
            if mirror not in path.read_text(encoding='utf-8'):
                errors.append(f'{rel}: missing current status mirror {mirror!r}')
        print(mirror)

    for error in errors:
        print(f'ERROR {error}')
    print(f'ADF status drift validation: {len(errors)} error(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
