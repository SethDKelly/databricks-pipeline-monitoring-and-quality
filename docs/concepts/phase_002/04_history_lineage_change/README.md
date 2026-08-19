# Group 04 — History, Lineage & Change

**Status:** Review complete — concepts accepted

## Goal

Preserve the historical, topological, and change-context evidence needed to answer **what was intended**, **what became active**, **what ran**, **what depended on what**, and **what actually changed** without converting chronology or topology into causation.

## Accepted concepts

- [Change Intent](change_intent.md)
- [Execution History](execution_history.md)
- [Deployment](deployment.md)
- [Lineage](lineage.md)
- [Change](change.md)

## Boundary decisions

### 1. Planned intent is separate from realized change

A registered plan to modify a pipeline is not the same fact as a change that actually occurred. **Change Intent** therefore records intended modifications and anticipated effects before activation; **Change** records realized differences or transitions established from evidence.

This distinction supports all of these outcomes without ambiguity:

- a planned change activates and behaves as intended;
- a planned change activates but produces unintended side effects;
- a planned change activates but differs materially from its anticipated magnitude/direction;
- a Change Intent is registered but never activated;
- a Deployment/Change occurs without registered intent;
- a health violation occurs with no relevant deployment or realized change.

### 2. Planned change can affect Baseline comparability without rewriting history

A Change Intent can pre-register that an existing Baseline is expected to become non-comparable if the intended structural change becomes active. The Baseline remains valid for its existing context until realization evidence establishes the transition.

A post-change Baseline is not manufactured from the planned value. It is derived from sufficient comparable post-change Observations. When immediate post-change validation is required, an explicit prospective **Expectation** can define acceptable post-change behavior from the activation boundary.

### 3. Deployment means activation evidence, not intent or cause

Deployment records attempts, activation, target/revision/configuration context, and supersession. It may realize one or more Change Intents, but a successful deployment does not prove that the intended data behavior occurred or that a later degradation was caused by the deployment.

### 4. Execution History records what actually ran

Execution History owns execution-instance continuity and lifecycle history. It does not own schedules/requirements, data-health conclusions, or deployment intent. Expected-but-never-started work requires Expectation plus sufficient absence evidence; missing telemetry cannot create a fictional missing run.

### 5. Lineage is typed, temporal, provenance-bearing, and naturally graph-shaped

Lineage relationships are directed/typed and have effective-time/provenance semantics. Planned topology belongs to Change Intent until evidence establishes that the topology actually changed.

The conceptual model is deliberately **graph-compatible** because ecosystem reasoning traverses connected entities and relationships. This does **not** select a graph database, graph processing framework, or graph API during Phase 002.

### 6. Change is descriptive and realized

Change describes differences/transitions that evidence establishes actually occurred. It may describe code/configuration, schema, volume, distribution, topology, semantics, responsibility, Expectation, Classification, Policy Context, or other material state changes.

Change does not decide whether the result is good/bad, intended/unintended, or causal. Those interpretations require synchronization with Change Intent, Assessment, and later Investigation/Causal Claim behavior.

### 7. Ledger-like historical semantics are a product requirement, not a storage selection

The monitoring ecosystem should behave like an evidence ledger across material historical facts: Change Intents, Deployments, executions, lineage relationships, Observations, Expectations, Baselines, Assessments, realized Changes, and later causal/annotation records should be provenance-bearing and historically reconstructable.

Corrections/supersessions should append or link new state rather than invisibly rewriting prior knowledge. Where material, the product must distinguish:

- **effective/event time** — when a condition was true or occurred;
- **recorded/knowledge time** — when the monitoring ecosystem learned or recorded it.

This is a semantic requirement. Phase 002 does not select blockchain, event sourcing, append-only database technology, temporal tables, or any other persistence mechanism.

## Planned-change / health outcome matrix

| Registered intent | Realized change | Assessment outcome | Interpretation available at this stage |
|---|---|---|---|
| Yes | Consistent with intent | Meets post-change Expectation | Planned change appears to have produced acceptable behavior; no causal overclaim required. |
| Yes | Consistent with some intent | Another dimension violates Expectation | Planned change context explains an expected difference but does not excuse an unintended quality failure. |
| Yes | Materially differs from intent | Violates/atypical/unresolved | Evidence shows the realized behavior did not match the registered plan; cause remains for Investigation. |
| Yes | None established | Existing behavior unchanged or unknown | Intent was not proven active; current Baseline/Expectation context remains unless other evidence changes it. |
| No | Yes | Any | The product can still monitor and investigate; planned context is unavailable, not proof of improper change. |
| No | No relevant change | Violation/atypical | Degradation can occur without deployment/change, requiring upstream/data/business investigation. |

## Scenario review

### S-01 — Join-volume degradation

Pass. A, B, and C retain typed lineage. If a filter Change Intent predicts lower C volume, the intent can mark the old volume Baseline prospectively non-comparable after activation. Deployment and Execution History establish what became active/ran; Observations establish the new volume; Change describes the realized difference; Assessment determines whether post-change Expectations are met and/or behavior is atypical. None of these alone asserts root cause.

### S-02 — Stale upstream with successful downstream execution

Pass. Execution History can show a downstream run succeeded while lineage identifies its upstream dependency. Observation/Assessment separately establish stale input. No deployment or Change is required for the violation to exist.

### S-03 — Deployment-correlated shift

Pass. Change Intent, Deployment activation, run sequence, realized Change, and Assessment can be aligned temporally. Correlation and intent-consistency can be shown without converting the deployment into a confirmed cause.

### S-04 — Cross-repository dependency

Pass. Entity Identity and typed Lineage cross repository boundaries. Change Intent/Deployment remain provenance-linked to their source repositories without making repository the reasoning boundary.

### S-05 — Conflicting governance metadata

Pass. Governance changes can be represented as realized Change with source provenance while underlying Group 02 conflicts remain conflicts. Change does not select metadata authority.

### S-06 — Policy-sensitive explanation

Pass. Lineage, Change Intent, Deployment, and Change can be represented at an authorized abstraction level. A viewer may learn that a restricted planned/upstream change affected the analysis without receiving sensitive implementation details.

### S-07 — Historical replay

Pass. Effective/event time, knowledge time, version/supersession history, execution/deployment activation, historical lineage, Change Intent versions, and realized Change evidence allow reconstruction of what was planned, known, active, connected, and observed at incident time.

## Additional adversarial scenarios

### Planned filter, valid lower volume
A filter is intentionally added to C. The old 20M-row Baseline is flagged prospectively, a post-change Expectation is explicitly revised, the Deployment activates, and C settles near 14M while satisfying the new criterion. A new Baseline is derived later from post-change evidence. The system does not call the valid structural break a degradation merely because it differs from old history.

### Planned filter, unintended data loss
The filter is intended to remove one cohort but also drops valid records from another. C's total decrease was partly anticipated, yet another completeness/reconciliation Expectation fails. The registered intent cannot suppress the separate violation.

### Change with no deployment
An upstream source changes its feed semantics without any monitored code deployment. Lineage/Observation/Change can reveal the shift; lack of a Deployment does not force the product to conclude there was no change.

### Deployment with no meaningful data change
A refactor is deployed but observed data behavior remains comparable and Expectations continue to pass. Deployment history remains useful evidence, but it is not automatically a data Change or causal event.

## Deferred questions

- minimum Change Intent fields and anticipated-effect dimensions for MVP;
- source/authority rules for registering planned changes;
- precise linkage to pull requests, tickets, configuration changes, or release metadata;
- minimal Lineage relationship taxonomy for MVP;
- execution-instance reconstruction semantics when one logical pipeline spans several jobs/tasks;
- how much event-time versus knowledge-time history MVP must expose directly;
- whether intent-to-realization conformance deserves a later standalone concept;
- which graph/temporal/ledger persistence patterns best realize the accepted semantics during technical design.

## Group exit gate

**Satisfied.** The ecosystem can reconstruct planned intent, deployment activation, execution, historical typed topology, and realized changes at a relevant time while preserving the separation among intention, fact, health interpretation, and cause. Ledger-like historical semantics and graph-compatible relationship semantics are explicit product constraints without prematurely selecting storage architecture.

The next review group is **Group 05 — Investigation, Impact & Explanation**.
