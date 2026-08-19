# Repository Agent Instructions

## Project status

**Phase 002 — Concept Specifications is complete.** All five groups and 20 retained concepts are accepted.

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is active.** Group 01 — Subject, Scope & Governance Context is accepted; Group 02 — Planned Change & Reference Transition is next.

Work remains documentation/design-first. Do not add application code, infrastructure, notebooks, schemas, APIs, services, deployment workflows, prototypes, or implementation scaffolding unless the user explicitly advances the project into technical/implementation design.

Treat this repository as a standalone data-pipeline monitoring/quality product. `docs/` is the design system of record.

## Read before changes

Read `README.md`, `docs/README.md`, relevant foundation docs, `docs/reference/glossary.md`, `docs/decisions/README.md`, accepted Phase 002 concept specifications, `docs/concepts/phase_003/README.md`, the synchronization template, and the active Phase 003 group.

## Concept Design and synchronization discipline

- Start from actor/ecosystem outcome, not vendor/tool/storage shape.
- Preserve accepted concept ownership/state boundaries.
- A synchronization coordinates accepted concept actions/results; it is not automatically a service call, workflow, transaction, message/event, database relationship, or API.
- Prefer partial ordering/independent branches where semantics allow it; do not manufacture total ordering.
- Synchronization order is never source authority.
- A trigger means coordination should be considered; it does not imply causation.
- Do not create umbrella state merely to make synchronization convenient.
- Preserve the accepted 20-concept catalog unless later evidence justifies an explicit reopen/revision.

## Product invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Entity Identity ≠ source name/reference;
- Monitoring Scope ≠ ecosystem existence ≠ authorization;
- Semantic Definition ≠ Responsibility Assignment;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- synchronization order ≠ authority;
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
- effective/event time ≠ recorded/knowledge time.

## Phase 003 rules

- Use `docs/concepts/phase_003/synchronization_template.md` for substantive synchronization contracts.
- Pass Entity Identity rather than raw names between subject-specific concept chains.
- Resolve Monitoring Scope independently; scope never grants authorization or evidence availability.
- Resolve semantic/responsibility/classification/policy branches independently and preserve category-local conflicts/gaps.
- Classification may support Policy Context applicability only where an explicit policy assertion/condition exists; never manufacture policy from classification alone.
- One failed/unknown branch must not erase independently valid branches.
- Preserve ledger-like append/supersede/correction semantics for material synchronization history.
- Distinguish effective/event time from recorded/knowledge time where material.

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

## Historical/graph/security rules

- Treat Entity Identity + typed temporal Lineage as graph-compatible semantics without selecting graph technology.
- Do not select blockchain, event sourcing, graph database, graph query language, persistence architecture, workflow engine, event bus, or service decomposition before technical design.
- Business and engineering explanations derive from the same authorized evidence/history and may differ only in allowed detail/abstraction.
- Restricted evidence must not be retrieved merely to leak it through summaries.
- Unknown/conflicting/non-comparable/unavailable/unauthorized/insufficient evidence are valid outcomes.
- Monitoring must not broaden raw-data access; metadata, intent, topology, causal claims, impact, and annotations may themselves be sensitive.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Integrate before duplicate; Collibra/Immuta remain optional until explicitly authoritative for required categories.

## Canonical scenario

Use A+B→C to test both concept truth boundaries and synchronization behavior: distinguish planned structural change from unplanned realized Change; Baseline atypicality from normative violation; valid intended change from unintended side effects; Deployment correlation from Causal Claim; multiple contributing causes from forced single-root answers; downstream reachability from exposure/effect/consequence; and current versus historical context. Preserve responsibility, authorization, evidence, provenance, and uncertainty across the whole chain.
