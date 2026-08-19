# Concept: Monitored Scope

**Status:** Candidate

## Purpose

Let an organization state which ecosystem entities and relationships are intended to participate in monitoring and reasoning.

## Operational principle

A data platform owner brings a logical pipeline and its produced tables into monitoring. One intermediate asset is intentionally excluded because it is ephemeral and has no monitoring value. Later, an investigation of a downstream table can distinguish between a known-but-out-of-scope upstream entity and an entity whose existence is unknown.

## Actors

- Data Platform Administrator
- Data Engineer
- Governance / Data Steward
- Monitoring framework

## State

- scope assertions about identified entities or relationship classes;
- inclusion/exclusion intent;
- reason/context for the assertion when supplied;
- effective time or lifecycle state of the assertion;
- assertion provenance and authority context;
- unresolved/conflicting scope assertions when they cannot be safely collapsed.

## Actions

### `include`
- **Initiated by:** authorized administrator, onboarding process, or authoritative source synchronization.
- **Intent:** declare that an identified entity/relationship should participate in monitoring.
- **State effect:** establishes or supersedes a scope assertion.
- **Observable result:** the entity is considered in-scope for applicable monitoring behavior.
- **Failure / unknown behavior:** unresolved identity or insufficient authority does not create a guessed inclusion.

### `exclude`
- **Initiated by:** authorized actor/source.
- **Intent:** declare that an entity/relationship should not currently participate.
- **State effect:** records an exclusion without deleting prior scope history.
- **Observable result:** later reasoning can distinguish intentional exclusion from missing discovery.

### `resolveAt`
- **Initiated by:** any concept needing scope context.
- **Intent:** determine the effective scope state for an identified entity at a relevant time.
- **Observable result:** included, excluded, conflicting, unknown, or unavailable with provenance.

## Invariants / behavioral expectations

- Scope membership never grants data access or authorization.
- Excluding an entity does not erase historical observations or relationships already collected under an earlier scope state.
- A missing scope assertion is not silently equivalent to exclusion.
- Scope applies to logical monitoring participation, not implementation deployment topology.
- Scope decisions retain provenance and effective time when those facts are available.

## Ambiguity and missing evidence

Conflicting scope assertions remain visible until an accepted authority rule resolves them. Unknown and unauthorized scope context are valid results. The concept must not infer inclusion only because an entity appears in lineage.

## Synchronizations

- **Asset Identity** provides the referent for scope assertions.
- **Observation** may synchronize with scope to determine whether evidence should be collected/considered.
- **Lineage** may expose known relationships that are outside monitored scope without silently onboarding them.
- **Explanation** may disclose that evidence is incomplete because an upstream entity is out of scope, subject to authorization.

## Security / privacy / governance considerations

The fact that an entity exists or is monitored can itself be sensitive. Scope visibility must respect the later authorization model.

## Evidence / provenance considerations

Every non-local assertion should retain its source and effective time. Scope should be explainable: the framework should be able to distinguish user declaration, synchronized authority, inherited rule, and unresolved conflict if those modes are adopted later.

## Representative scenarios

### Happy path
A logical pipeline and its output tables are included; observations and assessments reference that scope.

### Degraded path
A downstream asset is monitored while an upstream external feed is explicitly out of scope. The system reports the evidence gap instead of claiming full RCA coverage.

### Conflicting evidence
One source marks an asset in scope while another marks it excluded. The concept returns a conflict until authority is resolved.

### Unauthorized evidence
A user may be able to investigate a downstream asset without being allowed to discover the name/details of an excluded sensitive upstream asset.

## Non-goals

- authorizing users;
- discovering identity;
- defining what healthy means;
- guaranteeing telemetry collection;
- creating or modifying pipelines.

## Open questions

- Which entity/relationship kinds can be independently scoped?
- Is inheritance of scope across lineage useful, or too implicit?
- Who/what is authoritative for scope in the first MVP?
