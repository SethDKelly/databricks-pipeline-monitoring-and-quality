# HLTH-003 — Canonical Metric-Family Taxonomy

**Status:** Accepted — Phase 006 Group 01

## Purpose

Provide a stable functional taxonomy for health-relevant measurement without requiring every family on every asset or equating a family with an implementation engine.

## Accepted families

### 1. Operational / output
Examples: run occurrence/state, execution duration/latency, output existence, output production timing, task/job completion facts.

### 2. Temporal / freshness
Examples: data age, current-cycle status, lateness, freshness relative to a referenced time/cycle.

### 3. Structural / schema
Examples: field existence, observed type/nullability/nesting/key/grain structure and later compatibility/conformance results.

### 4. Volume / population
Examples: row/object/population count, partition counts, bounded source/output population size.

### 5. Completeness / missingness
Examples: null/missing/empty rate or count for semantically meaningful fields/populations.

### 6. Uniqueness / key integrity
Examples: duplicate count/rate, key uniqueness, key completeness combinations where declared key semantics make them meaningful.

### 7. Validity / domain conformance
Examples: allowed value/domain/range/format conformance, semantic validity rate.

### 8. Distribution / shape
Examples: selected quantiles, moments, category shares, cardinality, distribution distance or drift where statistically and semantically meaningful.

### 9. Relational / transformation integrity
Examples: join match/unmatched rates, fan-out, referential relationships, input/output reconciliation and transformation-specific invariants.

### 10. Business-semantic measurement
Examples: governed totals, balances, populations, ratios, rates or other business-defined measures whose meaning derives from Semantic Definition.

## Non-families

The following remain separate conclusions or concepts rather than metric families:

- readiness;
- overall/composite health;
- Impact/exposure/consequence;
- causality;
- Assertion Authority or Capability Authorization;
- gate/safeguard enforcement;
- compliance.

Metrics may provide evidence for those conclusions but cannot own them.

## Invariants

- Family membership does not make a metric profile-selected.
- Family membership does not make a metric semantically applicable to every table/column.
- A metric may reasonably serve more than one family/purpose when its definition is explicit; avoid duplicating the same Observation merely to satisfy taxonomy labels.
- `Structural/schema` is not a synonym for `validity`; observed structure and normative compatibility remain distinct.
- `Relational/transformation integrity` is not automatic propagation; valid reconciliation depends on transformation semantics and is refined in Group 05.
- `Business-semantic` does not mean business-only disclosure; audience visibility remains Capability Authorization/disclosure governance.
