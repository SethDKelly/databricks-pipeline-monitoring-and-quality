# 006 — Integration Boundaries and Tooling Considerations

## Goal

Identify what information the framework needs from surrounding systems and where existing tools may already be authoritative, without choosing an architecture prematurely.

## Guiding principle

**Integrate before duplicating.**

The framework should avoid recreating governance, access-policy, lineage, deployment, or quality capabilities that are already trustworthy and sufficiently accessible elsewhere. It should instead determine how those capabilities can participate in a unified reasoning and reporting experience.

## Databricks

Databricks is central because the Spark ETL pipelines execute there and their datasets reside in the platform ecosystem.

Later discovery should examine relevant Databricks capabilities for:

- job/run state;
- task state;
- lineage;
- table and view metadata;
- Unity Catalog governance context;
- data profiling/metrics;
- Metric Views;
- DQX;
- audit/operational history;
- environment and deployment identity.

Metric Views and DQX are favored considerations, but their role should be determined against the product requirements rather than assumed in advance.

## Git repositories

Source code is distributed across multiple repositories. Later design must determine how the framework associates:

- a logical pipeline with one or more repositories;
- code versions with deployments;
- pipeline changes with the time data behavior changed;
- cross-repository dependencies;
- ownership information maintained in source control.

## GitHub Actions

GitHub Actions is part of the deployment lineage. The framework should eventually be able to reason across a chain such as:

**repository → code version → workflow/deployment → Databricks job/task configuration → run → produced data → downstream consumers**

The precise mechanics are deferred.

## Collibra

Collibra is available and may be relevant for:

- business glossary;
- stewardship;
- ownership;
- governance workflows;
- business definitions;
- catalog metadata.

The project should discover whether Collibra is authoritative for any of these concerns before deciding how strongly to depend on it.

## Immuta

Immuta is available and may be relevant for:

- policy metadata;
- access-policy context;
- sensitive-data classification;
- enforcement context.

The framework should not assume that access-policy enforcement and data-quality monitoring are the same concern. It should determine what policy evidence or metadata is useful for transparency and impact analysis.

## Integration design questions for later phases

- Which system is authoritative for each metadata category?
- Which facts are observed directly versus synchronized from another system?
- How are conflicting descriptions, owners, or classifications resolved?
- Which identifiers remain stable across systems?
- What historical information is available from each system?
- Which integrations are required for MVP versus optional enrichment?
- How does the system remain useful if Collibra or Immuta is absent?
- What data can safely be exposed to different user audiences?
- How are sensitive metadata and underlying sensitive values kept distinct?

## Non-goal at this stage

This document does not select APIs, eventing patterns, storage systems, polling intervals, streaming approaches, or specific schemas.
