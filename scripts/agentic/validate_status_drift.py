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
STATE_RE = re.compile(r'^- \*\*ADF-([A-H]) — .*?: (COMPLETE / ACCEPTED|NEXT / READY)\.\*\*$', re.M)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    authority = repo / 'docs/agentic_development_foundation/README.md'
    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding='utf-8'))}
    complete = [c for c in 'ABCDEFGH' if states.get(c) == 'COMPLETE / ACCEPTED']
    nexts = [c for c in 'ABCDEFGH' if states.get(c) == 'NEXT / READY']
    errors: list[str] = []
    if len(nexts) != 1:
        errors.append(f'ADF authority must declare exactly one NEXT / READY group; found {nexts}')
    if complete:
        expected_complete = list('ABCDEFGH'[:len(complete)])
        if complete != expected_complete:
            errors.append(f'ADF completed groups are not contiguous from A: {complete}')
    if nexts and len(complete) < 8 and nexts[0] != 'ABCDEFGH'[len(complete)]:
        errors.append(f'ADF next group {nexts[0]} does not follow completed groups {complete}')

    if complete and nexts:
        mirror = f"ADF status mirror: COMPLETE ADF-A–ADF-{complete[-1]}; NEXT ADF-{nexts[0]}."
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
