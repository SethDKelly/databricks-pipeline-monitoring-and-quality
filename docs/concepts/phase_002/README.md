# Phase 002 — Concept Specifications

**Status:** **Complete — Groups 01–05 accepted; two explicit post-exit addenda accepted during Phase 003 preparation.**

## Purpose

Phase 002 turned the Phase 001 discovery catalog into explicit, implementation-neutral Concept Design specifications. The concepts define product behavior and truth boundaries without mapping them to services, schemas, APIs, Databricks objects, graph databases, ledger/event-store technologies, IAM schemes, language/framework choices, or vendor products.

The original Phase 002 review completed with 20 concepts. Later Phase 003 work exposed two independently motivated behaviors that could not be cleanly owned by those concepts. Phase 002 was therefore narrowly reopened through explicit addenda while preserving the original exit as historical truth.

## Accepted concept groups

| Group | Theme | Accepted concepts | Status |
|---|---|---|---|
| 01 | Scope & Identity | Monitoring Scope, Entity Identity | **Accepted** |
| 02 | Semantics, Governance & Policy | Semantic Definition, Responsibility Assignment, Classification, Policy Context | **Accepted** |
| 03 | Health Evaluation | Expectation, Baseline, Observation, Assessment | **Accepted** |
| 04 | History, Lineage & Change | Change Intent, Execution History, Deployment, Lineage, Change | **Accepted** |
| 05 | Investigation, Impact & Explanation | Investigation, Causal Claim, Impact, Annotation, Explanation | **Accepted** |

## Accepted post-exit addenda

- **Propagation Safeguard** — protective proposed/active/released hold or quarantine state for a defined data output, execution context, propagation boundary, environment/cohort, or consumer set. It does not own health Assessment, Investigation, causal truth, authorization, or implementation enforcement mechanics.
- **Capability Authorization** — provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time. It separates raw-data read, metadata/health visibility, Lineage/RCA participation, operational job authority, safeguard authority, and other capability categories without selecting an IAM/enforcement implementation.

**22 concepts are currently accepted.**

Review order was a design dependency, not an implementation dependency. Concepts remain independently motivated and compose through synchronizations.

## Accepted boundary refinements

### Group 01
- Monitoring Scope is monitoring responsibility, not authorization.
- Entity Identity is ecosystem-wide and distinct from replacement/succession.

### Group 02
- Semantic Definition is facet/context/provenance/time-aware.
- Responsibility Assignment replaces overloaded Ownership and is not universal authority or authorization.
- Classification is categorical metadata, separate from Policy Context, authorization, and compliance.
- Synchronization order never silently becomes governance authority.

### Group 03
- Expectation is normative; Baseline is descriptive.
- Observation is provenance-bearing fact; Assessment is interpretation against explicit normative/comparative basis.
- Missing telemetry is not observed absence.
- Typical is not automatically healthy; atypical is not automatically degraded.
- Health is dimension-scoped by default.

### Group 04
- Change Intent is separate from realized Change.
- Deployment attempt/activation/active state/supersession are distinct from intended effect.
- Planned values never become empirical Baselines.
- Lineage is typed, directed, temporal, provenance-bearing, graph-compatible, and not causal proof.
- Material history follows ledger-like append/supersede/correction semantics.

### Group 05
- Investigation organizes inquiry; Causal Claim owns causal propositions.
- Correlation, Lineage, Deployment timing, realized Change, and intent consistency cannot silently become confirmed causation.
- Impact separates reachability, exposure, observed effect, and business consequence.
- Annotation is attributed context rather than a catch-all truth mechanism.
- Explanation is authorization/time-aware communication over source concept state and does not become an independent truth source.

### Post-exit addendum — Propagation Safeguard
- Protective propagation state could not be owned by Assessment, Investigation, Impact, or Policy Context.
- A violated Expectation or Baseline atypicality can motivate safeguard review but does not automatically activate quarantine.
- `proposed` ≠ `active`; quarantine ≠ proof of defect; release ≠ proof of health.
- Missing output is not represented as a quarantined object; downstream advancement may be held instead.

### Post-exit addendum — Capability Authorization
- The model repeatedly relied on an `authorized evidence view`, but no concept owned whether a principal may perform a named capability on a subject/context/time.
- Raw-data read authorization, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, job/run operational control, and safeguard authority are independent capability categories.
- Denial of raw-data access does not automatically prohibit approved monitoring or RCA.
- Permission to operate/update a job does not grant raw-data read access; analysis permission does not grant production-control authority.
- Responsibility Assignment, Classification, Policy Context, and Monitoring Scope remain separate from authorization.
- Derived evidence can itself be sensitive and remains subject to its own authorized projection.

## Cross-cutting distinctions accepted by the current model

- Monitoring Scope ≠ ecosystem existence ≠ Capability Authorization;
- Entity Identity ≠ name ≠ replacement/succession;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Capability Authorization ≠ compliance;
- raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority;
- Expectation ≠ Baseline;
- normative requirement ≠ historical regularity;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- Change Intent ≠ Deployment ≠ realized Change;
- successful execution ≠ timely execution ≠ freshness ≠ data quality;
- planned topology ≠ active Lineage;
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- Propagation Safeguard ≠ health or causal truth;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time.

## Scenario implications of the addenda

### Protective hold/quarantine
A suspect or missing output can be protected at an explicit propagation boundary without rewriting the underlying Observation/Assessment or claiming defect/cause. Protected interval, authority, enforcement evidence, release, and safeguard-induced delay remain historical facts.

### Restricted-data analyst
A user may be denied direct Table C rows while being permitted approved aggregate health metrics, runtime/freshness Assessments, redacted Lineage, policy/restriction summaries, responsibility context, Investigation/Causal Claim state, and Impact/safeguard context. RCA remains possible over the authorized evidence view without smuggling restricted data into summaries.

### Job operator without raw-data read
A user may hold an explicit job/run operational capability while lacking permission to inspect the data the job processes. The action's actual outcome remains owned by Deployment/Execution History/Observation rather than being implied by permission.

## Phase 002 exit review and later boundary corrections

D-030 records that the original Phase 002 exit gate was satisfied with 20 concepts. That decision remains historically correct. Later requirements were added explicitly rather than silently overloading accepted concept purposes.

The current model still satisfies the original exit principles: each retained concept/addendum has a singular purpose; state/actions remain implementation-independent; ambiguity/evidence/security/temporal behavior are explicit; and no concept semantically requires DQX, Metric Views, Collibra, Immuta, GitHub Actions, a graph database, event store, quarantine mechanism, IAM model, or selected architecture.

## Current synchronization direction

Phase 003 composes all 22 concepts. Groups 01–04 are accepted. Capability Authorization is an accepted pre-Group-05 input. **Group 05 — Downstream Impact, Annotation & Explanation remains next and has not yet started.** See [`../phase_003/README.md`](../phase_003/README.md).
