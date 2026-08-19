# Phase 002 — Concept Specifications

**Status:** **Complete — Groups 01–05 accepted; post-exit Propagation Safeguard addendum accepted during Phase 003.**

## Purpose

Phase 002 turned the Phase 001 discovery catalog into explicit, implementation-neutral Concept Design specifications. The resulting concepts define product behavior and truth boundaries without mapping them to services, schemas, APIs, Databricks objects, graph databases, ledger/event-store technologies, language/framework choices, or vendor products.

The original Phase 002 review completed with 20 concepts. Phase 003 Group 03 later exposed one missing independently motivated behavior—protective hold/quarantine/release of data propagation. Phase 002 was therefore narrowly reopened through the accepted [`Propagation Safeguard`](addenda/propagation_safeguard.md) post-exit addendum. The original exit remains historically true for the requirements known at that time.

## Accepted concept groups

| Group | Theme | Accepted concepts | Status |
|---|---|---|---|
| 01 | Scope & Identity | Monitoring Scope, Entity Identity | **Accepted** |
| 02 | Semantics, Governance & Policy | Semantic Definition, Responsibility Assignment, Classification, Policy Context | **Accepted** |
| 03 | Health Evaluation | Expectation, Baseline, Observation, Assessment | **Accepted** |
| 04 | History, Lineage & Change | Change Intent, Execution History, Deployment, Lineage, Change | **Accepted** |
| 05 | Investigation, Impact & Explanation | Investigation, Causal Claim, Impact, Annotation, Explanation | **Accepted** |

## Accepted post-exit addendum

- **Propagation Safeguard** — protective proposed/active/released hold or quarantine state for a defined data output, execution context, propagation boundary, environment/cohort, or consumer set. It does not own health Assessment, Investigation, causal truth, authorization, or implementation enforcement mechanics.

**21 concepts are currently accepted.**

Review order was a design dependency, not an implementation dependency. Concepts remain independently motivated and compose through synchronizations.

## Accepted boundary refinements

### Group 01

- `Monitored Scope` → **Monitoring Scope**: monitoring responsibility applies to identified entities and does not implicitly propagate.
- `Asset Identity` → **Entity Identity**: identity behavior spans the ecosystem and remains distinct from replacement/succession.

### Group 02

- `Description / Semantics` → **Semantic Definition**: meaning is facet-, context-, provenance-, and time-aware.
- `Ownership` → **Responsibility Assignment**: technical ownership, business accountability, stewardship, and other responsibilities are distinct named assignment types.
- **Classification** is categorical metadata, separate from **Policy Context**, authorization, and compliance.
- Synchronization order never silently becomes governance authority.

### Group 03

- **Expectation** is normative; **Baseline** is descriptive.
- **Observation** is provenance-bearing fact; **Assessment** is interpretation against explicit normative and/or comparative basis.
- Missing telemetry is not observed absence.
- Typical is not automatically healthy; atypical is not automatically degraded.
- Health is dimension-scoped by default; composite health requires explicit aggregation semantics.

### Group 04

- **Change Intent** is introduced separately from realized **Change** because planned intent and realized fact have different truth conditions.
- `Deployment Record` → **Deployment**: attempt, activation, active state, and supersession are behavior, not merely a stored record.
- Change Intent may register a prospective Baseline comparability break, but intended values never become empirical Baseline values.
- Prospective acceptable post-change behavior belongs in explicit **Expectation** establishment/revision.
- **Lineage** is typed, directed, temporal, provenance-bearing, and graph-compatible without selecting graph technology.
- Material history follows ledger-like append/supersede/correction semantics without selecting persistence architecture.
- Effective/event time and recorded/knowledge time remain distinct where historical interpretation requires both.

### Group 05

- **Investigation** organizes inquiry and evidence; it does not own causal truth.
- **Causal Claim** is the explicit home for causal propositions, supporting/contradicting evidence, contribution roles, uncertainty, and confirmation/rejection history.
- Correlation, Lineage, Deployment timing, realized Change, and intent consistency cannot silently become confirmed causation.
- **Impact** separates downstream reachability, actual exposure/consumption, observed downstream effect, and evidenced business consequence.
- `Annotation / Confirmation` → **Annotation** plus confirmation/rejection actions on Causal Claim under an explicit evidence/authority standard.
- **Annotation** is human context, not a catch-all mechanism for Change Intent, Expectation, Responsibility Assignment, or causal confirmation.
- `Report / Explanation` → **Explanation**: presentation artifact is secondary; the product purpose is authorized, evidence-grounded communication.
- Explanation preserves the distinction between **what was known then** and **what we know now**.

### Post-exit addendum

- **Propagation Safeguard** is separate from Assessment, Investigation, Impact, and Policy Context because those concepts explicitly do not own remediation/protective-control state.
- A violated Expectation or Baseline atypicality can motivate safeguard review but does not automatically activate quarantine.
- `proposed` is distinct from `active`; activation requires explicit authority/enforcement evidence under applicable semantics.
- Quarantine may be precautionary and does not prove defect; release does not prove health.
- If no output exists, downstream advancement/current-cycle publication may be held rather than inventing a quarantined data object.
- Safeguard placement is context-specific and may itself create observable delivery delay.

## Cross-cutting distinctions accepted by Phase 002/current addendum model

- Monitoring Scope ≠ ecosystem existence ≠ authorization;
- Entity Identity ≠ name ≠ replacement/succession;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority ≠ authorization;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- Expectation ≠ Baseline;
- normative requirement ≠ historical regularity;
- planned anticipated effect ≠ normative Expectation;
- planned value ≠ empirical Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- Change Intent ≠ Deployment ≠ realized Change;
- Deployment attempt ≠ activation;
- activation ≠ intended effect realized;
- successful execution ≠ timely execution ≠ freshness ≠ data quality;
- planned topology ≠ active Lineage;
- Lineage reachability ≠ cause ≠ confirmed Impact;
- Change ≠ degradation ≠ cause;
- effective/event time ≠ recorded/knowledge time;
- Investigation ≠ evidence/causal truth;
- Causal Claim ≠ confirmed cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- Propagation Safeguard ≠ health or causal truth;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- release ≠ proof of health;
- Annotation ≠ Observation/Change Intent/Expectation/causal confirmation;
- Explanation ≠ independent truth source.

## Phase 002 scenario review

### S-01 — Join-volume degradation

**Pass.** A+B→C can be expressed as Observations, Baseline comparison, normative Assessment, Change Intent/Deployment/realized Change context, typed historical Lineage, competing/multiple Causal Claims, downstream Impact analysis, and authorized Explanation without forcing a cause.

### S-02 — Stale upstream with successful downstream execution

**Pass.** Execution success, freshness Observation, freshness Expectation/Assessment, upstream Lineage, Causal Claim, and downstream Impact remain separate.

### S-03 — Deployment-correlated shift

**Pass.** Registered intent, Deployment activation, execution sequence, realized Change, and Assessment can align temporally while the deployment-cause proposition remains a separately evaluated Causal Claim.

### S-04 — Cross-repository dependency

**Pass.** Repository boundaries preserve provenance but do not break Entity Identity, Lineage, Investigation, or Impact reasoning.

### S-05 — Conflicting governance metadata

**Pass.** Conflicting semantic, responsibility, classification, policy, or Expectation assertions retain provenance and conflict rather than last-write-wins flattening.

### S-06 — Policy-sensitive explanation

**Pass.** Authorization-aware opaque/redacted entities, evidence, claims, Annotations, and downstream consumers preserve usefulness without broadening raw-data access or leaking restricted context.

### S-07 — Historical replay

**Pass.** Ledger-like history plus effective/event time and recorded/knowledge time can reconstruct what was intended, active, executed, connected, expected, baselined, observed, assessed, investigated, believed, and explained at an earlier time.

### S-08 — Planned structural change

**Pass.** A planned filter can prospectively revise an Expectation and register a Baseline comparability break without manufacturing empirical history. Valid intended volume change can coexist with an unintended quality violation and competing causal explanations.

### Addendum scenario — Protective hold/quarantine

**Pass after addendum.** A suspect or missing output can be protected at an explicit propagation boundary without rewriting the underlying Observation/Assessment or claiming defect/cause. The protected interval, authority, enforcement evidence, release, and any safeguard-induced delay remain historical facts.

## Phase 002 exit review and later boundary correction

D-030 records that the original Phase 002 exit gate was satisfied with 20 concepts. That decision remains historically correct. Phase 003 later uncovered a new requirement that could not be expressed without overloading an accepted concept, so the catalog was explicitly extended rather than silently modifying ownership boundaries.

The current model still satisfies the original exit principles:

- every retained concept has a singular purpose and reviewed specification;
- boundary changes/addenda have rationale recorded;
- state/actions remain implementation-independent;
- ambiguity, evidence, security, and temporal behavior remain explicit;
- no concept depends semantically on DQX, Metric Views, Collibra, Immuta, GitHub Actions, graph database, event store, quarantine mechanism, or selected architecture.

## Current synchronization direction

Phase 003 composes all 21 concepts. Groups 01–03 are accepted, including prospective blast-radius review, execution-duration/dependency health, analyst Investigation handoff, and Propagation Safeguard. See [`../phase_003/README.md`](../phase_003/README.md).
