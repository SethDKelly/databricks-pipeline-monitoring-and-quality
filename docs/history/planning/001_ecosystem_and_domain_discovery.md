# 001 — Ecosystem and Domain Discovery

## Goal

Develop a shared model of the pipeline ecosystem before selecting technical implementation patterns.

The key design constraint is that operational truth is distributed: code lives in multiple repositories, GitHub Actions performs deployment, jobs execute in Databricks, datasets depend on other datasets, and business consumers sit downstream of those outputs.

## Discovery themes

### 1. Pipeline identity

Determine what uniquely identifies a pipeline across:

- source repository;
- branch/tag/commit or release;
- GitHub Actions deployment;
- Databricks job and task structure;
- environment;
- output datasets;
- owning team.

The project should avoid assuming that “repository,” “job,” and “pipeline” are interchangeable concepts.

### 2. Dependency identity

Discover how dependencies are expressed today:

- dataset-to-dataset;
- job-to-job;
- pipeline-to-pipeline;
- schedule or trigger dependencies;
- implicit dependencies through shared tables or files;
- cross-repository dependencies;
- external-source dependencies.

A dependency used for scheduling may differ from a lineage relationship used for data reasoning. Both may matter.

### 3. Data asset identity

Determine which assets need to participate in monitoring and reasoning:

- tables;
- views;
- metric views;
- files or external datasets;
- intermediate transformations;
- consumer-facing data products;
- dashboards/reports/semantic models where useful.

### 4. Change identity

Establish what kinds of change matter operationally:

- source-data movement;
- row-count movement;
- distribution shifts;
- null-rate or uniqueness changes;
- schema changes;
- transformation logic changes;
- deployment changes;
- schedule changes;
- job configuration changes;
- ownership or semantic changes;
- policy classification changes.

### 5. Consumer identity

Identify downstream consumers broadly enough to support impact analysis. A consumer may be:

- another table or pipeline;
- a metric;
- a dashboard or report;
- a model or application;
- an analyst workflow;
- an externally delivered extract;
- a business process.

## Questions the domain model must support

- Which repository and deployment produced this Databricks job version?
- Which data assets did that run read and write?
- Which upstream pipelines produced those inputs?
- Which downstream assets depend on this output?
- Which dependency crosses repository boundaries?
- Which owner is responsible for each part of the chain?
- Which semantics or policy classifications apply at each asset?
- Which relationships are observed versus declared?
- Which relationships are current versus historical?

## Important distinction: operational lineage and data lineage

The project should explicitly investigate at least two related but different forms of lineage:

**Operational/deployment lineage** connects source code, a code version, GitHub Actions deployment activity, Databricks job/task configuration, and job runs.

**Data lineage** connects inputs, transformations, outputs, and downstream consumers.

Root-cause analysis may require both. A table changed because an upstream source changed is a different explanation from a table changing immediately after transformation code was deployed, even if both produce the same downstream symptom.

## Historical topology

The ecosystem itself changes. Pipelines are added, renamed, split, merged, migrated, or retired. Dependencies and ownership also change.

Discovery should therefore consider whether the system must answer historical questions such as:

- What was upstream of this table when the incident began?
- Which code version and owner applied at that time?
- Was a downstream consumer newly introduced before the issue?

The likely answer is yes, but the required degree of historical fidelity should be established before implementation.
