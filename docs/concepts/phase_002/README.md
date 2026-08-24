# Phase 002 — Concept Specifications

**Status:** **Complete — Groups 01–05 accepted; four explicit post-exit addenda accepted through later-phase review.**

## Purpose

Phase 002 turned the Phase 001 discovery catalog into explicit, implementation-neutral Concept Design specifications. The concepts define product behavior and truth boundaries without mapping them to services, schemas, APIs, Databricks objects, graph databases, ledger/event-store technologies, IAM schemes, authority-rule engines, orchestration products, language/framework choices, or vendor products.

The original Phase 002 review completed with 20 concepts. Later work exposed four independently motivated behaviors that could not be cleanly owned by those concepts. Phase 002 was therefore narrowly reopened through explicit addenda while preserving the original exit as historical truth.

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
- **Capability Authorization** — provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time. It separates raw-data read, metadata/health visibility, Lineage/RCA participation, operational job authority, safeguard/gate authority, causal-confirmation capability, and other capability categories without selecting an IAM/enforcement implementation.
- **Execution Gate** — optional active control over whether a downstream execution opportunity is admitted, held, admitted after readiness, expired/cancelled, or explicitly overridden based on declared prerequisite readiness evidence. It remains separate from passive monitoring, Execution History, Assessment, Capability Authorization, and Propagation Safeguard.
- **Assertion Authority** — provenance-bearing authority-rule state determining which source/actor/role/governed process has authoritative standing for a bounded assertion category/facet/subject scope/context/time. It remains separate from the domain assertion itself, Responsibility Assignment, Capability Authorization, evidence sufficiency, Policy Context/Classification, and enforcement.

**24 concepts are currently accepted.**

Review order remains a design dependency, not an implementation dependency. Concepts remain independently motivated and compose through synchronizations/refinement contracts.

## Accepted boundary refinements

### Group 01
- Monitoring Scope is monitoring responsibility, not authorization or assertion authority.
- Entity Identity is ecosystem-wide and distinct from replacement/succession.

### Group 02
- Semantic Definition is facet/context/provenance/time-aware.
- Responsibility Assignment replaces overloaded Ownership and is not universal authority or authorization.
- Classification is categorical metadata, separate from Policy Context, authorization, and compliance.
- Synchronization order never silently becomes governance authority.
- Group 02 concepts preserve source assertions/conflicts; Phase 005 Assertion Authority later determines source/actor standing without moving those assertions out of their owning concepts.

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
- Raw-data read authorization, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, job/run operational control, safeguard authority, gate authority, and causal-confirmation capability are independent categories.
- Denial of raw-data access does not automatically prohibit approved monitoring or RCA.
- Permission to operate/update a job does not grant raw-data read access; analysis permission does not grant production-control authority.
- Responsibility Assignment, Classification, Policy Context, Monitoring Scope, and Assertion Authority remain separate from Capability Authorization.
- Derived evidence can itself be sensitive and remains subject to its own authorized projection.

### Post-exit addendum — Execution Gate
- SYN-011 can assess upstream dependency readiness but does not own scheduler blocking; Execution History records actual runs; Propagation Safeguard protects output/consumption rather than downstream start admission.
- Execution Gate therefore owns explicit downstream execution admission/hold/admit/override state for enabled dependency-readiness control.
- Passive monitoring remains non-blocking by default; no dependency/readiness Assessment silently creates a gate.
- A gate may require current-cycle output availability/freshness/version or another explicit readiness criterion rather than only successful upstream execution.
- `held` ≠ execution failure; `admitted` ≠ execution occurred; `override` ≠ prerequisite ready.
- Gate-induced delay remains observable/assessable and can create downstream Impact.
- Unknown/unavailable gate evidence requires explicit fallback semantics; no universal fail-open/fail-closed rule is assumed.

### Post-exit addendum — Assertion Authority
- Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation, and later metric/threshold governance repeatedly relied on source precedence/authority context but no concept owned the authority rules themselves.
- Assertion Authority therefore owns authority target, holder standing, conditions, explicit precedence/fallback, rule provenance/governing basis, effective/knowledge time, and authority-rule conflict/history.
- Source assertions remain in their owning concepts regardless of standing.
- A principal may have Capability Authorization to submit/revise an assertion while that assertion remains advisory.
- A responsible party does not automatically become authoritative for the assertion category they maintain.
- Authority is category/facet/scope/context/time specific; no source/vendor is globally authoritative by default.
- Authoritative/advisory/non-authoritative/conditional/unknown/unavailable/conflicting standing remain distinct.
- Assertion disagreement, resolved disagreement, authoritative assertion conflict, and authority-rule conflict remain distinct.
- Source count/majority, recency alone, synchronization/ingestion order, source availability, repository ownership, title/admin/responsibility, and apparent specificity do not create authority.
- Co-authority, ordered precedence, and conditional/fallback authority are valid only when explicitly defined.
- Fallback requires an explicit rule plus evidence the activation condition holds.
- Authority rules require provenance/governing basis and cannot self-validate.
- Authority history is bitemporal; later correction can revise retrospective resolution without changing what authority was known then.
- Assertion Authority does not waive REF-001–REF-030, prove factual correctness/compliance, or prove enforcement.

## Cross-cutting distinctions accepted by the current model

- Monitoring Scope ≠ ecosystem existence ≠ Assertion Authority ≠ Capability Authorization;
- Entity Identity ≠ name ≠ replacement/succession;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ Assertion Authority ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Assertion Authority ≠ Capability Authorization ≠ compliance;
- source assertion ≠ authoritative assertion;
- authoritative standing ≠ factual infallibility;
- assertion disagreement ≠ authoritative assertion conflict ≠ authority-rule conflict;
- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization ≠ enforcement;
- raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard/gate/confirmation authority;
- passive monitoring ≠ active execution gating;
- dependency readiness Assessment ≠ Execution Gate admission state;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- held execution opportunity ≠ failed execution;
- gate admission ≠ actual run occurrence;
- gate override ≠ readiness;
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
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence ≠ causal attribution;
- criticality/policy sensitivity ≠ actual Impact evidence;
- Propagation Safeguard ≠ health or causal truth;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time.

## Scenario implications of the addenda

### Protective hold/quarantine
A suspect or missing output can be protected at an explicit propagation boundary without rewriting Observation/Assessment or claiming defect/cause. Protected interval, authority, enforcement evidence, release, and safeguard-induced delay remain historical facts.

### Restricted-data analyst
A user may be denied direct Table C rows while being permitted approved aggregate health metrics, runtime/freshness Assessments, redacted Lineage, policy/restriction summaries, responsibility context, authority standing, Investigation/Causal Claim state, and Impact/safeguard/gate context. RCA remains possible without smuggling restricted data into summaries.

### Job operator without raw-data read
A user may hold an explicit job/run operational capability while lacking permission to inspect the data the job processes. The action outcome remains owned by Deployment/Execution History/Observation rather than being implied by permission.

### Layered downstream Impact
A downstream report can be reachable without exposure, exposed without observed degradation, affected with business consequence unknown, or protected from a suspect version while becoming late. Causal attribution remains explicit Causal Claim.

### Dependency-gated downstream execution
With no gate enabled, monitoring reports early/stale execution but does not delay it. With an explicit Execution Gate, downstream can be held until readiness or explicit fallback/override applies. Gate waiting remains separate operational health evidence.

### Authoritative versus advisory assertion
A governance catalog may be authoritative for a business-definition facet while a repository description remains advisory. Both remain recorded; the authoritative resolution uses Assertion Authority. If two co-authoritative sources disagree, conflict remains explicit instead of choosing the newest or most available source.

## Historical replay consequence

Phase 003 Group 06 did **not** require another concept at that time. Historical replay remains a synchronization view over concept histories. The later 24th concept is Assertion Authority, discovered in Phase 005 Group 01.

The model preserves:

- current state ≠ historical state cut;
- later evidence/authority correction ≠ evidence/authority known then;
- actual historical Assessment/authority/claim/control/Explanation ≠ replay-derived reconstruction;
- actual gate/safeguard action ≠ counterfactual action now preferred;
- historical Assertion Authority/Capability Authorization/control state ≠ current authority/disclosure permission.

## Phase 002 exit review and later boundary corrections

D-030 records that the original Phase 002 exit gate was satisfied with 20 concepts. That decision remains historically correct. Later requirements were added explicitly rather than silently overloading accepted concept purposes.

The current model still satisfies the original exit principles: each retained concept/addendum has a singular purpose; state/actions remain implementation-independent; ambiguity/evidence/security/temporal behavior are explicit; and no concept semantically requires DQX, Metric Views, Collibra, Immuta, GitHub Actions, an assertion-authority engine, graph database, event store, quarantine mechanism, IAM model, scheduler/orchestrator, or selected architecture.

## Current direction

**Phase 003 is complete with SYN-001–SYN-035. Phase 004 is complete with REF-001–REF-030. Phase 005 is active: Group 01 accepted Assertion Authority and AUTH-001–AUTH-008; Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**
