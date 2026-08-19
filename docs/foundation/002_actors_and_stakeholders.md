# 002 — Actors and Stakeholders

## Purpose

Identify who interacts with or materially constrains the monitoring ecosystem. Actors are defined by goals and authority, not by UI screens or organizational titles alone.

## Human actors

### Data engineer / pipeline maintainer

**Goals**

- know whether owned pipelines are operating normally;
- identify where a data-quality degradation began;
- relate anomalous data behavior to upstream inputs, code, configuration, and deployment history;
- understand downstream impact before changing or rerunning a pipeline;
- provide evidence when resolving an incident.

**Authority considerations**

May be able to change pipeline code or jobs, but should not automatically be able to change governance classifications, business definitions, or compliance determinations.

### Data platform engineer / platform operator

**Goals**

- understand ecosystem-level health and recurring failure modes;
- maintain platform-wide monitoring and metadata integrations;
- distinguish platform problems from pipeline/data problems;
- support safe, scalable onboarding of many repositories and jobs.

**Authority considerations**

Platform administration must not automatically confer unrestricted access to sensitive data values or business-policy decisions.

### Business analyst / data consumer

**Goals**

- know whether a dataset, metric, or report is trustworthy and current;
- understand what changed and whether a business conclusion may be affected;
- receive an understandable explanation of the likely source and affected scope;
- know who owns the problem and whether it is resolved.

**Authority considerations**

A business-facing explanation should reveal only metadata and evidence the viewer is authorized to see. Monitoring must not become a back door to restricted data.

### Data owner

**Goals**

- establish accountability for business use and fitness of important data assets;
- understand quality and freshness risk to business processes;
- approve or participate in expectations appropriate to the asset's purpose.

### Data steward / governance steward

**Goals**

- maintain or validate business definitions, classifications, criticality, stewardship, and quality semantics;
- understand where governance metadata is missing, conflicting, or stale;
- trace which system is authoritative for a definition or classification.

### Security / privacy / compliance stakeholder

**Goals**

- understand what sensitive-data categories and handling rules may apply;
- verify that monitoring does not unnecessarily expose restricted values;
- review evidence of policy/control operation without mistaking monitoring metadata for compliance certification;
- understand access, auditability, and metadata-provenance boundaries.

### Incident responder / on-call engineer

**Goals**

- move rapidly from symptom to probable origin;
- identify downstream blast radius;
- separate known evidence from hypotheses;
- understand ownership and recent changes;
- produce a durable incident explanation.

This may be the same person as a pipeline maintainer, but the incident-response role has a distinct time-sensitive goal.

### Monitoring framework administrator

**Goals**

- configure monitored scope and integrations;
- manage system-level policies and access appropriate to the framework;
- preserve metadata provenance and operational integrity.

This role must not be defined as an omnipotent bypass around source-system authorization.

## External system actors

External systems participate in the product without necessarily being implementation dependencies.

### Git repository

Represents source-controlled pipeline definitions, configuration, tests, ownership hints, and code history across many repositories.

### GitHub Actions

Represents deployment workflow and evidence connecting a code revision to a Databricks deployment.

### Databricks

Represents the execution environment and an authoritative source for jobs/tasks/runs, data assets, platform lineage, catalog metadata, and Databricks-native monitoring/quality capabilities where available.

### Collibra

Potential authoritative or enriching source for business glossary, stewardship, ownership, catalog descriptions, and governance workflows. Optional until authority is established.

### Immuta

Potential authoritative or enriching source for policy, sensitive-data classification, and access-control context. Optional until authority is established.

### Downstream analytical system

A report, dashboard, metric product, application, export, or business process that consumes monitored data and may be affected by degradation.

## Actor design rules

1. Do not assume one person owns all meanings of an asset.
2. Technical ownership, business ownership, stewardship, and policy authority are distinct.
3. Administrative platform power does not imply permission to see raw sensitive values.
4. Answers should be audience-aware but evidence-consistent.
5. Source systems may be actors with independent authority; synchronized metadata retains provenance.
6. Actor definitions describe goals and authority, not proposed UI roles or IAM implementation.

## Open actor questions

- Which role may create or change a quality expectation?
- Who may declare an anomaly expected versus unresolved?
- Who may confirm a root cause?
- Who owns cross-repository dependencies with no single pipeline owner?
- Which business consumers need direct product access versus generated reports?
- Which policy classifications may be visible when the underlying asset is not accessible?
