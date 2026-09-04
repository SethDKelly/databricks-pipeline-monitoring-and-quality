# Concept Design Method

**Canonical key:** `foundation.concept_design_method`

**Kind:** REFERENCE

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `foundation.concept_design_method`

**Owns current question:** What functional design method governs DMTZ concept boundaries, specifications, synchronizations, and semantic change?

**Stable IDs:** N/A

## Current semantics

DMTZ uses Daniel Jackson's **Concept Design** approach to keep user/system functionality independent from vendor products, schemas, services, UI screens, and technical architecture choices.

The method remains relevant after technical architecture selection: accepted concepts and their synchronization/refinement contracts continue to constrain implementation. Architecture and implementation may realize concepts; they do not redefine a concept's purpose or merge independent concepts for convenience.

## What qualifies as a concept

A candidate is concept-like when it:

- exists for one clear actor-relevant purpose;
- owns interesting functional state and behavior;
- has meaningful actions stated in domain language;
- has a representative operational principle explaining how it fulfills its purpose;
- can be understood substantially independently from neighboring concepts;
- composes with other concepts through explicit synchronizations;
- is not merely a vendor noun, database/table, API, service, queue, repository, job, class, dashboard, or screen.

The project uses **one concept ↔ one primary purpose** as a design heuristic. Unrelated purposes should be split or the boundary reconsidered.

## Required concept specification

Every accepted concept should define:

1. **Name** — stable noun/noun phrase for the functionality.
2. **Purpose** — one primary actor-centered reason the concept exists.
3. **Operational principle** — representative scenario rich enough to demonstrate essential behavior.
4. **State** — information the concept functionally owns/remembers, independent of storage representation.
5. **Actions** — actor/system actions that create/change/remove/expose state, stated in concept language.
6. **Invariants / behavioral expectations** — durable truths, including trust/evidence/security constraints where relevant.
7. **Synchronizations** — coordination with independent concepts without hidden state ownership transfer.
8. **Failure / ambiguity behavior** — treatment of missing, conflicting, stale, partial, unavailable, or unauthorized evidence.

## Concept independence

A concept must not be defined by a particular implementation provider or by a neighboring concept's internal state.

Examples of prohibited collapse include:

- defining quality semantics by a DQX syntax;
- defining Lineage as every kind of dependency/provenance/exposure relation in one untyped edge;
- making Investigation own copied Observations, Causal Claims, Impact, or Annotations;
- making Classification directly grant access instead of synchronizing with distinct authorization semantics;
- making a repository, Databricks job, service, or data asset into a giant container for unrelated functionality.

A domain entity may participate in many concepts without itself becoming a concept that owns all those behaviors.

## Synchronization discipline

Independent concepts coordinate through synchronizations. Synchronization is not permission to merge purposes, state, or authority.

Representative patterns include:

- Observation + Expectation/Baseline → Assessment;
- Assessment/change/question + Investigation → bounded inquiry context;
- Lineage + Investigation/Impact → candidate topology while preserving reachability/exposure/cause distinctions;
- Responsibility Assignment + Investigation/Explanation → relevant accountable contacts;
- Classification/Policy Context + Capability Authorization → bounded permitted projection without turning governance labels into authorization;
- Deployment + Change + Investigation → temporal/change evidence without converting correlation into causality.

These are functional relationships, not mandates for event buses, services, joins, queues, or APIs.

## Discovery and change workflow

For a proposed new capability or semantic change:

1. start from an actor need, current question, or recurring scenario;
2. state the purpose without naming an implementation tool;
3. identify the smallest independently motivated concept or existing concept that owns the behavior;
4. write/review the operational principle;
5. identify owned state/actions/invariants and ambiguity behavior;
6. test happy, degraded, missing-evidence, conflict, correction, historical, and authorization cases as applicable;
7. check for purpose overlap with existing concepts;
8. express cross-concept behavior as synchronization/refinement rather than merging concerns;
9. validate terminology and stable-ID compatibility;
10. only then map the accepted behavior to architecture/implementation.

Current CKR documentation migration follows the same discipline: moving authority cannot manufacture new purpose/state/action semantics.

## Acceptance gate

A candidate concept should not become accepted/current unless:

- purpose is singular and clear;
- operational principle demonstrates useful behavior;
- state/actions can be described independently;
- terminology is not overloaded;
- security/authorization/policy implications are explicit where relevant;
- evidence/provenance/time implications are explicit where relevant;
- dependencies are expressed as synchronizations rather than accidental coupling;
- ambiguity/unknown behavior is legitimate rather than forced certainty;
- technical implementation is not used as the semantic definition.

## Anti-patterns

- **Vendor-shaped design** — `UnityCatalogConcept`, `DQXConcept`, `CollibraConcept`.
- **Architecture-shaped design** — `MonitoringService`, `MetadataDatabase`, `GraphAPI` as product concepts.
- **UI-shaped design** — `Dashboard`, `PipelinePage`, `RCAChat` as foundational concepts.
- **One giant ecosystem concept** — every behavior/state centralized under a single entity.
- **Overconfident reasoning** — requiring a cause/negative/health state when evidence is insufficient.
- **Implementation convenience as change control** — rewriting accepted concepts because a chosen technology prefers another shape.

## Synchronizations / related canonical resources

- [Product definition](product-definition.md)
- [Foundational terminology](terminology.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Shared glossary](glossary.md)

The 24 accepted concept definitions themselves remain inventory-selected legacy authority until CKR-C.

## Provenance

- Original owner: [`../../foundation/004_concept_design_method.md`](../../foundation/004_concept_design_method.md)
- Accepted concept catalog/design application: [`../../concepts/README.md`](../../concepts/README.md), [`../../concepts/phase_002/README.md`](../../concepts/phase_002/README.md)
- Synchronization/refinement discipline: [`../../concepts/phase_003/README.md`](../../concepts/phase_003/README.md), [`../../concepts/phase_004/README.md`](../../concepts/phase_004/README.md)
- Architecture handoff preserving contract authority: [`../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md)
