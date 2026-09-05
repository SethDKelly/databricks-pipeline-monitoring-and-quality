#!/usr/bin/env python3
"""Resolve an accepted DMTZ stable ID to its deterministic canonical owner.

Default resolution is current/canonical only. Use --history explicitly to inspect
historical/provenance occurrences; history never participates in canonical owner selection.
"""
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
ID_RE=re.compile(r'^(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})$')
TOKEN_RE=re.compile(r'\b(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})\b')
HEADING_RE=re.compile(r'^#{2,6}\s+((?:SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-\d{3})(?:\s|—|-|:|$)')
INDEX_PREFIX='**Stable ID index:**'
RESOLUTION_MODE='canonical_target_stable_definition'

def load_json(path:Path)->dict: return json.loads(path.read_text(encoding='utf-8'))
def load_registry(repo:Path)->dict: return load_json(repo/'docs/agentic_development_foundation/stable_id_registry.json')
def load_inventory(repo:Path,registry:dict)->dict: return load_json(repo/registry['ownership_inventory'])

def canonical_hits(repo:Path,token:str,family:str,limits:dict,owner:dict)->list[dict]:
    hits=[]; low,high=int(limits['min']),int(limits['max'])
    for rel in owner.get('target_documents',[]):
        path=repo/rel
        if not path.is_file(): continue
        for line_no,raw in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
            line=raw.strip(); heading=HEADING_RE.match(line)
            if heading and heading.group(1)==token:
                hits.append({'path':rel,'line':line_no,'definition_form':'definition_heading','text':line})
            if family=='ARCH' and line.startswith(INDEX_PREFIX):
                indexed={f'{fam}-{num}' for fam,num in TOKEN_RE.findall(line)}
                if token in indexed: hits.append({'path':rel,'line':line_no,'definition_form':'stable_id_index_member','text':line})
            if family=='ARCH' and line.startswith('`ARCH-'):
                listed={f'{fam}-{num}' for fam,num in TOKEN_RE.findall(line)}
                if token in listed: hits.append({'path':rel,'line':line_no,'definition_form':'stable_contract_list_member','text':line})
    return hits

def history_hits(repo:Path,token:str)->list[dict]:
    pattern=re.compile(rf'(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])')
    excluded=('docs/canonical/','docs/implementation/','docs/agentic_development_foundation/','docs/canonical_knowledge_retrofit/')
    results=[]
    for path in sorted((repo/'docs').rglob('*.md')):
        rel=path.relative_to(repo).as_posix()
        if rel.startswith(excluded): continue
        try: lines=path.read_text(encoding='utf-8').splitlines()
        except UnicodeDecodeError: continue
        for line_no,line in enumerate(lines,1):
            if pattern.search(line): results.append({'path':rel,'line':line_no,'text':line.strip(),'role':'history_provenance'})
    return results

def main()->int:
    ap=argparse.ArgumentParser(description='Resolve a DMTZ stable ID to its canonical owner locator.')
    ap.add_argument('stable_id'); ap.add_argument('--repo',default='.'); ap.add_argument('--history',action='store_true',help='also return separate historical/provenance occurrences'); ap.add_argument('--json',action='store_true')
    a=ap.parse_args(); repo=Path(a.repo).resolve(); token=a.stable_id.strip().upper(); match=ID_RE.match(token)
    if not match:
        print(f'ERROR invalid stable ID format: {a.stable_id}',file=sys.stderr); return 2
    registry=load_registry(repo); family,num_text=match.groups(); number=int(num_text); limits=registry.get('families',{}).get(family)
    if not limits or number<int(limits['min']) or number>int(limits['max']):
        accepted=f"{family}-{int(limits['min']):03d}..{family}-{int(limits['max']):03d}" if limits else 'no accepted range'
        print(f'ERROR {token} is outside {accepted}',file=sys.stderr); return 2
    inventory=load_inventory(repo,registry); owner=inventory.get('stable_families',{}).get(family,{})
    if owner.get('migration_state')!='canonicalized':
        print(f'ERROR {family} is not canonicalized; current owner cannot be resolved by CKR-J',file=sys.stderr); return 3
    hits=canonical_hits(repo,token,family,limits,owner)
    if len(hits)!=1:
        print(f'ERROR {token} expected exactly one canonical stable definition; found {len(hits)}',file=sys.stderr); return 3
    hit=hits[0]; canonical_locator=f"{hit['path']}::{token}"
    payload={'stable_id':token,'family':family,'accepted_range':f"{family}-{int(limits['min']):03d}..{family}-{int(limits['max']):03d}",'resolution_mode':RESOLUTION_MODE,'canonical_owner':hit,'canonical_locator':canonical_locator,'canonicality_note':'Routing result derived from the accepted range registry + CKR ownership inventory + unique canonical stable definition. The resolver does not own or reinterpret semantic meaning.'}
    if a.history: payload['history_occurrences']=history_hits(repo,token)
    if a.json: print(json.dumps(payload,indent=2))
    else:
        print(f'{token} -> {canonical_locator}')
        print(f"definition_form={hit['definition_form']} line={hit['line']}")
        print(hit['text'])
        if a.history:
            history=payload.get('history_occurrences',[]); print(f'history occurrences: {len(history)}')
            for item in history: print(f"history_provenance {item['path']}:{item['line']}  {item['text']}")
        print(payload['canonicality_note'])
    return 0
if __name__=='__main__': raise SystemExit(main())
