# 008 — Initial MVP Boundary

## MVP objective

Prove that the framework can turn a fragmented Databricks pipeline ecosystem into an evidence-grounded, historically aware, lineage-aware explanation of pipeline/data health for engineering and business users.

## Required MVP capabilities

### 1. Ecosystem inventory
Represent logical pipelines, repositories, Databricks jobs/tasks/runs, data assets, cross-pipeline dependencies, and representative consumers.

### 2. Planned-change registration and realization context
For representative pipelines, register a **Change Intent** with target, anticipated effects, planned timing/context, provenance, and monitoring implications. Associate intent to realizing Deployment evidence when possible without requiring a specific ticket/PR system.

The MVP should demonstrate at least one structural planned change that can trigger prospective Expectation review and Baseline comparability handling.

### 3. Deployment/run association
Connect repository/revision/configuration → deployment attempt/activation → execution → produced data asset for representative pipelines. Exact technical realization is deferred.

### 4. Freshness/staleness
Answer when relevant data last updated, what normative behavior is expected, whether it violates that Expectation, and how it compares descriptively with history.

### 5. Core data-quality Observations
Track a small high-value set: row quantity, completeness/null measures, uniqueness where relevant, schema, selected domain checks, and join/match behavior for the canonical scenario.

### 6. Historical comparison and realized Change
Show how evidence changes over time; distinguish planned intent from realized Change and distinguish Baseline atypicality from normative violation.

### 7. Typed temporal Lineage
Support upstream/downstream historical traversal across enough ecosystem topology to answer A+B→C and cross-repository scenarios. Product semantics must be graph-compatible; graph technology is deferred.

### 8. Evidence-grounded investigation
For degradation/atypicality, present Observations, Assessments, upstream evidence, Change Intent, recent Deployment/config/schema/Lineage/Change context, downstream candidates, known unknowns, and provenance.

### 9. Governance/semantic context
Expose representative semantic meaning, Responsibility Assignments, criticality/classification/Policy Context, and provenance.

### 10. Business-facing explanation/question interaction
Support questions such as: Is it healthy/stale? What changed? Was a relevant change planned? What became active? Did realized behavior match the expected operating context? Where are likely origin candidates? What downstream assets may be affected? Who is responsible? What evidence supports this?

### 11. Ledger-like historical reconstruction
MVP history must preserve enough version/supersession/correction information to reconstruct what was intended, active, executed, connected, observed, expected, baselined, assessed, and changed at a representative incident time.

This is a behavioral requirement; no specific ledger/event-store architecture is required.

## MVP proof scenarios

### Scenario A — Stale upstream
Downstream execution succeeds but upstream input violates freshness Expectation.

### Scenario B — Join-volume degradation
C falls because A, B, join behavior, or some combination changes.

### Scenario C — Successful run, poor quality
Execution succeeds while a quality Expectation fails.

### Scenario D — Deployment-correlated change
Data changes after activation; product describes chronology/evidence without overclaiming cause.

### Scenario E — Planned structural change with valid outcome
A filter Change Intent predicts lower C volume, post-change Expectation is explicitly revised, old Baseline transitions after realization, and new Baseline derives later from post-change evidence.

### Scenario F — Planned change with unintended violation
Expected volume shift occurs but another quality dimension violates its Expectation. Planned context does not suppress the failure.

### Scenario G — Unregistered change
A source/data/topology Change occurs with no registered intent; monitoring remains effective and labels planned context unavailable.

### Scenario H — Business/policy-aware downstream impact
A degraded table feeds business consumers; explanation respects governance/policy visibility and identifies responsible parties.

## Explicitly outside initial MVP

Autonomous remediation/rollback; automated code fixes; universal platform/pattern support; every DQ dimension/governance tool; replacing source systems; legal compliance certification; broad raw-data exploration; unrestricted row samples; fully automatic causal inference; perfect column lineage; write-back/remediation workflows; mandatory graph database; mandatory event-sourcing/blockchain/ledger implementation.

## MVP exit test

A representative business analyst and data engineer can inspect the same incident/planned-change outcome and receive appropriately detailed but evidence-consistent explanations, including intent, active deployment, execution, historical topology, Observations/Assessments, realized changes, upstream origin candidates, downstream impact, responsibility, and uncertainty.
