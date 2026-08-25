# OPS-027 — Transformation & Reconciliation Change Review

**Status:** Accepted — Phase 007 Group 03

## Purpose

Identify when a proposed transformation change may invalidate or require revision of HLTH-041–HLTH-054 reconciliation semantics without inventing downstream metric propagation.

## Contract

Review the exact transformation/reconciliation definition when a proposal materially changes, for example:

- join input/role/key/type/cardinality assumptions;
- filter selection/inclusion/exclusion logic;
- aggregation grain or additive measure semantics;
- dedupe equivalence/survivor rule;
- union/merge/upsert overlap/action semantics;
- null/default/cast/value derivation;
- input cadence/current-cycle/version alignment;
- unit/normalization/distribution-preservation assumptions.

A review item should identify the affected transformation version, inputs/output, fields/keys/measures, candidate consumers and why the existing reconciliation rule may or may not remain applicable.

## Multi-hop behavior

Transformation-local review does not automatically compose into a direct multi-hop reconciliation. A downstream consumer can require separate review where the semantic path remains relevant.

## Invariants

- Lineage path ≠ reconciliation formula;
- proposed transformation change ≠ reconciliation failure;
- upstream local metric/status is not copied downstream;
- planned filter/join behavior ≠ realized output effect;
- reconciliation review/localization ≠ causality.

## Handoff

OPS-028 examines readiness/control assumptions that depend on changed outputs, versions or health evidence.