# Concept: Monitoring Scope

**Status:** Accepted — Phase 002 Group 01

## Purpose

Let an organization state which identified entities the monitoring product is responsible for monitoring at a given time, while preserving the difference between intentional exclusion and unknown scope.

## Operational principle

Table C is monitored and depends on Tables A and B. C and B are explicitly in scope. A is known through lineage but is intentionally out of scope because it is managed externally. When C degrades, the system can use the known relationship to A as authorized context, but it does not pretend that complete monitoring evidence for A should exist. Later, A is brought into scope; the new inclusion takes effect without rewriting the earlier period in which A was intentionally excluded.

## Actors

- Data Platform Administrator
- Data Engineer
- Governance / Data Steward
- Monitoring framework
- Authoritative onboarding or metadata synchronization source

## State

- scope assertions attached to an identified entity;
- participation disposition: included or excluded;
- effective-time context for each assertion;
- assertion provenance, actor/source, and authority context;
- optional reason or onboarding context;
- supersession/correction history;
- unresolved conflicting assertions when they cannot be safely collapsed.

A missing assertion is not stored as an exclusion. `Unknown` is a resolution result, not a synthetic scope assertion.

## Actions

### `include`
- **Initiated by:** an authorized actor or authoritative synchronization.
- **Intent:** declare that an identified entity is within monitoring responsibility from an effective time.
- **State effect:** records a new inclusion assertion and preserves any superseded history.
- **Observable result:** later concepts can resolve the entity as in scope for the applicable time.
- **Failure / unknown behavior:** ambiguous identity or insufficient authority does not create guessed inclusion.

### `exclude`
- **Initiated by:** an authorized actor or authoritative synchronization.
- **Intent:** declare that an identified entity is outside monitoring responsibility from an effective time.
- **State effect:** records exclusion without deleting earlier scope state, observations, or known relationships.
- **Observable result:** later reasoning can distinguish intentional exclusion from missing discovery or unknown scope.

### `resolveAt`
- **Initiated by:** any concept that needs monitoring-responsibility context.
- **Intent:** determine the effective scope state for an identified entity at a relevant time.
- **Observable result:** included, excluded, unknown, conflicting, unauthorized, or unavailable, with provenance where disclosure is allowed.

## Invariants / behavioral expectations

- Scope membership never grants data access or authorization.
- Scope is asserted against an **Entity Identity**; unresolved identity does not receive guessed scope.
- An entity may be known to exist while excluded from monitoring or while its scope is unknown.
- Monitoring Scope applies to entities, not to lineage edges, expectations, classifications, or policies.
- Scope does not implicitly propagate upstream, downstream, across a repository, or across a logical pipeline boundary.
- Inclusion does not guarantee that observations exist, are fresh, or are accessible.
- Exclusion does not erase historical evidence or prohibit authorized reasoning from using already-known contextual evidence.
- A known lineage/dependency relationship may cross the scope boundary without silently onboarding the out-of-scope endpoint.
- A scope change is time-aware and does not retroactively rewrite the monitoring responsibility that applied earlier.
- Scope applies to product monitoring responsibility, not implementation deployment topology.

## Ambiguity and missing evidence

A missing scope assertion resolves to `unknown`, not `excluded`. Conflicting effective assertions remain visible until an accepted authority decision resolves them. If identity itself is ambiguous, scope resolution remains unresolved rather than selecting a candidate entity. Authorization may permit a caller to learn that coverage is incomplete without revealing the restricted entity or reason.

## Synchronizations

- **Entity Identity** supplies the referent for every scope assertion.
- **Observation** can use Monitoring Scope to determine where monitoring evidence is expected to be collected, while existing authorized evidence can remain usable across a scope boundary.
- **Lineage** can preserve relationships to known out-of-scope or unknown-scope entities without changing their scope.
- **Investigation** can use scope state to identify evidence-coverage boundaries.
- **Explanation** can communicate that an analysis is incomplete because relevant upstream/downstream entities were excluded or not yet scoped, subject to authorization.
- Later authorization/governance behavior may constrain who can change or inspect scope without becoming part of this concept.

## Security / privacy / governance considerations

Monitoring participation can itself reveal sensitive system structure. A user may be authorized to know that an investigation reaches an unmonitored boundary while not being authorized to learn the boundary entity's identity. Scope state must therefore be authorization-aware when exposed.

Scope must not be used as a surrogate authorization system. Bringing an entity into monitoring cannot broaden access to its raw data, metadata, lineage, or policy details.

## Evidence / provenance considerations

Every scope assertion should retain the source/actor, assertion time, and effective time when known. Changes and corrections should remain reconstructable for historical replay. Synchronized scope claims should preserve the external authority/source rather than appearing to have originated locally.

## Representative scenarios

### Happy path
A production logical pipeline and its consumer-facing output tables are included. Monitoring concepts can resolve those entities as in scope at the relevant time.

### Known out-of-scope boundary
Table C is monitored but depends on an externally managed Table A that is explicitly excluded. Lineage preserves A as a boundary node; the investigation reports that upstream monitoring evidence is incomplete rather than treating A as nonexistent.

### Unknown scope
A newly discovered asset appears in lineage but has no scope assertion. It remains known with `unknown` scope and is not silently monitored or silently excluded.

### Scope change over time
A source table is excluded during January and included beginning February 1. An incident replay for January must still show that monitoring responsibility did not include that source then.

### Conflicting assertions
Two authoritative sources disagree on whether an entity is currently in scope. The concept returns `conflicting` until authority is resolved rather than arbitrarily choosing one.

### Unauthorized evidence
A business analyst can be told that RCA coverage stops at a restricted out-of-scope upstream boundary without being shown the restricted entity's name or metadata.

## Non-goals

- identifying or discovering entities;
- granting or evaluating user authorization;
- defining what healthy means;
- defining expectations or baselines;
- scoping individual lineage edges or hiding topology;
- guaranteeing telemetry collection;
- creating or modifying pipelines or data assets;
- automatically propagating scope across lineage or repository membership.

## Deferred questions

These do not block the concept boundary:

- Which entity kinds are independently scopeable in the first MVP beyond logical pipelines and data assets?
- Which source or role is authoritative when synchronized scope assertions conflict?
- Should automated discovery be allowed to create a non-active `proposed` onboarding state, or should proposals belong to a separate onboarding/discovery concept?
