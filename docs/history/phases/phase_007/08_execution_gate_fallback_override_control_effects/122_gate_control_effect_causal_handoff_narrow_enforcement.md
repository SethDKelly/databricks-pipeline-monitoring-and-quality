# OPS-122 — Gate Control-Effect Causal Handoff & Narrow Enforcement Effect

**Status:** Accepted — Phase 007 Group 08

## Purpose

Separate the narrow control fact established by enforcement from broader causal claims about downstream outcomes.

## Contract

When REF-026 evidence establishes that a Gate barrier actually constrained a specific execution opportunity, the framework may state the bounded control fact that **this Gate held/suppressed admission for that opportunity during interval W**.

Broader claims such as:

- the Gate caused a missed delivery;
- the Gate caused consumer staleness;
- the Gate prevented stale recomputation;
- the Gate prevented a business consequence;
- the override caused downstream degradation;

are causal propositions and use Causal Claim under REF-013–REF-020/REF-030.

## Rules

- temporal proximity is not sufficient causal attribution;
- scheduler/compute/upstream/downstream alternatives remain relevant;
- control enforcement evidence limits how strong a control-effect claim can be;
- actual consumption/version/effect evidence remains source-owned;
- no quantitative delay attribution or counterfactual simulator is accepted in Phase 007.