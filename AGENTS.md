# Repository Agent Instructions

## Project status

Phase 002 originally accepted 20 concepts. Two explicit post-exit addenda are accepted: **Propagation Safeguard** and **Capability Authorization**. Current accepted concept count: **22**.

**Phase 003 is active. Groups 01–04 are accepted. Capability Authorization is accepted as a pre-Group-05 input. Group 05 — Downstream Impact, Annotation & Explanation is next and has not started.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, deployment workflows, quarantine implementations, IAM implementations, graph/causal engines, or prototypes unless the user explicitly advances the project into technical design.

Treat `docs/` as the design system of record.

## Concept Design discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- Synchronization is not automatically a service call, workflow, transaction, event, database relation, or API.
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
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ defect proof;
- release ≠ health proof;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time.

## Capability Authorization rules

- Capability Authorization answers whether a principal may perform a named capability on a subject/context/time; it does not select IAM/enforcement architecture.
- Never infer authorization from Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, commit history, job creator identity, or platform-administrator status.
- Raw-data read, derived health/metric visibility, governance metadata visibility, Lineage/RCA participation, job/run operational control, safeguard actions, and Explanation access are independently resolvable.
- A restricted-data analyst may perform approved RCA over safe aggregate/redacted/opaque evidence without direct row access.
- A job operator may hold job-operation authority without raw-data read authority.
- Analytical visibility never implies permission to retry/update/modify a job or activate a safeguard.
- Derived metrics/thresholds/Lineage/policy/causal details may themselves be restricted; do not assume metadata is safe.
- Missing authorization evidence is not permission.
- Preserve authorization effective time and knowledge time for historical reconstruction.
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

## Group 05 preparation rules

- **Do not begin Group 05 without explicit user request.**
- When Group 05 begins, authorized analytical projection must be first-class in Impact/Explanation synchronizations.
- Restricted raw-data access must not automatically block authorized health/RCA analysis.
- Policy/restriction/responsibility/health transparency must not become access grants.
- Any causal assertion about downstream effect remains Causal Claim, not Impact or Explanation narrative.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Collibra/Immuta remain optional until explicitly authoritative for required categories. Do not select RBAC/ABAC, IAM provider, graph database, event store, quarantine store, LLM, or causal algorithm prematurely.
