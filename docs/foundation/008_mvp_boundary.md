# 008 — Initial MVP Boundary

## MVP objective

Prove that the framework can turn a fragmented Databricks pipeline ecosystem into an **evidence-grounded, historically aware, lineage-aware explanation of pipeline/data health** for both engineering and business users.

The MVP should optimize for one coherent end-to-end reasoning experience rather than maximal integration breadth.

## Required MVP capabilities

### 1. Ecosystem inventory

Represent a useful monitored scope spanning:

- logical pipelines;
- Git repositories;
- Databricks jobs/tasks;
- runs;
- produced/consumed data assets;
- cross-pipeline dependencies;
- basic downstream consumers where known.

### 2. Deployment/run association

For representative pipelines, connect:

**repository → code revision → GitHub Actions deployment → Databricks definition/run → produced data asset**

The exact technical method is deferred.

### 3. Freshness/staleness

Answer for monitored assets:

- when the relevant pipeline/data last updated;
- what update behavior is expected;
- whether the asset is currently stale or late;
- how that state compares with recent history.

### 4. Core data-quality observations

Track a deliberately small but high-value set of quality signals such as:

- row/record quantity;
- null/completeness measures for selected critical fields;
- uniqueness where relevant;
- schema change;
- selected domain checks;
- join/match behavior for at least the canonical join scenario.

DQX is strongly favored for evaluation where it maps cleanly to these needs.

### 5. Historical trend and change detection

Show how health/quality measures change over time and identify when a significant degradation begins.

The first version does not need advanced machine learning if explicit expectations, baselines, and comparisons are sufficient.

### 6. Typed lineage and dependency paths

Support upstream/downstream reasoning across enough of the ecosystem to answer the canonical Table A + Table B → Table C scenario.

### 7. Evidence-grounded investigation

For a degraded output, present:

- relevant observations;
- upstream comparisons;
- recent deployment/config/schema changes where available;
- candidate explanations;
- downstream impact;
- known unknowns;
- evidence references/provenance.

### 8. Governance and semantic context

For representative monitored assets, expose:

- description/business meaning;
- technical owner;
- business owner/steward where available;
- criticality if available;
- PII/PHI or other classification context when available;
- provenance of those facts.

Collibra/Immuta integration is optional for MVP unless discovery establishes them as the only practical authoritative source for a required fact.

### 9. Business-facing explanation

Produce a concise explanation suitable for a business analyst while retaining a path to deeper technical evidence.

### 10. Question-oriented interaction

The MVP must support the product's question model, even if the first implementation uses a constrained interface rather than a fully open-ended conversational system.

The product should be able to answer at least:

- Is this pipeline/data asset healthy?
- Is it stale?
- What changed?
- When did it change?
- Where is the likely degradation source?
- What downstream assets may be affected?
- Who owns it?
- What evidence supports that explanation?

## MVP proof scenarios

### Scenario A — Stale upstream

A downstream asset is late because an upstream pipeline did not refresh on time.

### Scenario B — Join-volume degradation

Table C falls materially because A, B, join match behavior, or some combination changes.

### Scenario C — Successful run, poor quality

A Databricks job succeeds but a key completeness/domain-quality measure degrades.

### Scenario D — Deployment-correlated change

A data change begins after a deployment, with the system clearly describing correlation and evidence without asserting causality beyond support.

### Scenario E — Business impact

A degraded table feeds a Metric View/report, and the business-facing explanation identifies potential downstream impact and owner.

### Scenario F — Policy-aware visibility

An affected asset has PII/PHI classification context, and the monitoring surface communicates the classification without exposing restricted values.

## Explicitly outside the initial MVP

- autonomous remediation or rollback;
- automated code fixes;
- universal support for every Spark/Databricks pipeline pattern;
- every possible data-quality dimension;
- every enterprise governance tool;
- replacing Collibra, Immuta, Databricks, or GitHub;
- legal/compliance certification;
- broad raw-data exploration;
- unrestricted row-level samples in the monitoring store;
- enterprise-grade multi-platform abstraction beyond what is needed to preserve concept boundaries;
- sophisticated predictive ML if transparent rules/baselines can prove the product first;
- fully automatic causal inference;
- perfect column-level lineage for all workloads if source evidence cannot reliably provide it;
- write-back/remediation workflows into production systems until safety/authority semantics are designed.

## MVP exit test

The MVP is successful when a representative business analyst and data engineer can look at the same degradation and receive different levels of detail but the **same evidence-grounded explanation**, including upstream origin candidates, downstream impact, time of onset, ownership, and uncertainty.
