# Repository Agent Instructions

## Project status

**Phase 002 concept specification is complete with a post-exit addendum.** The original five groups accepted 20 concepts; Phase 003 Group 03 accepted **Propagation Safeguard** as the 21st concept through a narrow documented boundary reopen.

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is active. Groups 01–03 are accepted; Group 04 — Lineage, Investigation & Causal Reasoning is next.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, services, deployment workflows, quarantine implementations, prototypes, or implementation scaffolding unless the user explicitly advances the project into technical/implementation design.

Treat this repository as a standalone data-pipeline monitoring/quality product. `docs/` is the design system of record.

## Read before changes

Read `README.md`, `docs/README.md`, relevant foundation docs, `docs/reference/glossary.md`, decision records, accepted Phase 002 concepts/addenda, `docs/concepts/phase_003/README.md`, the synchronization template, and the active Phase 003 group.

## Concept Design and synchronization discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- A synchronization is not automatically a service call, workflow, transaction, event, database relation, or API.
- Prefer partial ordering/independent branches where semantics allow it.
- Synchronization order is never authority; a trigger is never causation.
- Do not create umbrella state for convenience.
- The current catalog has 21 accepted concepts. Reopen earlier boundaries only explicitly with rationale, as done for Propagation Safeguard.

## Product invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Entity Identity ≠ source name/reference;
- Monitoring Scope ≠ ecosystem existence ≠ authorization;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective Impact ≠ actual Impact;
- planned topology ≠ active Lineage;
- anticipated effect ≠ normative Expectation;
- planned value ≠ empirical Baseline;
- prospective reference preparation ≠ realized transition;
- Deployment attempt ≠ intent association ≠ activation ≠ intended effect realized;
- successful run ≠ timely run ≠ freshness ≠ data quality;
- execution-duration Observation ≠ duration violation;
- Observation ≠ Assessment;
- missing telemetry ≠ observed absence/missing run/output;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- Investigation ≠ evidence/causal truth;
- Causal Claim ≠ confirmed cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- safeguard release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time.

## Runtime health rules

- Treat run duration, start/completion timing, queue/wait behavior, dependency latency, and delivery readiness as first-class operational evidence/health dimensions.
- Execution success never masks a timing, freshness, or data-quality issue.
- Derive timing Observations only from sufficient compatible execution evidence; missing timestamps do not become zero duration.
- Dependency readiness uses historical Lineage plus actual timing evidence; downstream success does not prove current upstream state was consumed.
- Use the correct time-valid Expectation/Baseline after Group 02 reference transitions.
- Ordinary Baseline variation must not become alert noise; raw differences need not become durable Change.

## Analyst intervention rules

- Analysts may manually open Investigation from material, atypical, violated, unresolved, or suspicious Assessments where authorized.
- Baseline atypicality alone does not mandate Investigation.
- Automatic Investigation initiation requires explicit accepted response criteria; never invent severity/urgency policy.
- Insufficient evidence may warrant human review in high-risk contexts without becoming a fabricated failure.

## Propagation Safeguard rules

- Propagation Safeguard is protective control state, not health/cause truth.
- Assessment/Impact/Change Intent may motivate `propose`; they do not automatically establish `active`.
- Activation requires explicit authority and enforcement evidence under applicable semantics.
- Use Lineage/Impact to inform the least disruptive effective placement; do not assume source-level quarantine is always correct.
- If no output exists, hold downstream advancement/current-cycle publication rather than inventing a quarantined object.
- Safeguard-induced delay/non-delivery remains observable/assessable.
- Release is explicit and does not itself prove health.

## Investigation / causality / impact rules

- Investigation organizes bounded inquiry; it does not confirm cause.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, or intent consistency alone.
- Preserve supporting and contradicting evidence; multiple contributors/unresolved outcomes are valid.
- `confirmed` requires explicit evidence/authority standards.
- Treat downstream Lineage as candidate discovery; preserve reachability/exposure/effect/consequence separately.
- Prospective blast-radius profile cannot be represented as actual downstream Impact.

## Historical/graph/security rules

- Preserve ledger-like append/supersede/correction semantics.
- Treat Entity Identity + typed temporal Lineage as graph-compatible without selecting graph technology.
- Restricted evidence must not be retrieved merely to leak it through summaries.
- Monitoring visibility does not grant raw-data access or production-control authority.
- Do not select graph database, event store, quarantine store, workflow engine, event bus, service decomposition, LLM, or causal algorithm before technical design.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Integrate before duplicate; Collibra/Immuta remain optional until explicitly authoritative for required categories.

## Canonical scenario

Use A+B→C to test planned blast radius, time-valid references, run duration/dependency latency, ordinary versus material variation, independent quality dimensions, analyst Investigation, protective quarantine, multiple causes, downstream exposure, and contemporaneous versus retrospective knowledge—without collapsing any of those truths.
