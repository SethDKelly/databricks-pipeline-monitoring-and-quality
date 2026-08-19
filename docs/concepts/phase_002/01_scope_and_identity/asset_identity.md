# Concept: Asset Identity

**Status:** Candidate

## Purpose

Let the ecosystem recognize the same logical entity across sources, names, observations, environments, and time without assuming any single external identifier is universal.

## Operational principle

A table is referenced by Databricks metadata, pipeline configuration, lineage evidence, and governance metadata. The names differ slightly and one source later reflects a rename. Asset Identity preserves the known source references, recognizes the logical continuity where justified, and preserves uncertainty when equivalence is not established.

## Actors

- Monitoring framework
- Data Engineer
- Data Platform Administrator
- Governance / Data Steward
- Integration sources

## State

- logical identity;
- entity kind or identity class when known;
- source-specific references/aliases;
- association evidence and provenance;
- validity/effective-time context for references;
- explicit equivalence, separation, replacement, or unresolved identity claims.

## Actions

### `recognize`
- **Intent:** resolve a source reference to a logical identity when sufficient evidence exists.
- **Observable result:** identified, ambiguous, unknown, or conflicting.

### `associateReference`
- **Intent:** assert that an external reference denotes an existing logical identity.
- **State effect:** adds a provenance-bearing association; does not erase prior references.

### `separate`
- **Intent:** correct an earlier conflation when two references are determined to represent distinct entities.
- **State effect:** preserves historical correction context rather than rewriting history invisibly.

### `relateReplacement`
- **Intent:** state that one entity replaced/superseded another without claiming they are identical.

## Invariants / behavioral expectations

- Human-readable name equality is insufficient proof of identity.
- Renaming does not automatically create a new logical identity.
- Replacement/succession is not the same as identity.
- Environment-specific instances may be related without being collapsed unless the product explicitly defines that equivalence.
- Identity correction preserves provenance and historical interpretability.
- Identity does not own semantics, ownership, quality, or lineage behavior.

## Ambiguity and missing evidence

When source references cannot be safely unified, the concept returns ambiguous/unresolved identity rather than guessing. Conflicting mappings remain visible. Unauthorized source references may be represented only at an allowed abstraction level.

## Synchronizations

Most later concepts synchronize through Asset Identity to refer to their subjects, including Semantic Definition, Ownership, Classification, Expectation, Observation, Execution History, Lineage, Change, Investigation, and Impact.

## Security / privacy / governance considerations

Cross-source identity resolution can reveal relationships among sensitive assets. Identity visibility must be authorization-aware even when no raw data is exposed.

## Evidence / provenance considerations

Equivalence and separation claims should retain why they were made and from which source/actor. Historical identity mapping must support incident-time replay.

## Representative scenarios

### Happy path
A table rename is recognized as continuity, so historical observations remain connected to the same logical asset.

### Degraded path
A repository declaration and Databricks metadata use different identifiers; equivalence remains unresolved, limiting automated RCA.

### Conflicting evidence
Two governance systems map the same external identifier to different logical assets. The conflict is preserved.

### Unauthorized evidence
A user can see an opaque upstream identity exists for reasoning purposes without learning restricted identifying metadata.

## Non-goals

- deciding whether an entity is in monitoring scope;
- defining business meaning;
- defining ownership;
- granting access;
- implementing a universal identifier format.

## Open questions

- Which domain entities need logical identity in MVP beyond data assets and pipelines?
- How should logical pipeline identity relate to Databricks job/task identities?
- Which identity associations can be inferred versus requiring explicit assertion?
