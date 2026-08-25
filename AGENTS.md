# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Four post-exit addenda are accepted: **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**. Current accepted concept count: **24**.

**Phase 003 is complete.** Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass end-to-end consolidation.

**Phase 004 — Evidence, Time, and Causality Refinement is complete.** Groups 01–05 accepted; REF-001–REF-030 accepted.

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is complete.** Groups 01–07 accepted; AUTH-001–AUTH-053 final; G07-01–G07-26 pass; D-251–D-265 close the phase.

**Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement is active. Groups 01–02 are accepted with HLTH-001–HLTH-018. H01-01–H01-20 and H02-01–H02-30 pass. Group 03 — Baselines, Comparability, Distribution & Statistical Context is next and has not started.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, IAM implementations, assertion-authority engines, approval/workflow engines, deployment workflows, quarantine implementations, gate/orchestration implementations, metric engines, graph/causal engines, redaction systems, LLMs, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the product/design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, API, persisted view, scheduler, orchestrator, temporal snapshot, or replay store.
- Phase 004 `REF-###` artifacts refine evidence/time/causal/control standards over accepted concepts/synchronizations.
- Phase 005 `AUTH-###` artifacts refine authority/governance/capability/disclosure standards over accepted concepts.
- Phase 006 `HLTH-###` artifacts refine health/metric/schema/statistical semantics over accepted concepts.
- REF, AUTH, and HLTH identifiers do not create hidden truth owners or extend the Phase 003 SYN range.
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

## Phase 005 authority/governance rules — COMPLETE

### Group 01 — AUTH-001–AUTH-008

- **Assertion Authority is the 24th concept.** It owns authority standing/rules, not the domain assertions.
- Bind authority to explicit target category/facet/scheme/type, subject scope, context, effective interval, and knowledge cutoff where relevant.
- Preserve source assertions regardless of standing.
- Keep disagreement, authoritative assertion conflict, and authority-rule conflict distinct.
- Authority rules require provenance/governing basis and cannot self-promote.
- Never infer authority/precedence from source count, recency, ingestion order, availability, repository ownership, title/responsibility, or apparent specificity.
- Sole authority, co-authority, precedence, and fallback exist only when explicit.
- Fallback requires explicit rule plus evidenced activation condition.
- Authority is bitemporal/non-rewriting.

### Group 02 — AUTH-009–AUTH-015

- Semantic authority is facet-specific across business/technical/schema/grain/key/unit/population/calculation/field-role meaning.
- Preserve **declared/governed schema meaning ≠ normative schema contract ≠ realized schema state ≠ compatibility Assessment**.
- Declared key role does not prove uniqueness/nullability.
- Responsibility authority is responsibility-type scoped.
- Classification authority is scheme/context scoped; criticality remains Classification.
- Policy reference authority may differ from applicability authority.
- Local governance does not automatically outrank broader governance.
- Lineage/container/tag inference does not silently propagate governance assertions/authority.
- Descriptive governance does not become normative health, access, enforcement, compliance, or Impact.

### Group 03 — AUTH-016–AUTH-023

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

### Group 04 — AUTH-024–AUTH-032

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

### Group 05 — AUTH-033–AUTH-043

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

### Group 06 — AUTH-044–AUTH-053

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

### Group 07 — consolidation / exit

- G07-01–G07-26 pass across metric/schema governance, threshold conflict/waiver, structural-change comparability, restricted RCA, causal confirmation, gating, safeguards, break-glass/outage, automation, disclosure, and history.
- No 25th concept and no AUTH-054 are required.
- **AUTH-001–AUTH-053 is final for Phase 005.**
- Authority standing, semantic/normative governance, permission, high-consequence authority, and disclosure remain separate layers over domain truth.
- No Phase 005 layer can manufacture Phase 004 evidence truth.
- Phase 006 remains free to define actual metric/statistical/schema-health/timing semantics without reopening authority ownership.

## Phase 006 health/metric rules — ACTIVE

### Group 01 — accepted HLTH-001–HLTH-008

- Every material measurement binds exact subject, metric/check definition/version, grain/population, window, relevant output/data/schema/current-cycle context, and material temporal context.
- Metric definition ≠ measured Observation ≠ normative/comparative Assessment.
- Calculation/extraction success is not health pass.
- Canonical metric families are operational/output; temporal/freshness; structural/schema; volume/population; completeness/missingness; uniqueness/key integrity; validity/domain; distribution/shape; relational/transformation integrity; business-semantic measurement.
- Readiness, composite health, Impact, causality, authorization, control enforcement, and compliance are not metric families.
- Material changes to formula, denominator, filters/population, unit, grain/window, missing-value handling, approximation/sampling, or equivalent semantics require explicit metric-definition revision/version handling.
- Metric profile roles are core operational/table, critical-field/business, transformation-specific reconciliation, and diagnostic/on-demand.
- AUTH-023 high-consequence/control eligibility is not a profile role; audience is not a profile role.
- Semantic applicability, governed profile selection, source support/computability, current evidence availability, and Assessment outcome are independent.
- Preserve `not applicable`, `not selected`, `unsupported`, `unavailable`, `pending/not evaluated`, and unknown/conflicting applicability distinctly; none becomes zero/pass/no issue.
- Technical availability does not justify routine metric inclusion; prefer a small stable routine core plus targeted critical/business/transformation checks and explicit diagnostic/on-demand expansion.
- Investigation-time diagnostic use does not automatically create permanent profile membership.
- Material metric/check Observations retain definition/version, source/input evidence, subject/window/grain/population, temporal provenance, approximation/sampling/coverage limitations and restriction state.
- Mirrored/copy-derived metric surfaces do not create independent corroboration.
- Local metric existence does not imply downstream propagation; Group 05 owns transformation-aware reconciliation.
- H01-01–H01-20 pass; no 25th concept is required.

### Group 02 — accepted HLTH-009–HLTH-018

- Structural observations and compatibility bind the consumer-visible interface/contract surface, not only producer physical schema.
- Preserve **declared/governed schema meaning ≠ normative structural Expectation/contract ≠ proposed/planned structural state ≠ realized structural Observation/Change ≠ compatibility Assessment**.
- Add, remove, rename, reorder, nested-path movement, type, precision/scale, nullability, default/generated-value, key/grain and nested-shape transitions remain independently representable.
- Rename identity requires evidence; drop/add coincidence is insufficient and same name does not prove unchanged semantic identity.
- Additive is not universally safe; removal is not universally breaking; reorder matters only for order-sensitive contracts.
- Engine cast/parse capability does not prove governed consumer compatibility.
- Type compatibility is directional and consumer-specific; precision/scale and nested shape can be independently material.
- Current zero nulls do not preserve a non-null structural guarantee after a nullable transition.
- Defaults/generated values can preserve physical presence while violating business completeness/validity semantics.
- Key/grain changes are structurally material even with unchanged columns/types and may invalidate volume, uniqueness, distribution and join assumptions without automatically constituting a defect.
- Compatibility is consumer/interface/version/time scoped and not automatically transitive.
- Stable views/projections may preserve consumer compatibility despite backing-table change; unchanged producer schema may become incompatible when consumer contract changes.
- Prospective/pre-deployment validation is separate from realized production validation; proposal validation does not prove deployment or realized schema.
- Structural change triggers scoped metric/profile/Baseline review rather than global reset.
- `Compatible` is a positive conclusion requiring sufficient coverage of all applicable required predicates in scope.
- Preserve unknown/unresolved, conflicting, unavailable and not-applicable structural states; missing/partial coverage is not compatible.
- Structural incompatibility does not prove downstream execution failure, exposure, Impact, consequence or causality.
- Physical layout/clustering/optimization is not logical schema incompatibility unless the relevant contract depends on it.
- Validation placement remains architecture-neutral; GitHub Actions, Databricks/Unity Catalog, DQX, Metric Views and independent monitoring remain later candidates.
- H02-01–H02-30 pass; no new concept is required.

### Group 03 — next

Baselines, Comparability, Distribution & Statistical Context is next and has not started.

Preserve:

- Baseline remains descriptive, not normative;
- AUTH-020 intended-use approval does not manufacture empirical comparability;
- same display name does not prove metric-definition continuity;
- same column/type shape does not prove same grain/meaning;
- structural compatibility does not automatically establish statistical comparability;
- structural change can segment or invalidate selected dimensions while unrelated dimensions remain valid;
- Group 03 owns low-volume/sample-size, seasonality/cohort, approximate/sampled uncertainty and distribution/quantile comparison semantics;
- Group 03 must not define threshold/waiver semantics or A+B→C propagation.

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

## Phase 006 metric-health direction

The accepted logical sequence is:

1. **Measurement Vocabulary, Metric Families, Profiles & Applicability — accepted, HLTH-001–HLTH-008.**
2. **Structural / Schema / DDL Compatibility — accepted, HLTH-009–HLTH-018.**
3. **Baselines, Comparability, Distribution & Statistical Context — next.**
4. Expectations, Thresholds, Margins, Waivers & Assessment Semantics.
5. Transformation Reconciliation & Metric Propagation.
6. Composite Health, Readiness Suitability & Progressive Result Timing.
7. Consolidation / Exit Review.

Phase 006 must not reopen Phase 005 authority ownership or select technical architecture.

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

- Phase 003 complete: SYN-001–SYN-035.
- Phase 004 complete: REF-001–REF-030; D-140–D-152 close the phase.
- Pre-Phase-005 metric-health planning accepted: D-153–D-160.
- Phase 005 Group 01: AUTH-001–AUTH-008; D-161–D-172.
- Phase 005 Group 02: AUTH-009–AUTH-015; D-173–D-188.
- Phase 005 Group 03: AUTH-016–AUTH-023; D-189–D-202.
- Phase 005 Group 04: AUTH-024–AUTH-032; D-203–D-217.
- Phase 005 Group 05: AUTH-033–AUTH-043; D-218–D-234.
- Phase 005 Group 06: AUTH-044–AUTH-053; D-235–D-250.
- Phase 005 Group 07: consolidation/exit; D-251–D-265.
- Phase 005 complete.
- Phase 006 Group 01 accepted: HLTH-001–HLTH-008; D-266–D-278.
- **Phase 006 Group 02 accepted: HLTH-009–HLTH-018; D-279–D-295. Group 03 — Baselines, Comparability, Distribution & Statistical Context is next and has not started. Do not begin Group 03 without explicit user request.**

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until mapped to explicit authority/integration roles. Do not select RBAC/ABAC, IAM provider, Assertion Authority implementation, approval workflow, graph database, temporal store, quarantine store, scheduler/orchestrator, Execution Gate implementation, metric engine/storage, redaction technology, LLM, causal algorithm, or technical architecture prematurely.
