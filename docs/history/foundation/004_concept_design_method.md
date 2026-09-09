# 004 — Concept Design Method

## Decision

**Foundation:** The entire monitoring and quality ecosystem will be designed using Daniel Jackson's Concept Design approach before technical architecture is selected.

Primary reference: Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*.

Useful public references:

- https://essenceofsoftware.com/
- https://essenceofsoftware.com/tutorials/
- https://www.csail.mit.edu/research/rethinking-software-design

## Why this project needs Concept Design

This product sits at the intersection of data engineering, governance, quality, security, lineage, business semantics, and incident analysis. Without a disciplined functional decomposition, it would be easy to design the product around whichever tools are already available: Databricks jobs, DQX checks, Metric Views, GitHub workflows, Collibra assets, or Immuta policies.

Those are important implementation/integration surfaces, but they are not the product's conceptual design.

Concept Design gives the project a way to define the user-visible/system-visible functionality independently and then decide later how each concept is realized or integrated.

## What counts as a concept

For this project, a candidate is concept-like when:

- it exists for a clear purpose that matters to an actor;
- it has interesting behavior, not merely data fields;
- it has state that it owns conceptually;
- it has meaningful actions;
- a representative operational principle can explain how it fulfills its purpose;
- it can be understood substantially independently from neighboring concepts;
- it is not merely an implementation component or vendor noun.

A table, API endpoint, Spark job, Git repository, Databricks workspace, service, queue, dashboard, or Python class is **not automatically a concept**.

## Required concept specification

Every accepted concept must define:

### Name

A concise, stable noun or noun phrase for the functionality.

### Purpose

One primary reason the concept exists. Prefer a pithy actor-centered need rather than a list of features.

The project adopts **one concept ↔ one primary purpose** as a design heuristic. If a candidate has several unrelated purposes, split it or reconsider its boundary. If two concepts claim the same purpose, examine whether they are redundant or poorly scoped.

### Operational principle

A representative scenario showing the concept in action and demonstrating why the actions/state satisfy the purpose.

The operational principle should be rich enough to reveal the concept's essential behavior, not merely the shortest happy path.

### State

The information the concept conceptually owns and remembers. State should be described functionally before any storage representation is considered.

### Actions

The actions that create, change, remove, or expose the concept's state.

Actions should use concept language and actor intent, not implementation verbs such as `POST`, `INSERT`, `SELECT`, or `runSparkJob` unless those later become deliberate technical mappings.

### Invariants / behavioral expectations

Important truths that should continue to hold across actions. This is a project extension to make trust, security, and evidence requirements explicit during concept refinement.

### Synchronizations

How actions or states of separate concepts coordinate to deliver larger behavior.

Synchronizations must not be used as an excuse to merge concept state or create hidden bidirectional coupling.

### Failure / ambiguity behavior

What the concept does when evidence is missing, conflicting, stale, unauthorized, or incomplete.

This is especially important for monitoring and root-cause reasoning because "unknown" is a legitimate state.

## Concept independence

Concepts should be designed so that each can be explained without first explaining the entire system.

Examples of harmful coupling to avoid:

- an Ownership concept that only works if Collibra is installed;
- a Quality Expectation concept whose semantics are defined by DQX syntax;
- an Investigation concept that silently assumes every anomaly has one root cause;
- a Lineage concept that mixes data derivation, deployment provenance, and run orchestration into one untyped relationship;
- a Classification concept that directly grants access instead of describing policy context and synchronizing with authorization concerns.

## Concept synchronization

The product will be composed by synchronizing independent concepts.

Illustrative examples, not final specifications:

- an **Observation** recorded for an asset can synchronize with an **Expectation** to produce an **Assessment**;
- a degraded **Assessment** can synchronize with **Investigation** to open or enrich an investigation;
- **Lineage** can synchronize with **Investigation** to enumerate upstream evidence and downstream impact candidates;
- **Ownership** can synchronize with **Investigation** or **Reporting** to identify responsible stakeholders;
- **Classification** can synchronize with **Presentation/Access** to constrain what evidence is revealed;
- a **Deployment** can synchronize with **Change** and **Investigation** when timing overlaps with a degradation.

These examples are intentionally functional. They do not imply event buses, services, database joins, or APIs.

## Concept versus domain entity

Some domain entities appear in many concepts but are not themselves concepts.

For example, a `Data Asset` may be referenced by Ownership, Description, Classification, Observation, Lineage, Expectation, and Investigation. That does not mean all those behaviors belong in one giant `DataAsset` concept.

Likewise, a repository or Databricks job can be an identified entity participating in several concepts without determining the product's concept boundaries.

## Concept discovery workflow

For each new product capability:

1. Start from an actor need or recurring scenario.
2. State the purpose without naming a tool or implementation.
3. Propose the smallest concept that can fulfill the purpose.
4. Write an operational principle.
5. Identify owned state and actions.
6. Test the concept against happy-path, degraded, missing-data, conflicting-data, and unauthorized scenarios.
7. Check whether the candidate duplicates another concept's purpose.
8. Identify required synchronizations rather than merging concerns.
9. Test vocabulary against the glossary.
10. Only after concept acceptance, discuss possible implementation mappings in a later technical-design phase.

## Anti-patterns

### Vendor-shaped concept design

Bad: `DQXConcept`, `UnityCatalogConcept`, `CollibraConcept`.

Better: define Quality Expectation, Quality Observation, Ownership, Classification, Lineage, etc., then evaluate which systems realize or supply them.

### Architecture-shaped concept design

Bad: `MonitoringService`, `MetadataDatabase`, `GraphAPI`.

These are possible implementation constructs, not conceptual functionality.

### UI-shaped concept design

Bad: `Dashboard`, `PipelinePage`, `RCAChat` as foundational concepts.

A UI may expose several concepts. The interaction design comes later.

### One giant ecosystem concept

If every action needs every state field, the design has failed to decompose functionality.

### Overconfident reasoning

A concept that must always output a root cause even when evidence is insufficient is misdesigned. Uncertainty and unresolved ambiguity are first-class outcomes.

## Concept acceptance gate

A candidate concept should not be promoted to an accepted specification until:

- its purpose is singular and clear;
- its operational principle demonstrates useful behavior;
- its state/actions can be described independently;
- its terminology is not overloaded;
- its security/policy implications are considered;
- its evidence/provenance implications are considered;
- its dependencies are expressed as synchronizations where possible;
- and it does not require a premature technical architecture.
