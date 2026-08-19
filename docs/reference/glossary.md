# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during concept discovery, but changes must be reflected consistently across foundation and concept documents.

## Data ecosystem

The connected set of repositories, deployments, Databricks jobs/tasks/runs, data assets, dependencies, lineage relationships, governance metadata, quality evidence, and downstream consumers relevant to the monitoring product. An entity may be known to the ecosystem while outside Monitoring Scope.

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

The observable condition of a data asset at a time or interval, including relevant freshness, volume, schema, distribution, and quality observations.

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

How recently an asset was materially updated relative to expected behavior and consumer need.

## Staleness

A state in which freshness no longer meets an applicable expectation.

## Expectation

A statement of what should be true or acceptable about execution, freshness, data behavior, quality, semantics, or policy-relevant state.

## Quality expectation

An expectation specifically describing acceptable data quality or behavior.

## Observation

A measured/retrieved fact about an asset, run, deployment, or time period, retained with provenance.

## Quality observation

An observation used to evaluate data quality, such as a null rate, row count, uniqueness result, distribution measure, schema change, or domain-rule result.

## Assessment

An interpretation of evidence relative to an expectation or baseline, such as healthy, stale, degraded, anomalous, or unresolved.

## Baseline

A historical or declared reference used for comparison. A baseline is not necessarily an expectation and should retain its derivation.

## Degradation

A meaningful worsening in operational, freshness, or data-quality behavior, potentially before a hard failure occurs.

## Change event

An observed change in data, code, deployment, configuration, metadata, schema, policy, responsibility, or topology that may be relevant to analysis.

## Evidence

An observable fact with provenance used to support an assessment or explanation.

## Root-cause hypothesis

A plausible explanation supported to some degree by evidence but not yet confirmed.

## Attribution

A reasoned statement assigning some portion of an observed change to one or more contributing conditions. Attribution may be partial and uncertain.

## Confirmed cause

A cause supported according to an agreed operational standard or explicit authorized human confirmation. That standard is not yet defined.

## Impact / business impact

The known or potential downstream effect of a pipeline/data condition on assets, metrics, reports, applications, decisions, or processes.

## Technical owner

A party assigned responsibility for technical implementation and operational maintenance. Technical ownership does not imply authority over business semantics, classification, policy, or data access.

## Business owner / accountable party

A party assigned accountability for business meaning, fitness, or authorized organizational use according to the relevant responsibility definition.

## Data steward

A party assigned stewardship responsibilities such as maintaining definitions, quality semantics, classifications, or governance metadata according to organizational practice.

## Responsibility type

A named kind of responsibility, such as technical ownership, business accountability, semantic stewardship, or privacy/security responsibility. Responsibility types are not interchangeable.

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

Information describing where a fact, definition, classification, responsibility assignment, policy-context assertion, or observation came from, who/what asserted it, and the relevant time/version context.

## Authority / source precedence

Rules or assertions determining which source or actor may be treated as authoritative for a particular metadata category, subject, context, and time. Phase 002 Group 02 deliberately does not define a universal authority rule; unresolved conflicts remain conflicts until such semantics are accepted.

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
