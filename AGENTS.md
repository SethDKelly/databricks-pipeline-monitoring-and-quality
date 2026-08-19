# Repository Agent Instructions

## Project status

**Phase 002 — Concept Specifications is complete.** All five groups and 20 retained concepts are accepted.

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is next, but has not yet started.** Do not begin Phase 003 unless the user explicitly requests it.

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, services, deployment workflows, prototypes, or implementation scaffolding unless the user explicitly advances the project into technical/implementation design.

Treat this repository as a standalone data-pipeline monitoring/quality product. `docs/` is the design system of record.

## Read before changes

Read `README.md`, `docs/README.md`, relevant foundation docs, `docs/reference/glossary.md`, `docs/decisions/README.md`, and the accepted concept specifications relevant to the requested work.

## Concept Design

- Start from actor need/purpose, not vendor/tool/storage shape.
- Concepts are independent functionality, not automatically services/tables/classes/screens/jobs/vendor features.
- Prefer synchronization over merged responsibilities.
- Do not map concept boundaries directly to technical architecture.
- Preserve the accepted 20-concept catalog unless later evidence justifies an explicit reopen/revision.

## Product invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Monitoring Scope ≠ authorization;
- Change Intent ≠ Deployment ≠ realized Change;
- anticipated effect ≠ normative Expectation;
- planned value ≠ empirical Baseline;
- Deployment attempt ≠ activation;
- activation ≠ intended effect realized;
- successful run ≠ freshness ≠ data quality;
- Expectation ≠ Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- planned topology ≠ active Lineage;
- Lineage reachability ≠ cause ≠ confirmed Impact;
- Change ≠ degradation ≠ cause;
- Investigation ≠ evidence/causal truth;
- Causal Claim ≠ confirmed cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- Annotation ≠ Observation/Change Intent/Expectation/causal confirmation;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.

## Planned change / Baseline rules

- Register planned modifications through Change Intent when the product is expected to know them.
- Change Intent may register a prospective Baseline comparability break but cannot set post-change Baseline values.
- New Baselines require sufficient comparable post-change Observations.
- Immediate post-change normative validation uses an explicitly established/revised Expectation when appropriate.
- Planned change can be valid while another health dimension fails; never suppress unexpected violations merely because intent exists.

## Investigation / causality / impact rules

- Investigation organizes a bounded inquiry; it does not confirm causes or own source evidence.
- Never infer cause from temporal proximity, Lineage, Deployment, realized Change, or intent consistency alone.
- Preserve supporting and contradicting evidence on Causal Claims; multiple contributors/unresolved outcomes are valid.
- `confirmed` requires an explicit evidence/authority standard; do not invent one.
- Treat downstream Lineage as candidate discovery only. Preserve reachability, exposure, downstream effect, and business consequence separately.
- Human Annotation is attributed context. Structured plan, norm, responsibility, classification/policy assertion, or causal confirmation belongs to its owning concept.

## Historical/graph rules

- Preserve ledger-like append/supersede/correction semantics for material historical state.
- Distinguish effective/event time from recorded/knowledge time where material.
- Treat Entity Identity + typed temporal Lineage as graph-compatible semantics.
- Do not select blockchain, event sourcing, graph database, graph query language, or persistence architecture before the technical-design phase.

## Explanation/security rules

- Business and engineering explanations derive from the same authorized evidence/history and may differ only in allowed detail/abstraction.
- Preserve epistemic labels and statement-to-basis traceability.
- Distinguish contemporaneous `what was known then` from retrospective `what we know now` when material.
- Restricted evidence must not be retrieved merely to leak it through summaries.
- Unknown/conflicting/non-comparable/unavailable/unauthorized/insufficient evidence are valid outcomes.
- Monitoring must not broaden raw-data access; metadata, intent, topology, causal claims, impact, and annotations may themselves be sensitive.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Integrate before duplicate; Collibra/Immuta remain optional until explicitly authoritative for required categories.

## Canonical scenario

Use A+B→C: distinguish planned structural change from unplanned realized Change; Baseline atypicality from normative violation; valid intended change from unintended side effects; Deployment correlation from Causal Claim; multiple contributing causes from forced single-root answers; and downstream reachability from actual exposure/effect/business consequence. Preserve responsibility, authorization, history, evidence, and uncertainty.
