# Concept Catalog

## Status

**24 concepts are Accepted.** Phase 002 originally exited with 20 accepted concepts. Later work exposed four missing independent behaviors: **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**, each accepted through a narrow post-exit addendum.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, IAM, authority-rule engine, orchestration, temporal-replay, metric-governance, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The original review and later addenda are in [`phase_002/README.md`](phase_002/README.md) and [`phase_002/addenda/`](phase_002/addenda/).

## Accepted concepts

### Group 01 — Scope & Identity
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md) — time-aware monitoring responsibility for identified entities without implicit propagation or access grant.
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md) — cross-source/time sameness and separation with ambiguity/correction provenance.

### Group 02 — Semantics, Governance & Policy
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md) — facet/context-aware meaning and interpretation, including governed schema/grain/key semantics.
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md) — named responsibility assignments without universal authority implication.
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md) — category membership under named governance/sensitivity/criticality vocabularies.
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md) — declared policy/handling applicability without enforcement/compliance claims.

### Group 03 — Health Evaluation
- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria for acceptable behavior, including structural/schema compatibility conditions where applicable.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — descriptive reference behavior from comparable evidence.
- [`Observation`](phase_002/03_health_evaluation/observation.md) — provenance-bearing measured/retrieved facts.
- [`Assessment`](phase_002/03_health_evaluation/assessment.md) — dimension-scoped interpretation against explicit Expectation/Baseline basis.

### Group 04 — History, Lineage & Change
- [`Change Intent`](phase_002/04_history_lineage_change/change_intent.md) — registered intended modification and anticipated effects before realization.
- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md) — actual execution-instance lifecycle history.
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md) — deployment attempt/activation/active-state/supersession history.
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md) — typed, directed, temporal, provenance-bearing relationships and historical traversal.
- [`Change`](phase_002/04_history_lineage_change/change.md) — realized differences/state transitions without health or causal judgment.

### Group 05 — Investigation, Impact & Explanation
- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md) — bounded inquiry that organizes evidence, claims, impact, and context without owning truth.
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md) — explicit causal proposition with epistemic status and supporting/contradicting evidence.
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md) — downstream reachability, exposure, observed effect, and business consequence kept distinct.
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md) — attributed human context without source-evidence mutation or hidden structured truth.
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md) — authorization/time-aware evidence-grounded communication with statement-to-basis traceability.

### Post-exit addenda
- [`Propagation Safeguard`](phase_002/addenda/propagation_safeguard.md) — proposed/active/released protective hold or quarantine state for an explicit output/consumption boundary.
- [`Capability Authorization`](phase_002/addenda/capability_authorization.md) — principal/capability/subject authorization state separating raw-data visibility, analytical visibility, operational control, safeguard/gate authority, and causal-confirmation capability.
- [`Execution Gate`](phase_002/addenda/execution_gate.md) — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness evidence, separate from passive monitoring and output quarantine.
- [`Assertion Authority`](phase_002/addenda/assertion_authority.md) — target/context/time-scoped rules determining which source/actor assertions have authoritative standing without owning the domain assertions, evidence sufficiency, permission, or enforcement.

## Core authority and access boundaries

The concept model explicitly distinguishes three cross-cutting questions:

**Which assertion has authoritative standing? → Assertion Authority**

**What condition should be considered acceptable? → Expectation under scoped normative authority**

**May this principal perform/view this capability? → Capability Authorization**

without making Responsibility Assignment, Policy Context, Classification, Monitoring Scope, source availability, repository ownership, job creator identity, organizational title, metric computation, or criticality an automatic authority/permission source.

A principal may be permitted to submit an assertion that remains advisory. A responsible steward may not have authoritative standing for every category. A source may be authoritative for one semantic facet and advisory for another. An authoritative source can still later be corrected; authority does not create factual infallibility.

A restricted-data analyst may be permitted to inspect approved aggregate health metrics, execution timing, Assessments, redacted Lineage, policy/restriction summaries, responsibility context, causal status, Impact, safeguards, gate state, authority standing, normative result/waiver state, and Annotation while being denied rows, sensitive columns, exact thresholds, schemas, source-holder identities, or other restricted evidence. A job operator can separately be authorized to retry/update/control a job without receiving raw-data read permission. Causal-confirmation capability is independently resolvable.

Derived evidence, authority metadata, schemas, metric values, thresholds, and normative rules are not automatically unrestricted; authorization applies to metadata/metrics/topology/causal/consequence/control/authority/normative detail independently where necessary.

## Assertion Authority boundary — Phase 005 Group 01

Group 01 discovered a genuine concept boundary because the same source-precedence/conflict/history behavior recurred across Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation, and later metric/threshold governance.

The accepted chain is:

**source assertion → Assertion Authority standing/rule resolution → owning concept authoritative resolution**

without moving the assertion itself into Assertion Authority.

The authority vocabulary preserves:

- **source assertion** — provenance-bearing contribution regardless of standing;
- **authority target** — concept/category/facet/scheme/type + explicit subject scope/context/time;
- **authority holder** — source/actor/role/governed process named by a rule;
- **authority rule** — provenance-bearing rule establishing standing/conditions/precedence/fallback;
- **authoritative assertion** — assertion from a holder with authoritative standing;
- **advisory assertion** — useful context/challenge that cannot displace authoritative state;
- **resolved assertion disagreement** — disagreement remains recorded but authority rules yield an authoritative resolution;
- **authoritative assertion conflict** — simultaneously authoritative assertions disagree and no resolver applies;
- **authority-rule conflict** — authority rules themselves disagree and no governing rule resolves them;
- **authority unknown/unavailable** — no applicable accepted rule can be established or required authority evidence is unavailable.

No hidden precedence is permitted. Source count/majority, recency alone, synchronization/ingestion order, source availability, repository ownership, administrator/title/responsibility, and apparent scope specificity do not create authority unless an explicit applicable rule says so.

Sole authority, co-authority, ordered precedence, and conditional/fallback authority are valid functional forms only when explicitly defined. Co-authoritative disagreement remains conflict unless an accepted resolver applies. Fallback requires both an explicit rule and evidence that the activation condition holds.

Authority rules themselves require provenance and governing basis; a source/rule cannot self-promote simply by claiming authority. Authority is bitemporal: prospective changes, corrections, supersession, and late discovery remain distinct, and later correction can revise retrospective resolution without changing what authority was known/used at the earlier cutoff.

## Semantic / schema governance boundary — Phase 005 Group 02

AUTH-009–AUTH-015 apply Assertion Authority separately to Semantic Definition facets, Responsibility Assignment types, Classification/criticality schemes, Policy Context applicability, contextual overrides, and derived/inherited governance assertions.

Semantic authority is facet-specific. Business definition, technical/schema declaration, grain, unit, population/inclusion meaning, calculation meaning, field role, and key/identifier role can legitimately have different authoritative holders.

Preserve:

**declared/governed schema meaning ≠ normative structural compatibility ≠ realized schema Observation/Change ≠ compatibility Assessment**.

An authoritative schema/key declaration does not prove the physical schema conforms, and a declared key does not prove uniqueness/nullability. Runtime schema metadata does not by itself establish authoritative business meaning. A column drop plus a similarly named add does not prove a rename without semantic/identity/planned-change evidence.

Responsibility authority remains responsibility-type scoped. Classification authority remains scheme/context specific, with criticality represented as explicit Classification schemes/contexts rather than Impact or health truth. Policy reference/text authority can differ from subject/context applicability authority.

Local/context governance does not automatically outrank broader governance, and Lineage, repository/container membership, schema/tag inference, or parent-domain state do not implicitly propagate Semantic Definition, Responsibility Assignment, Classification/criticality, Policy Context, or Assertion Authority. Derived/inherited assertions require provenance and explicit standing.

Group 02 requires no 25th concept.

## Normative health / metric governance boundary — Phase 005 Group 03

AUTH-016–AUTH-023 govern normative health standing while leaving measured/statistical truth in the existing concepts.

Preserve:

**metric/schema meaning ≠ metric-profile selection ≠ Expectation/threshold ≠ severity ≠ waiver/exception ≠ high-consequence-use eligibility**.

A metric profile is a governed selection/applicability structure, not a new truth-owning concept. It should preserve the reason a metric/check matters, its applicability, intended use/audience, authority/owner, and lifecycle/retirement context. Technical availability alone is not enough reason to compute or retain a metric, which creates the governance-side anti-bloat rule.

Baseline remains descriptive. A Baseline-derived range becomes normative only when an authoritative Expectation explicitly adopts a criterion. Authority can suspend or retire Baseline use after structural Change but cannot make empirically non-comparable evidence comparable; replacement Baselines remain evidence-derived.

Structural/schema compatibility rules are normative Expectations distinct from governed technical schema meaning and realized schema state. Consumer-specific rules can legitimately differ, so the same additive DDL change can be acceptable for one consumer and violating for another.

A bounded exception, waiver, or suspension can change normative applicability or required response, but it does not rewrite Observations, realized schema, Baseline deviations, or historical evidence and must not manufacture a false `pass`.

Normative conflict remains explicit. `Strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and latest-record wins are not implicit resolution rules.

Criticality can influence priority, review, and governance requirements, but it does not automatically tighten thresholds or establish health failure, exposure, or Impact.

A metric or Expectation is not automatically eligible for active control merely because it is authoritative, profile-selected, severe, or business-critical. AUTH-023 requires explicit high-consequence-use eligibility, while preserving:

**control-use eligibility ≠ gate/safeguard/job capability ≠ evidence readiness/sufficiency ≠ actual enforcement**.

Group 03 requires no 25th concept.

## Observation versus active control boundary

The default framework mode is observational and should remain out-of-band from production execution. Monitoring evidence collection or framework degradation must not delay production merely because an asset is monitored.

An **Execution Gate** is an explicit opt-in active-control boundary. It can hold a downstream execution until a declared upstream readiness condition is satisfied, admit it when ready, or record an authorized override. It is not implicitly created by Lineage, Assessment, Assertion Authority, schema change, or high-consequence-use eligibility and does not replace Execution History.

**Execution Gate ≠ Propagation Safeguard**: a gate controls whether a downstream run starts; a safeguard controls whether output/current state propagates or is consumed. Both can independently create observable latency/delivery consequences.

Phase 004 preserves:

**readiness result ≠ gate decision ≠ gate enforcement ≠ actual execution**

and:

**safeguard proposal/configuration/request ≠ enforced active safeguard ≠ prevented exposure**.

Assertion Authority or normative eligibility for a control criterion does not prove that a gate/safeguard/control actually enforced it or that the required evidence was ready.

## Cross-cutting reasoning model

The reasoning chain can distinguish:

**identified subject → source assertions / Assertion Authority resolution → semantic/responsibility/classification/policy context → governed metric-profile / Expectation / threshold / waiver state → Capability Authorization / Authorized Analytical Projection → planned intent / prospective downstream profile → active Deployment → execution/timing/dependency evidence → Observation → time-valid Assessment → criterion-bound readiness → optional Execution Gate decision/enforcement when explicitly enabled → actual Execution History / realized Change → Investigation → Causal Claim with explicit epistemic status → downstream Impact candidate → exposure/non-exposure → observed effect → consequence evidence → Propagation Safeguard enforcement/prevention/operational effect where applicable → Annotation → Explanation**

Causal attribution from an origin, gate, or safeguard to a downstream effect remains explicit **Causal Claim** rather than becoming an Impact/control/authority shortcut.

This is a reasoning/synchronization model, not a service topology, IAM architecture, authority-rule engine, scheduler/orchestration design, metric engine, persistence schema, causal algorithm, or temporal replay implementation.

## Historical replay boundary

Phase 003 Group 06 added **no new concept at that time**. Historical replay is a synchronization view over concept histories. The catalog moved from 23 to 24 concepts only later, when Phase 005 Group 01 discovered **Assertion Authority**.

Historical replay preserves:

- **effective/event time ≠ recorded/knowledge time**;
- current state ≠ historical state cut;
- later evidence/authority/normative correction ≠ evidence/authority/rule known then;
- actual historical state/action/Explanation ≠ replay-derived interpretation/reconstruction;
- actual gate/safeguard action ≠ counterfactual action now preferred;
- historical Assertion Authority/Capability Authorization/normative/control state ≠ current authority/disclosure permission.

A present-day `as-known-then` computation may be useful, but it cannot be presented as an Assessment, belief, authority resolution, normative rule/waiver state, causal status, readiness/enforcement conclusion, decision, or Explanation that actually existed then unless historical state proves that it did.

## Phase 004 refinement boundary — COMPLETE

Phase 004 did **not** add a generic evidence/causal/exposure/readiness/control concept merely to hold refinement metadata. `REF-###` contracts define standards over accepted concept truth.

### Group 01 — accepted REF-001–REF-005

**evidence item → applicability to a defined proposition → bounded coverage/opportunity-to-observe → corroboration/conflict relationship → conclusion-specific sufficiency**

without a universal trust score, hidden source authority, or authorization grant.

### Group 02 — accepted REF-006–REF-012

Distinguishes event/effective time, source availability, framework knowledge, derived evaluation time, exact historical knowledge-cut eligibility, negative epistemic claims, progressive analytical availability, late evidence/correction/conflict/reinterpretation, material dependent reevaluation, and actual-retained versus reconstructible historical state.

### Group 03 — accepted REF-013–REF-020

Defines explicit causal proposition/role binding; `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`; multidimensional causal evidence; bounded alternatives; claim-class confirmation profiles; evidence/authority separation; multiple contributors; qualitative roles without percentage attribution; progressive RCA; and challenge/reversal of previously confirmed claims.

`Confirmed` requires the applicable profile/standard, sufficient evidence, contradiction/alternative review, adequate negative-evidence coverage where relied upon, independently resolved confirmation capability/authority, and provenance-bearing confirmation action.

### Group 04 — accepted REF-021–REF-030

Defines encounter-bound exposure, non-exposure coverage, criterion-bound readiness, separate gate evaluation/decision/enforcement/execution, safeguard enforcement/prevention, fallback evidence, control-effect causality, and retrospective revision without rewriting historical actions.

Examples remain:

- a report can be `not exposed to suspect V` because it used V-1 while separately being stale;
- `upstream job succeeded` may satisfy one readiness predicate but not a gate requiring current output + freshness;
- a configured hold is not proven enforced merely because no run is visible when execution telemetry is incomplete;
- `safeguard active + consumer not exposed` is not automatically `prevented exposure` if no relevant encounter opportunity existed;
- blocking suspect V does not prove downstream state is fresh/healthy.

### Group 05 — accepted consolidation / exit

REF-001–REF-030 compose across E-01–E-22 and all Phase 004 scenario checks. Progressive analytical availability does not weaken evidence burden; restricted-data analysis remains useful without declassification; late evidence may revise retrospective conclusions without rewriting historical actions; passive monitoring remains non-blocking for ungated production; source/actor authority remained deliberately deferred to Phase 005.

Assertion Authority and later Phase 005 governance now fill those authority boundaries without changing the Phase 004 evidence meaning of any conclusion.

## Phase 005 authority refinement boundary — ACTIVE

### Group 01 — accepted AUTH-001–AUTH-008

- AUTH-001 — authority target binding and vocabulary;
- AUTH-002 — authority-rule provenance and governing basis;
- AUTH-003 — assertion standing and conditional authority;
- AUTH-004 — assertion disagreement and authority conflict;
- AUTH-005 — explicit precedence, co-authority, and fallback;
- AUTH-006 — authority revision/correction/supersession/time;
- AUTH-007 — unknown/unavailable/resolution limits;
- AUTH-008 — separation from evidence, permission, responsibility, policy, and enforcement.

### Group 02 — accepted AUTH-009–AUTH-015

- AUTH-009 — semantic facet and schema-meaning authority;
- AUTH-010 — responsibility-type authority and assignment governance;
- AUTH-011 — classification-scheme and criticality authority;
- AUTH-012 — policy-context applicability authority;
- AUTH-013 — contextual overrides, local governance, and cross-facet conflict;
- AUTH-014 — derived, inherited, and propagated governance assertions;
- AUTH-015 — governance-state separation from normative health and operational truth.

### Group 03 — accepted AUTH-016–AUTH-023

- AUTH-016 — Expectation-class and normative authority;
- AUTH-017 — metric-profile selection, purpose, and critical-metric authority;
- AUTH-018 — threshold, margin, tolerance, and severity authority;
- AUTH-019 — structural/schema compatibility Expectation authority;
- AUTH-020 — metric applicability, Baseline use, and structural-change review authority;
- AUTH-021 — exception, waiver, suspension, and retirement governance;
- AUTH-022 — normative conflict, business/technical coexistence, and rule composition;
- AUTH-023 — high-consequence metric/Expectation use eligibility.

### Group 04 — next

Capability Authorization & Restricted Analytical Visibility is next and has not started. It will refine permission to view/propose/edit/approve/waive/retire normative state and to access restricted metric/schema/threshold evidence without conflating permission with Assertion Authority or operational truth.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, execution opportunities, tables, views, Metric Views, repositories, workflows, columns, business metrics, metric profiles, reports, applications, business processes, teams, people, source revisions, deployment targets, client-delivery endpoints, roles, and groups may participate in concepts without becoming giant concepts themselves.

## Phase state

**Phase 003 is complete.** Accepted synchronization range: **SYN-001–SYN-035**. E-01–E-22 pass end-to-end consolidation.

**Phase 004 is complete.** Groups 01–05 are accepted with **REF-001–REF-030**.

**Phase 005 is active. Groups 01–03 are accepted with AUTH-001–AUTH-023. Group 04 — Capability Authorization & Restricted Analytical Visibility is next and has not started.**