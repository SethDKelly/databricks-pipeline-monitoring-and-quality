# Group 01 — Subject, Scope & Governance Context

**Status:** Review complete — synchronizations accepted

## Goal

Define how a source-specific subject reference becomes a safely reasoned-about ecosystem subject: resolve Entity Identity first, resolve Monitoring Scope independently, then resolve semantic/responsibility/classification/policy context without guessing, inheriting authority, or widening access.

## Accepted synchronizations

- [`SYN-001 — Entity Identity + Monitoring Scope Resolution`](001_entity_identity_and_scope_resolution.md)
- [`SYN-002 — Identified Subject + Governance Context Resolution`](002_governance_context_resolution.md)
- [`SYN-003 — Classification as Policy-Context Evidence`](003_classification_policy_context_evidence.md)

## Boundary decisions

### 1. Identity resolution precedes subject-specific synchronization

A downstream chain cannot attach scope, governance, health, change, lineage, or investigation state to a guessed entity. If identity is unresolved, subject-specific coordination remains unresolved rather than choosing a convenient candidate.

### 2. Monitoring Scope resolves independently from ecosystem existence

A known entity may be included, excluded, unknown, conflicting, or restricted. Scope does not create identity and does not grant authorization. An excluded/out-of-scope entity can remain a known contextual boundary when authorized.

### 3. Governance dimensions resolve independently

Semantic Definition, Responsibility Assignment, Classification, and Policy Context attach to the same Entity Identity/time/context but do not form a single last-write-wins metadata record. Missing or conflicting state in one dimension does not erase valid state in another.

### 4. Synchronization order is never authority

Resolving Collibra-like metadata before or after another source cannot determine authority. Conflicts remain conflicts until explicit authority semantics are accepted later.

### 5. Classification may support Policy Context but cannot manufacture it

A PHI/PII/etc. Classification may be evidence relevant to policy applicability. It does not automatically create a Policy Context assertion, grant access, or establish compliance.

### 6. Authorization constrains disclosure, not concept truth

Phase 003 does not introduce an Authorization concept. The existing product-security model acts as a cross-cutting constraint: a synchronization may preserve an opaque/restricted result internally or expose only an allowed abstraction. It must never retrieve or reveal restricted detail merely because another concept needs context.

## Scenario review

### A+B→C with out-of-scope A
Pass. C/B identify normally and may be in scope. A can resolve as a known Entity Identity but excluded from Monitoring Scope. Later reasoning can report an upstream monitoring boundary without pretending A is nonexistent or fully monitored.

### Cross-repository dependency
Pass. Repository identity/provenance does not change logical Entity Identity or cause scope/governance inheritance.

### Conflicting responsibility/classification
Pass. Responsibility and Classification conflicts remain category-specific; one does not poison or overwrite the other.

### Policy-sensitive subject
Pass. A viewer may be told that special/restricted handling context exists while sensitive classification/policy details remain hidden.

### Ambiguous identity
Pass. Similar table names in prod/dev do not receive combined scope/governance state; the chain stops at identity ambiguity for the unresolved reference.

### Historical replay
Pass. Identity-reference validity, scope effective time, and governance effective-time/provenance resolve for the incident time rather than projecting current metadata backward.

## Group exit gate

**Satisfied.** A subject can be resolved into identity, monitoring responsibility, and independent governance context without conflating existence, scope, authorization, authority, or policy consequence.

The next group is **Group 02 — Planned Change & Reference Transition**.
