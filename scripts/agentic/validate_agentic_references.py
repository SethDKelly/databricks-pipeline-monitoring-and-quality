#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from urllib.parse import urlparse
LINK_RE=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
ID_RE=re.compile(r'\b(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})\b')
HEADING_RE=re.compile(r'^#{2,6}\s+((?:SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-\d{3})(?:\s|—|-|:|$)')
TOKEN_RE=re.compile(r'\b(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})\b')
INDEX_PREFIX='**Stable ID index:**'
def local_target(source,target,repo):
    target=target.strip().split('#',1)[0].strip()
    if not target or target.startswith(('http://','https://','mailto:')) or urlparse(target).scheme: return None
    return (repo/target.lstrip('/')).resolve() if target.startswith('/') else (source.parent/target).resolve()
def files_for_links(repo):
    paths=[repo/'AGENTS.md',repo/'IMPLEMENTATION.md',repo/'docs/implementation/AGENTS.md',repo/'docs/implementation/agent_reference_index.md']
    for root in (repo/'docs/agentic_development_foundation',repo/'docs/canonical_knowledge_retrofit',repo/'docs/canonical',repo/'docs/design_history',repo/'.agents',repo/'.claude',repo/'.cursor',repo/'knowledge'):
        if root.exists(): paths.extend(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in {'.md','.mdc'})
    return sorted(set(paths))
def operational_files(repo):
    paths=[repo/'AGENTS.md',repo/'IMPLEMENTATION.md',repo/'docs/implementation/AGENTS.md',repo/'docs/implementation/agent_reference_index.md']
    for root in (repo/'.agents',repo/'.claude',repo/'.cursor',repo/'knowledge'):
        if root.exists(): paths.extend(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in {'.md','.mdc'})
    return sorted(set(paths))
def canonical_count(repo,family,token,owner):
    count=0
    for rel in owner.get('target_documents',[]):
        path=repo/rel
        if not path.is_file(): continue
        for raw in path.read_text(encoding='utf-8',errors='ignore').splitlines():
            line=raw.strip(); h=HEADING_RE.match(line)
            if h and h.group(1)==token: count+=1
            if family=='ARCH' and line.startswith(INDEX_PREFIX):
                if token in {f'{fam}-{num}' for fam,num in TOKEN_RE.findall(line)}: count+=1
            if family=='ARCH' and line.startswith('`ARCH-'):
                if token in {f'{fam}-{num}' for fam,num in TOKEN_RE.findall(line)}: count+=1
    return count
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); a=ap.parse_args(); repo=Path(a.repo).resolve(); errors=[]
    for path in files_for_links(repo):
        if not path.is_file(): errors.append(f'missing agent-facing file: {path.relative_to(repo)}'); continue
        text=path.read_text(encoding='utf-8')
        for raw in LINK_RE.findall(text):
            target=local_target(path,raw,repo)
            if target is not None and not target.exists(): errors.append(f'{path.relative_to(repo)}: broken local link {raw}')
    registry=json.loads((repo/'docs/agentic_development_foundation/stable_id_registry.json').read_text(encoding='utf-8'))['families']
    inventory=json.loads((repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8'))['stable_families']
    ids=set()
    for path in operational_files(repo):
        if path.is_file():
            for family,number in ID_RE.findall(path.read_text(encoding='utf-8')): ids.add((family,int(number)))
    for family,number in sorted(ids):
        limits=registry.get(family); token=f'{family}-{number:03d}'
        if not limits or not (limits['min']<=number<=limits['max']):
            errors.append(f'operational agent-facing artifact cites unaccepted stable ID {token}'); continue
        owner=inventory.get(family,{})
        if owner.get('migration_state')!='canonicalized':
            errors.append(f'{token}: owning family is not canonicalized'); continue
        count=canonical_count(repo,family,token,owner)
        if count!=1: errors.append(f'{token}: expected exactly one canonical stable definition in inventoried target documents; found {count}')
    for e in errors: print('ERROR',e)
    print(f'Agentic reference validation: {len(errors)} error(s), {len(ids)} unique stable ID(s) checked against canonical owners')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
