# HLTH-054 — Reconciliation Relevance, Localization, Downstream Assessment & Causal Separation

## Rule

Transformation reconciliation can establish that an upstream condition is materially relevant to a downstream transformation, localize where a discrepancy appears, or show that an expected cross-asset relationship was not satisfied. Those conclusions remain distinct from downstream normative failure and causal attribution.

## Invariants

- Upstream `violates` + Lineage + downstream `violates` does not by itself establish cause.
- Upstream `violates` can coexist with downstream `meets` when the transformation filters, repairs, defaults, aggregates, or otherwise isolates the condition.
- Upstream `meets` does not guarantee downstream `meets`; transformation logic itself can introduce defects.
- A reconciliation violation can be a downstream dimension-specific Assessment without implying overall/composite health status.
- First mismatch localization is not root cause.
- Multiple upstream conditions can remain simultaneously relevant without forced primary/percentage attribution.
- Causal propositions about A/B causing C belong in Causal Claim and use REF-013–REF-020; reconciliation evidence can support, weaken or leave them unresolved.
- Actual downstream exposure/Impact remains separately evidenced under Phase 004/Impact rules.
