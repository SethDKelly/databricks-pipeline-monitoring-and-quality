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
EXIT_ACCEPTED = '**Status:** ACCEPTED — AGENTIC DEVELOPMENT FOUNDATION EXECUTION EXIT COMPLETE'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    authority = repo / 'docs/agentic_development_foundation/README.md'
    states = {letter: state for letter, state in STATE_RE.findall(authority.read_text(encoding='utf-8'))}
    complete = [c for c in 'ABCDEFGH' if str(states.get(c, '')).startswith('COMPLETE / ACCEPTED')]
    nexts = [c for c in 'ABCDEFGH' if states.get(c) == 'NEXT / READY']
    in_progress = [c for c in 'ABCDEFGH' if str(states.get(c, '')).startswith('IN EXECUTION')]
    deferred = [c for c in complete if 'DEFERRED VERIFICATION' in str(states.get(c, ''))]
    exit_review = repo / 'docs/agentic_development_foundation/execution_exit_review.md'
    exit_accepted = exit_review.is_file() and EXIT_ACCEPTED in exit_review.read_text(encoding='utf-8')
    errors: list[str] = []

    if complete:
        expected_complete = list('ABCDEFGH'[:len(complete)])
        if complete != expected_complete:
            errors.append(f'ADF completed groups are not contiguous from A: {complete}')

    active = nexts + in_progress
    if len(complete) < 8:
        if exit_accepted:
            errors.append('ADF execution exit cannot be accepted before all ADF-A–ADF-H groups are complete')
        if len(active) != 1:
            errors.append(f'ADF authority must declare exactly one NEXT / READY or IN EXECUTION group; found next={nexts}, in_progress={in_progress}')
        elif active[0] != 'ABCDEFGH'[len(complete)]:
            errors.append(f'ADF active group {active[0]} does not follow completed groups {complete}')
    elif active:
        errors.append(f'all ADF groups are complete; no ADF group may remain active: {active}')
    if nexts and in_progress:
        errors.append('ADF authority cannot declare NEXT / READY and IN EXECUTION groups simultaneously')
    if deferred and deferred != ['G']:
        errors.append(f'only the explicit ADF-G runtime verification exception is currently authorized; found deferred={deferred}')

    mirror = None
    deferred_suffix = ' (ADF-EX-17 deferred)' if deferred else ''
    if len(complete) == 8:
        mirror = 'ADF status mirror: COMPLETE ADF-A–ADF-H; '
        if deferred:
            mirror += 'ADF-EX-17 DEFERRED VERIFICATION; '
        if exit_accepted:
            mirror += 'FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.'
        else:
            mirror += 'EXECUTION EXIT REVIEW NEXT.'
    elif complete and in_progress:
        mirror = f"ADF status mirror: COMPLETE ADF-A–ADF-{complete[-1]}{deferred_suffix}; IN EXECUTION ADF-{in_progress[0]}."
    elif complete and nexts:
        mirror = f"ADF status mirror: COMPLETE ADF-A–ADF-{complete[-1]}{deferred_suffix}; NEXT ADF-{nexts[0]}."

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
