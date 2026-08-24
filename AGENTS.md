# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Two explicit post-exit addenda are accepted: **Propagation Safeguard** and **Capability Authorization**. Current accepted concept count: **22**.

**Phase 003 is active. Groups 01–05 are accepted. Group 06 — Historical Replay & Phase 003 Consolidation is next.**

Accepted synchronization range: **SYN-001–SYN-031**.

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, deployment workflows, quarantine implementations, IAM implementations, graph/causal engines, LLMs, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, API, or persisted view.
- Synchronization order is never authority; a trigger is never causation.
- Do not create umbrella state for convenience.
- Reopen earlier boundaries only explicitly with rationale.

## Core invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Monitoring Scope ≠ Capability Authorization;
- Responsibility Assignment ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Capability Authorization ≠ compliance;
- raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
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
- historical authorization ≠ current disclosure permission;
- effective/event time ≠ recorded/knowledge time.

## Capability Authorization / analytical projection rules

- Capability Authorization answers whether a principal may perform a named capability on a subject/context/time; it does not select IAM/enforcement architecture.
- Never infer authorization from Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, or platform-administrator status.
- Raw-data read, derived health/metric visibility, governance metadata visibility, Lineage/RCA participation, job/run operational control, safeguard actions, and Explanation access are independently resolvable.
- A restricted-data analyst may perform approved RCA/Impact analysis over safe aggregate/redacted/opaque evidence without direct row access.
- A job operator may hold job-operation authority without raw-data read authority.
- Analytical visibility never implies permission to retry/update/modify a job or activate a safeguard.
- Derived metrics/thresholds/Lineage/policy/causal/Impact details may themselves be restricted; do not assume metadata is safe.
- Missing authorization evidence is not permission.
- The Authorized Analytical Projection is a synchronization result/view over permitted concept state; it does not create new truth or declassify by inference.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized audience.
- Historical authorization can be evidence about what a past actor could know/do; current requester authorization still governs current disclosure.
- Permission to perform an action is not evidence the action succeeded; resulting facts belong to Deployment/Execution History/Observation/etc.

## Investigation / causality rules

- Investigation starts from a question/outcome, not a presumed cause.
- Use historical typed Lineage for candidate discovery; current/planned topology cannot silently replace incident-time topology.
- First-observed deviation is localization, not root cause.
- Preserve supporting and contradicting evidence.
- Negative/exclusion evidence requires sufficient coverage.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, Prospective Impact, or intent consistency alone.
- Every causal proposition belongs in Causal Claim.
- Multiple contributors/unresolved outcomes are valid.
- `confirmed` requires an explicit accepted evidence/authority standard; do not invent it.
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
- Any assertion that an origin caused/contributed to downstream effect/consequence belongs in Causal Claim.
- Prevented exposure requires active/enforced safeguard evidence plus sufficient negative-consumption coverage.
- Blocking a suspect version does not prove fresh/healthy downstream delivery.
- A safeguard may prevent suspect exposure while separately causing lateness/non-delivery.

## Annotation / Explanation rules

- Annotation remains attributed human context; structured facts/claims/intents/norms/governance assertions route to their owning concepts.
- Disputed/withdrawn Annotation cannot be presented as uncontested current fact.
- Explanation composes only from the Authorized Analytical Projection.
- Explanation preserves statement-to-basis traceability, Impact layers, Causal Claim status, human-source status, policy/authorization limitations, and temporal perspective.
- Safe omission/redaction cannot be worded as evidence that hidden entities/evidence do not exist.
- Explanation may surface an authorized operational capability but never executes the action.

## Group 06 preparation rules

- Compose E-01–E-20 end to end using only accepted concepts/SYN-001–SYN-031.
- Reconstruct separately: what happened, what was known then, what was believed then, what was authorized then, what was explained then, and what is known now.
- Current topology/reference/governance/authorization must not be silently projected backward.
- Historical authorization cannot bypass current requester disclosure controls.
- Verify corrections/supersessions preserve prior knowledge and explanation state.
- Verify restricted/opaque paths remain useful without leakage.
- Verify no synchronization has become a hidden architecture/persistence/IAM/LLM concept.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until explicitly authoritative for required categories. Do not select RBAC/ABAC, IAM provider, graph database, event store, quarantine store, LLM, or causal algorithm prematurely.
