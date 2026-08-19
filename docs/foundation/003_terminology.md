# 003 — Foundational Terminology

This document establishes distinctions that must remain stable during discovery. The fuller glossary remains in [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem

The connected set of repositories, deployments, Databricks jobs/tasks/runs, data assets, dependencies, lineage relationships, governance metadata, quality expectations/observations, and downstream consumers within monitoring scope.

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

A monitored data object such as a table, view, metric view, external dataset, intermediate dataset, or other durable/meaningful data product.

### Consumer-facing data asset

A data asset intended for consumption outside the producing pipeline's internal processing boundary.

### Dataset state

The observable condition of a data asset at a point or interval in time, including relevant freshness, volume, schema, distribution, and quality observations.

### Upstream

An asset, pipeline, source, deployment, or process whose state may influence another asset or pipeline.

### Downstream

An asset, metric, report, application, export, business process, or pipeline that depends on another asset or pipeline.

## Monitoring and quality terms

### Expectation

A statement of what should be true or acceptable about execution, freshness, data behavior, quality, semantics, or policy-relevant state.

An expectation is not an observation.

### Observation

A measured or retrieved fact associated with an asset, run, deployment, or time period. Examples include run completion, record count, null rate, schema fingerprint, DQ result, or last update time.

### Assessment

An interpretation produced by comparing evidence against an expectation or baseline. Examples: healthy, stale, degraded, anomalous, or unresolved.

### Baseline

A historical or declared reference used for comparison. A baseline is not necessarily an expectation and must retain its derivation.

### Freshness

How current an asset is relative to its expected update behavior and consumer need.

### Staleness

A state in which freshness no longer meets an applicable expectation.

### Data quality

The degree to which data satisfies explicit expectations relevant to its intended use. Quality may include completeness, validity, uniqueness, consistency, timeliness/freshness, referential behavior, volume, distribution, and domain-specific dimensions.

### Degradation

A meaningful worsening in operational, freshness, or data-quality behavior. Degradation may occur without a hard job failure.

### Quality rule / check

A repeatable evaluation that produces one or more quality observations. Tool-specific implementations such as DQX may realize this later, but the product concept should not be reduced to a vendor implementation.

## Reasoning terms

### Evidence

An observable fact with provenance used to support an assessment or explanation.

### Change event

An observed change in data, code, deployment, configuration, schema, topology, semantics, ownership, policy, or another relevant condition.

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

### Technical owner

The person or team responsible for technical implementation and operational maintenance.

### Business owner

The stakeholder accountable for business meaning, fitness, or authorized use of an asset.

### Data steward

A role responsible for stewardship of definitions, quality expectations, classifications, or related governance responsibilities according to organizational practice.

### Classification

Metadata describing sensitivity, type, handling category, criticality, or another governance category.

### PII

Personally identifiable information according to the applicable organizational/legal definition. The framework should store/refer to classification metadata without assuming one universal definition.

### PHI

Protected health information according to the applicable legal and organizational context.

### HIPAA-related policy context

Metadata indicating that HIPAA-related obligations, controls, or handling expectations may apply. The label is not itself proof of HIPAA compliance.

### Provenance

Evidence of where a fact, definition, classification, ownership assignment, metric, or assessment came from and when it was observed or asserted.

## Terms to avoid conflating

- pipeline ≠ repository;
- pipeline ≠ Databricks job;
- run success ≠ data quality;
- freshness ≠ job completion;
- quality observation ≠ quality assessment;
- anomaly ≠ defect;
- correlation ≠ cause;
- root-cause hypothesis ≠ confirmed cause;
- classification ≠ authorization;
- policy metadata ≠ compliance;
- data lineage ≠ deployment lineage;
- current topology ≠ historical topology;
- business meaning ≠ physical schema;
- business owner ≠ technical owner.
