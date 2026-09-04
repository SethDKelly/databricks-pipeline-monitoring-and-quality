#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

ALLOWED_STATES={'legacy_authoritative','candidate_ready','canonicalized','history_only'}
REQUIRED_CANONICAL_INDEXES=(
'docs/canonical/README.md','docs/canonical/concepts/README.md','docs/canonical/contracts/README.md',
'docs/canonical/policies/README.md','docs/canonical/invariants/README.md','docs/canonical/authority/README.md',
'docs/canonical/experience/README.md','docs/canonical/architecture/README.md','docs/canonical/reference/README.md')
RANGE_RE=re.compile(r'^([A-Z]+)-(\d{3})\.\.\1-(\d{3})$')

def is_under(path:str,root:str)->bool:
    try: Path(path).relative_to(Path(root)); return True
    except ValueError: return False

def authority_marker(path:Path)->str|None:
    if not path.is_file(): return None
    text=path.read_text(encoding='utf-8',errors='ignore')
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text: return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text: return 'candidate'
    return None

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); args=ap.parse_args(); repo=Path(args.repo).resolve(); errors=[]
    inv_path=repo/'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json'
    if not inv_path.is_file(): print('ERROR missing canonical ownership inventory'); return 1
    try: inv=json.loads(inv_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc: print(f'ERROR invalid canonical ownership inventory JSON: {exc}'); return 1
    if inv.get('schema_version')!='1.0': errors.append('canonical ownership inventory schema_version must be 1.0')
    if set(inv.get('allowed_states',[]))!=ALLOWED_STATES: errors.append('canonical ownership inventory allowed_states does not match CKR migration contract')
    if inv.get('canonical_root')!='docs/canonical': errors.append('canonical_root must be docs/canonical')
    for rel in REQUIRED_CANONICAL_INDEXES:
        if not (repo/rel).is_file(): errors.append(f'missing canonical structural index: {rel}')
    for rel in ('docs/design_history/README.md','docs/canonical_knowledge_retrofit/authority_model.md','docs/canonical_knowledge_retrofit/migration_contract.md','docs/canonical_knowledge_retrofit/canonical_document_template.md'):
        if not (repo/rel).is_file(): errors.append(f'missing CKR authority artifact: {rel}')
    records=inv.get('records',[]); seen_ids=set(); seen_targets=set(); concept_records=0
    for rec in records:
        rid=rec.get('record_id'); state=rec.get('migration_state'); current=rec.get('current_owner'); target=rec.get('target_owner')
        if not rid or rid in seen_ids: errors.append(f'invalid or duplicate ownership record_id: {rid!r}'); continue
        seen_ids.add(rid)
        if state not in ALLOWED_STATES: errors.append(f'{rid}: invalid migration_state {state!r}')
        if rec.get('kind')=='concept': concept_records+=1
        if state in {'legacy_authoritative','candidate_ready','canonicalized'}:
            if not current or not (repo/current).is_file(): errors.append(f'{rid}: current_owner missing or not a file: {current!r}')
            if not target or not is_under(target,'docs/canonical'): errors.append(f'{rid}: target_owner must be under docs/canonical: {target!r}')
            elif target in seen_targets: errors.append(f'{rid}: duplicate target_owner {target}')
            else: seen_targets.add(target)
        target_path=repo/target if target else None; marker=authority_marker(target_path) if target_path else None
        if state=='legacy_authoritative' and marker=='canonical': errors.append(f'{rid}: legacy_authoritative record has target claiming canonical authority')
        elif state=='candidate_ready':
            if not target_path or not target_path.is_file(): errors.append(f'{rid}: candidate_ready target is missing')
            elif marker!='candidate': errors.append(f'{rid}: candidate_ready target must declare CANDIDATE / NOT CURRENT AUTHORITY')
        elif state=='canonicalized':
            if not target_path or not target_path.is_file(): errors.append(f'{rid}: canonicalized target is missing')
            elif marker!='canonical': errors.append(f'{rid}: canonicalized target must declare CANONICAL CURRENT AUTHORITY')
    if concept_records!=inv.get('concept_count') or concept_records!=24: errors.append(f'concept inventory must contain exactly 24 concepts; found {concept_records}')
    registry=json.loads((repo/'docs/agentic_development_foundation/stable_id_registry.json').read_text(encoding='utf-8'))
    families=inv.get('stable_families',{})
    if set(families)!=set(registry.get('families',{})): errors.append('stable_families must cover exactly the accepted stable-ID registry families')
    family_targets=set()
    for family,limits in registry.get('families',{}).items():
        item=families.get(family,{}); expected_range=f"{family}-{limits['min']:03d}..{family}-{limits['max']:03d}"
        if item.get('accepted_range')!=expected_range: errors.append(f'{family}: accepted_range must be {expected_range}')
        state=item.get('migration_state')
        if state not in ALLOWED_STATES: errors.append(f'{family}: invalid migration_state')
        current_root=item.get('current_owner_root'); target_root=item.get('target_owner_root')
        if not current_root or not (repo/current_root).exists(): errors.append(f'{family}: current_owner_root missing: {current_root!r}')
        if not target_root or not is_under(target_root,'docs/canonical'): errors.append(f'{family}: target_owner_root must be under docs/canonical')
        docs=item.get('target_documents',[])
        if state in {'candidate_ready','canonicalized'} and not docs: errors.append(f'{family}: candidate/canonical stable family requires explicit target_documents')
        expected_marker='candidate' if state=='candidate_ready' else 'canonical' if state=='canonicalized' else None
        for target in docs:
            if not is_under(target,target_root or ''): errors.append(f'{family}: target document outside target_owner_root: {target}')
            if target in seen_targets or target in family_targets: errors.append(f'{family}: duplicate target document {target}')
            family_targets.add(target)
            path=repo/target
            if not path.is_file(): errors.append(f'{family}: missing target document {target}')
            elif expected_marker and authority_marker(path)!=expected_marker: errors.append(f'{family}: {target} authority marker does not match {state}')
            elif state=='legacy_authoritative' and authority_marker(path)=='canonical': errors.append(f'{family}: legacy family target claims canonical authority: {target}')
    arch_segments=inv.get('architecture_segments',[]); covered=[]
    for segment in arch_segments:
        state=segment.get('migration_state')
        if state not in ALLOWED_STATES: errors.append(f"{segment.get('record_id')}: invalid architecture migration_state")
        current=segment.get('current_owner'); target=segment.get('target_owner')
        if not current or not (repo/current).is_file(): errors.append(f"{segment.get('record_id')}: missing architecture current_owner")
        if not target or not is_under(target,'docs/canonical/architecture'): errors.append(f"{segment.get('record_id')}: architecture target must be under docs/canonical/architecture")
        raw=segment.get('range')
        if raw:
            m=RANGE_RE.match(raw)
            if not m or m.group(1)!='ARCH': errors.append(f"{segment.get('record_id')}: invalid ARCH range {raw!r}")
            else: covered.append((int(m.group(2)),int(m.group(3))))
    if sorted(covered)!=[(1,32),(33,80),(81,132),(133,190),(191,274),(275,350),(351,420),(421,500)]: errors.append(f'architecture segment coverage must exactly partition ARCH-001..ARCH-500; found {sorted(covered)}')
    for item in inv.get('history_sources',[]):
        path=item.get('path')
        if not path or not (repo/path).exists(): errors.append(f'design-history source missing: {path!r}')
    canonical_root=repo/'docs/canonical'; structural={(repo/r).resolve() for r in REQUIRED_CANONICAL_INDEXES}
    # Any nested README is structural only when it contains no authority marker.
    for p in canonical_root.rglob('README.md'):
        if authority_marker(p) is None: structural.add(p.resolve())
    declared={(repo/p).resolve() for p in seen_targets|family_targets}
    declared.update((repo/s.get('target_owner')).resolve() for s in arch_segments if s.get('target_owner'))
    for path in canonical_root.rglob('*.md'):
        r=path.resolve()
        if r in structural: continue
        if r not in declared: errors.append(f'unregistered substantive canonical document: {path.relative_to(repo)}')
    for e in errors: print('ERROR',e)
    canonicalized=sum(1 for r in records if r.get('migration_state')=='canonicalized'); candidates=sum(1 for r in records if r.get('migration_state')=='candidate_ready')
    fam_can=sum(1 for f in families.values() if f.get('migration_state')=='canonicalized'); fam_cand=sum(1 for f in families.values() if f.get('migration_state')=='candidate_ready')
    print(f'Canonical knowledge validation: {len(errors)} error(s), {len(records)} ownership record(s), {concept_records} concept(s), {canonicalized} canonicalized, {candidates} candidate(s), stable families canonicalized={fam_can}, candidate={fam_cand}')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
