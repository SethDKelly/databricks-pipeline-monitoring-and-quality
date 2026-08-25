# OPS-026 — Metric, Profile, Expectation & Baseline Review Surface

**Status:** Accepted — Phase 007 Group 03

## Purpose

Identify which accepted health/reference assumptions may require scoped review when a proposal changes measurement meaning or operating context.

## Contract

A prospective change-aware review may mark as relevant, not relevant or indeterminate the need to inspect:

- metric/check definition and semantic applicability;
- governed metric/profile selection;
- normative Expectation/threshold/margin applicability;
- field/key/grain/population measurement binding;
- Baseline reference regime and prospective comparability break;
- composite-health profile membership/logic where the changed component is material.

Review relevance is derived from the exact proposed change and semantic dependencies. It is not a global reset.

## Baseline boundary

A proposal may establish that an existing Baseline is **expected to require comparability review** or may register a prospective break. It cannot make the Baseline empirically non-comparable before the operating context actually changes, nor can it populate a future Baseline from planned values.

## Invariants

- change proposal ≠ metric/profile invalidation;
- structural review trigger ≠ empirical non-comparability;
- anticipated value ≠ Baseline;
- anticipated effect ≠ Expectation;
- review of one field/grain does not invalidate unrelated execution/freshness metrics;
- AUTH-020 governs authoritative applicability/use decisions; analytical relevance does not grant that authority.

## Handoff

OPS-027 applies the same scoped discipline to transformation/reconciliation assumptions.