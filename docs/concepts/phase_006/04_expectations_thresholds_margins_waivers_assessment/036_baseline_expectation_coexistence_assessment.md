# HLTH-036 — Baseline and Expectation Coexistence in Assessment

## Purpose

Allow descriptive and normative interpretations of the same Observation to coexist without one overriding the other.

## Rule

An Assessment may carry separate basis-specific results for:

- normative Expectation evaluation; and
- descriptive Baseline comparison.

Representative combinations include:

- typical + meets;
- atypical + meets;
- typical + violates;
- atypical + violates;
- non-comparable/insufficient Baseline + meets/violates where the normative criterion is independently evaluable;
- descriptive comparison available while no applicable Expectation exists.

## Invariants

- `within Baseline` never substitutes for `meets`.
- `outside Baseline` never substitutes for `violates`.
- A newly changed regime can lack a Baseline while still receiving a normative result from an independently applicable Expectation.
- A relative Expectation explicitly referencing a Baseline is different: that specific normative criterion may become indeterminate if its required reference is unusable.
- Repeated violations can become typical without becoming acceptable.
- Atypical improvement can still meet or outperform a normative criterion.

## Non-goals

- composite health;
- causal interpretation of atypicality;
- automatic Expectation generation from Baseline.