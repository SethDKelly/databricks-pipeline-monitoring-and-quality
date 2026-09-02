#!/usr/bin/env python3
"""High-confidence secret/sensitive-file checks for checked-in agentic surfaces.

This is a narrow repository guard, not a replacement for organization-wide secret
scanning. It intentionally favors high-confidence credential forms to avoid turning
policy prose into false positives.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
from pathlib import Path

ROOTS = (
    'AGENTS.md',
    'IMPLEMENTATION.md',
    '.agents',
    '.claude',
    '.cursor',
    'knowledge',
    'docs/agentic_development_foundation',
    'docs/implementation/AGENTS.md',
    'docs/implementation/agent_reference_index.md',
)

TEXT_SUFFIXES = {'.md', '.mdc', '.json', '.yaml', '.yml', '.toml', '.txt'}
FORBIDDEN_FILE_PATTERNS = (
    '.env', '.env.*', '*.pem', '*.key', '*.p12', '*.pfx',
    'credentials.json', 'secrets.json', 'secrets.yaml', 'secrets.yml',
    'id_rsa', 'id_ed25519',
)

SECRET_PATTERNS = (
    ('private key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')),
    ('aws access key', re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b')),
    ('github classic token', re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b')),
    ('github fine-grained token', re.compile(r'\bgithub_pat_[A-Za-z0-9_]{40,}\b')),
    ('openai-style secret key', re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b')),
    ('anthropic secret key', re.compile(r'\bsk-ant-[A-Za-z0-9_-]{20,}\b')),
    ('slack token', re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b')),
    ('google api key', re.compile(r'\bAIza[0-9A-Za-z_-]{30,}\b')),
)

STRUCTURED_SECRET = re.compile(
    r'^\s*(password|passwd|secret|api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret)\s*[:=]\s*["\']?([^"\'\s#]+)',
    re.IGNORECASE | re.MULTILINE,
)
PLACEHOLDER_MARKERS = ('<', '${', 'redacted', 'placeholder', 'example', 'dummy', 'changeme', 'not-a-secret', 'not_secret')


def candidate_files(repo: Path):
    seen: set[Path] = set()
    for rel in ROOTS:
        path = repo / rel
        if path.is_file():
            files = [path]
        elif path.is_dir():
            files = [p for p in path.rglob('*') if p.is_file()]
        else:
            continue
        for file in files:
            if file in seen:
                continue
            seen.add(file)
            yield file


def is_forbidden_name(path: Path) -> bool:
    name = path.name
    return any(fnmatch.fnmatch(name, pattern) for pattern in FORBIDDEN_FILE_PATTERNS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    scanned = 0

    for path in candidate_files(repo):
        rel = path.relative_to(repo)
        if is_forbidden_name(path):
            errors.append(f'{rel}: secret-bearing filename is not allowed in agentic surfaces')
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {'AGENTS.md', 'CLAUDE.md'}:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        scanned += 1
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f'{rel}: high-confidence {label} pattern detected')
        for match in STRUCTURED_SECRET.finditer(text):
            value = match.group(2)
            lowered = value.lower()
            if len(value) >= 8 and not any(marker in lowered for marker in PLACEHOLDER_MARKERS):
                errors.append(f'{rel}: non-placeholder structured secret field {match.group(1)!r} detected')

    for error in errors:
        print(f'ERROR {error}')
    print(f'Agentic secret scan: {len(errors)} error(s), {scanned} text file(s) scanned')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
