# Lineage

**Canonical key:** `concept.lineage`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.lineage`

**Owns current question:** Which typed directed relationships among identified entities were applicable at a relevant time, with what evidence/provenance/coverage?

**Stable IDs:** N/A

## Current semantics

Lineage owns source/target identities, typed relationship meaning, effective interval, provenance/knowledge time, evidence applicability/opportunity/coverage/corroboration/conflict/conclusion-specific sufficiency, correction/supersession, and bounded traversal completeness. Minimum operational relationship families are `data_derivation`, `production`, `operational_dependency`, `publication`, and `consumption_path`, with field/key/population/consumer/version-capable scope where evidence supports it.

## Actions

- `assertRelationship` — record a provenance-bearing relationship assertion.
- `observeRelationship` — record a relationship established/inferred from evidence with limitations.
- `supersedeRelationship` — end/revise effective relationship history.
- `correctRelationship` — preserve correction plus prior knowledge state.
- `traverseAt` — return typed authorized historical subgraph/path plus completeness/ambiguity limitations.

## Invariants / boundaries

- Generic untyped edges are insufficient for serious reasoning.
- Data derivation, production, operational dependency, publication/consumption, Deployment provenance, control, authority, and causality are not silently conflated.
- Planned/proposed topology remains Change Intent until realization evidence establishes active Lineage.
- Current topology does not rewrite historical topology.
- Lineage/reachability ≠ actual encounter/exposure ≠ Impact ≠ cause.
- Missing Lineage ≠ proof no relationship exists; a bounded negative requires adequate opportunity/coverage.
- Inferred/derived relationships retain evidence basis/limitations; no universal confidence/completeness score is accepted.
- Entity identities remain distinct across replacement/migration/derivation relationships.
- Lineage is graph-compatible semantically without requiring a graph database/query language.

## Ambiguity / evidence

Partial/stale/conflicting/restricted topology remains incomplete/unknown/conflicting/unavailable rather than falsely complete.

## Synchronizations / related canonical resources

Entity Identity supplies endpoints; Monitoring Scope does not erase cross-boundary relationships; Change Intent supplies planned topology; Deployment/Execution may provide evidence/context; Investigation uses upstream paths as evidence candidates; Impact uses downstream paths as candidates only.

## Non-goals

Root cause, confirmed Impact, execution lifecycle, deployment activation, planned-change registration, or graph-storage selection.

## Provenance

- `docs/concepts/phase_002/04_history_lineage_change/lineage.md`
- `docs/concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/`
