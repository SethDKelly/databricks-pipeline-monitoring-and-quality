# 003 — Foundational Terminology

This document establishes distinctions that must remain stable during discovery. The fuller glossary remains in [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem
The connected set of repositories, planned/realized changes, deployments, Databricks jobs/tasks/runs, data assets, dependencies, lineage relationships, governance metadata, health/quality evidence, and downstream consumers relevant to monitoring. Known entities may exist outside Monitoring Scope.

### Logical pipeline
A named data-processing responsibility that transforms or moves data for a purpose. A logical pipeline may span multiple jobs/tasks and is not automatically one repository or Databricks job.

### Pipeline dependency
A relationship in which one logical pipeline's timely/correct operation depends on another pipeline. This may be operational, data-based, or both.

### Repository
A source-control boundary. It preserves provenance but is not the product reasoning boundary.

## Change, execution, and deployment terms

### Change Intent
A provenance-bearing registered statement of an intended modification and its anticipated effects before the change is proven active/realized.

Change Intent is not Deployment, Observation, Expectation, realized Change, or cause. Anticipated effects are descriptive planned context unless separately established as normative Expectations.

### Job
A Databricks orchestration/execution definition. Exact mapping from logical pipeline to job is a discovery concern.

### Task
A unit of execution within a Databricks job.

### Run / execution instance
A time-bounded instance of actual job/task/logical-pipeline work established by execution evidence.

### Execution History
Historical continuity/lifecycle of actual execution instances. It does not synthesize expected-but-missing executions from absent telemetry.

### Code revision
A specific source-controlled version associated with deployment/pipeline definition.

### Deployment
A provenance-bearing record of attempted and/or active source/configuration state for a runtime target. Deployment attempt and activation are distinct.

Deployment activation does not prove that a Change Intent's anticipated effect occurred and does not prove healthy output.

### Deployment lineage/provenance
Relationships among repository, revision/configuration, deployment workflow/evidence, active runtime definition, and subsequent executions. It is distinct from data derivation Lineage.

## Data terms

### Data asset
A data object such as a table, view, Metric View, external/intermediate dataset, or other meaningful data product. A known asset is not necessarily inside Monitoring Scope.

### Consumer-facing data asset
A data asset intended for consumption outside the producing pipeline's internal processing boundary.

### Dataset state
Observable condition of a data asset at a time/interval, including freshness, volume, schema, distribution, and quality Observations.

### Upstream / Downstream
Upstream entities may influence another entity; downstream entities depend on or consume another entity. Reachability alone does not prove cause or confirmed impact.

## Monitoring and quality terms

### Expectation
A provenance-bearing normative assertion of what should be true/acceptable for a subject, dimension, context, and time.

A Change Intent may prompt an Expectation revision, but anticipated effects do not become normative automatically.

### Baseline
Descriptive reference behavior derived from comparable Observation evidence. A Baseline is not normative.

A Change Intent may register a **prospective comparability break**. That break becomes effective only when realization evidence establishes the new context. A post-change Baseline must be derived from post-change evidence, never from intended values.

### Observation
A provenance-bearing measured/retrieved fact. Observation does not declare health, anomaly, staleness, degradation, intent conformance, or cause. Missing evidence is not observed absence.

### Assessment
A dimension-scoped interpretation of Observation evidence against an explicit Expectation and/or comparable Baseline. Assessment preserves basis/history and does not establish root cause.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that freshness violates an applicable Expectation.

### Data quality
Degree to which data satisfies explicit Expectations relevant to intended use across applicable dimensions.

### Degradation
Meaningful worsening supported by explicit directional/normative interpretation. Baseline deviation or realized Change alone does not establish degradation.

## History, lineage, and reasoning terms

### Change
A provenance-bearing description of a realized difference/state transition established by evidence. Change may be planned or unplanned in context, but the Change record itself describes what actually occurred.

Change is not Change Intent, health judgment, intent-conformance judgment, or cause.

### Lineage
Typed, directed, temporal, provenance-bearing relationship semantics for tracing derivation/dependency/production/consumption. Planned topology is not active Lineage until realization evidence establishes it.

Lineage is naturally graph-shaped and must support graph-compatible traversal semantics; no graph-storage technology is selected in Phase 002.

### Data lineage
How data assets derive from/flow into other data assets.

### Operational dependency lineage
How pipelines/jobs/executions depend on other availability/execution conditions.

### Evidence ledger semantics
A cross-cutting product requirement that material historical assertions/events remain provenance-bearing, versioned/superseding, and reconstructable rather than invisibly overwritten.

This does not mean blockchain or any specific event-store technology.

### Effective/event time
When a condition was true or an event occurred in the modeled ecosystem.

### Recorded/knowledge time
When the monitoring ecosystem learned/recorded an assertion/event. It may differ from effective/event time because evidence can arrive late or be corrected.

### Root-cause hypothesis / Causal Claim
A proposed causal explanation supported to some degree by evidence but distinct from confirmed cause.

### Attribution / Confirmed cause
Attribution assigns contribution under uncertainty. Confirmed cause requires an agreed evidence/authority standard that is not yet fully defined.

### Impact
A known or plausible downstream effect; lineage reachability provides candidates, not proof of actual impact.

## Governance and policy terms

### Responsibility Assignment
A provenance-bearing assertion that a party bears a named responsibility for a subject/time/context. Responsibility is not universal authority or authorization.

### Technical owner / Business accountable party / Data steward
Distinct responsibility types; none is automatically authoritative for all metadata, policy, Expectation, or access decisions.

### Classification
Category membership under a named governance/sensitivity vocabulary; not Policy Context or authorization.

### Policy Context
Declared policy/handling applicability for subject/context/time; not access enforcement, legal interpretation, or compliance determination.

### Provenance
Where/when/by whom or what an assertion/fact/derivation was produced, including source and temporal context.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ authorization;
- pipeline ≠ repository ≠ Databricks job;
- Change Intent ≠ Deployment ≠ realized Change;
- anticipated effect ≠ normative Expectation;
- Deployment attempt ≠ activation;
- Deployment activation ≠ intended effect realized;
- run success ≠ freshness ≠ data quality;
- Expectation ≠ Baseline;
- planned value ≠ empirical Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- planned topology ≠ active Lineage;
- Lineage/reachability ≠ cause/confirmed impact;
- Change ≠ degradation ≠ cause;
- effective/event time ≠ recorded/knowledge time;
- Semantic Definition ≠ Responsibility Assignment;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- data Lineage ≠ deployment provenance;
- current topology ≠ historical topology.
