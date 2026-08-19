# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **health, freshness, quality, lineage, governance, planned/realized change history, causal evidence, and downstream business impact** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is not another dashboard of isolated alerts. It is an **evidence-grounded reasoning layer over the data ecosystem**: a person should be able to ask what is happening, what was intended, what changed, where a degradation likely originated, what is actually exposed or affected downstream, who is responsible, what governance/policy context applies, and what evidence supports each conclusion.

## Current design state

**Phase 002 — Concept Specifications: COMPLETE**

All five strategic concept groups and all **20 retained concepts** have been reviewed and accepted. Phase 002 remained documentation-only and selected no implementation architecture, service decomposition, storage model, graph database, event/ledger store, API design, runtime framework, or vendor mapping.

The next planned phase is **Phase 003 — Concept Synchronizations and Ecosystem Scenarios**. Phase 003 has not yet started.

See [`docs/concepts/phase_002/README.md`](docs/concepts/phase_002/README.md) for the completed Phase 002 review and exit gate.

## Product thesis

A modern data pipeline can be operationally successful and still produce untrustworthy data. A job may complete on time while its inputs are stale, a join loses matches, a source feed changes shape, a planned filter legitimately changes population, or a downstream metric no longer reflects its intended business definition.

The product therefore treats **operation, freshness, quality, planned intent, realized change, historical topology, governance, causality, downstream consequence, and business meaning as related but distinct concerns** that must be reasoned about together.

The system should ultimately make questions like these straightforward to answer:

- Is this pipeline running as expected?
- Is the output fresh and normatively acceptable?
- Is current behavior merely atypical versus history or actually violating an Expectation?
- Was a relevant change planned?
- Which Change Intent was realized, which Deployment became active, and what actually changed afterward?
- Did a planned change behave as intended while causing or coinciding with another quality violation?
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

The product uses Concept Design, following Daniel Jackson's approach, before technical architecture. A concept is an independently understandable unit of functionality with one primary purpose, operational principle, state, actions, invariants, ambiguity behavior, provenance/security considerations, and synchronizations.

A concept is **not automatically** a class, service, database table, graph node, UI page, API, Databricks job, or vendor feature.

See [`docs/foundation/004_concept_design_method.md`](docs/foundation/004_concept_design_method.md) and [`docs/concepts/`](docs/concepts/).

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.** Repository/job boundaries preserve provenance but do not limit reasoning.
3. **Time/history are first-class.** Effective/event time and recorded/knowledge time remain distinguishable where material.
4. **Evidence over narrative completion.** Missing evidence may leave an answer unresolved.
5. **Intent, fact, assessment, and causality are distinct.** Change Intent ≠ Deployment ≠ realized Change ≠ Assessment ≠ Causal Claim.
6. **Expectation is normative; Baseline is descriptive.** Planned values do not become empirical Baselines.
7. **Observation is not Assessment.** Missing telemetry is not observed absence.
8. **Lineage is typed, temporal, and graph-compatible.** Reachability is not cause or confirmed Impact.
9. **Historical state has ledger-like semantics.** Corrections/supersessions preserve prior knowledge rather than silently rewriting history.
10. **Degradation is not execution failure.** Successful execution can coexist with stale or poor-quality data.
11. **Causal claims remain epistemically explicit.** Correlation, deployment timing, and intent consistency do not confirm cause.
12. **Impact has layers.** Reachability, exposure, downstream effect, and business consequence are different strengths of statement.
13. **Human context remains attributed.** Annotation does not rewrite evidence or substitute for structured concepts.
14. **Explanation is a view over authorized evidence.** Business and engineering views may differ in detail but remain evidence-consistent.
15. **Policy transparency is not compliance certification.**
16. **Monitoring must not broaden raw-data access.** Metadata, topology, intent, claims, and annotations can themselves be sensitive.
17. **Authoritative sources/provenance remain explicit.** Synchronization order is not authority.
18. **Databricks-native first where it fits; integrate before duplicate.** Favored tools remain evaluations, not concept definitions.

## Canonical example

Suppose **Table C** is produced by joining **Table A** and **Table B**. C historically produces about 20 million rows and the newest run produces 14 million.

The accepted concept model can distinguish at least these possibilities:

- 14M is atypical versus the old Baseline but no normative row-count Expectation exists;
- 14M violates an explicit row-count Expectation;
- a registered filter Change Intent anticipated a lower population and a revised prospective Expectation accepts 13–15M;
- the lower volume is valid as planned, but a separate completeness/uniqueness/reconciliation Expectation fails;
- B changed first, join-key quality changed, both contributed, or cause remains unresolved;
- a nearby Deployment is correlated but contradicted as a cause by earlier upstream timing;
- downstream reports may be reachable, actually exposed, visibly affected, or tied to evidenced business consequence at different levels;
- an Explanation can show what the team knew during the incident separately from what later retrospective evidence establishes.

This scenario remains the recurring design test.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation system of record and navigation.
- [`docs/foundation/`](docs/foundation/) — accepted product foundation and roadmap.
- [`docs/concepts/`](docs/concepts/) — accepted Concept Design catalog and completed Phase 002 specifications.
- [`docs/planning/`](docs/planning/) — earlier discovery tracks retained as non-authoritative inputs where superseded by accepted concepts.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) — repository-agent instructions.
- [`.cursor/rules/`](.cursor/rules/) — Cursor project rules.

## Phase transition

Phase 002 exit criteria are satisfied. The repository should **not** jump directly to technical architecture: the next planned work is Phase 003 synchronization/scenario design, followed by deeper evidence/authority/quality/lineage/questioning/integration refinement before technical architecture is selected.
