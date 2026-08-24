# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Four explicit post-exit addenda are now accepted: **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**. Current accepted concept count: **24**.

**Phase 003 is complete. Groups 01–06 are accepted. Accepted synchronization range: SYN-001–SYN-035. E-01–E-22 pass end-to-end consolidation.**

**Phase 004 — Evidence, Time, and Causality Refinement is complete. Groups 01–05 are accepted with REF-001–REF-030.**

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is active. Groups 01–05 are accepted with AUTH-001–AUTH-043. Group 06 — Disclosure, Explanation & Audience Governance is next and has not started.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, deployment workflows, quarantine implementations, gate/orchestration implementations, IAM implementations, assertion-authority engines, approval/workflow engines, graph/causal engines, LLMs, or prototypes unless the user explicitly advances the project into technical design.

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
- metric meaning ≠ metric-profile selection ≠ threshold/margin authority ≠ severity authority ≠ waiver authority ≠ high-consequence-use eligibility;
- Baseline-derived range ≠ normative Expectation unless explicitly adopted;
- criticality ≠ threshold severity ≠ actual Impact;
- waiver/exception ≠ rewritten Observation/Baseline/Assessment ≠ false `pass`;
- control-use eligibility ≠ control capability ≠ evidence readiness ≠ enforcement;
- proposal/request ≠ approval/authorization ≠ action issuance ≠ control-plane acceptance ≠ enforcement/effect ≠ outcome;
- confirmation authority ≠ causal evidence sufficiency;
- job operation ≠ raw-data access ≠ gate authority ≠ safeguard authority;
- gate configuration ≠ normal hold/admit operation ≠ override ≠ enforcement;
- safeguard proposal ≠ activation ≠ release ≠ health;
- capability exercise ≠ delegation authority;
- delegated capability ≠ implicit re-delegation;
- break-glass ≠ universal superuser ≠ evidence/readiness/health/cause truth;
- service/model technical ability ≠ high-consequence authority;
- authorization unknown/conflicting/unavailable ≠ invented allow/deny;
- existing control state ≠ authority to change it;
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
- historical Assertion Authority/Capability Authorization/control/normative state ≠ current authority/disclosure permission;
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
- Human title/service identity/automation does not self-authorize confirmation.
- Multiple compatible contributors may be simultaneously supported/confirmed; never force one root cause.
- `Primary` requires comparative evidence; qualitative roles never imply percentage attribution.
- RCA may mature progressively; elapsed time never upgrades causal status.
- Confirmed claims remain challengeable while historical confirmation remains reconstructable.

## Phase 004 Group 04 exposure/readiness/control evidence rules — accepted REF-021–REF-030

- Bind every exposure proposition to affected subject/state/version/window, downstream candidate, historical relationship, encounter mode, consumer opportunity/window, and exact conclusion.
- Reachability, downstream timing, a refresh, or a run alone does not prove the affected state was encountered.
- Positive exposure requires actual encounter evidence sufficiently associated with the affected state.
- `Not exposed` requires sufficient negative-consumption and material-path coverage.
- Safe-version use can establish non-exposure to suspect V while still being stale.
- Readiness is criterion-relative and keeps completion/output/version/freshness/publication/quality predicates separate when required.
- A fallback can act on readiness uncertainty but never converts it to `ready`.
- Preserve readiness evaluation, gate decision/action, opportunity-specific enforcement, and actual Execution History as separate evidence claims.
- If reliable Execution History shows a downstream run began during an applicable unoverridden hold, full hold enforcement is contradicted.
- Configured/enabled gate state or a decision emitted to an external control plane is not opportunity-specific enforcement proof.
- Safeguard proposal/configuration/activation request/operator intent is not external enforcement.
- `Prevented exposure` requires an enforced safeguard materially operative on the relevant encounter path, a relevant encounter opportunity/control condition, sufficient negative consumption/version evidence, and adequate alternate-path coverage.
- Blocking suspect V does not prove downstream freshness/health.
- Control-effect causal claims use REF-013–REF-020.
- Late enforcement/execution/refresh/version/consumption evidence may revise retrospective conclusions without rewriting historical decisions/actions/executions/Explanations.

## Phase 004 Group 05 consolidation / exit rules — accepted

- REF-001–REF-030 compose across E-01–E-22 and all Phase 004 scenario checks without another synchronization or refinement contract.
- Negative-evidence semantics remain unified across run/output absence, historical negative claims, causal exclusion, non-exposure, control suppression, and prevented exposure.
- Progressive analytical availability never weakens evidence burden.
- Passive monitoring remains non-blocking for ungated production; explicitly gated paths may later require stronger/faster control-path availability.
- Evidence sufficiency remains separate from source authority, Capability Authorization, control authority, and confirmation authority.
- Historical reevaluation remains non-rewriting across Assessment, causality, exposure, readiness, enforcement, prevention, and Explanation.

## Phase 005 Group 01 Assertion Authority rules — accepted AUTH-001–AUTH-008

- **Assertion Authority is the 24th concept.** It owns authority standing/rules, not assertions belonging to Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation, or later metric/threshold state.
- Bind authority resolution to an explicit authority target: concept/category/facet/scheme/type, subject scope, context, effective interval, and knowledge cutoff where relevant.
- Preserve source assertions regardless of standing.
- Keep assertion disagreement, resolved assertion disagreement, authoritative assertion conflict, and authority-rule conflict distinct.
- Authority rules require provenance and accepted governing basis; no self-promotion.
- Never infer authority/precedence from source count, recency, ingestion order, availability, repository ownership, admin/title/responsibility, or apparent specificity.
- Sole authority, co-authority, ordered precedence, and fallback are valid only when explicit.
- Fallback requires explicit rule plus evidenced activation condition.
- Authority is bitemporal and non-rewriting.
- Assertion Authority ≠ Capability Authorization ≠ evidence sufficiency ≠ enforcement.

## Phase 005 Group 02 semantic/governance authority rules — accepted AUTH-009–AUTH-015

- Semantic authority is facet-specific across business/technical/schema/grain/key/unit/population/calculation/field-role meaning.
- Preserve **declared/governed schema meaning ≠ normative schema contract ≠ realized schema state ≠ compatibility Assessment**.
- Declared key role does not prove observed uniqueness/nullability.
- Responsibility authority is responsibility-type scoped.
- Classification authority is scheme/context specific; criticality remains Classification.
- Policy text/reference authority may differ from subject/context applicability authority.
- Specific/local governance does not automatically override broader governance.
- Lineage/container/tag inference does not silently propagate governance assertions/authority.
- Descriptive governance truth does not become normative health, access, enforcement, compliance, or Impact truth.

## Phase 005 Group 03 normative health rules — accepted AUTH-016–AUTH-023

- Expectation authority is subject/dimension/property/context/time/action scoped.
- **Metric meaning ≠ profile selection ≠ threshold/margin ≠ severity ≠ waiver ≠ high-consequence-use eligibility.**
- Metric profiles are governed selection/applicability structures, not truth concepts.
- Technical availability is not sufficient for profile inclusion; resist metric bloat.
- Baseline regularity is descriptive until an authoritative Expectation adopts a norm.
- Structural/schema compatibility Expectations require explicit normative authority.
- Structural Change triggers scoped metric/profile/Baseline review; governance cannot manufacture empirical comparability.
- Waiver/exception/suspension does not rewrite Observations/Baseline or create false pass.
- Normative conflict remains explicit; no strictest/business/technical/latest/highest-severity default.
- Criticality may affect priority/review, not threshold truth/Impact.
- High-consequence-use eligibility is explicit and separate from control capability/evidence/enforcement.

## Phase 005 Group 04 Capability Authorization rules — accepted AUTH-024–AUTH-032

- Capability Authorization remains the permission truth owner; no 25th concept.
- Bind exact principal + capability/action + subject + context/time + material detail level.
- Preserve `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` distinctly.
- Missing/conflicting/unavailable authorization never becomes permission; runtime refusal without positive allow does not invent a deny.
- No universal deny/direct-user/role/latest/specificity precedence.
- Principal composition and capability inheritance require explicit rules and historical evidence.
- Raw data, schema, metrics, thresholds, Baselines, Lineage, RCA, causal/Impact/control state, authority basis, normative actions, and Explanation may be independently authorized.
- Result visibility does not imply basis visibility; hidden basis remains restricted, not absent.
- Normative action permission and Assertion Authority over the result remain separate.
- Authorized Analytical Projection is a synchronization/view over existing truth, not declassification/new truth.
- Requester visibility and framework/service-principal processing authorization are separate.
- Aggregated/derived monitoring evidence can still be sensitive/inference-leaking.
- Historical authorization is non-rewriting and not reusable current permission.
- Authorization does not prove action occurrence, enforcement, or success.

## Phase 005 Group 05 high-consequence authority rules — accepted AUTH-033–AUTH-043

- Bind high-consequence authorization to exact action/lifecycle stage: request/propose, approve/authorize, execute/issue, override/release/cancel, review.
- Broad `admin`, `operator`, `owner`, `on-call`, or service-account labels never create universal authority.
- Causal confirmation remains jointly evidence- and authority-gated. Human/automated confirmation is claim-class/profile scoped.
- Job trigger/retry/restart/cancel/other operations are granular and independent from raw-data, gate, safeguard, and deployment authority.
- Gate registration/configuration/readiness-fallback configuration/enable-disable/ordinary hold-admit execution/override/retirement may have different principals.
- Override never changes readiness truth and authorization never proves enforcement.
- Safeguard proposal/approval/activation/extension/cancel/release/retirement are independently governable; release does not prove health.
- Multi-party approval, quorum, ordering, independence, and self-approval rules exist only when explicit; approval completion does not execute action.
- Capability exercise does not imply delegation authority; delegated grants are bounded, historical, expiring/revocable, and re-delegation is not implicit.
- Break-glass requires explicit scope/condition/time/provenance/review rules; urgency or authorization outage does not create it.
- Break-glass does not create raw-data access, readiness, health, causal evidence, or enforcement truth.
- Automated/service-principal action requires exact explicit capability; technical ability/model recommendation is not authority and required human review cannot be bypassed.
- Authorization-outage fallback is action-specific; no universal fail-open/fail-closed/always-hold/always-release rule.
- Existing protective control state during an outage is separate from authority to change it.
- Preserve request → approval/authorization → issuance → external acceptance → enforcement/effect → resulting state/outcome as separate provenance-bearing stages.
- Group 05 requires no 25th concept.

## Passive monitoring / integration-independence rules

- Baseline monitoring is **out-of-band and non-blocking by default**.
- Monitoring collection, Assessment, Investigation, Impact analysis, or Explanation must not become a production start dependency merely because an asset is monitored.
- Monitoring-framework degradation must not delay ungated production jobs.
- Prefer Databricks/platform/source metadata and independently deployed monitoring components over ETL-code changes, injected framework libraries, or monitoring steps in every production GitHub Actions workflow when equivalent evidence is available externally.
- Production-repository independence is an architectural objective, not an absolute guarantee; future exceptions must be explicit, minimal, and justified.

## Execution Gate rules

- **Execution Gate is optional active control.** Lineage, schedule timing, readiness Assessment, Assertion Authority, or high-consequence-use eligibility does not silently enable gating.
- A gate may hold a downstream execution opportunity until explicitly declared prerequisite readiness is evidenced.
- Gate `hold` does not mean execution failure; `admit` does not prove execution occurred; `override` does not prove readiness.
- Missing readiness/control evidence is not automatically ready.
- Never invent a universal fail-open/fail-closed policy.
- Gate authorization is decomposed by Group 05; configuration/operation/override permission remains separate from enforcement evidence.
- Execution Gate controls start/admission; Propagation Safeguard controls output/consumption propagation.
- Gate-induced delay/non-delivery remains Observation/Assessment/Impact evidence; causal propositions use Causal Claim.
- Do not choose Databricks Workflows dependencies, external orchestration, sensors, event triggers, or another gate implementation before technical architecture.

## Capability Authorization / analytical projection rules

- Capability Authorization answers whether a principal may perform a named capability on a subject/context/time; it does not select IAM/enforcement architecture.
- Never infer authorization from Responsibility Assignment, Assertion Authority, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, platform-admin status, Investigation role, causal expertise, normative authority, or control-use eligibility.
- Raw-data read, derived health/metric visibility, governance metadata visibility, Lineage/RCA participation, job/run operational control, safeguard actions, gate actions/override, causal-confirmation capability, and Explanation access are independently resolvable.
- A restricted-data analyst may perform approved RCA/Impact analysis over safe aggregate/redacted/opaque evidence without direct row access.
- Analytical visibility never implies production-control or causal-confirmation authority.
- Derived metrics/thresholds/schema/Lineage/policy/causal/Impact/gate/authority/approval/break-glass details may themselves be restricted.
- Missing authorization evidence is not permission.
- Authorized Analytical Projection is a view over permitted concept state; it does not create truth or declassify by inference.
- Historical authorization/authority/control/confirmation state is evidence about past state; current requester authorization governs current disclosure.
- Permission to perform an action is not evidence the action succeeded.

## Investigation / causality rules

- Investigation starts from a question/outcome, not a presumed cause.
- Use historical typed Lineage for candidate discovery; current/planned topology cannot silently replace incident-time topology.
- First-observed deviation is localization, not root cause.
- Preserve supporting and contradicting evidence.
- Negative/exclusion evidence requires sufficient applicability and coverage.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, gate state, Prospective Impact, authority state, authorization state, or intent consistency alone.
- Every causal proposition belongs in Causal Claim.
- Multiple contributors/unresolved outcomes are valid.
- Investigation closure never changes Causal Claim status.
- Confirmation requires both REF evidence and Group 05 confirmation capability/authority.

## Runtime / safeguard rules

- Treat execution duration/dependency latency as first-class operational evidence.
- Use the correct time-valid Expectation/Baseline/waiver state.
- Ordinary Baseline variation must not become alert noise.
- Propagation Safeguard is protective state, not health/cause truth.
- Safeguard proposal, activation, release and related authority are independently governed; permission does not prove enforcement.
- Safeguard-induced delay remains observable/assessable; causal attribution uses Causal Claim evidence/status rules.

## Downstream Impact rules

- Historical downstream Lineage yields Impact candidates only.
- Exposure requires actual encounter/consumption evidence appropriate to the consumer class.
- `Not exposed` requires sufficient negative consumption/refresh/version/path coverage; missing telemetry cannot become non-exposure.
- Downstream effect uses Observation/Assessment/Change and can exist while exposure remains unknown.
- Technical/analytical/business consequence requires separate provenance-bearing evidence.
- Criticality/client-facing/Classification/Policy Context may affect priority but do not manufacture exposure/effect/consequence/compliance harm.
- Any assertion that an origin, gate, or safeguard caused/contributed to downstream effect/consequence belongs in Causal Claim.
- Prevented exposure requires Phase 004 safeguard-enforcement/material-control plus negative-consumption/path evidence.
- Blocking a suspect version does not prove fresh/healthy downstream delivery.

## Annotation / Explanation rules

- Annotation remains attributed human context; structured facts/claims/intents/norms/governance assertions route to owning concepts.
- Explanation composes only from the Authorized Analytical Projection.
- Explanation preserves statement-to-basis traceability, Impact layers, exact Causal Claim status, Assertion Authority standing/conflict, normative rule/waiver state, readiness/control evidence state, high-consequence authorization/action stage, human-source status, policy/authorization limitations, and temporal perspective.
- Never paraphrase `supported`, `weakened`, or `unresolved` as `confirmed root cause`.
- Never paraphrase `configured/requested` control as `enforced`, `not exposed to suspect version` as `healthy/current`, advisory assertion as authoritative state, waived violation as a clean underlying measurement, or approved action as executed/enforced.
- Safe omission/redaction cannot be worded as evidence hidden entities/evidence/authority/authorization rules do not exist.
- Explanation may surface authorized operational/gate/confirmation capability but never executes the action.

## Historical replay rules — Phase 003 Group 06 + Phase 004/005 refinement

- Historical replay uses **event/effective time + recorded/knowledge cutoff**.
- Resolve each concept, Assertion Authority, Capability Authorization, normative rule/waiver, approval/delegation/break-glass/control state from evidence/rules available under the cut; never project current state backward.
- Evidence or authority rules recorded later but effective earlier are excluded from a contemporaneous cut and may appear in a later retrospective cut.
- Distinguish actual historical state/authority/authorization/action from replay-derived interpretation.
- Late/corrected evidence or authority/authorization rules may create a new retrospective conclusion; preserve the prior contemporaneous conclusion.
- A historical confirmed Causal Claim remains reconstructable even if later evidence changes current status.
- Historical gate/safeguard approvals/actions/enforcement and executions are never rewritten.
- Historical Assertion Authority and Capability Authorization are evidence about past standing/permission; current authority/requester authorization govern current resolution/disclosure.
- Partial/unknown/conflicting/restricted replay remains valid rather than being completed by guesswork.

## Metric-health handoff

- Table health is broader than successful load occurrence.
- Phase 005 Group 03 has accepted **who** can govern metric profiles, structural/schema Expectations, thresholds, margins/tolerance bands, severity, waivers/retirement, and high-consequence-use eligibility through AUTH-016–AUTH-023.
- Phase 006 owns metric families, metric/statistical/schema-health semantics, Baseline comparability behavior, metric-bloat operational semantics, technical/business health composition, selective metric propagation/reconciliation, waiver presentation, and metric timing objectives.
- Phase 007 later owns Lineage-aware propagation behavior.
- Metrics do not recursively propagate merely because Lineage exists.
- Technical and business metric views are authorized projections over the same health truth, not separate truth models.

## Phase direction

- Phase 003 is complete: SYN-001–SYN-035.
- Phase 004 is complete: REF-001–REF-030; Group 05 exit accepted; D-140–D-152.
- Pre-Phase-005 metric-health planning accepted: D-153–D-160.
- Phase 005 Group 01 accepted: Assertion Authority + AUTH-001–AUTH-008; D-161–D-172.
- Phase 005 Group 02 accepted: AUTH-009–AUTH-015; D-173–D-188.
- Phase 005 Group 03 accepted: AUTH-016–AUTH-023; D-189–D-202.
- Phase 005 Group 04 accepted: AUTH-024–AUTH-032; D-203–D-217.
- Phase 005 Group 05 accepted: AUTH-033–AUTH-043; D-218–D-234.
- **Group 06 — Disclosure, Explanation & Audience Governance is next and has not started.**
- Do not begin Group 06 or later groups without explicit user request.
- Phase 005 authority decisions must not weaken Phase 004 evidence burdens or select technical architecture.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until explicitly authoritative for required categories. Do not select RBAC/ABAC, IAM provider, Assertion Authority implementation/rule engine, approval workflow engine, graph database, event/temporal store, quarantine store, scheduler/orchestrator, Execution Gate implementation, LLM, causal algorithm, or technical architecture prematurely.
