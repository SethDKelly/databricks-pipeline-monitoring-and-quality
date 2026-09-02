#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from urllib.parse import urlparse

LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
ID_RE = re.compile(r'\b(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})\b')


def local_target(source: Path, target: str, repo: Path) -> Path | None:
    target = target.strip().split('#', 1)[0].strip()
    if not target or target.startswith(('http://', 'https://', 'mailto:')):
        return None
    if urlparse(target).scheme:
        return None
    return (repo / target.lstrip('/')).resolve() if target.startswith('/') else (source.parent / target).resolve()


def files_for_links(repo: Path) -> list[Path]:
    paths = [repo/'AGENTS.md', repo/'IMPLEMENTATION.md', repo/'docs/implementation/AGENTS.md', repo/'docs/implementation/agent_reference_index.md']
    for root in (repo/'docs/agentic_development_foundation', repo/'.agents', repo/'.claude', repo/'.cursor', repo/'knowledge'):
        if root.exists():
            paths.extend(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in {'.md', '.mdc'})
    return sorted(set(paths))


def operational_files(repo: Path) -> list[Path]:
    paths = [repo/'AGENTS.md', repo/'IMPLEMENTATION.md', repo/'docs/implementation/AGENTS.md', repo/'docs/implementation/agent_reference_index.md']
    for root in (repo/'.agents', repo/'.claude', repo/'.cursor', repo/'knowledge'):
        if root.exists():
            paths.extend(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in {'.md', '.mdc'})
    return sorted(set(paths))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    for path in files_for_links(repo):
        if not path.is_file():
            errors.append(f'missing agent-facing file: {path.relative_to(repo)}')
            continue
        text = path.read_text(encoding='utf-8')
        for raw in LINK_RE.findall(text):
            target = local_target(path, raw, repo)
            if target is not None and not target.exists():
                errors.append(f'{path.relative_to(repo)}: broken local link {raw}')

    registry = json.loads((repo/'docs/agentic_development_foundation/stable_id_registry.json').read_text(encoding='utf-8'))['families']
    ids: set[tuple[str, int]] = set()
    for path in operational_files(repo):
        if path.is_file():
            for family, number in ID_RE.findall(path.read_text(encoding='utf-8')):
                ids.add((family, int(number)))

    canonical_parts: list[str] = []
    for path in (repo/'docs').rglob('*.md'):
        rel = path.relative_to(repo).as_posix()
        if rel.startswith('docs/agentic_development_foundation/') or rel.startswith('docs/implementation/'):
            continue
        canonical_parts.append(path.read_text(encoding='utf-8', errors='ignore'))
    canonical_text = '\n'.join(canonical_parts)

    for family, number in sorted(ids):
        limits = registry.get(family)
        token = f'{family}-{number:03d}'
        if not limits or not (limits['min'] <= number <= limits['max']):
            errors.append(f'operational agent-facing artifact cites unaccepted stable ID {token}')
        elif not re.search(rf'(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])', canonical_text):
            errors.append(f'{token}: no occurrence found in canonical non-implementation docs')

    for error in errors:
        print(f'ERROR {error}')
    print(f'Agentic reference validation: {len(errors)} error(s), {len(ids)} unique stable ID(s) checked')
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
