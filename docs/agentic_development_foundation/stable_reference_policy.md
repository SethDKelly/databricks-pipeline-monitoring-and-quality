# DMTZ Stable Reference Policy

**Status:** ACCEPTED — ADF-E

## Purpose

Use accepted stable IDs as precise semantic lookup keys without mistaking arbitrary text occurrences for canonical ownership.

## Frozen accepted families

The current accepted contract ranges are recorded machine-readably in `stable_id_registry.json`:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

An ID outside these ranges is not silently treated as accepted merely because text resembling it exists.

## Exact-ID resolution

For an exact ID:

1. validate family, width, and accepted range;
2. search the exact token in canonical `docs/`;
3. return every exact occurrence with file and line context;
4. classify definition-like occurrences separately from ordinary references when mechanically possible;
5. use live phase/program authority and the accepted owning document to determine canonical meaning;
6. read the smallest surrounding section required to apply the contract.

`scripts/agentic/resolve_stable_id.py` implements steps 1–4 deterministically. It deliberately does **not** select the first match as canonical.

## Definition candidate is not canonicality

A heading or line beginning with an ID can be marked a `definition_candidate` by the helper. That label is only a retrieval aid.

Canonicality still depends on accepted repository authority. Indexes, validation matrices, implementation handoffs, examples, and historical documents may quote the same ID.

## Semantic questions without an ID

When the user/task provides only a bounded semantic question:

1. route through `knowledge/index.md` to the smallest relevant domain resource;
2. identify the governing stable IDs in canonical docs;
3. resolve those IDs exactly;
4. do not invent a new stable ID or collapse multiple independently motivated contracts.

## Stable ID versus implementation evidence

Implementation/scenario/test identifiers may reference accepted contracts, but do not replace them. Traceability should retain both identities where they serve different purposes.

## Broken or ambiguous resolution

- no exact occurrence: report unresolved/missing; do not infer from memory;
- multiple occurrences: present candidates and verify against live authority;
- conflicting accepted sources: escalate through change control;
- historical/deprecated occurrence only: do not treat it as current without live authority;
- range-invalid token: report invalid/unaccepted rather than searching for a convenient substitute.

## Generated indexes

A generated occurrence index may accelerate lookup, but it remains derived and rebuildable. It cannot become the only copy of contract semantics or an independent canonical registry.
