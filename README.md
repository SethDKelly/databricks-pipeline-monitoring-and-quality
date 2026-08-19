# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **health, freshness, quality, lineage, governance, planned/realized change history, causal evidence, and downstream business impact** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**: a person should be able to ask what is happening, what was intended, what changed, where a degradation likely originated, what is actually exposed or affected downstream, who is responsible, what governance/policy context applies, and what evidence supports each conclusion.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: ACTIVE**

Phase 002 is complete with all 20 retained concepts accepted. Phase 003 defines how those independent concepts coordinate end to end without collapsing their truth boundaries or selecting implementation architecture.

**Groups 01–02 are accepted. Group 03 — Runtime Evidence, Health & Realized Change is next.**

Group 02 formalized how Change Intent prepares prospective reference context, how intent associates with Deployment realization evidence, how reference applicability changes only at an evidence-backed operating-context transition, and how a new Baseline is learned later from post-transition Observations.

See [`docs/concepts/phase_003/README.md`](docs/concepts/phase_003/README.md) for the active Phase 003 group plan and [`docs/concepts/phase_002/README.md`](docs/concepts/phase_002/README.md) for the completed concept specifications.

## Product thesis

A modern data pipeline can be operationally successful and still produce untrustworthy data. A job may complete on time while its inputs are stale, a join loses matches, a source feed changes shape, a planned filter legitimately changes population, or a downstream metric no longer reflects its intended business definition.

The product therefore treats **operation, freshness, quality, planned intent, realized change, historical topology, governance, causality, downstream consequence, and business meaning as related but distinct concerns** that must be reasoned about together.

The system should ultimately make questions like these straightforward to answer:

- Is this pipeline running as expected?
- Is the output fresh and normatively acceptable?
- Is current behavior merely atypical versus history or actually violating an Expectation?
- Was a relevant change planned?
- Which Change Intent was associated with which Deployment, and what state actually became active?
- Did a planned change require a new Expectation or make an old Baseline non-comparable?
- Is a post-change run being evaluated against the correct time-valid reference context?
- Did a planned change behave as intended while another quality dimension failed?
- Where in upstream Lineage did a relevant condition first become observable?
- Which causal explanations are proposed, supported, weakened, rejected, confirmed, or unresolved?
- Which downstream entities are only reachable, which actually consumed affected state, and which show observed/business consequences?
- Who bears the relevant technical/business/governance responsibility?
- What policy/sensitivity context applies?
- What evidence supports each material conclusion?
- What was known at the incident time versus what later evidence reveals retrospectively?

## Operating environment

Known environment facts remain deliberately small:

- Spark ETL pipelines execute in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a key execution and metadata source;
- Databricks Metric Views and DQX are strongly favored capabilities for later evaluation;
- Collibra and Immuta are available but optional.

These are environmental facts, not an implementation architecture.

## Design method: Concept Design

The product uses Concept Design, following Daniel Jackson's approach, before technical architecture. Phase 002 established independently understandable concepts; Phase 003 composes them through explicit synchronization contracts.

A synchronization is **not automatically** a service call, workflow engine, transaction, event, database relation, API, graph traversal implementation, or orchestration mechanism.

See [`docs/foundation/004_concept_design_method.md`](docs/foundation/004_concept_design_method.md), [`docs/concepts/`](docs/concepts/), and [`docs/concepts/phase_003/`](docs/concepts/phase_003/).

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.** Repository/job boundaries preserve provenance but do not limit reasoning.
3. **Time/history are first-class.** Effective/event time and recorded/knowledge time remain distinguishable where material.
4. **Evidence over narrative completion.** Missing evidence may leave an answer unresolved.
5. **Intent, fact, assessment, and causality are distinct.** Change Intent ≠ Deployment ≠ realized Change ≠ Assessment ≠ Causal Claim.
6. **Expectation is normative; Baseline is descriptive.** Planned values do not become empirical Baselines.
7. **Prospective reference preparation is not realized transition.** Reference context changes only when sufficient realization evidence establishes the relevant operating boundary.
8. **Observation is not Assessment.** Missing telemetry is not observed absence.
9. **Lineage is typed, temporal, and graph-compatible.** Reachability is not cause or confirmed Impact.
10. **Historical state has ledger-like semantics.** Corrections/supersessions preserve prior knowledge rather than silently rewriting history.
11. **Degradation is not execution failure.** Successful execution can coexist with stale or poor-quality data.
12. **Causal claims remain epistemically explicit.** Correlation, deployment timing, and intent consistency do not confirm cause.
13. **Impact has layers.** Reachability, exposure, downstream effect, and business consequence are different strengths of statement.
14. **Human context remains attributed.** Annotation does not rewrite evidence or substitute for structured concepts.
15. **Explanation is a view over authorized evidence.** Business and engineering views may differ in detail but remain evidence-consistent.
16. **Synchronization never manufactures authority.** Coordination order cannot choose a source of truth.
17. **Partial synchronization is valid.** One unresolved context branch must not erase independently valid context.
18. **Policy transparency is not compliance certification.**
19. **Monitoring must not broaden raw-data access.** Metadata, topology, intent, claims, and annotations can themselves be sensitive.
20. **Databricks-native first where it fits; integrate before duplicate.** Favored tools remain evaluations, not concept definitions.

## Canonical example

Suppose **Table C** is produced by joining **Table A** and **Table B**. C historically produces about 20 million rows and the newest run produces 14 million.

The accepted model can distinguish at least these possibilities:

- 14M is atypical versus the old Baseline but no normative row-count Expectation exists;
- 14M violates an explicit row-count Expectation;
- a registered filter Change Intent anticipated a lower population and prompted a prospective Expectation plus a pending Baseline comparability break;
- the relevant structural configuration becomes active, making the old Baseline non-comparable for the changed context while the new Expectation becomes applicable;
- the first post-change run can be evaluated against that Expectation even though no new Baseline exists yet;
- a later Baseline is derived only from sufficient comparable post-change Observations;
- the lower volume is valid as planned, but a separate completeness/uniqueness/reconciliation Expectation fails;
- B changed first, join-key quality changed, both contributed, or cause remains unresolved;
- a nearby Deployment is correlated but not automatically causal;
- downstream reports may be reachable, actually exposed, visibly affected, or tied to evidenced business consequence at different levels;
- an Explanation can show what the team knew during the incident separately from what later retrospective evidence establishes.

Phase 003 requires that each transition among these concept states be governed by explicit synchronization semantics rather than hidden workflow assumptions.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation system of record and navigation.
- [`docs/foundation/`](docs/foundation/) — accepted product foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — completed 20-concept specifications.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — active synchronization contracts and ecosystem scenarios.
- [`docs/planning/`](docs/planning/) — earlier discovery tracks retained as non-authoritative inputs where superseded.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) — repository-agent instructions.
- [`.cursor/rules/`](.cursor/rules/) — Cursor project rules.

## Phase direction

Phase 003 remains documentation/design-first. The project must not jump from synchronization semantics directly to technical architecture; later refinement phases still define evidence/time/causality, authority/governance, quality, lineage/impact, explanation, and integration contracts before architecture selection.
