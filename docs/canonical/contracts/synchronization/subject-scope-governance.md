# Subject, Scope & Governance Synchronizations

**Canonical key:** `contract.synchronization.subject_scope_governance`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.SYN`

**Owns current question:** How do identity, monitoring scope, and governance-context concepts coordinate without merging their truth or using synchronization order as authority?

**Stable IDs:** SYN-001–SYN-003

## Current semantics

Synchronization coordinates information exchange/order and preserves each concept's independent state/actions/authority. It is not an umbrella concept, workflow engine, transaction, event bus, storage relationship, or source-precedence mechanism. Unknown/conflicting/unauthorized/unavailable results remain first-class and may validly stop subject-specific coordination.

### SYN-001 — Entity Identity + Monitoring Scope Resolution
Resolve source reference to Entity Identity before attaching subject-specific scope. Then resolve Monitoring Scope independently as included/excluded/unknown/conflicting/restricted. Identity does not create scope; scope does not create identity or authorization. Known out-of-scope entities may remain contextual boundaries.

### SYN-002 — Identified Subject + Governance Context Resolution
For an identified subject/time/context, resolve Semantic Definition, Responsibility Assignment, Classification, and Policy Context independently. Missing/conflicting state in one dimension does not erase or poison another. Synchronization order, recency, and source availability never determine authority.

### SYN-003 — Classification as Policy-Context Evidence
Classification may be provenance-bearing evidence relevant to Policy Context applicability but cannot manufacture a policy/applicability assertion, access decision, enforcement fact, or compliance conclusion.

## Invariants / boundaries

- Concept state remains owned by its concept.
- Identity resolution precedes subject-specific joins; ambiguous identity is not guessed.
- Monitoring responsibility ≠ ecosystem existence ≠ authorization.
- Governance dimensions are independently motivated; no last-write-wins metadata blob.
- Synchronization order is never Assertion Authority.
- Authorization constrains disclosure/projection; it does not change concept truth.

## Provenance

- `docs/concepts/phase_003/01_subject_scope_and_context/`
- `docs/concepts/phase_003/README.md`
