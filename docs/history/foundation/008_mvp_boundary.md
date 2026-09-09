# 008 — Initial MVP Boundary

## MVP objective

Prove that the framework can turn a fragmented Databricks pipeline ecosystem into an evidence-grounded, historically aware, Lineage-aware explanation of pipeline/data health, planned/realized change, likely causal context, and downstream consequence for engineering and business users.

## Required MVP capabilities

### 1. Ecosystem inventory
Represent logical pipelines, repositories, Databricks jobs/tasks/runs, data assets, cross-pipeline dependencies, and representative consumers.

### 2. Planned-change registration and realization context
For representative pipelines, register Change Intent with target, anticipated effects, planned timing/context, provenance, and monitoring implications. Associate intent to realizing Deployment evidence when possible without requiring a specific ticket/PR system.

Demonstrate at least one structural planned change that triggers prospective Expectation review and Baseline comparability handling.

### 3. Deployment/run association
Connect repository/revision/configuration → Deployment attempt/activation → execution → produced data asset for representative pipelines.

### 4. Freshness/staleness
Answer when relevant data last updated, what normative behavior is expected, whether it violates that Expectation, and how it compares descriptively with history.

### 5. Core data-quality Observations
Track a small high-value set: row quantity, completeness/null measures, uniqueness where relevant, schema, selected domain checks, and join/match behavior for A+B→C.

### 6. Historical comparison and realized Change
Show how evidence changes over time; distinguish planned intent from realized Change and Baseline atypicality from normative violation.

### 7. Typed temporal Lineage
Support upstream/downstream historical traversal across enough topology to answer A+B→C and cross-repository scenarios. Semantics are graph-compatible; graph technology is deferred.

### 8. Evidence-grounded Investigation and Causal Claims
For degradation/atypicality/unexpected planned-change outcome, organize Observations, Assessments, upstream evidence, Change Intent, Deployment/config/schema/Lineage/Change context, competing Causal Claims, supporting/contradicting evidence, and known unknowns.

MVP must support unresolved and multiple-contributor outcomes; it need not automatically confirm root cause.

### 9. Downstream Impact refinement
Distinguish downstream candidate/reachability from actual exposure/consumption, observed downstream effect, and evidenced business consequence for representative consumers.

### 10. Governance/semantic context
Expose representative Semantic Definition, Responsibility Assignments, criticality/Classification/Policy Context, and provenance.

### 11. Human context
Support attributed Annotation for representative Investigation context without using Annotation as a substitute for structured Change Intent, Expectation, responsibility, or causal confirmation.

### 12. Business-facing Explanation/question interaction
Support questions such as: Is it healthy/stale? What changed? Was a relevant change planned? What became active? Did realized behavior match the expected operating context? Which causal claims are supported or unresolved? Which downstream assets are merely reachable versus actually exposed/affected? Who is responsible? What evidence supports this?

Business and engineering views must remain evidence-consistent and authorization-aware.

### 13. Historical knowledge reconstruction
MVP history must preserve enough version/supersession/correction information to reconstruct what was intended, active, executed, connected, expected, baselined, observed, assessed, investigated, believed, and explained at a representative incident time.

Demonstrate `what was known then` separately from a later retrospective view when later evidence materially changes the conclusion.

This is behavioral; no specific ledger/event-store architecture is required.

## MVP proof scenarios

### Scenario A — Stale upstream
Downstream execution succeeds but upstream input violates freshness Expectation.

### Scenario B — Join-volume degradation
C falls because A, B, join behavior, or multiple contributors change; root cause may remain unresolved.

### Scenario C — Successful run, poor quality
Execution succeeds while a quality Expectation fails.

### Scenario D — Deployment-correlated change
Data changes after activation; product describes chronology/evidence and Causal Claim status without converting correlation into cause.

### Scenario E — Planned structural change with valid outcome
A filter Change Intent predicts lower C volume, post-change Expectation is explicitly revised, old Baseline transitions after realization, and new Baseline derives later from post-change evidence.

### Scenario F — Planned change with unintended violation
Expected volume shift occurs but another quality dimension violates its Expectation. Planned context does not suppress failure or predetermine cause.

### Scenario G — Unregistered change
A source/data/topology Change occurs with no registered intent; monitoring remains effective and labels planned context unavailable.

### Scenario H — Downstream reachability versus exposure
A report is reachable through Lineage but has not consumed affected data; another consumer is exposed. They are not given the same Impact status.

### Scenario I — Multiple contributing causes
B volume reduction and join-key quality both contribute plausibly to C degradation; Investigation preserves both Causal Claims and evidence.

### Scenario J — Historical knowledge correction
The initial leading cause is later weakened by evidence discovered after the incident. Contemporaneous and retrospective Explanations remain distinguishable.

### Scenario K — Policy-aware business explanation
An affected sensitive asset and restricted downstream consumer are represented at safe abstraction levels without raw-data or metadata leakage.

## Explicitly outside initial MVP

Autonomous remediation/rollback; automated code fixes; universal platform/pattern support; every DQ dimension/governance tool; replacing source systems; legal compliance certification; broad raw-data exploration; unrestricted row samples; guaranteed fully automatic causal confirmation; quantitative causal attribution unless later required; perfect column Lineage; write-back/remediation workflows; mandatory graph database; mandatory event-sourcing/blockchain/ledger implementation; mandatory LLM explanation generation.

## MVP exit test

A representative business analyst and data engineer can inspect the same incident/planned-change outcome and receive appropriately detailed but evidence-consistent Explanations including intent, active Deployment, execution, historical topology, Observations/Assessments, realized Changes, competing causal evidence, downstream reachability/exposure/consequence, responsibility, policy context, and uncertainty.
