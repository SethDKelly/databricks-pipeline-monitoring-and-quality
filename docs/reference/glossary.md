# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during concept discovery, but changes must be reflected consistently across foundation and concept documents.

## Core ecosystem

### Data ecosystem
The connected set of repositories, Change Intents, deployments, executions, data assets, dependencies, Lineage relationships, governance metadata, health/quality evidence, and downstream consumers relevant to monitoring. An entity may be known while outside Monitoring Scope.

### Logical pipeline
A logical data-processing responsibility that transforms or moves data. It may span one or more jobs/tasks and does not automatically equal a repository.

### Repository
A source-control boundary and provenance context, not the product reasoning boundary.

### Job / Task / Run
A Job is a Databricks orchestration definition; Task is a unit inside it; Run/execution instance is time-bounded actual work established by execution evidence.

### Code revision
A source-controlled version of code/configuration relevant to Deployment provenance.

## Group 04 — history, lineage, and change

### Change Intent — Accepted
The functionality for registering an intended modification and anticipated effects before realization. It preserves target, planned/effective context, anticipated effects, monitoring implications, provenance, and revision/withdrawal history.

Anticipated effects are not automatically Expectations, Observations, Changes, or causes.

### Execution History — Accepted
The functionality for reconstructing actual execution instances/lifecycle states and their provenance over time. Missing telemetry does not create a fictional missing execution.

### Deployment — Accepted
The functionality for recording deployment attempts and resolving which source/configuration state was actually active for a target/time. Attempt, workflow success, and activation remain distinct; activation does not prove data effect or health.

### Lineage — Accepted
The functionality for maintaining/traversing typed, directed, temporal, provenance-bearing relationships among Entity Identities. Current topology does not overwrite historical topology; planned topology is not active until evidence establishes it.

Lineage requires **graph-compatible semantics**, but Phase 002 selects no graph database, graph query language, or graph service.

### Change — Accepted
The functionality for identifying/describing a realized difference or state transition established by evidence, preserving before/after or source-event basis, time, magnitude, provenance, comparability, and uncertainty.

Change does not by itself mean intended, unintended, healthy, degraded, valid, invalid, or causal.

### Evidence-ledger semantics
A cross-cutting requirement that material historical facts/assertions remain provenance-bearing, reconstructable, and corrected through append/supersede relationships rather than invisible mutation.

This is **not** a blockchain/event-sourcing/storage selection.

### Effective/event time
When a condition was true or event occurred.

### Recorded/knowledge time
When the monitoring ecosystem learned or recorded it. Historical replay may need both.

## Scope and identity

### Monitoring Scope — Accepted
The time-aware declaration of whether the product is responsible for monitoring an Entity Identity. Scope is not authorization and does not implicitly propagate through Lineage.

### Entity Identity — Accepted
Functionality for deciding when source-specific references denote the same logical entity across systems/time while preserving ambiguity, separation, validity, and correction provenance.

## Semantics, responsibility, governance, policy

### Semantic Definition — Accepted
Provenance-bearing semantic assertions describing what an entity means in a relevant business/technical context/time.

### Responsibility Assignment — Accepted
Who bears a named responsibility for an identified subject/time. Responsibility does not imply universal authority or authorization.

### Classification — Accepted
Category membership under named governance/sensitivity vocabularies, preserving source meaning/provenance/time/conflict.

### Policy Context — Accepted
Declared policy applicability/handling context for subject/context/time without claiming enforcement, legal interpretation, or compliance.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational categories/context according to applicable definitions. Presence of such metadata does not itself establish compliance.

## Health evaluation

### Expectation — Accepted
A provenance-bearing normative assertion describing what should be true/acceptable for subject/dimension/context/time.

A Change Intent may prompt explicit establishment/revision of a post-change Expectation, but anticipated effects do not become normative automatically.

### Quality expectation
An Expectation specifically describing acceptable data-quality behavior.

### Baseline — Accepted
Descriptive reference behavior derived from comparable Observation evidence. It preserves evidence population/window, comparison context, derivation meaning, version, and limitations.

A Change Intent can register a prospective comparability break; realization evidence is required before the break becomes effective. A new Baseline must be derived from post-change observations rather than intended values.

### Observation — Accepted
A provenance-bearing measured/retrieved fact. Observation preserves measurement meaning/time/provenance without declaring health, anomaly, staleness, intent conformance, or cause. Missing evidence is not observed absence.

### Assessment — Accepted
A dimension-scoped interpretation of authorized Observation evidence against explicit Expectation and/or comparable Baseline context, preserving its basis/history.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that observed freshness violates an applicable freshness Expectation.

### Degradation
A meaningful worsening supported by explicit directional/normative interpretation. Baseline deviation or realized Change alone is insufficient.

## Lineage families

### Data lineage
How data assets derive from or flow into other data assets.

### Operational dependency lineage
How pipelines/jobs/executions depend on other availability/execution conditions.

### Deployment provenance
How repositories/revisions/configuration/deployments/active targets/executions relate over time. It remains distinct from data derivation Lineage.

## Reasoning terms

### Evidence
A provenance-bearing fact used to support Assessment, Investigation, Causal Claim, or Explanation.

### Root-cause hypothesis
A plausible explanation supported to some degree by evidence but not confirmed.

### Attribution
A reasoned statement assigning contribution to one or more conditions with uncertainty.

### Confirmed cause
A cause supported under an agreed evidence/authority standard or explicit authorized human confirmation.

### Impact / business impact
Known or potential downstream effect. Lineage reachability creates candidates, not confirmed impact.

### Causal Claim — Candidate
A proposed/reviewed causal explanation with explicit epistemic status and linked supporting/contradicting evidence.

### Annotation — Candidate
Human-authored context attached without mutating underlying source facts.

### Explanation — Candidate
Evidence-grounded, authorization-aware account of what happened, what is affected, what is known/uncertain, and where evidence comes from.

## Governance roles/metadata

### Technical owner / Business accountable party / Data steward
Distinct Responsibility Assignment types.

### Provenance
Information describing where a fact/assertion/definition/classification/intent/deployment/relationship/Expectation/Baseline/Observation/Assessment/Change came from, who/what asserted or derived it, and relevant temporal/version context.

### Authority / source precedence
Rules determining which source/actor is authoritative for a category/subject/context/time. The project has no universal authority rule; unresolved conflicts remain conflicts.

## Concept Design

### Concept
An independently understandable unit of functionality with a clear purpose, operational principle, state, and actions, composed via synchronizations.

### Synchronization
Defined coordination between independent concepts without collapsing their purposes/state into one concept.
