# Phase 002 — Concept Specifications

**Status:** Active — Groups 01–04 accepted; Group 05 next

## Purpose

Phase 002 turns the Phase 001 candidate catalog into explicit Concept Design specifications without mapping concepts to services, schemas, APIs, Databricks objects, graph databases, ledger/event-store technologies, or vendor products.

## Strategic review order

| Group | Theme | Concepts | Status |
|---|---|---|---|
| 01 | Scope & Identity | Monitoring Scope, Entity Identity | **Accepted** |
| 02 | Semantics, Governance & Policy | Semantic Definition, Responsibility Assignment, Classification, Policy Context | **Accepted** |
| 03 | Health Evaluation | Expectation, Baseline, Observation, Assessment | **Accepted** |
| 04 | History, Lineage & Change | Change Intent, Execution History, Deployment, Lineage, Change | **Accepted** |
| 05 | Investigation, Impact & Explanation | Investigation, Causal Claim, Impact, Annotation, Explanation | **Next** |

Review order is a design dependency, not an implementation dependency.

## Accepted Group 04 refinements

- **Change Intent** is added as a separate concept because planned intent has different truth conditions from realized Change.
- `Deployment Record` → **Deployment**: attempt/activation/configuration history is behavior, not merely a stored record.
- **Execution History** owns actual execution-instance continuity, not schedule expectations or data health.
- **Lineage** is typed, temporal, provenance-bearing, historical, and graph-compatible; graph storage/query technology remains deferred.
- **Change** describes realized differences/state transitions and does not own intent, health, or causation.
- Change Intent can pre-register a prospective Baseline comparability break, but activation/realized Change evidence is needed before the break becomes effective.
- planned values never become Baseline values; post-change Baselines require empirical post-change Observations.
- prospective post-change normative behavior belongs to explicit Expectation establishment/revision.
- ledger-like append/supersede historical semantics are accepted as a cross-cutting product requirement; persistence technology remains deferred.
- effective/event time and recorded/knowledge time must remain distinguishable where historical interpretation depends on when the system learned a fact.

## Cross-cutting distinctions that must survive every group

- monitoring scope ≠ ecosystem existence ≠ authorization;
- identity ≠ name ≠ replacement/succession;
- semantic definition ≠ responsibility assignment;
- classification ≠ policy context ≠ authorization ≠ compliance;
- expectation ≠ baseline;
- planned/anticipated effect ≠ normative expectation;
- observation ≠ assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- Change Intent ≠ Deployment ≠ realized Change;
- Deployment activation ≠ intended effect realized;
- execution success ≠ freshness ≠ data quality;
- planned topology ≠ active Lineage;
- lineage/reachability ≠ cause/confirmed impact;
- change ≠ degradation ≠ cause;
- event/effective time ≠ recorded/knowledge time;
- hypothesis/causal claim ≠ confirmed cause;
- explanation ≠ independent truth source.

## Group workflow

Each group should validate purposes, challenge names/boundaries, test state/actions, preserve ambiguity/security/provenance, run canonical/adversarial scenarios, and update catalog/glossary/decisions before advancing.

## Required scenario set

### S-01 — Join-volume degradation
C is produced from A+B and falls materially. The product must distinguish atypicality, normative violation, planned structural change, realized change, upstream source change, join behavior, and unresolved cause.

### S-02 — Stale upstream with successful downstream execution
Execution success and freshness remain separate; no deployment/change is required for staleness.

### S-03 — Deployment-correlated shift
Registered intent, Deployment activation, execution, realized Change, and Assessment can be aligned without asserting deployment causation.

### S-04 — Cross-repository dependency
Repository boundaries preserve provenance but do not break Entity Identity/Lineage reasoning.

### S-05 — Conflicting governance metadata
Conflicts remain provenance-bearing until authority is defined.

### S-06 — Policy-sensitive explanation
Authorized abstraction can expose material context without restricted details/raw data.

### S-07 — Historical replay
The product can reconstruct what was intended, known, active, executed, connected, expected, baselined, observed, assessed, governed, and changed at an earlier time.

### S-08 — Planned structural change
A registered filter is expected to alter C's population. The product can transition Expectation/Baseline context without treating the plan as observed fact and can still identify unintended post-change violations.

## Phase 002 exit gate

Phase 002 is complete when every retained concept is reviewed; boundaries/rationale are recorded; the catalog/glossary agree; Phase 003 synchronizations are identifiable; no concept depends semantically on a selected implementation architecture/vendor; and all canonical scenarios are expressible without hidden functionality.
