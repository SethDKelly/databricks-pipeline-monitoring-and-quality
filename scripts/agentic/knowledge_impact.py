#!/usr/bin/env python3
"""Report OKF routing concepts affected by changed canonical resources.

RESOURCE and BODY-LINK relationships are review-impact hints only. A candidate is
not automatically stale and this helper never changes canonical semantics.
"""
from __future__ import annotations
import argparse,re
from pathlib import Path
from urllib.parse import urlparse
TOP_KEY=re.compile(r'^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$')
LINK_RE=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
def frontmatter(path):
    lines=path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0].strip()!='---': return {}
    data={}
    for line in lines[1:]:
        if line.strip()=='---': break
        m=TOP_KEY.match(line)
        if m: data[m.group(1)]=m.group(2).strip().strip("\"'")
    return data
def local_target(source,target,repo):
    target=target.strip().split('#',1)[0].strip()
    if not target or target.startswith(('http://','https://','mailto:')) or urlparse(target).scheme: return None
    return (repo/target.lstrip('/')).resolve() if target.startswith('/') else (source.parent/target).resolve()
def add(reverse,target,concept,role):
    reverse.setdefault(target,[])
    item=(concept,role)
    if item not in reverse[target]: reverse[target].append(item)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--changed',action='append',default=[]); ap.add_argument('--all',action='store_true',help='show complete reverse routing map'); a=ap.parse_args()
    repo=Path(a.repo).resolve(); reverse={}
    for concept in sorted((repo/'knowledge').rglob('*.md')):
        if concept.name in {'index.md','log.md'}: continue
        text=concept.read_text(encoding='utf-8'); meta=frontmatter(concept)
        resource=local_target(concept,meta.get('resource',''),repo)
        if resource is not None: add(reverse,resource,concept,'RESOURCE')
        for raw in LINK_RE.findall(text):
            target=local_target(concept,raw,repo)
            if target is not None and target.is_relative_to(repo) and target.relative_to(repo).as_posix().startswith('docs/canonical/'):
                add(reverse,target,concept,'BODY-LINK')
    if a.all:
        for target,items in sorted(reverse.items(),key=lambda x:str(x[0])):
            shown=target.relative_to(repo) if target.is_relative_to(repo) else target; print(shown)
            for concept,role in sorted(items,key=lambda x:(str(x[0]),x[1])): print(f'  {role:9} {concept.relative_to(repo)}')
        return 0
    if not a.changed: ap.error('provide --changed <repository-path> or --all')
    found=0
    for raw in a.changed:
        changed=(repo/raw).resolve(); items=reverse.get(changed,[]); print(f'CHANGED {raw}')
        if not items: print('  no OKF RESOURCE/BODY-LINK routes; no automatic knowledge edit required')
        for concept,role in sorted(items,key=lambda x:(str(x[0]),x[1])):
            found+=1; print(f'  REVIEW-CANDIDATE {role} {concept.relative_to(repo)}')
    print(f'Knowledge impact: {found} routing review candidate(s). A candidate is not automatically stale.')
    return 0
if __name__=='__main__': raise SystemExit(main())
