# Repository Agent Instructions

## Project status

**Phase 002 concept specification is complete with a post-exit addendum.** The original five groups accepted 20 concepts; Phase 003 Group 03 accepted **Propagation Safeguard** as the 21st concept through a narrow documented boundary reopen.

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is active. Groups 01–04 are accepted; Group 05 — Downstream Impact, Annotation & Explanation is next.**

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, services, deployment workflows, quarantine implementations, graph/causal engines, prototypes, or implementation scaffolding unless the user explicitly advances the project into technical/implementation design.

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
- prospective Impact ≠ actual Impact ≠ retrospective cause;
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
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Causal Claim ≠ confirmed cause;
- absence of contradiction ≠ confirmation;
- Investigation closure ≠ Causal Claim confirmation;
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
- Human research routes to the concept owning its meaning: reproducible fact → Observation; realized difference → Change; causal proposition → Causal Claim; context → Annotation; structured plan/norm/governance truth → its owning concept.

## Investigation / causality rules

- Investigation organizes bounded inquiry around the outcome/question; it does not confirm cause.
- Use historical typed Lineage effective during the incident window to discover evidence candidates; current/planned topology cannot substitute silently.
- Preserve relationship type, direct/transitive path, provenance, completeness, inferred/asserted state, and out-of-scope/restricted boundaries.
- First-observed deviation is localization within monitored evidence, never automatic root cause.
- Assemble both supporting and contradicting evidence from Execution History, Observation, Assessment, Change, Deployment, Change Intent, Baseline/Expectation, Lineage, and Propagation Safeguard.
- Missing evidence cannot become reassuring negative/exclusion evidence. `unchanged`, `not consumed`, or similar negatives require sufficient source/topology coverage.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, safeguard state, Prospective Impact Profile, or intent consistency alone.
- Every causal proposition belongs in explicit Causal Claim with a defined outcome/cause condition and evidence links.
- Evaluate claims across temporal ordering, relationship applicability, actual encounter/consumption where required, realized state/change, semantic/mechanism compatibility, controlled contrasts, alternatives, and evidence coverage rather than an unexplained score.
- Reliable evidence that the effect predates a proposed cause materially contradicts that claim.
- Preserve supporting and contradicting evidence simultaneously where applicable.
- Multiple contributing/competing claims and unresolved outcomes are valid; never force one root cause.
- `confirmed` requires an explicit accepted evidence/authority standard. Automated ranking/support cannot manufacture confirmation.
- Investigation closure does not upgrade a Causal Claim.
- Late evidence can reopen Investigation/revise claims while preserving earlier knowledge-time state.
- Prospective blast-radius context may guide where to inspect but is not retrospective causal evidence by itself.
- Active safeguard can be a causal condition for delivery delay only when enforcement/timing evidence supports that separate claim; it is not proof that protected data was defective.

## Propagation Safeguard rules

- Propagation Safeguard is protective control state, not health/cause truth.
- Assessment/Impact/Change Intent may motivate `propose`; they do not automatically establish `active`.
- Activation requires explicit authority and enforcement evidence under applicable semantics.
- Use Lineage/Impact to inform the least disruptive effective placement; do not assume source-level quarantine is always correct.
- If no output exists, hold downstream advancement/current-cycle publication rather than inventing a quarantined object.
- Safeguard-induced delay/non-delivery remains observable/assessable.
- Release is explicit and does not itself prove health.

## Impact rules

- Treat downstream Lineage as candidate discovery; preserve reachability/exposure/effect/consequence separately.
- Prospective blast-radius profile cannot be represented as actual downstream Impact.
- Any proposition that an upstream condition caused a downstream effect belongs in Causal Claim rather than being hidden in Impact.

## Historical/graph/security rules

- Preserve ledger-like append/supersede/correction semantics.
- Treat Entity Identity + typed temporal Lineage as graph-compatible without selecting graph technology.
- Restricted evidence must not be retrieved merely to leak it through summaries.
- Monitoring visibility does not grant raw-data access or production-control authority.
- Do not select graph database, event store, quarantine store, workflow engine, event bus, service decomposition, LLM, or causal algorithm before technical design.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Integrate before duplicate; Collibra/Immuta remain optional until explicitly authoritative for required categories.

## Canonical scenario

Use A+B→C to test planned blast radius, time-valid references, run duration/dependency latency, ordinary versus material variation, independent quality dimensions, first-observed localization, competing causal claims with support/contradiction, analyst research, protective quarantine, multiple causes, downstream exposure, and contemporaneous versus retrospective knowledge—without collapsing any of those truths.
