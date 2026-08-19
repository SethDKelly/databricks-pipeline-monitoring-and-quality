# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during concept discovery, but changes must be reflected consistently across foundation and concept documents.

## Data ecosystem

The connected set of repositories, deployments, Databricks jobs/tasks/runs, data assets, dependencies, lineage relationships, governance metadata, health/quality evidence, and downstream consumers relevant to the monitoring product. An entity may be known to the ecosystem while outside Monitoring Scope.

## Logical pipeline

A logical data-processing responsibility that transforms or moves data. A logical pipeline may span one or more Databricks jobs/tasks and must not automatically be equated with a repository.

## Repository

A source-control boundary. It may contain one or more logical pipelines and is not the product reasoning boundary.

## Job

A Databricks execution/orchestration definition. Its exact relationship to a logical pipeline is discovered rather than assumed.

## Task

A unit of execution within a Databricks job.

## Run

A time-bounded execution instance of a job, task, or logical pipeline.

## Code revision

A specific version of source-controlled code/configuration relevant to deployment lineage.

## Deployment

An event that makes a code/configuration revision available in a target Databricks environment. GitHub Actions is a known deployment mechanism in the current ecosystem.

## Data asset / dataset

A data object such as a table, view, Metric View, external dataset, intermediate dataset, or other durable/meaningful data structure. A known data asset is not necessarily in Monitoring Scope.

## Consumer-facing data asset

A data asset intended for consumption beyond the producing pipeline's internal processing boundary.

## Dataset state

The observable condition of a data asset at a time or interval, including relevant freshness, volume, schema, distribution, and quality Observations.

## Upstream

An asset, pipeline, source, deployment, or process whose state may influence another asset or pipeline.

## Downstream

An asset, pipeline, metric, report, application, export, or business process that depends on another asset or pipeline.

## Dependency

A relationship in which correct or timely operation/use of one component depends on another. Operational dependency and data lineage may overlap but are not necessarily identical.

## Lineage

A typed relationship supporting derivation, dependency, or influence tracing. The project distinguishes data, operational, deployment, and consumption/impact relationships where useful.

## Data lineage

How data assets derive from or flow into other data assets.

## Operational dependency lineage

How pipelines/jobs depend on other execution or availability conditions.

## Deployment lineage

How repository/code revisions, GitHub Actions deployments, Databricks definitions, and runs relate over time.

## Freshness

The observed currency/timeliness of an asset relative to a meaningful event or material-update time. Whether that freshness is acceptable is an Assessment against an applicable Expectation; historical behavior alone is not a normative freshness requirement.

## Staleness

A normative Assessment that observed freshness fails an applicable freshness Expectation. When no normative criterion exists, the product may describe freshness as atypical relative to a Baseline but should not silently label it stale.

## Expectation

An accepted Phase 002 concept: a provenance-bearing normative assertion describing what should be true or acceptable for an identified subject, dimension, context, and time.

An Expectation is not a Baseline, Observation, or Assessment.

## Quality expectation

An Expectation specifically describing acceptable data-quality behavior, such as completeness, validity, uniqueness, consistency, volume, schema, referential behavior, or a domain-specific criterion.

## Baseline

An accepted Phase 002 concept: descriptive reference behavior derived from a defined population of comparable evidence. A Baseline preserves its evidence window, comparison context, derivation meaning, version, and limitations.

A Baseline is not normative. `Typical` does not mean `healthy`; `atypical` does not mean `degraded`.

## Observation

An accepted Phase 002 concept: a provenance-bearing measured or retrieved fact about an identified subject and relevant time/context. An Observation preserves measurement meaning and evidence provenance without declaring health, anomaly, staleness, or cause.

Missing evidence is not an Observation of zero/no-event. Observed absence requires sufficient evidence coverage to establish non-occurrence over a defined interval.

## Quality observation

An Observation used as data-quality evidence, such as row count, null rate, uniqueness result, schema fingerprint/change fact, distribution measure, reconciliation result, or domain-rule measurement.

## Assessment

An accepted Phase 002 concept: a dimension-scoped interpretation of authorized Observation evidence against an explicit normative Expectation and/or comparable descriptive Baseline.

Assessment preserves its basis, supporting Observation references, Expectation/Baseline versions, evaluation context, limitations, and reassessment history. Baseline-only typicality/atypicality is not silently converted into normative health/failure.

## Degradation

A meaningful worsening supported by explicit directional/normative interpretation. A Baseline deviation alone is not sufficient to establish degradation: atypical behavior can be neutral, beneficial, or harmful depending on semantics and Expectations.

## Change event

An observed change in data, code, deployment, configuration, metadata, schema, policy, responsibility, expectation, topology, or another relevant condition that may be relevant to later analysis. Change does not by itself imply degradation or cause.

## Evidence

A provenance-bearing fact used to support an Assessment, Investigation, or Explanation. Observation is the primary accepted concept for measured/retrieved evidence; later concepts may preserve additional evidence relationships without redefining source facts.

## Root-cause hypothesis

A plausible explanation supported to some degree by evidence but not yet confirmed.

## Attribution

A reasoned statement assigning some portion of an observed change to one or more contributing conditions. Attribution may be partial and uncertain.

## Confirmed cause

A cause supported according to an agreed operational standard or explicit authorized human confirmation. That standard is not yet defined.

## Impact / business impact

The known or potential downstream effect of a pipeline/data condition on assets, metrics, reports, applications, decisions, or processes.

## Technical owner

A party assigned responsibility for technical implementation and operational maintenance. Technical ownership does not imply authority over business semantics, classification, policy, Expectations, or data access.

## Business owner / accountable party

A party assigned accountability for business meaning, fitness, or authorized organizational use according to the relevant Responsibility Assignment definition.

## Data steward

A party assigned stewardship responsibilities such as maintaining definitions, quality semantics, classifications, Expectations, or governance metadata according to organizational practice.

## Responsibility type

A named kind of responsibility, such as technical ownership, business accountability, semantic stewardship, quality-expectation stewardship, or privacy/security responsibility. Responsibility types are not interchangeable.

## Classification

A provenance-bearing assertion that an identified subject or facet belongs to a category in a named governance or sensitivity vocabulary. Classification is not authorization or policy applicability.

## PII

Personally identifiable information according to applicable organizational/legal definitions and policies.

## PHI

Protected health information according to applicable legal and organizational context.

## Policy context

A provenance-bearing assertion that a declared policy, handling expectation, restriction, or governance obligation applies to an identified subject in a relevant context and time. Policy Context is not access enforcement, legal interpretation, or compliance determination.

## HIPAA-related policy context

Policy context indicating that HIPAA-related obligations, controls, or handling expectations may apply. This context alone does not establish HIPAA compliance.

## Provenance

Information describing where a fact, definition, classification, responsibility assignment, policy-context assertion, Expectation, Baseline, Observation, or Assessment came from, who/what asserted or derived it, and the relevant time/version context.

## Authority / source precedence

Rules or assertions determining which source or actor may be treated as authoritative for a particular metadata or normative category, subject, context, and time. Phase 002 has deliberately not defined a universal authority rule; unresolved conflicts remain conflicts until such semantics are accepted.

## Phase 002 concept terms

### Monitoring Scope — Accepted

The time-aware declaration of whether the monitoring product is responsible for monitoring an identified entity. Scope can resolve as included, excluded, unknown, conflicting, unauthorized, or unavailable. Scope is not authorization and does not implicitly propagate through lineage.

### Entity Identity — Accepted

The functionality for determining when source-specific references denote the same logical entity across systems and time, while preserving ambiguity, separation, validity history, and correction provenance.

### Semantic Definition — Accepted

The functionality for recording and resolving provenance-bearing semantic assertions that describe what an identified entity means in a relevant business or technical context and time. Semantic facets may coexist; the concept does not assume one canonical definition string.

### Responsibility Assignment — Accepted

The functionality for recording and resolving who bears a named responsibility for an identified subject at a relevant time. Responsibility does not imply universal authority or authorization.

### Classification — Accepted

The functionality for recording and resolving category membership under named governance/sensitivity vocabularies while preserving source meaning, provenance, time, and conflict.

### Policy Context — Accepted

The functionality for recording and resolving declared policy applicability/handling context for a subject/context/time without claiming enforcement, legal interpretation, or compliance.

### Expectation — Accepted

The functionality for recording and resolving normative criteria describing what should be true or acceptable for an identified subject/dimension/context/time.

### Baseline — Accepted

The functionality for deriving and resolving descriptive reference behavior from comparable evidence while preserving evidence population, context, version, provenance, and comparability limitations.

### Observation — Accepted

The functionality for recording provenance-bearing measured/retrieved facts without interpreting health or cause, including explicit evidence-coverage semantics for legitimate observed absence.

### Assessment — Accepted

The functionality for interpreting Observation evidence against explicit Expectation and/or Baseline context with a basis-appropriate, dimension-scoped result and reproducible historical provenance.

### Causal Claim — Candidate

A proposed or reviewed causal explanation with explicit epistemic status and linked supporting/contradicting evidence.

### Annotation — Candidate

Human-authored context attached to evidence, an investigation, or a claim without mutating the underlying source facts.

### Explanation — Candidate

An evidence-grounded, authorization-aware account of what happened, what is affected, what is known/uncertain, and where the supporting evidence comes from.

## Concept

An independently understandable unit of functionality with a clear purpose, operational principle, state, and actions, composed with other concepts through synchronizations.

A concept is not automatically an implementation component or domain entity.

## Synchronization

A defined coordination between otherwise independent concepts that composes their behaviors without collapsing their purposes/state into one concept.
