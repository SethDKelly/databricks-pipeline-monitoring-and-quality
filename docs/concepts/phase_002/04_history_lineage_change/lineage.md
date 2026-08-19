# Concept: Lineage

**Status:** Candidate

## Purpose

Let users trace typed upstream/downstream relationships among identified ecosystem entities, including the historical topology applicable to a relevant time.

## Operational principle

Table C is derived by joining A and B and feeds a Metric View and report. Lineage can traverse upstream to A/B and downstream to consumers using typed relationships and incident-time validity, while keeping data derivation distinct from execution dependency and deployment provenance.

## Actors

- Data Engineer
- Data Platform Administrator
- Monitoring framework
- Business Analyst / Data Steward

## State

- source/target identities;
- relationship type and direction;
- validity/effective time;
- provenance/source and evidence quality;
- confidence/ambiguity if inferred rather than directly asserted;
- supersession/correction history.

## Actions

### `assertRelationship`
Records an authoritative or explicit relationship.

### `observeRelationship`
Records a relationship inferred/observed from runtime or metadata evidence with provenance/quality.

### `supersedeRelationship`
Ends/revises validity without erasing historical topology.

### `traverseAt`
Returns typed upstream/downstream relationships applicable at a time, subject to scope/authorization.

## Invariants / behavioral expectations

- Relationship type is explicit; untyped edges are insufficient for serious RCA.
- Data lineage, execution dependency, consumption relationship, and deployment provenance are not silently conflated.
- Current topology does not overwrite historical topology.
- Lineage indicates relationship, not causal blame.
- Missing lineage is not evidence of no relationship.

## Ambiguity and missing evidence

Conflicting relationships, partial topology, inferred edges, stale metadata, and unauthorized nodes are explicit conditions. Traversal may return incomplete-with-reason rather than a falsely complete graph.

## Synchronizations

- Asset Identity supplies relationship endpoints.
- Monitored Scope determines participation without erasing known out-of-scope relationships.
- Investigation uses upstream lineage to discover evidence candidates.
- Impact uses downstream lineage to discover affected candidates.
- Change can describe topology changes.

## Security / privacy / governance considerations

Lineage can disclose sensitive architecture and asset existence even when values are hidden.

## Evidence / provenance considerations

Relationship assertions retain source, type, direction, effective time, and whether they were asserted, observed, or inferred. Traversal completeness must be explainable rather than implied.

## Representative scenarios

### Happy path
C resolves upstream derivation to A/B and downstream consumption to a Metric View/report.

### Degraded path
One cross-repository upstream relationship is missing; traversal reports incomplete topology.

### Conflicting evidence
Two sources disagree on whether a relationship was active at incident time.

### Unauthorized evidence
A restricted upstream node may be represented as redacted/opaque while preserving that the path is incomplete.

## Non-goals

- root-cause determination;
- ownership;
- execution history;
- deployment history;
- selecting a graph storage architecture.

## Open questions

- What minimal relationship type taxonomy is required for MVP?
- Which sources are sufficiently trustworthy for historical lineage?
