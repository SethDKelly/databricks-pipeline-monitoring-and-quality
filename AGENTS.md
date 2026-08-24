# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Three explicit post-exit addenda are accepted: **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate**. Current accepted concept count: **23**.

**Phase 003 is complete. Groups 01–06 are accepted. Accepted synchronization range: SYN-001–SYN-035. E-01–E-22 pass end-to-end consolidation.**

**Phase 004 — Evidence, Time, and Causality Refinement is active. Groups 01–02 are accepted with REF-001–REF-012. Group 03 — Causal Epistemics, Confirmation & Multiple Contributors is next and has not started.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, deployment workflows, quarantine implementations, gate/orchestration implementations, IAM implementations, graph/causal engines, LLMs, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, API, persisted view, scheduler, orchestrator, temporal snapshot, or replay store.
- Phase 004 `REF-###` artifacts refine evidence/time/causal standards over accepted concepts and synchronizations; they are not new truth-owning concepts or Phase 003 synchronizations.
- Synchronization/refinement order is never authority; a trigger is never causation.
- Do not create umbrella state for convenience.
- Reopen earlier boundaries only explicitly with rationale.

## Core invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Monitoring Scope ≠ Capability Authorization;
- Responsibility Assignment ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Capability Authorization ≠ compliance;
- raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority ≠ gate-control authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- passive monitoring ≠ active Execution Gate;
- monitoring availability ≠ ungated production-job availability;
- dependency readiness Assessment ≠ Execution Gate admission state;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- gate hold ≠ execution failure;
- gate admission ≠ actual run occurrence;
- gate override ≠ prerequisite ready;
- missing readiness evidence ≠ ready;
- permission to act ≠ action succeeded;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- planned topology ≠ active Lineage;
- successful run ≠ timely run ≠ freshness ≠ data quality;
- Observation ≠ Assessment;
- missing telemetry ≠ observed absence/missing run/output;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- Investigation ≠ evidence/causal truth;
- Lineage evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence ≠ causal attribution;
- `not exposed` ≠ missing consumer telemetry;
- criticality ≠ actual Impact;
- safeguard proposal ≠ active/enforced safeguard;
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
- historical authorization/control state ≠ current disclosure permission;
- evidence applicability ≠ evidence coverage ≠ conclusion sufficiency;
- evidence not found ≠ observed absence;
- source count ≠ independent corroboration;
- evidence sufficiency ≠ disclosure authorization;
- `known by K` ≠ `learned after K` ≠ `not recorded by K` ≠ `not known by K` ≠ `not available by K`;
- late evidence ≠ source correction ≠ independent conflict ≠ reinterpretation ≠ later authority resolution;
- immediate operational validation ≠ enriched health evaluation ≠ investigative/RCA reasoning ≠ retrospective/post-ops review.

## Phase 004 Group 01 evidence rules

- Bind every material evidence-sufficiency evaluation to a defined proposition/conclusion, subject, context, event time/window, grain/version, and intended conclusion strength.
- Evaluate evidence applicability before treating it as support, contradiction, exclusion, or corroboration.
- Applicability considers subject identity, semantic/property alignment, time, grain/version, derivation, and relevant Lineage/dependency context.
- Coverage is bounded and multidimensional. Name the observation universe/window before using terms such as `complete` or `sufficient coverage`.
- Preserve temporal, population/partition, source/query, identity/version, measurement, sampling/estimation, monitoring/instrumentation, derivation, and known-gap context where material.
- Negative/absence/exclusion conclusions require both an adequate opportunity to observe and sufficient coverage of the bounded opportunities where the event/state could have occurred.
- No telemetry, query failure, monitoring outage, inaccessible/restricted evidence, out-of-scope evidence, or unresolved identity/version state is not a negative fact.
- Positive and negative propositions can require asymmetric coverage: one observed event can establish existence while absence normally requires coverage of all relevant bounded opportunities.
- Do not multiply evidentiary strength merely because the same underlying telemetry is copied/mirrored/indexed in several systems.
- Preserve duplicated, commonly derived, complementary, independently corroborating, partially independent, conflicting, and non-comparable evidence relationships where provenance permits.
- Applicable conflicts remain explicit unless an accepted category-specific authority rule resolves them. Do not use majority vote, recency alone, synchronization order, repository ownership, or source count as hidden authority.
- Evidence sufficiency is conclusion-relative and may resolve sufficient, insufficient, conflicting/indeterminate, non-applicable/non-comparable, unavailable, or unknown.
- `Sufficient` for one conclusion does not imply sufficiency for related broader conclusions; `insufficient` does not mean false.
- Do not create a universal evidence trust/confidence number. Statistical uncertainty may later be represented for appropriate measurements without becoming a generic evidence score.
- Sufficiency evaluation does not grant Capability Authorization, source authority, job/safeguard/gate authority, or action permission.
- A requester may receive an authorized safe conclusion/limitation while basis details remain restricted; if the framework itself cannot access required evidence, that is an evidence-availability limitation.

## Phase 004 Group 02 temporal and progressive-availability rules

- Distinguish event/effective time, source production/observation time, source availability time, framework collection/retrieval time, framework recorded/knowledge time, derived evaluation time, and correction/supersession time where material.
- Source availability before a cutoff does not mean the framework knew the evidence by that cutoff.
- Current retrieval of an old source record gives current framework knowledge unless retained evidence proves earlier framework knowledge.
- For event/window `T` and knowledge cutoff `K`, an `as-known` cut includes only evidence applicable to `T` that was recorded/known by the framework at or before `K`; corrections used in the cut must also be known by `K`.
- `Not known by K` is a negative epistemic claim and requires sufficient retention/collection coverage; missing historical records or monitoring outages cannot establish it.
- Actual historical Assessment/claim/Impact/control/Explanation state requires evidence the state/action/communication existed by the cutoff. Otherwise label the output replay-derived/reconstructed.
- Produce the narrowest trustworthy result as soon as the evidence required for that result is available.
- Preserve progressive analytical horizons: immediate operational validation, enriched health evaluation, investigative/RCA reasoning, retrospective/post-operations review.
- Do not treat those horizons as services, jobs, UI screens, fixed SLAs, or architecture tiers.
- A fast `job succeeded` result never implies pipeline health, freshness, quality, or causal resolution while those evidence classes remain pending.
- Do not weaken high-consequence evidence standards for latency convenience.
- Late evidence, source correction, independent conflict, semantic reinterpretation, and later authority resolution remain distinct.
- Source correction/supersession preserves prior state; independent disagreement remains conflict absent accepted resolution.
- Reevaluate retained conclusions only when new/corrected evidence materially bears on their basis/applicability/coverage/contradiction set.
- Closed Investigations can become review/reopen candidates when materially challenged; do not automatically reopen every closed Investigation.
- Current requester authorization continues to govern historical/reconstructed disclosure.
- Exact monitoring-result timing targets are deferred: Phase 006 defines health-result timing expectations, Phase 009 source availability/collection characteristics, Phase 010 architecture/performance budgets, and Phase 011 MVP acceptance criteria.

## Passive monitoring / integration-independence rules

- Baseline monitoring is **out-of-band and non-blocking by default**.
- Monitoring collection, Assessment, Investigation, Impact analysis, or Explanation must not become a production start dependency merely because an asset is monitored.
- Monitoring-framework degradation must not delay ungated production jobs.
- Prefer Databricks/platform/source metadata and independently deployed monitoring components over ETL-code changes, injected framework libraries, or monitoring steps in every production GitHub Actions workflow when equivalent evidence is available externally.
- Production-repository independence is an architectural objective, not an absolute guarantee; any future source-code/workflow integration requirement must be explicit, minimal, and justified.

## Execution Gate rules

- **Execution Gate is optional active control.** Lineage, schedule timing, or readiness Assessment does not silently enable gating.
- A gate may hold a downstream execution opportunity until explicitly declared prerequisite readiness is evidenced.
- Readiness may require current qualifying output/freshness/version/completion rather than only `upstream job succeeded`.
- Gate `hold` does not mean the downstream execution failed; it may never have started.
- Gate `admit` does not prove the execution actually ran; Execution History owns actual run evidence.
- Gate `override` does not transform an unmet/unknown prerequisite into `ready`.
- Missing readiness/control evidence is not automatically ready.
- Never invent a universal fail-open/fail-closed policy. Gate unavailable/unknown behavior, timeout, escalation, expiry, and override must come from explicit accepted semantics/configuration.
- Gate configuration/control/override authority is resolved separately through Capability Authorization.
- Execution Gate controls **start/admission**. Propagation Safeguard controls **output/consumption propagation**. Do not merge them.
- Gate-induced delay/non-delivery remains Observation/Assessment/Impact evidence. Any proposition that the gate caused a consequence belongs in Causal Claim.
- Do not choose Databricks Workflows dependencies, external orchestration, sensors, event triggers, or another gate implementation before the technical architecture phase.

## Capability Authorization / analytical projection rules

- Capability Authorization answers whether a principal may perform a named capability on a subject/context/time; it does not select IAM/enforcement architecture.
- Never infer authorization from Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, or platform-administrator status.
- Raw-data read, derived health/metric visibility, governance metadata visibility, Lineage/RCA participation, job/run operational control, safeguard actions, gate actions/override, and Explanation access are independently resolvable.
- A restricted-data analyst may perform approved RCA/Impact analysis over safe aggregate/redacted/opaque evidence without direct row access.
- A job/gate operator may hold operational authority without raw-data read authority.
- Analytical visibility never implies permission to retry/update/modify a job, activate a safeguard, or override a gate.
- Derived metrics/thresholds/Lineage/policy/causal/Impact/gate details may themselves be restricted; do not assume metadata is safe.
- Missing authorization evidence is not permission.
- The Authorized Analytical Projection is a synchronization result/view over permitted concept state; it does not create new truth or declassify by inference.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized audience.
- Historical authorization/control state can be evidence about what a past actor could know/do; current requester authorization still governs current disclosure.
- Permission to perform an action is not evidence the action succeeded; resulting facts belong to Deployment/Execution History/Observation/etc.

## Investigation / causality rules

- Investigation starts from a question/outcome, not a presumed cause.
- Use historical typed Lineage for candidate discovery; current/planned topology cannot silently replace incident-time topology.
- First-observed deviation is localization, not root cause.
- Preserve supporting and contradicting evidence.
- Negative/exclusion evidence requires sufficient applicability and coverage under the Phase 004 Group 01 framework.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, gate state, Prospective Impact, or intent consistency alone.
- Every causal proposition belongs in Causal Claim.
- Multiple contributors/unresolved outcomes are valid.
- `confirmed` requires an explicit accepted evidence/authority standard; do not invent it before Phase 004 Group 03.
- Human reproducible findings use Observation/Change; causal interpretations use Causal Claim; contextual notes use Annotation.

## Runtime / safeguard rules

- Treat execution duration/dependency latency as first-class operational evidence.
- Use the correct time-valid Expectation/Baseline.
- Ordinary Baseline variation must not become alert noise.
- Propagation Safeguard is protective state, not health/cause truth.
- Activation requires explicit safeguard capability/authority and enforcement evidence where applicable.
- Safeguard-induced delay remains observable/assessable.

## Downstream Impact rules

- Historical downstream Lineage yields Impact candidates only.
- Exposure requires actual encounter/consumption evidence appropriate to the consumer class.
- `Not exposed` requires sufficient negative consumption/refresh/version coverage; missing telemetry cannot become non-exposure.
- Downstream effect uses Observation/Assessment/Change and can exist while exposure remains unknown.
- Exposure can exist while monitored downstream health remains acceptable.
- Technical/analytical/business consequence requires separate provenance-bearing consequence evidence.
- Criticality, client-facing status, Classification, or Policy Context may affect priority/handling but do not manufacture exposure/effect/consequence or compliance harm.
- Any assertion that an origin, gate, or safeguard caused/contributed to downstream effect/consequence belongs in Causal Claim.
- Prevented exposure requires active/enforced safeguard evidence plus sufficient negative-consumption coverage.
- Blocking a suspect version does not prove fresh/healthy downstream delivery.
- A safeguard or gate may correctly prevent stale/suspect propagation while separately causing lateness/non-delivery.

## Annotation / Explanation rules

- Annotation remains attributed human context; structured facts/claims/intents/norms/governance assertions route to their owning concepts.
- Disputed/withdrawn Annotation cannot be presented as uncontested current fact.
- Explanation composes only from the Authorized Analytical Projection.
- Explanation preserves statement-to-basis traceability, Impact layers, Causal Claim status, human-source status, gate/safeguard state, policy/authorization limitations, and temporal perspective.
- Safe omission/redaction cannot be worded as evidence that hidden entities/evidence do not exist.
- Explanation may surface an authorized operational/gate capability but never executes the action.

## Historical replay rules — accepted Phase 003 Group 06 + Phase 004 Group 02 refinement

- Historical replay uses **event/effective time + recorded/knowledge cutoff**.
- Resolve each concept from state/evidence available under the cut; never project current identity/topology/reference/governance/authorization/control backward.
- Evidence recorded later but effective earlier is excluded from a contemporaneous cut and may appear in a later retrospective cut.
- Distinguish **actual historical state** from **replay-derived interpretation**. A current replay result does not prove an Assessment/claim/Impact/decision/Explanation actually existed then.
- Late/corrected evidence may create a new retrospective conclusion with a later knowledge time; preserve the prior contemporaneous conclusion.
- Do not counterfactually rewrite actual historical Execution Gate or Propagation Safeguard actions.
- Do not backfill later realized Lineage/Impact/causal evidence into earlier prospective knowledge.
- If no historical Explanation snapshot exists, an `as-known-then` answer is reconstructed—not something responders actually saw.
- Historical Capability Authorization is evidence about past permission; current requester authorization still governs disclosure.
- Partial/unknown/conflicting/restricted replay remains valid rather than being completed by guesswork.

## Phase 004 direction

- Group 01 is accepted: REF-001–REF-005.
- Group 02 is accepted: REF-006–REF-012.
- **Do not begin Group 03 — Causal Epistemics, Confirmation & Multiple Contributors without explicit user request.**
- Group 03 must refine Causal Claim status vocabulary/transitions, support/contradiction, alternatives, confirmation evidence/authority boundaries, multiple contributors, progressive RCA maturity, and challenge after confirmation.
- Group 04 specializes exposure/readiness/control evidence; Group 05 consolidates Phase 004.
- Do not choose implementation architecture while refining these semantics.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until explicitly authoritative for required categories. Do not select RBAC/ABAC, IAM provider, graph database, event/temporal store, quarantine store, scheduler/orchestrator, Execution Gate implementation, LLM, or causal algorithm prematurely.
