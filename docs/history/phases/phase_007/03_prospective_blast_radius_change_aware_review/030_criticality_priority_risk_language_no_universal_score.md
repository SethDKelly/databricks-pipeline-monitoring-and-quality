# OPS-030 — Criticality, Priority, Risk Language & No Universal Score

**Status:** Accepted — Phase 007 Group 03

## Purpose

Allow prospective review to prioritize meaningful consumers while preventing criticality or graph properties from becoming fabricated probability/severity/Impact scores.

## Contract

Authorized context may enrich a candidate with:

- Criticality/Classification;
- business/technical Semantic Definition;
- Responsibility Assignment;
- Policy Context;
- client-facing or operational-use context where explicitly established.

This context can influence **review priority, sequencing, required expertise or governed review obligation**. It does not strengthen Lineage evidence or prove likely exposure/effect/consequence.

## Risk language

Group 03 accepts no universal numeric change-risk score, probability-of-failure, severity-weighted blast-radius score, path-count score or shortest-path heuristic.

A later explicitly governed qualitative/quantitative risk model may be designed only with defined proposition, inputs, semantics, evidence limits and authority. Until then, use precise statements such as:

- `critical downstream candidate via planned-only path`;
- `structural compatibility unresolved for consumer X`;
- `Baseline/reconciliation review relevant`;
- `candidate set incomplete due to topology coverage`.

## Invariants

- Criticality ≠ Impact;
- Criticality ≠ evidence strength;
- path count/directness ≠ probability;
- high priority ≠ predicted defect;
- low criticality ≠ safe/no-impact;
- missing criticality ≠ low criticality.

## Handoff

OPS-031 defines completeness and negative candidate/exclusion claims.