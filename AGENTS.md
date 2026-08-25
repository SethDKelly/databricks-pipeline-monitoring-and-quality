# Repository Agent Instructions

## Project status authority

The accepted concept catalog contains **24 concepts**: the original 20 plus **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**.

**Live repository phase and group progression is declared only in [`docs/README.md#current-state`](docs/README.md#current-state).** This root agent file intentionally does not maintain a parallel current/next phase declaration. For Phase 007 group-local accepted contracts and handoff, use [`docs/concepts/phase_007/AGENTS.md`](docs/concepts/phase_007/AGENTS.md).

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, IAM implementations, assertion-authority engines, approval/workflow engines, deployment workflows, quarantine implementations, gate/orchestration implementations, metric engines, graph/causal engines, redaction systems, LLMs, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the product/design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, API, persisted view, scheduler, orchestrator, temporal snapshot, or replay store.
- Phase 004 `REF-###` artifacts refine evidence/time/causal/control standards over accepted concepts/synchronizations.
- Phase 005 `AUTH-###` artifacts refine authority/governance/capability/disclosure standards over accepted concepts.
- Phase 006 `HLTH-###` artifacts refine health/metric/schema/statistical/reconciliation/composite/timing semantics over accepted concepts.
- Phase 007 `OPS-###` artifacts refine operational/topology/change/impact/control semantics over accepted concepts.
- REF, AUTH, HLTH, and OPS identifiers do not create hidden truth owners or extend the Phase 003 SYN range.
- Synchronization/refinement order is never authority; a trigger is never causation.
- Do not create umbrella state for implementation convenience.
- Reopen accepted boundaries only explicitly, with a concrete scenario that cannot be represented otherwise.

## Immutable environment facts

- multiple Git repositories;
- GitHub Actions deploy jobs to Databricks;
- Spark ETL pipelines;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a major runtime/metadata source;
- Databricks Metric Views and DQX are favored later evaluations, not selected architecture;
- Collibra and Immuta are available but optional;
- no technical architecture is selected.

## Core invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- Responsibility Assignment ≠ Assertion Authority ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Assertion Authority ≠ Capability Authorization ≠ compliance;
- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization ≠ action/enforcement authority ≠ disclosure authority;
- source assertion ≠ authoritative assertion;
- authoritative standing ≠ factual infallibility;
- authoritative standing ≠ permission to act/view/disclose;
- authoritative rule/configuration ≠ actual enforcement;
- metric/schema meaning ≠ metric-profile selection ≠ threshold/margin ≠ severity ≠ waiver ≠ high-consequence-use eligibility;
- metric definition ≠ metric Observation ≠ Assessment;
- semantic metric applicability ≠ profile selection ≠ source support/computability ≠ current evidence availability ≠ Assessment outcome;
- `not applicable` ≠ `not selected` ≠ `unsupported` ≠ `unavailable` ≠ `pending` ≠ `pass`;
- same metric display name ≠ same definition/version when material calculation semantics change;
- available statistic ≠ useful routine metric;
- local metric ≠ downstream propagated/reconciliation metric;
- producer physical schema ≠ consumer-visible interface schema;
- declared/governed schema meaning ≠ structural Expectation ≠ proposed/planned state ≠ realized structural Observation/Change ≠ compatibility Assessment;
- add/drop coincidence ≠ rename identity;
- engine cast capability ≠ consumer compatibility;
- structural compatibility ≠ statistical/Baseline comparability;
- Observation ≠ reference-set membership ≠ Baseline summary/version ≠ comparative Assessment ≠ normative Expectation;
- available history ≠ eligible reference history;
- directly comparable ≠ comparable only under explicit normalization ≠ non-comparable;
- within Baseline ≠ healthy/meets Expectation;
- outside Baseline ≠ failed/degraded/unacceptable;
- Baseline-derived range ≠ normative Expectation unless explicitly adopted;
- criterion outcome ≠ warning/proximity ≠ Baseline typicality ≠ severity/priority ≠ waiver/disposition;
- criticality ≠ threshold severity ≠ actual Impact;
- waiver/exception ≠ rewritten Observation/Baseline/Assessment ≠ false `pass`;
- Lineage relationship proposition ≠ generic graph edge;
- Lineage relation ≠ metric/status propagation;
- Lineage reachability ≠ question-bound operational relevance;
- operational relevance ≠ encounter/exposure ≠ Impact ≠ cause;
- asset-level relationship ≠ field/key/population/consumer-specific relationship unless evidenced;
- planned topology ≠ effective Lineage topology ≠ specific runtime/consumer encounter;
- Lineage `established` ≠ `absent` ≠ `unknown` ≠ `conflicting` ≠ `unavailable`;
- missing edge evidence ≠ absent edge;
- no universal Lineage edge confidence/completeness score;
- Lineage Assertion Authority ≠ Lineage evidence sufficiency;
- local Observation ≠ downstream-relevant context ≠ reconciliation Observation ≠ reconciliation Assessment ≠ Causal Claim;
- reconciliation localization ≠ root cause;
- component Assessment ≠ composite health Assessment;
- composite health ≠ result freshness/maturity/suitability ≠ readiness result;
- evaluation recency ≠ evidence freshness/current-cycle validity;
- AUTH-023 control-use eligibility ≠ evidence suitability ≠ readiness ≠ control capability ≠ enforcement;
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
- assertion disagreement ≠ authoritative assertion conflict ≠ authority-rule conflict ≠ normative conflict ≠ authorization conflict ≠ disclosure conflict;
- source count/majority ≠ authority precedence;
- record recency ≠ authority precedence;
- synchronization/ingestion order ≠ authority precedence;
- source availability ≠ authority precedence;
- responsibility/title/admin/repository ownership ≠ assertion authority;
- apparent specificity ≠ precedence unless explicit;
- unavailable primary authority ≠ automatic fallback authority;
- raw-data read ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority ≠ gate authority ≠ causal-confirmation authority ≠ publication/disclosure authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification;
- view permission ≠ export/forward/publish/client disclosure;
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
- successful run ≠ timely run ≠ freshness ≠ structural compatibility ≠ data quality;
- successful upstream run ≠ criterion-bound readiness;
- Observation ≠ Assessment;
- missing telemetry ≠ observed absence/missing run/output;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- Investigation ≠ evidence/causal truth;
- Lineage candidate ≠ cause;
- first-observed localization ≠ root cause;
- proposed ≠ supported ≠ weakened ≠ unresolved ≠ rejected ≠ confirmed Causal Claim;
- leading hypothesis ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- causal contribution ≠ percentage attribution;
- one supported/confirmed contributor ≠ rejection of compatible contributors;
- Impact candidate/reachability ≠ exposure;
- exposure ≠ downstream effect ≠ business consequence ≠ causal attribution;
- downstream run/refresh timing ≠ exposure to affected state;
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
- audience simplification ≠ status upgrade;
- effective/event time ≠ source availability time ≠ framework recorded/knowledge time ≠ derived evaluation time;
- source availability ≠ framework knowledge;
- current state ≠ historical state;
- later evidence ≠ evidence known then;
- actual historical state ≠ replay-derived interpretation;
- actual historical control action ≠ counterfactual preferred action;
- actual retained historical Explanation ≠ reconstructed historical Explanation;
- historical Assertion Authority/Capability Authorization/control/normative/disclosure state ≠ current authority/disclosure permission;
- evidence applicability ≠ evidence coverage ≠ conclusion sufficiency;
- evidence not found ≠ observed absence;
- source count ≠ independent corroboration;
- evidence sufficiency ≠ disclosure authorization;
- `known by K` ≠ `learned after K` ≠ `not recorded by K` ≠ `not known by K` ≠ `not available by K`;
- late evidence ≠ source correction ≠ independent conflict ≠ reinterpretation ≠ later authority resolution;
- immediate operational validation ≠ enriched health evaluation ≠ investigative/RCA reasoning ≠ retrospective/post-ops review.

## Phase 004 evidence / time / causality / control rules — accepted

### REF-001–REF-005 — evidence sufficiency

- Bind evidence-sufficiency evaluation to a defined proposition/conclusion, subject, context, time/window, grain/version, and intended conclusion strength.
- Evaluate applicability before support/contradiction/exclusion/corroboration.
- Coverage is bounded and multidimensional.
- Negative/absence/exclusion conclusions require adequate opportunity-to-observe plus sufficient bounded coverage.
- No telemetry, query failure, monitoring outage, inaccessible/restricted evidence, out-of-scope evidence, or unresolved identity/version state is not a negative fact.
- Positive and negative propositions can require asymmetric coverage.
- Copied/mirrored/common-derived telemetry is not automatically independent corroboration.
- Evidence conflict remains explicit when unresolved.
- Sufficiency is conclusion-relative; do not create universal trust/confidence scores.
- Sufficiency does not grant authority, permission, control, confirmation, or disclosure.

### REF-006–REF-012 — temporal/progressive availability

- Distinguish event/effective time, source production/observation time, source availability, framework collection/retrieval, framework recorded/knowledge, derived evaluation, and correction/supersession time where material.
- Source availability before cutoff does not mean framework knowledge before cutoff.
- Current retrieval of an old record does not backdate framework knowledge.
- `Not known by K` is a negative epistemic claim requiring sufficient retention/collection coverage.
- Actual historical Assessment/claim/Impact/control/Explanation state requires evidence it existed then; otherwise label reconstructed.
- Produce the narrowest trustworthy result as soon as its evidence standard is met.
- Preserve immediate operational → enriched health → RCA → retrospective horizons without turning them into architecture tiers.
- Fast `job succeeded` never implies broader health while other evidence is pending.
- Do not weaken evidence standards for latency.
- Late evidence, correction, independent conflict, reinterpretation, and later authority resolution remain distinct.

### REF-013–REF-020 — causal epistemics

- Bind cause/effect/context/time/role/mechanism.
- Use `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`.
- `Rejected` requires sufficient contradiction/exclusion evidence.
- Evaluate cause/effect occurrence, temporal ordering, relationship/mechanism, encounter/transmission, semantic direction, contrasts/interventions, alternatives, and exclusion coverage as applicable.
- Maintain bounded material alternatives; compatible contributors need not compete.
- `Confirmed` is a high-consequence evidence gate, not `leading`, `first observed`, or `Investigation closed`.
- Confirmation requires the applicable profile, sufficient evidence, alternative/contradiction review, required exclusion coverage, resolved confirmation authority, and provenance-bearing confirmation action.
- Multiple contributors may be simultaneously supported/confirmed.
- `Primary` requires comparative evidence; qualitative roles never imply percentage attribution.
- Confirmed claims remain challengeable with history retained.

### REF-021–REF-030 — exposure/readiness/control

- Bind exposure to affected state/version/window, downstream candidate, historical relation, encounter mode, and opportunity.
- Reachability/run/refresh/timing alone does not prove affected-state encounter.
- Positive exposure requires actual encounter evidence.
- `Not exposed` requires negative-consumption and material-path coverage.
- Safe-version use can mean `not exposed to V` while stale.
- Readiness is criterion-relative and preserves completion/output/version/freshness/publication/quality predicates.
- Fallback can act on uncertainty but never converts it to `ready`.
- Readiness evaluation, gate decision, enforcement, and Execution History are separate.
- Reliable run during an applicable unoverridden hold contradicts full hold enforcement.
- Configured gate/decision emitted is not opportunity-specific enforcement proof.
- Safeguard request/intention is not external enforcement.
- `Prevented exposure` requires materially operative enforced control plus encounter opportunity and sufficient negative/path coverage.
- Blocking suspect V does not prove downstream freshness/health.
- Control-effect causal claims use REF-013–REF-020.
- Late enforcement/consumption evidence may revise retrospective conclusions without rewriting historical actions.

## Phase 005 authority/governance rules — accepted

### AUTH-001–AUTH-008 — authority vocabulary and conflict

- Assertion Authority owns authority standing/rules, not domain assertions.
- Bind authority to explicit target category/facet/scheme/type, subject scope, context, effective interval, and knowledge cutoff where relevant.
- Preserve source assertions regardless of standing.
- Keep disagreement, authoritative assertion conflict, and authority-rule conflict distinct.
- Authority rules require provenance/governing basis and cannot self-promote.
- Never infer authority/precedence from source count, recency, ingestion order, availability, repository ownership, title/responsibility, or apparent specificity.
- Sole authority, co-authority, precedence, and fallback exist only when explicit.
- Fallback requires explicit rule plus evidenced activation condition.
- Authority is bitemporal/non-rewriting.

### AUTH-009–AUTH-015 — semantic governance authority

- Semantic authority is facet-specific across business/technical/schema/grain/key/unit/population/calculation/field-role meaning.
- Preserve **declared/governed schema meaning ≠ normative schema contract ≠ realized schema state ≠ compatibility Assessment**.
- Declared key role does not prove uniqueness/nullability.
- Responsibility authority is responsibility-type scoped.
- Classification authority is scheme/context scoped; criticality remains Classification.
- Policy reference authority may differ from applicability authority.
- Local governance does not automatically outrank broader governance.
- Lineage/container/tag inference does not silently propagate governance assertions/authority.
- Descriptive governance does not become normative health, access, enforcement, compliance, or Impact.

### AUTH-016–AUTH-023 — normative health governance

- Expectation authority is subject/dimension/property/context/time/action scoped.
- **Metric meaning ≠ profile selection ≠ threshold/margin ≠ severity ≠ waiver ≠ high-consequence-use eligibility.**
- Metric profiles are governed selection structures; technical availability is not enough for inclusion.
- Baseline remains descriptive until an authoritative Expectation adopts a norm.
- Structural/schema compatibility Expectations require explicit normative authority.
- Structural Change triggers scoped metric/profile/Baseline review; authority cannot manufacture comparability.
- Waiver/exception/suspension does not rewrite evidence or create false pass.
- Normative conflict remains explicit; no strictest/business/technical/latest/highest-severity default.
- Criticality may affect review/priority, not threshold truth/Impact.
- High-consequence-use eligibility is separate from control capability/evidence/enforcement.

### AUTH-024–AUTH-032 — Capability Authorization

- Capability Authorization is the permission truth owner.
- Bind exact principal + capability/action + subject + context/time + material detail level.
- Preserve `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, `unavailable` distinctly.
- Missing/conflicting/unavailable authorization never becomes permission; fail-safe refusal does not invent deny.
- No universal deny/direct-user/role/latest/specificity precedence.
- Principal composition and capability inheritance require explicit rules and historical evidence.
- Raw data, schema, metrics, thresholds, Baselines, Lineage, RCA, causal/Impact/control state, authority basis, normative actions, and Explanation can be independently authorized.
- Result visibility does not imply basis visibility; hidden basis remains restricted, not absent.
- Normative action permission and Assertion Authority over the result are separate.
- Authorized Analytical Projection is a view over existing truth, not declassification/new truth.
- Framework processing authorization and requester visibility are separate.
- Aggregated/derived monitoring evidence can remain sensitive/inference-leaking.
- Historical authorization is non-rewriting and not reusable current permission.
- Authorization does not prove action occurrence, enforcement, or success.

### AUTH-033–AUTH-043 — high-consequence authority

- High-consequence authorization is action/lifecycle-stage scoped: request/propose, approve, execute/issue, override/release/cancel, review.
- Broad `admin`, `operator`, `owner`, `on-call`, or service-account labels never create universal authority.
- Causal confirmation remains jointly evidence- and authority-gated; human/automated confirmation is claim-profile scoped.
- Job trigger/retry/restart/cancel operations are granular and independent from raw-data/gate/safeguard/deployment authority.
- Gate registration/configuration/fallback/enable-disable/normal HOLD-ADMIT/override/retirement may have different principals.
- Override never changes readiness and never proves enforcement.
- Safeguard proposal/approval/activation/extension/cancel/release/retirement are independently governable; release does not prove health.
- Multi-party approval/quorum/ordering/independence/self-approval rules exist only when explicit; approvals do not execute action.
- Capability exercise does not imply delegation; delegated grants are bounded, expiring/revocable, non-transitive unless explicit.
- Break-glass requires explicit scope/condition/time/provenance/review; urgency/outage does not create it.
- Break-glass does not create data access, readiness, health, causal evidence, or enforcement truth.
- Automation requires exact service-principal capability and cannot bypass required human review.
- Authorization-outage fallback is action-specific; no universal fail-open/fail-closed/always-hold/always-release.
- Existing protective state during outage is separate from authority to change it.
- Preserve request → authorization/approval → issuance → control-plane acceptance → enforcement/effect → resulting state/outcome.

### AUTH-044–AUTH-053 — disclosure governance

- Bind disclosure to requester/audience + information/detail class + subject/context + purpose + temporal perspective + delivery scope.
- Audience labels do not grant authorization.
- View ≠ publish/export/forward/client disclosure.
- Result visibility ≠ basis/detail/source/actor/authority visibility.
- Hidden basis ≠ absent basis.
- Safe abstraction/redaction/opacity must preserve proposition meaning and uncertainty.
- Opaque existence is allowed only when existence itself may be disclosed.
- Aggregation/redaction ≠ automatic declassification.
- Evaluate mosaic/differencing/repeated-query leakage, not only single-field permission.
- Technical/business/executive/audit views are one truth at different authorized detail.
- High-consequence communication review/approval ≠ evidence sufficiency/causal confirmation/health/compliance/enforcement.
- Preserve status in wording: supported ≠ confirmed; reachable ≠ exposed; not exposed to V ≠ fresh; hold decided ≠ enforced; safeguard active ≠ prevented exposure; released ≠ healthy; waived ≠ clean pass.
- Confirmer/approver/operator/authority-holder/delegation/break-glass/service-principal metadata can be independently sensitive.
- Annotation disclosed without exact author identity remains human-provided context where material.
- Retained historical Explanation ≠ reconstructed as-known-then ≠ retrospective Explanation.
- Current requester authorization governs present historical disclosure.
- Unknown/conflicting/unavailable/unsafe-to-project disclosure state never becomes permission.

## Phase 006 health/metric rules — accepted

### HLTH-001–HLTH-008 — measurement vocabulary and profiles

- Every material measurement binds exact subject, metric/check definition/version, grain/population, window, relevant output/data/schema/current-cycle context, and material temporal context.
- Metric definition ≠ measured Observation ≠ normative/comparative Assessment.
- Calculation/extraction success is not health pass.
- Canonical metric families are operational/output; temporal/freshness; structural/schema; volume/population; completeness/missingness; uniqueness/key integrity; validity/domain; distribution/shape; relational/transformation integrity; business-semantic measurement.
- Metric profile roles are core operational/table, critical-field/business, transformation-specific reconciliation, and diagnostic/on-demand.
- Semantic applicability, governed profile selection, source support/computability, current evidence availability, and Assessment outcome are independent.
- Technical availability does not justify routine metric inclusion.
- Material Observations retain definition/source/scope/time/coverage/approximation/restriction provenance.
- Local metric existence does not imply downstream propagation.

### HLTH-009–HLTH-018 — structural/schema compatibility

- Structural observations and compatibility bind the consumer-visible interface/contract surface, not only producer physical schema.
- Preserve governed schema meaning ≠ structural Expectation ≠ planned state ≠ realized structural state ≠ compatibility Assessment.
- Add/drop/rename/reorder/type/precision/nullability/default/generated/key/grain/nested changes remain independently representable.
- Rename identity requires evidence; engine cast/parse capability does not prove compatibility.
- Key/grain changes may invalidate selected volume/uniqueness/distribution/join assumptions without automatically being defects.
- Compatibility is consumer/interface/version/time scoped and not automatically transitive.
- Prospective validation is separate from realized production validation.
- Structural change triggers scoped metric/profile/Baseline review, not global reset.
- `Compatible` requires positive evidence coverage.
- Structural incompatibility does not prove execution failure, exposure, Impact or causality.
- Validation placement remains architecture-neutral.

### HLTH-019–HLTH-029 — Baselines/comparability/statistical context

- Observation ≠ reference-set membership ≠ Baseline summary/version ≠ comparative Assessment ≠ normative Expectation/health.
- Available history is not automatically eligible reference history.
- Comparability is multidimensional and conclusion-relative; no universal comparability/confidence score.
- Fixed, rolling, seasonal/cadence, cohort and post-change Baselines are functional classes, not algorithms.
- Recency does not override business-calendar/cadence/cohort context.
- Realized semantic/structural/method breaks segment affected references only.
- New post-change Baselines derive from realized evidence, never planned targets.
- Reference sufficiency is conclusion-relative; no universal sample minimum exists.
- Low-volume, approximation/sampling and material uncertainty remain visible limitations.
- Distribution references remain purpose-driven; no universal drift score.
- Explicit normalization can support a derived comparison while raw values remain non-comparable.
- Adaptive Baselines require explicit lag/holdout/inclusion/exclusion/version semantics and cannot silently normalize incidents.
- Repeated abnormal behavior can become descriptively typical without becoming acceptable.
- Historical Baselines/Assessments remain non-rewriting.

### HLTH-030–HLTH-040 — criteria/thresholds/waivers

- Criteria bind exact subject/dimension, metric/check/structural definition, grain/population/window/context, operator/direction, boundary, unit/denominator and required reference basis.
- Warning/proximity is separate from criterion outcome and can coexist with `meets`.
- Relative criteria explicitly bind their reference; Baseline remains descriptive generally.
- Authoritative criterion + unsuitable/sparse/approximate/unavailable evidence does not create pass/fail.
- Preserve at least `meets`, `violates`, `indeterminate/insufficient evidence`, `conflicting`, `unavailable`, and `not applicable` for one bound criterion.
- Baseline typicality and normative outcome coexist independently.
- Distinct context/dimension rules can coexist; same-proposition incompatible rules remain conflict absent explicit resolver.
- `violates + waived response` differs from bounded non-applicability.
- Waiver does not mutate evidence or automatically propagate to another consequence class.
- Severity/priority does not decide criterion outcome; Criticality does not prove Impact.
- Historical rule/reference/waiver versions and corrected-evidence reassessments are non-rewriting.

### HLTH-041–HLTH-054 — transformation reconciliation

- Local Observation ≠ downstream-relevant context ≠ reconciliation Observation ≠ reconciliation Assessment ≠ Causal Claim.
- Every reconciliation binds exact transformation/version, input/output roles, fields/keys/measures, grain/population/window and cycle/version context.
- Lineage supplies relationship context but never a formula or status copy.
- Joins use directional eligible/matched/unmatched/fan-out/cardinality semantics; A+B→C never means generic row arithmetic.
- Filters, aggregation, dedupe, union/merge/upsert and null/default/cast/value logic have transformation-specific reconciliation semantics.
- Aggregation conservation is measure-specific; averages/ratios/quantiles/distinct counts are not generically composable.
- Output completion does not prove all required inputs current.
- Distribution/quantile/normalization relationships require semantics that preserve meaning.
- Derived reconciliation retains availability, coverage, approximation/uncertainty, restriction and temporal limitations; derivation is not declassification.
- Multi-hop reconciliation requires explicit valid composition.
- Upstream warning/violation/Baseline/severity/waiver never recursively propagates downstream.
- Upstream violation can coexist with downstream meets; upstream meets can coexist with downstream violation.
- Reconciliation/localization is Investigation evidence, not causal confirmation.
- Historical reconciliation uses then-effective Lineage/transformation/reconciliation/input/output versions.

### HLTH-055–HLTH-066 — composite health/readiness timing

- Component Assessment ≠ composite health Assessment ≠ result freshness/suitability ≠ readiness result ≠ gate decision ≠ enforcement ≠ execution.
- Composite health binds subject, consumer/use/context, profile/version, component roles/logic, cycle/window and evaluation/knowledge time.
- No universal majority, weighted average, health score, severity weighting or post-hoc convenient composition.
- A positive conjunctive `healthy` requires all applicable required components to meet and no required unresolved state.
- A required violation can establish degraded while unresolved/unavailable qualifiers remain visible.
- `violates + waived response` remains violation/degraded.
- Severity/criticality/priority guide governance/escalation/presentation but do not manufacture health/Impact truth.
- Technical/business/executive/audit/consumer views remain authorized projections over one underlying proposition.
- Recent evaluation does not make old evidence fresh; no universal result TTL.
- Analytical horizons are evidence/maturity semantics: immediate operational → fast core/schema/current-cycle → enriched DQ/reconciliation/distribution → diagnostic/RCA → retrospective/post-ops.
- Elapsed time never upgrades maturity; narrow trustworthy results do not wait for slower broader evidence.
- Readiness suitability is exact-opportunity bound and outcome-neutral: suitable violation can support not-ready, stale meets can be unsuitable.
- AUTH-023 high-consequence eligibility ≠ evidence suitability ≠ readiness ≠ control authority.
- Unavailable/unsuitable evidence does not invent fail-open/fail-closed/hold/release behavior.
- Passive monitoring remains non-blocking for ungated production.
- Late/corrected evidence revises broader summaries through reassessment without rewriting earlier narrow/historical results.
- Historical composite/suitability replay uses then-effective profiles/rules/evidence and knowledge cut.

## Phase 007 operational/topology rules

For live group-local status and handoff, read [`docs/concepts/phase_007/AGENTS.md`](docs/concepts/phase_007/AGENTS.md). Do not infer current group state from this root file.

Accepted operational Lineage rules from Phase 007 Group 01 include:

- every material Lineage relationship is a bounded proposition with explicit source/target identity, semantic family/role, relevant scope/version/context, effective interval and evidence basis;
- minimum Lineage families are `data_derivation`, `production`, `operational_dependency`, `publication`, and `consumption_path`;
- repository membership, Deployment/Change/execution/control/authority/causal facts remain owned by their existing concepts rather than becoming generic Lineage edges;
- field/key/population/consumer/version scope can narrow relationship meaning;
- planned topology remains Change Intent context until sufficient realization evidence establishes effective Lineage;
- effective topology does not prove a particular run/consumer encountered a particular version;
- Phase 004 evidence semantics replace generic edge confidence: applicability, provenance, opportunity/coverage, corroboration/conflict and conclusion-specific sufficiency;
- `absent` relationship conclusions require adequate negative-evidence coverage;
- runtime/catalog/code/human/platform sources have no hidden universal precedence;
- Assertion Authority over a relationship assertion remains separate from empirical evidence sufficiency;
- operational relevance is traversal-question bound and may be `relevant`, `not relevant`, or `indeterminate`;
- multi-hop relevance requires semantic scope composition rather than graph reachability alone;
- Lineage is graph-compatible but not assumed to be a DAG; traversal must remain bounded/cycle-safe;
- topology completeness is bounded to an exact relationship universe/time/scope/depth/evidence/authorization context and is never a universal percentage;
- opaque/restricted topology remains hidden/restricted rather than absent.

Phase 007 as a whole refines:

- Lineage taxonomy and historical topology evidence;
- Change Intent realization, Deployment and realized Change;
- prospective blast radius/change-aware downstream review;
- execution/dependency reconstruction;
- Investigation lifecycle and first-deviation localization;
- prospective versus actual Impact and consumer/version encounter patterns;
- Lineage-aware operational relevance under accepted reconciliation rules;
- Propagation Safeguard placement/release/recovery;
- Execution Gate classes, timeout/fallback/escalation/override/recovery;
- control-induced delay/freshness/availability effects;
- historical operational replay.

Do not let Phase 007 turn Lineage/reconciliation/localization into causality, prospective reachability into actual Impact, health/readiness into enforcement, or implementation convenience into a reason to reopen HLTH-001–HLTH-066.

## Passive monitoring / integration-independence rules

- Baseline monitoring is **out-of-band/non-blocking by default**.
- Monitoring collection, Assessment, Investigation, Impact analysis, or Explanation must not become a production start dependency merely because an asset is monitored.
- Monitoring-framework degradation must not delay ungated production jobs.
- Prefer Databricks/platform/source metadata and independently deployed monitoring components over ETL-code changes or monitoring steps in every production GitHub Actions workflow when equivalent evidence is available externally.
- Production-repository independence is an architectural objective; future exceptions must be explicit, minimal, justified.

## Execution Gate rules

- Execution Gate is optional active control; Monitoring Scope, Lineage, readiness Assessment, Assertion Authority, or control-use eligibility does not silently enable gating.
- A gate may hold a downstream opportunity until declared readiness is evidenced, admit when ready, or record an authorized override.
- Gate hold does not mean execution failure; admit does not prove run occurrence; override does not prove readiness.
- Missing readiness/control evidence is not automatically ready.
- Never invent a universal fail-open/fail-closed policy.
- Gate configuration/operation/override permission remains separate from enforcement evidence.
- Gate controls start/admission; Safeguard controls output/consumption propagation.
- Gate-induced delay/non-delivery remains Observation/Assessment/Impact evidence; causal propositions use Causal Claim.
- Do not choose Databricks Workflows dependencies, external orchestration, sensors, event triggers, or another implementation before technical architecture.

## Capability / restricted-analysis rules

- Never infer authorization from Responsibility Assignment, Assertion Authority, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, platform-admin status, Investigation role, causal expertise, normative authority, criticality, or control-use eligibility.
- A restricted-data analyst may perform approved RCA/Impact analysis over safe aggregate/redacted/opaque evidence without direct row access.
- Analytical visibility never implies production-control, causal-confirmation, or publication authority.
- Derived metrics/thresholds/schema/Lineage/policy/causal/Impact/gate/authority/approval/break-glass/disclosure detail may itself be restricted.
- Missing authorization evidence is not permission.
- Historical permission/authority/action/disclosure is evidence about past state; current requester authorization governs current disclosure.

## Investigation / causality rules

- Investigation starts from a question/outcome, not presumed cause.
- Use historical typed Lineage for candidate discovery; current/planned topology cannot replace incident-time topology.
- First-observed deviation is localization, not root cause.
- Preserve supporting and contradicting evidence.
- Negative/exclusion evidence requires sufficient applicability/coverage.
- Never infer cause from temporal proximity, Lineage, Deployment, Change, safeguard/gate state, Impact, authority, authorization, or intent consistency alone.
- Every causal proposition belongs in Causal Claim.
- Multiple contributors/unresolved outcomes are valid.
- Investigation closure never changes Causal Claim status.

## Runtime / safeguard rules

- Treat execution duration/dependency latency as first-class evidence.
- Use correct time-valid Expectation/Baseline/waiver state.
- Ordinary Baseline variation must not become alert noise.
- Propagation Safeguard is protective state, not health/cause truth.
- Safeguard proposal/activation/release authority is independently governed; permission does not prove enforcement.
- Safeguard-induced delay remains observable/assessable; causal attribution uses Causal Claim.

## Downstream Impact rules

- Historical downstream Lineage yields Impact candidates only.
- Exposure requires actual encounter/consumption evidence appropriate to consumer class.
- `Not exposed` requires negative consumption/refresh/version/path coverage; missing telemetry cannot become non-exposure.
- Downstream effect uses Observation/Assessment/Change and can exist while exposure remains unknown.
- Technical/analytical/business consequence requires separate provenance-bearing evidence.
- Criticality/client-facing/Classification/Policy Context may affect priority but do not manufacture exposure/effect/consequence/compliance harm.
- Any assertion that origin/gate/safeguard caused/contributed belongs in Causal Claim.
- Prevented exposure requires Phase 004 safeguard-enforcement/material-control plus negative-consumption/path evidence.
- Blocking suspect version does not prove fresh/healthy downstream delivery.

## Annotation / Explanation / disclosure rules

- Annotation remains attributed human context; structured facts/claims/intents/norms/governance assertions route to owning concepts.
- Explanation composes only from Authorized Analytical Projection.
- Explanation preserves statement-to-basis traceability, Impact layers, exact Causal Claim status, authority standing/conflict, normative rule/waiver state, readiness/control evidence, action stage, human-source status, authorization/disclosure limitations, and temporal perspective.
- Never paraphrase supported/weakened/unresolved as confirmed root cause.
- Never paraphrase configured/requested control as enforced, not-exposed-to-V as healthy/current, advisory assertion as authoritative, waived violation as clean pass, or approved action as executed/enforced.
- Safe omission/redaction cannot imply hidden entities/evidence/authority/authorization do not exist.
- Explanation may surface authorized operational/gate/confirmation/disclosure state but never executes the action or creates truth.

## Historical replay rules

- Historical replay uses **event/effective time + recorded/knowledge cutoff**.
- Resolve each concept, Assertion Authority, Capability Authorization, normative rule/waiver, approval/delegation/break-glass/control/disclosure state from evidence/rules available under the cut; never project current state backward.
- Evidence/rules recorded later but effective earlier are excluded from contemporaneous cuts and may appear in retrospective cuts.
- Distinguish actual historical state/authority/authorization/action/Explanation from replay-derived interpretation.
- Late/corrected evidence or authority/authorization rules may create new retrospective conclusions; preserve prior contemporaneous conclusions.
- Historical confirmed Causal Claims remain reconstructable even if current status changes.
- Historical gate/safeguard approvals/actions/enforcement/executions are never rewritten.
- Historical Assertion Authority/Capability Authorization/disclosure is evidence about past standing/permission/disclosure; current authority/requester authorization governs present resolution/disclosure.
- Partial/unknown/conflicting/restricted replay remains valid rather than being completed by guesswork.
- Historical Baseline replay uses the exact Baseline/reference version and context available/used at the historical knowledge cut; current refreshed Baselines are not substituted backward.
- Historical metric/schema/reconciliation/composite/suitability replay uses then-effective definitions/profiles/rules and does not project current state backward.

## GitHub repository mutation guardrail

For batch planning/design work on this repository:

1. fetch and verify current `main` head/tree;
2. use Git object operations (`create_blob`, `create_tree`, `create_commit`) to build a detached candidate commit;
3. compare the detached commit against the accepted base before moving the branch;
4. preserve richer accepted canonical detail rather than compressing prior docs during status propagation;
5. move `main` only once via `update_ref` after verification;
6. verify final `main` with commit/branch fetch plus `compare_commits`;
7. avoid `create_file`/`update_file` for staged batch work because contents-API writes create immediate commits;
8. if a contents-API staging attempt fails on a nonexistent branch, confirm it created no repository state and continue with the detached workflow.

Remote GitHub `main` is authoritative; local/ZIP copies are archival or working aids only.

## Phase direction

For live repository phase/group progression, use **[`docs/README.md#current-state`](docs/README.md#current-state)**. Phase-local accepted contract ranges and handoffs are recorded in the corresponding phase README/AGENTS files. Historical decision numbering and exit records remain evidence of accepted work but are not a second current-status authority.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until mapped to explicit authority/integration roles. Do not select RBAC/ABAC, IAM provider, Assertion Authority implementation, approval workflow, graph database, temporal store, quarantine store, scheduler/orchestrator, Execution Gate implementation, metric engine/storage, redaction technology, LLM, causal algorithm, anomaly algorithm, statistical library, concrete latency/TTL architecture, or technical architecture prematurely.
