# Repository Agent Instructions

## Project status

This repository is in **Phase 002 — Concept Specifications**. Groups 01–04 are accepted; Group 05 is next.

**Documentation-only rule:** do not add application code, infrastructure, notebooks, schemas, APIs, services, deployment workflows, prototypes, or framework scaffolding unless the user explicitly advances the project into technical/implementation design.

Treat this repository as a standalone data-pipeline monitoring/quality product. `docs/` is the design system of record.

## Read before changes

Read `README.md`, `docs/README.md`, relevant foundation docs, Concept Design method/template, glossary, relevant concept group, and decision records.

## Concept Design

- Start from actor need/purpose, not vendor/tool/storage shape.
- Concepts are independent functionality, not automatically services/tables/classes/screens/jobs/vendor features.
- Prefer synchronization over merged responsibilities.
- No vendor-shaped concepts.
- Do not map concept boundaries to technical architecture during Phase 002.

## Product invariants

Preserve:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Change Intent ≠ Deployment ≠ realized Change;
- anticipated effect ≠ normative Expectation;
- Deployment attempt ≠ activation;
- activation ≠ intended effect realized;
- successful run ≠ freshness ≠ data quality;
- Expectation ≠ Baseline;
- planned value ≠ empirical Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- planned topology ≠ active Lineage;
- Lineage/reachability ≠ cause/confirmed impact;
- Change ≠ degradation ≠ cause;
- event/effective time ≠ recorded/knowledge time;
- hypothesis ≠ confirmed cause;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.

## Planned change / Baseline rules

- Register planned pipeline modifications through Change Intent when the product is expected to know them.
- Change Intent may flag a prospective Baseline comparability break but must never directly set post-change Baseline values.
- New Baselines require post-change Observation evidence.
- If immediate post-change normative validation is needed, use an explicit prospective Expectation with appropriate authority/effective semantics.
- Planned change can be valid while another health dimension fails; do not suppress unexpected violations.

## Historical/graph rules

- Preserve ledger-like append/supersede/correction semantics for material historical state.
- Distinguish effective/event time from recorded/knowledge time where material.
- Treat Entity Identity + typed temporal Lineage as graph-compatible semantics.
- Do **not** select blockchain, event sourcing, graph database, graph query language, or persistence architecture during Phase 002.

## Evidence/security

Unknown/conflicting/non-comparable/unavailable/unauthorized/insufficient evidence are valid. Never infer absence from missing telemetry or invent causation. Monitoring must not broaden raw-data access; metadata/intent/topology can themselves be sensitive.

## Tooling stance

Databricks Metric Views/DQX are favored later evaluations, not settled architecture. Integrate before duplicate; optional systems remain optional until explicitly authoritative.

## Canonical scenario

Use A+B→C: distinguish planned structural change from unplanned realized Change; Baseline atypicality from normative violation; Deployment correlation from cause; and expected volume shift from unintended side effects. Preserve upstream/downstream history, responsibility, evidence, and uncertainty.
