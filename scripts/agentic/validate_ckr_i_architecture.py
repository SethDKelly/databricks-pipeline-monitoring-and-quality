#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ARCH_DOCS = (
    ('architecture.frame_environment_decision_criteria', 1, 32, 'docs/canonical/architecture/frame-environment-decision-criteria.md'),
    ('architecture.evidence_provenance_temporal_persistence', 33, 80, 'docs/canonical/architecture/evidence-provenance-temporal-persistence.md'),
    ('architecture.identity_scope_authority_authorization_disclosure', 81, 132, 'docs/canonical/architecture/identity-scope-authority-authorization-disclosure.md'),
    ('architecture.source_acquisition_adapter_integration_health', 133, 190, 'docs/canonical/architecture/source-acquisition-adapter-integration-health.md'),
    ('architecture.runtime_health_lineage_impact', 191, 274, 'docs/canonical/architecture/runtime-provenance-health-lineage-impact.md'),
    ('architecture.investigation_reasoning_replay_explanation', 275, 350, 'docs/canonical/architecture/investigation-reasoning-replay-explanation.md'),
    ('architecture.active_control', 351, 420, 'docs/canonical/architecture/active-control.md'),
    ('architecture.serving_security_deployment_operations', 421, 500, 'docs/canonical/architecture/serving-security-deployment-operations.md'),
)
REFERENCE = ('architecture.reference_architecture', 'docs/canonical/architecture/reference-architecture.md')
ARCH_TARGETS = tuple(item[3] for item in ARCH_DOCS)
STATE_RE = re.compile(r'^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$', re.M)
ARCH_ID_RE = re.compile(r'\bARCH-(\d{3})\b')
ATOMIC_RE = re.compile(r'^(\d{3})_.+\.md$')


def marker(text: str) -> str | None:
    if '**Authority:** CANONICAL CURRENT AUTHORITY' in text:
        return 'canonical'
    if '**Authority:** CANDIDATE / NOT CURRENT AUTHORITY' in text:
        return 'candidate'
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    inv = json.loads((repo / 'docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json').read_text(encoding='utf-8'))
    arch = inv['stable_families']['ARCH']
    state = arch.get('migration_state')
    if state not in {'candidate_ready', 'canonicalized'}:
        errors.append(f'ARCH must be candidate_ready/canonicalized during/after CKR-I, found {state!r}')
    expected_marker = 'candidate' if state == 'candidate_ready' else 'canonical'
    if arch.get('migration_group') != 'CKR-I':
        errors.append('ARCH migration_group must remain CKR-I')
    if arch.get('accepted_range') != 'ARCH-001..ARCH-500':
        errors.append('ARCH accepted range must remain ARCH-001..ARCH-500')
    if arch.get('target_documents') != list(ARCH_TARGETS):
        errors.append('ARCH target_documents do not match CKR-I eight-segment topology')

    segments = {s.get('record_id'): s for s in inv.get('architecture_segments', [])}
    expected_segment_ids = {x[0] for x in ARCH_DOCS} | {REFERENCE[0]}
    if set(segments) != expected_segment_ids:
        errors.append(f'architecture segment inventory must contain exact CKR-I records; found {sorted(segments)}')

    all_canonical_ids: set[int] = set()
    for record_id, lo, hi, rel in ARCH_DOCS:
        seg = segments.get(record_id, {})
        expected_range = f'ARCH-{lo:03d}..ARCH-{hi:03d}'
        if seg.get('range') != expected_range:
            errors.append(f'{record_id}: range must remain {expected_range}')
        if seg.get('target_owner') != rel:
            errors.append(f'{record_id}: target owner drifted from {rel}')
        if seg.get('migration_state') != state:
            errors.append(f'{record_id}: migration state {seg.get("migration_state")!r} must move atomically with ARCH={state!r}')
        path = repo / rel
        if not path.is_file():
            errors.append(f'missing ARCH canonical target {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        if marker(text) != expected_marker:
            errors.append(f'{rel}: authority marker does not match {state}')
        if '**Migration records:** `stable_family.ARCH`' not in text:
            errors.append(f'{rel}: missing stable-family migration record')
        if 'docs/concepts/phase_010/' not in text:
            errors.append(f'{rel}: missing Phase 010 provenance')
        if f'**Stable IDs:** ARCH-{lo:03d}–ARCH-{hi:03d}' not in text:
            errors.append(f'{rel}: missing exact stable range declaration')
        ids = {int(x) for x in ARCH_ID_RE.findall(text) if 1 <= int(x) <= 500}
        missing = set(range(lo, hi + 1)) - ids
        outside = ids - set(range(lo, hi + 1))
        if missing:
            errors.append(f'{rel}: missing addressable ARCH IDs {sorted(missing)[:8]}{"..." if len(missing) > 8 else ""}')
        if outside:
            errors.append(f'{rel}: contains out-of-segment ARCH IDs {sorted(outside)[:8]}{"..." if len(outside) > 8 else ""}')
        all_canonical_ids.update(ids)

    ref_id, ref_rel = REFERENCE
    ref_seg = segments.get(ref_id, {})
    if ref_seg.get('range') is not None:
        errors.append('reference architecture must remain outside the ARCH stable-ID partition')
    if ref_seg.get('target_owner') != ref_rel:
        errors.append('reference architecture target owner drifted')
    if ref_seg.get('migration_state') != state:
        errors.append('reference architecture must migrate atomically with ARCH')
    ref_path = repo / ref_rel
    if not ref_path.is_file():
        errors.append('missing canonical reference architecture')
    else:
        ref_text = ref_path.read_text(encoding='utf-8')
        if marker(ref_text) != expected_marker:
            errors.append(f'{ref_rel}: authority marker does not match {state}')
        if '**Migration record:** `architecture.reference_architecture`' not in ref_text:
            errors.append('reference architecture missing migration record')
        if 'docs/concepts/phase_010/' not in ref_text:
            errors.append('reference architecture missing Phase 010 provenance')
        if 'composes ARCH-001–ARCH-500' not in ref_text or 'No ARCH-501 is required' not in ref_text:
            errors.append('reference architecture must compose ARCH-001–500 without creating ARCH-501')
        if re.search(r'\bARCH-501\b', ref_text.replace('No ARCH-501 is required', '')):
            errors.append('reference architecture contains unaccepted ARCH-501 outside explicit rejection statement')

    if all_canonical_ids != set(range(1, 501)):
        errors.append(f'canonical ARCH corpus must address ARCH-001..ARCH-500; found {len(all_canonical_ids)} unique IDs')

    # Provenance conservation: all 500 accepted atomic Phase 010 ARCH source files must remain present exactly once.
    atomic: dict[int, list[str]] = {}
    phase10 = repo / 'docs/concepts/phase_010'
    for p in phase10.rglob('*.md'):
        m = ATOMIC_RE.match(p.name)
        if not m:
            continue
        n = int(m.group(1))
        if 1 <= n <= 500:
            text = p.read_text(encoding='utf-8', errors='ignore')
            if re.search(rf'^# ARCH-{n:03d} —', text, re.M):
                atomic.setdefault(n, []).append(str(p.relative_to(repo)))
    if set(atomic) != set(range(1, 501)):
        missing = sorted(set(range(1, 501)) - set(atomic))
        errors.append(f'Phase 010 provenance must retain all 500 atomic ARCH files; missing {missing[:8]}{"..." if len(missing) > 8 else ""}')
    dupes = {k: v for k, v in atomic.items() if len(v) != 1}
    if dupes:
        errors.append(f'Phase 010 atomic ARCH provenance must be unique; duplicate IDs {sorted(dupes)[:8]}')

    matrix = repo / 'docs/canonical_knowledge_retrofit/ckr_i_semantic_conservation_matrix.md'
    if not matrix.is_file():
        errors.append('missing CKR-I semantic conservation matrix')
    else:
        mt = matrix.read_text(encoding='utf-8')
        required = (
            'documented capability ≠ deployment presence ≠ entitlement ≠ enablement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability',
            'framework retention authority ≠ source Assertion Authority',
            'copied evidence ≠ newly authoritative evidence ≠ independent corroboration',
            'current state/config/policy ≠ historical state; Delta transaction-log time travel ≠ DMTZ historical replay contract',
            'source-local identifier/name ≠ ecosystem Entity Identity',
            'authentication ≠ Capability Authorization ≠ Assertion Authority',
            'Monitoring Scope ≠ technical accessibility ≠ authorization ≠ successful observation',
            'authorization decision ≠ issuance ≠ enforcement ≠ action ≠ outcome',
            'source acquisition transports evidence; integration success/failure ≠ monitored-domain truth',
            'empty result ≠ absence; partial pagination/window/partition ≠ complete coverage',
            'GitHub Actions success ≠ Databricks activation; deployment ≠ activation ≠ run',
            'dependency/Lineage/write history ≠ exact consumed/produced version',
            'execution success ≠ output existence ≠ freshness/currentness ≠ health',
            'Baseline ≠ Expectation ≠ Observation ≠ Assessment',
            'Lineage/reachability ≠ encounter/consumption ≠ exposure',
            'exposure ≠ effect ≠ consequence ≠ causal attribution',
            'Investigation lead/localization ≠ Causal Claim',
            '`confirmed` requires REF-017 evidence + AUTH-034 eligible authority',
            'graph/search/vector projection ≠ source truth/authority/completeness/causality',
            'LLM/model output/confidence/agreement ≠ evidence strength, authority or independent corroboration',
            'historical source state ≠ as-known-at-K Explanation ≠ retained actual communication ≠ current retrospective Explanation',
            'evidence suitability ≠ readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution',
            'Safeguard active + not exposed ≠ REF-028 prevention without opportunity/path/alternate-path evidence',
            'Execution Gate ≠ Propagation Safeguard',
            'cache/page/index/derived read model ≠ canonical completeness/freshness/authority',
            'SLO breach ≠ monitored-domain health',
            'cost/quota/capacity pressure ≠ permission to weaken scope/evidence/retention/control promises',
            'ARCH-001–ARCH-500 final; no ARCH-501',
            'reference architecture composes ARCH-001–500; it does not create another truth layer',
        )
        for phrase in required:
            if phrase not in mt:
                errors.append(f'CKR-I matrix missing boundary: {phrase}')

    for fam in ('SYN', 'REF', 'AUTH', 'HLTH', 'OPS', 'EXPL', 'INTG'):
        if inv['stable_families'][fam]['migration_state'] != 'canonicalized':
            errors.append(f'{fam} must remain canonicalized during/after CKR-I')
    vocab = next(r for r in inv['records'] if r['record_id'] == 'reference.authority_vocabulary')
    if vocab['migration_state'] != 'canonicalized':
        errors.append('authority vocabulary must remain canonicalized during/after CKR-I')
    concepts = [r for r in inv['records'] if r.get('kind') == 'concept']
    if len(concepts) != 24 or any(r['migration_state'] != 'canonicalized' for r in concepts):
        errors.append('all 24 concepts must remain canonicalized during/after CKR-I')

    phase10_history = next((x for x in inv.get('history_sources', []) if x.get('path') == 'docs/concepts/phase_010'), None)
    if state == 'candidate_ready':
        if not phase10_history or phase10_history.get('classification_during_migration') != 'mixed_legacy_authority_and_design_history':
            errors.append('Phase 010 must remain mixed legacy authority/design history while ARCH is candidate_ready')
    elif state == 'canonicalized':
        if not phase10_history or phase10_history.get('classification_during_migration') != 'design_history_and_provenance_for_canonicalized_ARCH':
            errors.append('Phase 010 must become design history/provenance after ARCH cutover')

    states = {k: v for k, v in STATE_RE.findall((repo / 'docs/canonical_knowledge_retrofit/README.md').read_text(encoding='utf-8'))}
    if states.get('I') not in {'IN EXECUTION', 'COMPLETE / ACCEPTED'}:
        errors.append(f'CKR-I must be in execution or complete while ARCH has moved, found {states.get("I")!r}')

    fixture = repo / 'docs/canonical_knowledge_retrofit/fixtures/ckr_i_architecture_scenarios.yaml'
    if not fixture.is_file():
        errors.append('missing CKR-I fixture catalog')
    else:
        count = len(re.findall(r'^\s*- id: CKRI-\d{2}$', fixture.read_text(encoding='utf-8'), re.M))
        if count < 80:
            errors.append(f'CKR-I fixture catalog too small; found {count}')

    for error in errors:
        print('ERROR', error)
    print(f'CKR-I architecture validation: {len(errors)} error(s), ARCH={len(all_canonical_ids)}/500, atomic={len(atomic)}/500, segments={len(segments)}/9, state={state}')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
