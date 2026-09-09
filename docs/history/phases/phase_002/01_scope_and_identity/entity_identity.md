# Concept: Entity Identity

**Status:** Accepted — Phase 002 Group 01

## Purpose

Let the ecosystem determine when source-specific references denote the same logical entity across systems and time, while preserving ambiguity, separation, and correction when equivalence is not justified.

## Operational principle

A production table is referenced by Databricks metadata, a Spark pipeline declaration, lineage evidence, and governance metadata. The source-specific names and identifiers differ, and the table is later renamed. Entity Identity associates the justified references with one logical entity so historical observations remain connected. A similarly named development table is kept separate. If a later correction shows that two previously associated references were actually different entities, the correction is preserved without rewriting the original source evidence.

## Actors

- Monitoring framework
- Data Engineer
- Data Platform Administrator
- Governance / Data Steward
- Integration sources

## State

- logical entity identities;
- entity kind or identity class when known;
- source-specific references, qualified by source/system and relevant namespace/environment context;
- validity/effective-time context for references when known;
- equivalence and separation claims;
- supporting evidence, provenance, actor/source, and assertion time for identity claims;
- correction/supersession history;
- unresolved or conflicting identity claims.

Replacement, split, merge, derivation, and succession relationships are deliberately not owned as identity equivalence state.

## Actions

### `establish`
- **Intent:** create a logical identity for a reference that is sufficiently established as a distinct entity.
- **State effect:** records the logical identity and initial provenance-bearing reference.
- **Failure / unknown behavior:** when the reference may denote an existing entity and evidence is insufficient, establishment remains unresolved rather than manufacturing duplication.

### `recognize`
- **Intent:** resolve a source-specific reference at a relevant time to a logical entity.
- **Observable result:** identified, ambiguous, unknown, conflicting, unauthorized, or unavailable.

### `associateReference`
- **Intent:** assert that an additional source-specific reference denotes an existing logical entity.
- **State effect:** records a provenance-bearing equivalence association and preserves prior references.
- **Failure / unknown behavior:** incompatible entity kind, environment/context mismatch, or insufficient evidence prevents automatic association.

### `separate`
- **Intent:** correct an earlier conflation or explicitly assert that references denote distinct entities.
- **State effect:** records separation/correction without deleting the original source facts or silently rewriting history.

### `endReference`
- **Intent:** state that a source-specific reference is no longer valid for the entity after a relevant time, for example after a rename.
- **State effect:** closes the reference's validity without retiring or changing the logical entity itself.

## Invariants / behavioral expectations

- A human-readable name is never sufficient proof of identity by itself.
- An external reference is understood in source/system plus namespace/environment/time context; the identifier string alone is not universal identity.
- No single vendor identifier is assumed to be universal across the ecosystem.
- Entity-kind incompatibility blocks automatic equivalence unless the kind itself is unresolved and later clarified.
- A rename may preserve logical identity when evidence supports continuity.
- Delete-and-recreate under the same name is not automatically the same identity.
- Production, test, development, and other environment-specific instances remain distinct by default even if names/configuration are similar.
- Split, merge, replacement, migration, and succession do not imply identity. They produce or preserve distinct identities whose relationships belong in **Change** and/or **Lineage**.
- Identity correction does not mutate the source observations, deployments, or lineage facts that originally carried a source-specific reference.
- Historical resolution must preserve the ability to explain which references were valid and which identity claims were known/effective at the relevant time.
- Entity Identity does not own semantics, ownership, monitoring scope, health, lineage, or authorization behavior.

## Ambiguity and missing evidence

When a reference cannot be safely unified with an existing identity, `recognize` returns ambiguous, unknown, or conflicting rather than guessing. Conflicting mappings remain visible. Restricted identifying metadata may be represented as an opaque entity reference when authorization permits reasoning but not disclosure.

A stable provider identifier is strong evidence within that provider's documented scope, but it does not by itself prove equivalence to identifiers from another source.

## Synchronizations

- **Monitoring Scope** attaches monitoring participation to an Entity Identity.
- **Semantic Definition**, **Ownership**, **Classification**, **Policy Context**, **Expectation**, **Observation**, **Execution History**, **Deployment**, **Lineage**, **Change**, **Investigation**, and **Impact** use Entity Identity to identify their subjects without owning identity resolution.
- **Change** and **Lineage** represent replacement, split, merge, migration, derivation, and other relationships among distinct identities.
- External integrations can initiate `establish`, `associateReference`, or `separate` without the identity concept becoming vendor-specific.

## Security / privacy / governance considerations

Cross-source identity resolution can reveal that restricted assets, pipelines, repositories, or consumers are related. Identity visibility must respect authorization even when no raw data is exposed.

Opaque identity may be sufficient for some reasoning paths. The concept should support "a restricted entity exists here" without requiring disclosure of its sensitive name or source references.

## Evidence / provenance considerations

Equivalence and separation are claims and should retain why they were made, by whom/what, and with what source evidence. Effective time and assertion/correction time should remain distinguishable where historical reconstruction requires it.

Identity resolution should be auditable enough to explain why two references were considered the same entity or why the system refused to unify them.

## Representative scenarios

### Rename continuity
A production table is renamed while retaining sufficient provider/deployment continuity. The new reference is associated with the existing Entity Identity and the old reference validity ends without severing historical observations.

### Same name, different environment
`customer` exists in production and development. The references remain separate identities by default even though the names and schemas resemble one another.

### Delete and recreate
A table name disappears and later reappears with evidence of a new underlying object. A new identity is established rather than attaching the new object to the retired reference solely because the name matches.

### Cross-source ambiguity
A repository declaration and governance catalog entry appear to describe the same logical pipeline, but available evidence is insufficient. Equivalence remains unresolved and downstream RCA reports the identity limitation.

### Split / replacement
One source table is replaced by two successor tables. The original and successors retain distinct identities; the relationship is represented later through Change/Lineage rather than pretending all three are one entity.

### Correction
Two aliases were previously associated and later proven to refer to separate assets. `separate` preserves the correction and original provenance so prior analysis remains explainable.

### Unauthorized evidence
A caller may receive an opaque upstream entity identity for dependency reasoning while restricted aliases and source-system details remain hidden.

## Non-goals

- deciding whether an entity is in monitoring scope;
- discovering all entities in an external system;
- defining business meaning, ownership, quality, or lineage;
- granting access;
- creating a universal identifier format;
- treating replacement/succession as identity;
- collapsing environment-specific instances for convenience.

## Deferred questions

These do not block the concept boundary:

- Which entity kinds require first-MVP identity coverage beyond logical pipelines, data assets, Databricks jobs/tasks, repositories, and deployment-related entities?
- Which classes of identity association may be inferred automatically versus requiring explicit or authoritative assertion?
- How should source-identifier reuse be detected when an external platform does not expose durable object identity?
