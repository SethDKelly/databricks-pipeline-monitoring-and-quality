# DMTZ Stable Reference Policy

**Status:** ACCEPTED — ADF-E / REFINED CKR-J

## Purpose

Use accepted stable IDs as deterministic current-semantic lookup keys while keeping routing identity separate from contract meaning and historical provenance.

## Frozen accepted families

The machine-readable ranges remain in `stable_id_registry.json`:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

The accepted total is **1,237 IDs**. A range-invalid token is invalid/unaccepted even if similar text exists elsewhere.

## Deterministic current resolution

For an exact ID:

1. validate family, three-digit width and accepted range;
2. read the CKR ownership inventory for that family;
3. require the family to be `canonicalized`;
4. inspect only the inventoried canonical `target_documents`;
5. require exactly one accepted canonical stable definition;
6. return the stable locator `owner_path::STABLE-ID`;
7. read the smallest surrounding canonical owner context needed to apply the rule.

`scripts/agentic/resolve_stable_id.py <ID>` performs this current-owner resolution. The returned line is navigation metadata; the stable locator is the owner path plus stable-ID token.

## Accepted canonical definition forms

CKR-J preserves the canonical topology already accepted by CKR-B–I:

- `definition_heading` — 737 SYN/REF/AUTH/HLTH/OPS/EXPL/INTG definitions;
- `stable_id_index_member` — 416 ARCH IDs in compact CKR-I segment indexes;
- `stable_contract_list_member` — 84 ARCH IDs in the runtime/health/Lineage/Impact segment's named stable-contract lists.

These are routing/addressability forms, not different semantic strengths. CKR-J does not manufacture 500 ARCH headings or restore the Phase 010 one-file-per-ID topology.

## Historical occurrence discovery

Historical/provenance occurrences are intentionally separate:

```bash
python3 scripts/agentic/resolve_stable_id.py <ID> --history
```

The canonical owner is resolved first. Historical results are then returned as `history_provenance` only and cannot compete with, supersede or weaken the current owner.

## What is not stable identity

The following may help navigation but cannot establish semantic ownership:

- repository search rank or first textual occurrence;
- line number;
- generated Markdown-renderer slug;
- file recency or Git history position;
- OKF lifecycle state;
- model/tool memory;
- a derived index or cache.

## Semantic questions without an ID

When no exact ID is known, route through the smallest relevant OKF domain concept, follow its canonical resource/body links, identify the governing stable IDs, then resolve those IDs exactly. Do not traverse OKF when the canonical path/ID is already known.

## Stable ID versus implementation evidence

A stable locator proves where the current accepted contract is routed; it does **not** prove that product behavior implements the contract. Traceability must retain contract identity/location and executable/static/runtime evidence separately.

## Failure behavior

- no canonical stable definition: fail/report; do not infer from history or memory;
- multiple canonical stable definitions: fail/report ownership drift; do not choose first match;
- non-canonicalized family: resolve through live CKR authority rather than pretending CKR-J applies;
- range-invalid token: report invalid/unaccepted;
- history-only match: provenance only, never current truth.

## Derived routing machinery

The registry, resolver, OKF bundle and any generated reverse index are rebuildable routing aids. None owns contract prose, creates Assertion Authority, or changes accepted meaning.
