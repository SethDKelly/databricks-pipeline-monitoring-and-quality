# 003 — Foundational Terminology

This document establishes distinctions that must remain stable during discovery. The fuller glossary remains in [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem

The connected set of repositories, deployments, Databricks jobs/tasks/runs, data assets, dependencies, lineage relationships, governance metadata, health/quality evidence, and downstream consumers relevant to the monitoring product. Known entities may exist outside Monitoring Scope.

### Logical pipeline

A named data-processing responsibility that transforms or moves data for a purpose. A logical pipeline may span multiple Databricks tasks or jobs and must not be equated automatically with one Git repository.

### Pipeline dependency

A relationship in which one logical pipeline's timely or correct operation depends on another pipeline. This may be operational, data-based, or both.

### Repository

A source-control boundary. It may contain one or many logical pipelines, and a logical pipeline may depend on code or assets outside its repository.

## Execution and deployment terms

### Job

A Databricks orchestration/execution definition. Exact mapping from logical pipeline to Databricks job is a discovery concern.

### Task

A unit of execution within a Databricks job.

### Run

A time-bounded execution instance of a job, task, or logical pipeline.

### Code revision

A specific source-controlled version associated with a deployment or pipeline definition.

### Deployment

An event that makes a code/configuration revision available to a target Databricks environment. GitHub Actions is a known deployment mechanism.

### Deployment lineage

The relationship among repository, code revision, GitHub Actions workflow/run, deployed Databricks definition/configuration, and subsequent job/task runs.

## Data terms

### Data asset

A data object such as a table, view, Metric View, external dataset, intermediate dataset, or other durable/meaningful data product. A known data asset is not necessarily inside Monitoring Scope.

### Consumer-facing data asset

A data asset intended for consumption outside the producing pipeline's internal processing boundary.

### Dataset state

The observable condition of a data asset at a point or interval in time, including relevant freshness, volume, schema, distribution, and quality Observations.

### Upstream

An asset, pipeline, source, deployment, or process whose state may influence another asset or pipeline.

### Downstream

An asset, metric, report, application, export, business process, or pipeline that depends on another asset or pipeline.

## Monitoring and quality terms

### Expectation

A provenance-bearing normative assertion of what should be true or acceptable for an identified subject, dimension, context, and time.

An Expectation is not a Baseline, Observation, or Assessment.

### Baseline

Descriptive reference behavior derived from comparable evidence. A Baseline retains its evidence window/population, comparison context, derivation meaning, version, and limitations.

A Baseline is not normative. Typical behavior is not automatically healthy; atypical behavior is not automatically degraded.

### Observation

A provenance-bearing measured or retrieved fact associated with an identified subject and relevant time/context. Examples include run completion, record count, null rate, schema fingerprint, last material-update time, or a complete query establishing zero qualifying events in an interval.

Observation does not declare health, staleness, anomaly, degradation, or cause. Missing evidence is not an Observation of absence.

### Assessment

A dimension-scoped interpretation of Observation evidence against an explicit normative Expectation and/or comparable descriptive Baseline. The Assessment preserves its reference basis, evidence, versions, time context, limitations, and reassessment history.

Baseline-only typicality/atypicality is not silently converted into normative health/failure.

### Freshness

The observed currency/timeliness of an asset relative to a meaningful update/event time. Whether freshness is acceptable is determined by Assessment against an applicable freshness Expectation.

### Staleness

A normative Assessment that observed freshness violates an applicable freshness Expectation. Without a normative criterion, the product may describe unusual age relative to Baseline but should not silently declare staleness.

### Data quality

The degree to which data satisfies explicit Expectations relevant to its intended use. Quality may include completeness, validity, uniqueness, consistency, timeliness/freshness, referential behavior, volume, distribution, schema, and domain-specific dimensions.

### Degradation

A meaningful worsening supported by explicit directional/normative interpretation. A Baseline deviation alone does not establish degradation.

### Quality rule / check

A repeatable mechanism that produces one or more quality Observations and/or evaluates them against an Expectation. Tool-specific implementations such as DQX may realize this later, but the product concept should not be reduced to vendor syntax.

## Reasoning terms

### Evidence

A provenance-bearing fact used to support an Assessment or later Explanation/Investigation. Observation is the primary concept for measured/retrieved evidence.

### Change event

An observed change in data, code, deployment, configuration, schema, topology, semantics, responsibility, policy, Expectation, or another relevant condition. Change does not by itself imply degradation or cause.

### Lineage

A relationship that supports tracing derivation, dependency, or influence. The project intentionally distinguishes several lineage families rather than using one overloaded graph.

### Data lineage

How data assets derive from or flow into other data assets.

### Operational dependency lineage

How pipeline/job execution depends on other execution or availability conditions.

### Deployment lineage

How code/configuration changes become deployed execution definitions and produce runs.

### Root-cause hypothesis

A plausible explanation supported to some degree by evidence but not yet confirmed.

### Attribution

A reasoned statement assigning some portion of an observed change to one or more contributing conditions. Attribution may be partial and may carry uncertainty.

### Confirmed cause

A cause considered sufficiently established under an agreed operational standard or explicit human confirmation. The project must define that standard before automating the label.

### Impact

A known or plausible downstream effect on data assets, metrics, reports, applications, decisions, or business processes.

## Governance and policy terms

### Responsibility Assignment

A provenance-bearing assertion that a person, team, organizational role, or other party bears a named responsibility for an identified subject in a relevant time/context.

Responsibility is not universal authority or authorization.

### Technical owner

A party assigned technical implementation/operational responsibility.

### Business owner / accountable party

A party assigned business accountability for meaning, fitness, or organizational use under a defined responsibility type.

### Data steward

A party assigned stewardship responsibilities for semantics, quality expectations, classifications, or related governance metadata according to organizational practice.

### Classification

A provenance-bearing assertion that an identified subject or facet belongs to a category in a named governance/sensitivity vocabulary. Classification is not Policy Context or authorization.

### Policy Context

A provenance-bearing assertion that a declared policy, handling expectation, restriction, or governance obligation applies to an identified subject/context/time. Policy Context is not access enforcement, legal interpretation, or compliance determination.

### PII

Personally identifiable information according to the applicable organizational/legal definition. The framework should store/refer to classification metadata without assuming one universal definition.

### PHI

Protected health information according to the applicable legal and organizational context.

### HIPAA-related policy context

Policy Context indicating that HIPAA-related obligations, controls, or handling expectations may apply. The context is not itself proof of HIPAA compliance.

### Provenance

Evidence of where a fact, definition, classification, Responsibility Assignment, Policy Context assertion, Expectation, Baseline, Observation, or Assessment came from and when it was observed, asserted, or derived.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ authorization;
- pipeline ≠ repository ≠ Databricks job;
- run success ≠ freshness ≠ data quality;
- Expectation ≠ Baseline;
- normative requirement ≠ historical regularity;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- quality Observation ≠ quality Assessment;
- Assessment ≠ cause;
- anomaly ≠ defect;
- correlation ≠ cause;
- root-cause hypothesis ≠ confirmed cause;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- data lineage ≠ deployment lineage;
- current topology ≠ historical topology;
- business meaning ≠ physical schema;
- business accountability ≠ technical ownership.
