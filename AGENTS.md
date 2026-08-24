# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Four explicit post-exit addenda are now accepted: **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**. Current accepted concept count: **24**.

**Phase 003 is complete. Groups 01–06 are accepted. Accepted synchronization range: SYN-001–SYN-035. E-01–E-22 pass end-to-end consolidation.**

**Phase 004 — Evidence, Time, and Causality Refinement is complete. Groups 01–05 are accepted with REF-001–REF-030.**

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is active. Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution is accepted with AUTH-001–AUTH-008. Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, deployment workflows, quarantine implementations, gate/orchestration implementations, IAM implementations, assertion-authority engines, graph/causal engines, LLMs, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, API, persisted view, scheduler, orchestrator, temporal snapshot, or replay store.
- Phase 004 `REF-###` artifacts refine evidence/time/causal/control standards over accepted concepts and synchronizations; they are not new truth-owning concepts or Phase 003 synchronizations.
- Phase 005 `AUTH-###` artifacts refine authority/governance semantics; they are not hidden architecture or substitutes for concept ownership.
- Synchronization/refinement order is never authority; a trigger is never causation.
- Do not create umbrella state for convenience.
- Reopen earlier boundaries only explicitly with rationale.

## Core invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- Responsibility Assignment ≠ Assertion Authority ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Assertion Authority ≠ Capability Authorization ≠ compliance;
- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization ≠ action/enforcement authority;
- source assertion ≠ authoritative assertion;
- authoritative standing ≠ factual infallibility;
- authoritative standing ≠ permission to act;
- authoritative rule/configuration ≠ actual enforcement;
- assertion disagreement ≠ authoritative assertion conflict ≠ authority-rule conflict;
- source count/majority ≠ authority precedence;
- record recency ≠ authority precedence;
- synchronization/ingestion order ≠ authority precedence;
- source availability ≠ authority precedence;
- responsibility/title/admin/repository ownership ≠ assertion authority;
- apparent scope specificity ≠ precedence unless an explicit rule says so;
- unavailable primary authority ≠ automatic fallback authority;
- raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority ≠ gate-control authority ≠ causal-confirmation authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- passive monitoring ≠ active Execution Gate;
- monitoring availability ≠ ungated production-job availability;
- dependency readiness Assessment ≠ criterion-bound readiness;
- readiness result ≠ gate decision ≠ gate enforcement ≠ actual execution;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- gate hold ≠ execution failure;
- gate admission ≠ actual run occurrence;
- gate override ≠ prerequisite ready;
- configured fallback ≠ actual fallback application;
- missing readiness/control evidence ≠ ready/enforced/fail-open/fail-closed;
- permission to act ≠ action succeeded;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- planned topology ≠ active Lineage;
- successful run ≠ timely run ≠ freshness ≠ data quality;
- successful upstream run ≠ criterion-bound readiness;
- Observation ≠ Assessment;
- missing telemetry ≠ observed absence/missing run/output;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- Investigation ≠ evidence/causal truth;
- Lineage evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- proposed Causal Claim ≠ supported Causal Claim ≠ confirmed cause;
- leading hypothesis ≠ confirmed cause;
- rejected claim ≠ merely unsupported/lower-ranked claim;
- unresolved claim ≠ unevaluated/proposed claim;
- Investigation closure ≠ confirmation;
- causal contribution ≠ quantitative percentage attribution;
- one supported/confirmed contributor ≠ rejection of compatible contributors;
- Impact candidate/reachability ≠ exposure;
- exposure ≠ downstream effect ≠ business consequence ≠ causal attribution;
- downstream activity/refresh timing ≠ exposure to affected state;
- `not exposed` ≠ missing consumer telemetry;
- `not exposed to suspect version` ≠ current/fresh/healthy delivery;
- no encounter opportunity ≠ no encounter ≠ safe-version encounter ≠ unknown-version encounter;
- criticality ≠ actual Impact;
- safeguard proposal/configuration/request ≠ active/enforced safeguard;
- active safeguard + non-exposure ≠ automatically prevented exposure;
- prevented exposure ≠ fresh/healthy delivery;
- quarantine ≠ defect proof;
- release ≠ health proof;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth/authorization source;
- effective/event time ≠ source availability time ≠ framework recorded/knowledge time ≠ derived evaluation time;
- source availability ≠ framework knowledge;
- current state ≠ historical state;
- later evidence ≠ evidence known then;
- actual historical state ≠ replay-derived interpretation;
- actual historical control action ≠ counterfactual preferred action;
- actual retained historical Explanation ≠ reconstructed historical Explanation;
- historical Assertion Authority/Capability Authorization/control state ≠ current authority/disclosure permission;
- evidence applicability ≠ evidence coverage ≠ conclusion sufficiency;
- evidence not found ≠ observed absence;
- source count ≠ independent corroboration;
- evidence sufficiency ≠ disclosure authorization;
- `known by K` ≠ `learned after K` ≠ `not recorded by K` ≠ `not known by K` ≠ `not available by K`;
- late evidence ≠ source correction ≠ independent conflict ≠ reinterpretation ≠ later authority resolution;
- immediate operational validation ≠ enriched health evaluation ≠ investigative/RCA reasoning ≠ retrospective/post-ops review.

## Phase 004 Group 01 evidence rules — accepted REF-001–REF-005

- Bind every material evidence-sufficiency evaluation to a defined proposition/conclusion, subject, context, event time/window, grain/version, and intended conclusion strength.
- Evaluate evidence applicability before treating it as support, contradiction, exclusion, or corroboration.
- Coverage is bounded and multidimensional; name the observation universe/window before using `complete` or `sufficient coverage`.
- Negative/absence/exclusion conclusions require both an adequate opportunity to observe and sufficient coverage of relevant bounded opportunities.
- No telemetry, query failure, monitoring outage, inaccessible/restricted evidence, out-of-scope evidence, or unresolved identity/version state is not a negative fact.
- Positive and negative propositions can require asymmetric coverage.
- Do not multiply evidentiary strength because the same telemetry is copied/mirrored/indexed in several systems.
- Preserve independent, partially independent, duplicated/common-derived, complementary, contradicting, non-comparable, unavailable, and unknown relationships where provenance permits.
- Applicable evidence conflict remains explicit unless an accepted authority rule resolves the **assertion/source-standing** question. Assertion Authority never makes otherwise insufficient evidence sufficient.
- Evidence sufficiency is conclusion-relative and may resolve sufficient, insufficient, conflicting/indeterminate, non-applicable/non-comparable, unavailable, or unknown.
- Do not create a universal evidence trust/confidence number.
- Sufficiency evaluation does not grant Capability Authorization, Assertion Authority, job/safeguard/gate/confirmation authority, or action permission.

## Phase 004 Group 02 temporal and progressive-availability rules — accepted REF-006–REF-012

- Distinguish event/effective time, source production/observation time, source availability time, framework collection/retrieval time, framework recorded/knowledge time, derived evaluation time, and correction/supersession time where material.
- Source availability before a cutoff does not mean the framework knew the evidence by that cutoff.
- Current retrieval of an old source record gives current framework knowledge unless retained evidence proves earlier framework knowledge.
- For event/window `T` and cutoff `K`, an `as-known` cut includes only evidence applicable to `T` that was known by `K`; corrections used in the cut must also be known by `K`.
- `Not known by K` is a negative epistemic claim requiring sufficient retention/collection coverage.
- Actual historical Assessment/claim/Impact/control/Explanation state requires evidence the state/action/communication existed by the cutoff; otherwise label replay-derived/reconstructed.
- Produce the narrowest trustworthy result as soon as the evidence required for that result is available.
- Preserve progressive analytical horizons: immediate operational validation, enriched health evaluation, investigative/RCA reasoning, retrospective/post-operations review.
- Do not treat those horizons as services, jobs, UI screens, fixed SLAs, or architecture tiers.
- A fast `job succeeded` result never implies pipeline health/freshness/quality/causal resolution while those evidence classes are pending.
- Do not weaken high-consequence evidence standards for latency convenience.
- Late evidence, source correction, independent conflict, semantic reinterpretation, and later authority resolution remain distinct.
- Reevaluate retained conclusions only when new/corrected evidence materially bears on their basis/applicability/coverage/contradiction set.
- Closed Investigations can become review/reopen candidates when materially challenged; do not auto-reopen every closed Investigation.
- Exact monitoring-result timing targets remain deferred to Phases 006/009/010/011.

## Phase 004 Group 03 causal epistemics rules — accepted REF-013–REF-020

- Bind a material causal proposition to cause, effect, subjects/context/time, causal role, and material mechanism/transmission assumptions.
- Accepted status vocabulary: `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`.
- `Unresolved` means substantive evaluation occurred but evidence remains insufficient/conflicting/non-discriminating/unavailable/restricted.
- `Rejected` requires sufficient contradiction/exclusion evidence under the applicable claim/rejection standard.
- Evaluate causal support/contradiction across applicable dimensions: cause/effect occurrence, temporal ordering, relationship/mechanism, encounter/transmission, semantic direction, contrasts/interventions, material alternatives, and coverage for exclusions.
- Do not collapse causal evidence into a universal numeric confidence score.
- Maintain a bounded material alternative set appropriate to Investigation scope; compatible contributors do not compete merely because several claims exist.
- `Confirmed` is a separate high-consequence evidence gate, not `strongly supported`, `leading`, `first observed`, or `Investigation closed`.
- Every confirmation requires a bound proposition, sufficient cause/effect evidence, required ordering/mechanism/transmission evidence, material contradiction/alternative review, sufficient coverage for relied-upon exclusions, named standard/profile provenance, resolved confirmation authority/capability, and provenance-bearing confirmation action.
- Phase 004 does not decide who/what has confirmation authority; titles/roles/service identity/automation do not self-authorize.
- Automated confirmation is possible only if later accepted semantics explicitly permit it, authorization resolves, and the evidence gate is satisfied.
- Multiple compatible contributors may be simultaneously supported/confirmed; never force one root cause.
- `Primary` requires comparative evidence; qualitative roles never imply percentage attribution.
- RCA may mature progressively; elapsed time never upgrades causal status.
- Confirmed claims remain challengeable while historical confirmation remains reconstructable.

## Phase 004 Group 04 exposure/readiness/control evidence rules — accepted REF-021–REF-030

- Bind every exposure proposition to affected subject/state/version/window, downstream candidate, historical relationship, encounter mode, consumer opportunity/window, and exact conclusion.
- Reachability, downstream timing, a refresh, or a run alone does not prove the affected state was encountered.
- Exposure to a report/output and exposure/use by a business process are separate propositions when an intermediate use boundary exists.
- Positive exposure requires actual encounter evidence sufficiently associated with the affected state.
- `Not exposed` requires sufficient negative-consumption and material-path coverage.
- Preserve no encounter opportunity, no encounter, safe-version encounter, unknown-version encounter, unavailable/restricted evidence, and affected-state encounter separately where material.
- Safe-version use can establish non-exposure to suspect V while still being stale.
- Readiness is criterion-relative. Bind gate/downstream opportunity, prerequisite set, criterion/profile/version, event/current-cycle context, evidence cut, and evaluation time.
- Completion, output existence, expected version/currentness, freshness, publication availability, and named quality conditions remain separate readiness predicates when required.
- A failed required predicate may establish not-ready; an unresolved required predicate remains unknown/conflicting/unavailable unless the criterion logically resolves otherwise.
- A fallback can act on readiness uncertainty but never converts it to `ready`.
- Preserve readiness evaluation, gate decision/action, opportunity-specific enforcement, and actual Execution History as separate evidence claims.
- If reliable Execution History shows a downstream run began during an applicable unoverridden hold, full hold enforcement is contradicted.
- Lack of a run supports hold enforcement only with sufficient execution-opportunity/history coverage.
- An admitted opportunity that never runs does not by itself prove admission failed; the gate only removes its own barrier.
- Configured/enabled gate state or a decision emitted to an external control plane is not opportunity-specific enforcement proof.
- Preserve `control source unavailable`, `decision delivery unknown`, `enforcement unknown`, and `enforcement contradicted` distinctly.
- A configured fallback policy describes intended behavior; actual fallback recognition/application/enforcement/outcome requires separate evidence.
- Bind safeguard enforcement to protected subject/output/missing-output context, exact propagation boundary, consumer/path scope, effective interval, action/state, evidence source, and knowledge time.
- Safeguard proposal/configuration/activation request/operator intent is not external enforcement.
- Enforcement at one boundary/path does not silently prove all alternate routes were protected.
- `Prevented exposure` requires an enforced safeguard materially operative on the relevant encounter path, a relevant encounter opportunity/control condition, sufficient negative consumption/version evidence, and adequate alternate-path coverage.
- `Safeguard active + consumer not exposed` is insufficient when no relevant encounter opportunity existed or the safeguard was incidental.
- Blocking suspect V does not prove downstream freshness/health; earlier state or non-delivery remains separately assessed.
- Control-effect causal claims use REF-013–REF-020. Direct deterministic mechanism evidence may support strong status quickly, but broader delay/non-delivery/business consequence claims still require material alternatives/coverage review.
- Late enforcement/execution/refresh/version/consumption evidence may revise retrospective readiness/exposure/prevention/causal conclusions without rewriting historical decisions/actions/executions/Explanations.

## Phase 004 Group 05 consolidation / exit rules — accepted

- REF-001–REF-030 compose across E-01–E-22 and all Phase 004 scenario checks without another synchronization or refinement contract.
- Negative-evidence semantics remain unified across run/output absence, historical negative claims, causal exclusion, non-exposure, control suppression, and prevented exposure.
- Progressive analytical availability never weakens evidence burden.
- Passive monitoring remains non-blocking for ungated production; explicitly gated paths may later require stronger/faster control-path availability.
- Evidence sufficiency remains separate from source authority, Capability Authorization, control authority, and confirmation authority.
- Historical reevaluation remains non-rewriting across Assessment, causality, exposure, readiness, enforcement, prevention, and Explanation.
- Phase 005 may refine authority/capability but must not redefine the Phase 004 evidence meaning of any accepted conclusion.

## Phase 005 Group 01 Assertion Authority rules — accepted AUTH-001–AUTH-008

- **Assertion Authority is the 24th concept.** It owns authority standing/rules, not assertions belonging to Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation, or later metric/threshold state.
- Bind authority resolution to an explicit authority target: concept/category/facet/scheme/type, subject scope, context, effective interval, and knowledge cutoff where relevant.
- Preserve source assertions regardless of standing.
- Common standing states include authoritative, advisory, explicitly non-authoritative, conditional, unknown, unavailable, and conflicting.
- Keep assertion disagreement, resolved assertion disagreement, authoritative assertion conflict, and authority-rule conflict distinct.
- Authority rules require provenance and an accepted governing basis/trust root appropriate to the environment. A source/rule cannot self-promote merely by claiming authority.
- Do not use source count, recency, synchronization/ingestion order, availability, repository ownership, admin/title/responsibility, or apparent specificity as hidden precedence.
- More-specific-wins behavior is valid only when explicitly defined by an accepted rule.
- Sole authority, co-authority, ordered precedence, and conditional/fallback authority are permitted only when explicitly defined.
- Co-authoritative disagreement remains authoritative conflict unless another accepted resolver applies.
- Conditional/fallback authority requires evidence that the rule's activation condition is satisfied.
- Unknown/unavailable authority never means the most convenient source may decide.
- Prospective revision, correction, supersession, retirement, and late discovery remain distinct.
- Authority is bitemporal: current corrections may revise retrospective resolution without changing what authority was known/used at an earlier cutoff.
- Assertion Authority ≠ Capability Authorization. Permission to submit/edit an assertion does not make it authoritative; authoritative standing does not grant unrelated action permission.
- Assertion Authority ≠ Responsibility Assignment / Policy Context / Classification / Monitoring Scope.
- Assertion Authority does not waive REF-001–REF-030, prove factual correctness, prove compliance, or prove enforcement.
- Concrete source/vendor authority assignments remain category/environment-specific later work; do not infer that Collibra, Immuta, Databricks/Unity Catalog, GitHub, or a human role is universally authoritative.

## Passive monitoring / integration-independence rules

- Baseline monitoring is **out-of-band and non-blocking by default**.
- Monitoring collection, Assessment, Investigation, Impact analysis, or Explanation must not become a production start dependency merely because an asset is monitored.
- Monitoring-framework degradation must not delay ungated production jobs.
- Prefer Databricks/platform/source metadata and independently deployed monitoring components over ETL-code changes, injected framework libraries, or monitoring steps in every production GitHub Actions workflow when equivalent evidence is available externally.
- Production-repository independence is an architectural objective, not an absolute guarantee; future exceptions must be explicit, minimal, and justified.

## Execution Gate rules

- **Execution Gate is optional active control.** Lineage, schedule timing, readiness Assessment, or Assertion Authority does not silently enable gating.
- A gate may hold a downstream execution opportunity until explicitly declared prerequisite readiness is evidenced.
- Gate `hold` does not mean execution failure; `admit` does not prove execution occurred; `override` does not prove readiness.
- Missing readiness/control evidence is not automatically ready.
- Never invent a universal fail-open/fail-closed policy. Unknown/unavailable behavior, timeout, escalation, expiry, and override must come from explicit accepted semantics/configuration.
- Gate configuration/control/override authority is resolved separately through Capability Authorization/later high-consequence authority semantics.
- Execution Gate controls start/admission; Propagation Safeguard controls output/consumption propagation.
- Gate-induced delay/non-delivery remains Observation/Assessment/Impact evidence; causal propositions use Causal Claim.
- Do not choose Databricks Workflows dependencies, external orchestration, sensors, event triggers, or another gate implementation before technical architecture.

## Capability Authorization / analytical projection rules

- Capability Authorization answers whether a principal may perform a named capability on a subject/context/time; it does not select IAM/enforcement architecture.
- Never infer authorization from Responsibility Assignment, Assertion Authority, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, platform-admin status, Investigation role, or causal expertise.
- Raw-data read, derived health/metric visibility, governance metadata visibility, Lineage/RCA participation, job/run operational control, safeguard actions, gate actions/override, causal-confirmation capability, and Explanation access are independently resolvable.
- A restricted-data analyst may perform approved RCA/Impact analysis over safe aggregate/redacted/opaque evidence without direct row access.
- Analytical visibility never implies permission to retry/update/modify a job, activate a safeguard, override a gate, confirm a Causal Claim, or authoritatively define governance state.
- Derived metrics/thresholds/Lineage/policy/causal/Impact/gate/authority details may themselves be restricted.
- Missing authorization evidence is not permission.
- Authorized Analytical Projection is a view over permitted concept state; it does not create truth or declassify by inference.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized audience.
- Historical authorization/authority/control/confirmation state is evidence about past state; current requester authorization governs current disclosure.
- Permission to perform an action is not evidence the action succeeded.

## Investigation / causality rules

- Investigation starts from a question/outcome, not a presumed cause.
- Use historical typed Lineage for candidate discovery; current/planned topology cannot silently replace incident-time topology.
- First-observed deviation is localization, not root cause.
- Preserve supporting and contradicting evidence.
- Negative/exclusion evidence requires sufficient applicability and coverage.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, gate state, Prospective Impact, authority state, or intent consistency alone.
- Every causal proposition belongs in Causal Claim.
- Multiple contributors/unresolved outcomes are valid.
- Investigation closure never changes Causal Claim status.
- Human reproducible findings use Observation/Change; causal interpretations use Causal Claim; contextual notes use Annotation.

## Runtime / safeguard rules

- Treat execution duration/dependency latency as first-class operational evidence.
- Use the correct time-valid Expectation/Baseline.
- Ordinary Baseline variation must not become alert noise.
- Propagation Safeguard is protective state, not health/cause truth.
- Activation requires explicit safeguard capability/authority and enforcement evidence where applicable.
- Safeguard-induced delay remains observable/assessable; causal attribution uses Causal Claim evidence/status rules.

## Downstream Impact rules

- Historical downstream Lineage yields Impact candidates only.
- Exposure requires actual encounter/consumption evidence appropriate to the consumer class.
- `Not exposed` requires sufficient negative consumption/refresh/version/path coverage; missing telemetry cannot become non-exposure.
- Downstream effect uses Observation/Assessment/Change and can exist while exposure remains unknown.
- Exposure can exist while monitored downstream health remains acceptable.
- Technical/analytical/business consequence requires separate provenance-bearing evidence.
- Criticality/client-facing/Classification/Policy Context may affect priority but do not manufacture exposure/effect/consequence/compliance harm.
- Any assertion that an origin, gate, or safeguard caused/contributed to downstream effect/consequence belongs in Causal Claim.
- Prevented exposure requires Phase 004 safeguard-enforcement/material-control plus negative-consumption/path evidence.
- Blocking a suspect version does not prove fresh/healthy downstream delivery.
- A safeguard or gate may correctly prevent stale/suspect propagation while separately causing lateness/non-delivery.

## Annotation / Explanation rules

- Annotation remains attributed human context; structured facts/claims/intents/norms/governance assertions route to owning concepts.
- Disputed/withdrawn Annotation cannot be presented as uncontested current fact.
- Explanation composes only from the Authorized Analytical Projection.
- Explanation preserves statement-to-basis traceability, Impact layers, exact Causal Claim status, Assertion Authority standing/conflict, readiness/control evidence state, human-source status, policy/authorization limitations, and temporal perspective.
- Never paraphrase `supported`, `weakened`, or `unresolved` as `confirmed root cause`.
- Never paraphrase `configured/requested` control as `enforced`, `not exposed to suspect version` as `healthy/current`, or advisory assertion as authoritative state.
- Safe omission/redaction cannot be worded as evidence hidden entities/evidence/authority rules do not exist.
- Explanation may surface authorized operational/gate/confirmation capability but never executes the action.

## Historical replay rules — Phase 003 Group 06 + Phase 004/005 refinement

- Historical replay uses **event/effective time + recorded/knowledge cutoff**.
- Resolve each concept, Assertion Authority, Capability Authorization, and control state from evidence/rules available under the cut; never project current identity/topology/reference/governance/authority/authorization/control backward.
- Evidence or authority rules recorded later but effective earlier are excluded from a contemporaneous cut and may appear in a later retrospective cut.
- Distinguish actual historical state/authority resolution from replay-derived interpretation.
- Late/corrected evidence or authority rules may create a new retrospective conclusion; preserve the prior contemporaneous conclusion.
- A historical confirmed Causal Claim remains reconstructable even if later evidence changes current status.
- Historical readiness/enforcement/exposure/prevention conclusions may change retrospectively as late evidence arrives; actual gate/safeguard decisions and executions are never rewritten.
- Do not backfill later realized Lineage/Impact/causal/authority evidence into earlier prospective knowledge.
- If no historical Explanation snapshot exists, an `as-known-then` answer is reconstructed.
- Historical Assertion Authority and Capability Authorization are evidence about past standing/permission; current authority/requester authorization govern current resolution/disclosure.
- Partial/unknown/conflicting/restricted replay remains valid rather than being completed by guesswork.

## Metric-health handoff

- Table health is broader than successful load occurrence.
- Phase 005 Group 03 may decide **who** may define/approve/revise/waive/retire metric profiles, Expectations, thresholds, margins/tolerance bands, severity, or high-consequence metric use.
- Phase 006 owns metric families, metric profiles, threshold/statistical semantics, metric-bloat controls, technical/business health composition, selective metric propagation/reconciliation, and metric timing objectives.
- Phase 007 later owns Lineage-aware propagation behavior.
- Metrics do not recursively propagate merely because Lineage exists.
- Technical and business metric views are authorized projections over the same health truth, not separate truth models.

## Phase direction

- Phase 003 is complete: SYN-001–SYN-035.
- Phase 004 is complete: REF-001–REF-030; Group 05 exit accepted; D-140–D-152.
- Pre-Phase-005 metric-health planning accepted: D-153–D-160.
- Phase 005 Group 01 accepted: Assertion Authority + AUTH-001–AUTH-008; D-161–D-172.
- **Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**
- Do not begin Group 02 or later groups without explicit user request.
- Phase 005 authority decisions must not weaken Phase 004 evidence burdens or select technical architecture.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until explicitly authoritative for required categories. Do not select RBAC/ABAC, IAM provider, Assertion Authority implementation/rule engine, graph database, event/temporal store, quarantine store, scheduler/orchestrator, Execution Gate implementation, LLM, causal algorithm, or technical architecture prematurely.
