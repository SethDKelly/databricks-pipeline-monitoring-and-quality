# Concept Catalog

## Status

**23 concepts are Accepted.** Phase 002 originally exited with 20 accepted concepts. Later Phase 003 work exposed three missing independent behaviors: **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate**, each accepted through a narrow post-exit addendum.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, IAM, orchestration, temporal-replay, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The original review and later addenda are in [`phase_002/README.md`](phase_002/README.md) and [`phase_002/addenda/`](phase_002/addenda/).

## Accepted concepts

### Group 01 — Scope & Identity
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md) — time-aware monitoring responsibility for identified entities without implicit propagation or access grant.
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md) — cross-source/time sameness and separation with ambiguity/correction provenance.

### Group 02 — Semantics, Governance & Policy
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md) — facet/context-aware meaning and interpretation.
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md) — named responsibility assignments without universal authority implication.
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md) — category membership under named governance/sensitivity vocabularies.
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md) — declared policy/handling applicability without enforcement/compliance claims.

### Group 03 — Health Evaluation
- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria for acceptable behavior.
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

## Core access boundary

The concept model explicitly distinguishes:

**responsibility/policy context → Capability Authorization → authorized evidence/action view**

without making Responsibility Assignment or Policy Context themselves authorization sources.

A restricted-data analyst may be permitted to inspect approved aggregate health metrics, execution timing, Assessments, redacted Lineage, policy/restriction summaries, responsibility context, causal status, Impact, safeguards, gate state, and Annotation while being denied rows, sensitive columns, thresholds, identities, or other restricted evidence. A job operator can separately be authorized to retry/update/control a job without receiving raw-data read permission. Causal-confirmation capability is also independently resolvable and is not granted merely by RCA visibility or organizational title.

Derived evidence is not automatically unrestricted; authorization applies to metadata/metrics/topology/causal/consequence/control detail independently where necessary.

## Observation versus active control boundary

The default framework mode is observational and should remain out-of-band from production execution. Monitoring evidence collection or framework degradation must not delay production merely because an asset is monitored.

An **Execution Gate** is an explicit opt-in active-control boundary. It can hold a downstream execution until a declared upstream readiness condition is satisfied, admit it when ready, or record an authorized override. It is not implicitly created by Lineage or Assessment and does not replace Execution History.

**Execution Gate ≠ Propagation Safeguard**: a gate controls whether a downstream run starts; a safeguard controls whether output/current state propagates or is consumed. Both can independently create observable latency/delivery consequences.

Phase 004 further preserves:

**readiness result ≠ gate decision ≠ gate enforcement ≠ actual execution**

and:

**safeguard proposal/configuration/request ≠ enforced active safeguard ≠ prevented exposure**.

## Cross-cutting reasoning model

The reasoning chain can distinguish:

**identified subject → monitoring/governance context → Capability Authorization / Authorized Analytical Projection → planned intent / prospective downstream profile → active Deployment → execution/timing/dependency evidence → Observation → time-valid Assessment → criterion-bound readiness → optional Execution Gate decision/enforcement when explicitly enabled → actual Execution History / realized Change → Investigation → Causal Claim with explicit epistemic status → downstream Impact candidate → exposure/non-exposure → observed effect → consequence evidence → Propagation Safeguard enforcement/prevention/operational effect where applicable → Annotation → Explanation**

Causal attribution from an origin, gate, or safeguard to a downstream effect remains explicit **Causal Claim** rather than becoming an Impact or control-state shortcut.

This is a reasoning/synchronization model, not a service topology, IAM architecture, scheduler/orchestration design, persistence schema, causal algorithm, or temporal replay implementation.

## Historical replay boundary

Phase 003 Group 06 adds **no 24th concept**. Historical replay is a synchronization view over the existing concept histories.

It preserves:

- **effective/event time ≠ recorded/knowledge time**;
- current state ≠ historical state cut;
- later evidence ≠ evidence known then;
- actual historical state/action/Explanation ≠ replay-derived interpretation/reconstruction;
- actual gate/safeguard action ≠ counterfactual action now preferred;
- historical authorization/control/confirmation capability ≠ current disclosure permission.

A present-day `as-known-then` computation may be useful, but it cannot be presented as an Assessment, belief, causal status, readiness/enforcement conclusion, decision, or Explanation that actually existed then unless historical state proves that it did.

## Phase 004 refinement boundary — COMPLETE

Phase 004 does **not** add a new evidence, causal, exposure, readiness, or control concept merely to hold refinement metadata. The accepted concepts already own their evidence/state. Phase 004 `REF-###` contracts define standards for how that evidence can support conclusions.

### Group 01 — accepted REF-001–REF-005

The key chain is:

**evidence item → applicability to a defined proposition → bounded coverage/opportunity-to-observe → corroboration/conflict relationship → conclusion-specific sufficiency**

without turning that chain into a universal trust score, new source authority, or new authorization grant.

### Group 02 — accepted REF-006–REF-012

Group 02 distinguishes event/effective time, source availability, framework knowledge, and derived evaluation time; defines exact historical knowledge-cut eligibility; separates `known by`/`learned after`/`not recorded by`/`not known by`/`not available by`; supports progressive analytical availability; distinguishes late evidence/correction/conflict/reinterpretation; and defines material dependent reevaluation plus actual-retained versus reconstructible historical state.

### Group 03 — accepted REF-013–REF-020

Group 03 defines:

- explicit causal proposition/role binding;
- status vocabulary `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- multidimensional causal support/contradiction without a universal score;
- bounded material alternative evaluation;
- claim-class confirmation profiles and a common confirmation evidence gate;
- confirmation evidence sufficiency separate from confirmation authority;
- multiple compatible contributors without a forced single root cause;
- qualitative causal roles without percentage attribution;
- progressive RCA maturity without latency-driven status inflation;
- challenge/reversal of previously confirmed claims with historical preservation.

`Confirmed` is not merely `strongly supported` or the leading hypothesis. It requires the applicable confirmation profile/standard, sufficient evidence, material contradiction/alternative review, adequate negative-evidence coverage where relied upon, independently resolved confirmation capability/authority, and provenance-bearing confirmation action. Phase 005 determines who/what may confirm by context; Phase 004 does not grant that authority.

### Group 04 — accepted REF-021–REF-030

Group 04 defines:

- exposure propositions bound to affected state/version/window, consumer, historical relationship, encounter mode, and consumer opportunity;
- positive exposure from actual encounter evidence rather than reachability/timing/activity;
- `not exposed` as a negative conclusion requiring sufficient consumption/version and material-path coverage;
- explicit distinction among no encounter opportunity, no encounter, safe-version encounter, unknown-version encounter, unavailable/restricted evidence, and affected-state encounter;
- criterion-bound readiness rather than global upstream readiness;
- separate completion/output/version/currentness/freshness/publication/quality predicates where a criterion requires them;
- gate readiness evaluation, gate decision, opportunity-specific enforcement, and actual Execution History as separate claims;
- hold/admit enforcement asymmetry: a reliable run during an unoverridden hold contradicts full hold enforcement, while an admitted opportunity that never runs does not prove admission failed;
- safeguard proposal/configuration/request separate from boundary-specific enforcement;
- prevented exposure only when safeguard enforcement was materially operative on the encounter path with sufficient negative-consumption/version and alternate-path coverage;
- configured fallback policy separate from actual fallback recognition/application/enforcement/outcome;
- control-effect causal conclusions under the same REF-013–REF-020 causal standards;
- retrospective revision from late control/consumption evidence without rewriting historical actions.

Examples:

- a report can be `not exposed to suspect V` because it used V-1 while separately being stale;
- `upstream job succeeded` may satisfy one readiness predicate but not a gate requiring current output + freshness;
- a configured hold is not proven enforced merely because no run is visible when execution telemetry is incomplete;
- `safeguard active + consumer not exposed` is not automatically `prevented exposure` if no relevant encounter opportunity existed;
- blocking suspect V does not prove the downstream state is fresh/healthy.

### Group 05 — accepted consolidation / exit

Group 05 adds no new Concept, synchronization, or `REF-031`. It applies REF-001–REF-030 across E-01–E-22 and all Phase 004 scenario checks and confirms:

- one evidence model composes across positive and negative runtime/historical/causal/exposure/control conclusions;
- progressive analytical availability does not weaken evidence burden;
- causal confirmation, multiple contributors, and challenge/reversal compose with control/Impact reasoning;
- exposure/readiness/decision/enforcement/action/prevention remain separately evidenced;
- restricted-data analysis remains useful without declassification;
- late evidence may revise retrospective conclusions without rewriting historical actions/communications;
- passive monitoring remains non-blocking for ungated production, while active gates may later require stronger control-path availability;
- source/actor authority remains deliberately deferred to Phase 005/009 rather than being inferred from evidence order/count/recency.

See [`phase_004/05_consolidation_and_exit/README.md`](phase_004/05_consolidation_and_exit/README.md), [`scenario_consolidation_matrix.md`](phase_004/05_consolidation_and_exit/scenario_consolidation_matrix.md), and [`phase_004_exit_review.md`](phase_004/05_consolidation_and_exit/phase_004_exit_review.md).

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, execution opportunities, tables, views, Metric Views, repositories, workflows, columns, business metrics, reports, applications, business processes, teams, people, source revisions, deployment targets, client-delivery endpoints, roles, and groups may participate in concepts without becoming giant concepts themselves.

## Phase state

**Phase 003 is complete.** Accepted synchronization range: **SYN-001–SYN-035**. E-01–E-22 pass end-to-end consolidation. Current results are documented in [`phase_003/README.md`](phase_003/README.md), with Group 06 in [`phase_003/06_historical_replay_and_consolidation/`](phase_003/06_historical_replay_and_consolidation/).

**Phase 004 is complete. Groups 01–05 are accepted with REF-001–REF-030.** See [`phase_004/README.md`](phase_004/README.md).

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is next and has not started.** See [`phase_005/README.md`](phase_005/README.md).
