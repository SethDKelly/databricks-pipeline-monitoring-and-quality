# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **health, freshness, quality, lineage, governance, change history, and business impact** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is not another dashboard of isolated alerts. It is an **evidence-grounded reasoning layer over the data ecosystem**: a person should be able to ask what is happening, what changed, where a degradation likely originated, what is affected downstream, who owns the relevant assets, and what governance or policy context applies.

## Current phase

**Phase 002 — Concept Specifications**

Phase 001 established the product foundation. Phase 002 remains **documentation-only** and now turns the candidate concept catalog into explicit Concept Design specifications. No implementation architecture, language, service decomposition, storage model, API design, deployment topology, runtime framework, or vendor mapping has been selected.

The current work is organized into five strategic concept groups:

1. Scope & Identity;
2. Semantics, Governance & Policy;
3. Health Evaluation;
4. History, Lineage & Change;
5. Investigation, Impact & Explanation.

See [`docs/concepts/phase_002/README.md`](docs/concepts/phase_002/README.md) for the active review plan.

## Product thesis

A modern data pipeline can be operationally successful and still produce untrustworthy data. A job may complete on time while its inputs are stale, a join loses matches, a source feed changes shape, a filter silently reduces volume, or a downstream metric no longer reflects its intended business definition.

This project therefore treats **pipeline operation, data freshness, data quality, change, lineage, governance, and business meaning as related but distinct concerns** that must be reasoned about together.

The system should ultimately make questions like these straightforward to answer:

- Is this pipeline running as expected?
- When did it last run successfully?
- Is its output stale relative to its expected cadence and consumer needs?
- Has data quality improved or degraded over time?
- What changed, when did it begin, and how large was the change?
- Where in the upstream lineage did a degradation first become observable?
- If Table C is produced by joining Tables A and B and C loses rows, did the reduction originate in A, B, the join behavior, or some combination?
- What deployment or code change produced the affected run?
- Which downstream tables, metrics, reports, applications, or business processes may be affected?
- Who owns the pipeline, data asset, quality expectation, semantic definition, and remediation decision?
- What does the data mean?
- What policy context applies, including PII, PHI, HIPAA-related handling, retention, or other organizational restrictions?
- What evidence supports a root-cause statement?
- What remains uncertain?
- Can a business analyst understand the issue without reconstructing the engineering topology first?

## Operating environment

The known environment at project inception is deliberately small:

- data processing is implemented as Spark ETL pipelines in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- some pipelines depend on other pipelines, including cross-repository dependencies;
- Databricks is therefore both an execution environment and a key source of operational/data metadata;
- Databricks Metric Views and DQX are strongly favored capabilities for later evaluation;
- Collibra and Immuta are available but optional and must not become accidental hard dependencies.

These are environmental facts, not an implementation architecture.

## Design method: Concept Design

The product will use **Concept Design**, following Daniel Jackson's work in *The Essence of Software*, as its primary functional design method.

We will design the monitoring ecosystem as a set of understandable, independently motivated concepts that synchronize to deliver larger user outcomes. A concept is not automatically a class, service, database table, UI page, API, or vendor feature.

For this project, every accepted concept should have at minimum:

1. **Name** — a stable term for the functional idea.
2. **Purpose** — the user or ecosystem need it exists to satisfy.
3. **Operational principle** — a representative scenario showing how its behavior fulfills that purpose.
4. **State** — the information the concept owns and must remember.
5. **Actions** — the meaningful operations that change or reveal that state.
6. **Synchronizations** — explicit relationships with other concepts without dissolving their independence.

See [`docs/foundation/004_concept_design_method.md`](docs/foundation/004_concept_design_method.md) and [`docs/concepts/`](docs/concepts/).

## Foundational principles

1. **Concepts before architecture.** Define what the product means and does before deciding how it is implemented.
2. **Ecosystem over repository.** Repository and job boundaries matter for attribution, but must not limit reasoning.
3. **Time is first-class.** Current state without history is insufficient for degradation and root-cause analysis.
4. **Evidence over assertions.** Health, quality, and causal statements must be traceable to observations.
5. **Observed facts are not conclusions.** Preserve the distinction among observation, assessment, hypothesis, attribution, and confirmed cause.
6. **Lineage must explain.** Lineage exists to support origin analysis, change attribution, and downstream impact—not only visualization.
7. **Degradation is not failure.** Successful execution does not imply fresh, complete, valid, or trustworthy data.
8. **Semantics travel with assets.** Business meaning, descriptions, ownership, and criticality must participate in analysis.
9. **Policy must be transparent without overclaiming.** PII/PHI/HIPAA-related metadata describes context and expectations; it is not proof of compliance.
10. **Monitoring must not broaden data access.** The framework should minimize access to raw sensitive values and preserve source-system authorization boundaries.
11. **Authoritative sources must remain explicit.** Synced metadata must retain provenance and must not silently become a new source of truth.
12. **Databricks-native first where it fits.** Favor existing platform capabilities when they satisfy the concept without compromising clarity or portability.
13. **Integration before duplication.** Collibra, Immuta, GitHub, GitHub Actions, Databricks, and future systems should participate through clear boundaries rather than being unnecessarily recreated.
14. **Business-facing answers and engineering evidence share one truth.** Different presentations may exist, but they must resolve to the same underlying evidence.
15. **Historical topology matters.** The system must eventually be able to reason about what the ecosystem looked like when an event occurred, not only what it looks like now.

## Canonical example

Suppose **Table C** is produced by joining **Table A** and **Table B**. Table C normally contains about 20 million rows but the newest run produces 14 million.

A useful system should not stop at "row count decreased 30%." It should help establish, with evidence:

- whether A changed in volume, freshness, schema, distribution, or quality;
- whether B changed in the same dimensions;
- whether both changed;
- whether the join keys or match rate changed;
- whether the transformation or deployment changed;
- when the first anomalous condition appeared;
- which upstream pipeline/run produced the relevant inputs;
- which downstream consumers may now be affected;
- who owns the affected assets and expectations;
- and what parts of the explanation are observed, inferred, or still unresolved.

This scenario is a recurring design test for the project.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation system of record and navigation.
- [`docs/foundation/`](docs/foundation/) — Phase 001 product foundation.
- [`docs/concepts/`](docs/concepts/) — Concept Design catalog, specification template, and active Phase 002 grouped specifications.
- [`docs/planning/`](docs/planning/) — earlier discovery tracks retained as working material.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — shared vocabulary.
- [`docs/decisions/`](docs/decisions/) — explicit decision and open-question tracking.
- [`AGENTS.md`](AGENTS.md) — Codex/repository agent instructions.
- [`.cursor/rules/`](.cursor/rules/) — Cursor project rules.

## Phase 002 exit gate

Phase 002 is complete only when:

- each retained concept has a reviewed specification with a singular purpose;
- renamed, split, merged, or rejected candidates have rationale preserved;
- state/actions can be described independently of implementation architecture;
- missing, conflicting, stale, unauthorized, and insufficient evidence behavior is explicit;
- security, provenance, and effective-time implications are explicit;
- the catalog and glossary agree with the reviewed specifications;
- the synchronizations needed for Phase 003 are identifiable;
- and the canonical RCA scenarios can be expressed without hidden functionality or vendor-shaped concepts.

The active grouped plan is in [`docs/concepts/phase_002/`](docs/concepts/phase_002/).
