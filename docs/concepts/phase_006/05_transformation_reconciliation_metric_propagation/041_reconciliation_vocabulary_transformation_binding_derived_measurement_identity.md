# HLTH-041 — Reconciliation Vocabulary, Transformation Binding & Derived Measurement Identity

## Rule

Cross-transformation health reasoning must distinguish:

1. **local input/output measurement** — an Observation about one bound asset/run/version;
2. **downstream-relevant upstream context** — a local Observation whose relevance is established by a time-valid typed transformation/dependency relationship;
3. **reconciliation definition/check** — a versioned semantic rule describing a valid relationship among bound inputs, transformation behavior, and output;
4. **reconciliation Observation** — a derived Observation produced from the bound evidence under that rule; and
5. **reconciliation Assessment** — an Assessment of the derived Observation against an explicit Expectation and/or comparable Baseline.

A reconciliation definition binds the exact transformation/version, input/output identities, roles, grain/population/window/current-cycle context, relevant fields/keys/measures, and derivation logic.

## Invariants

- Lineage identifies a relationship candidate; it does not create a reconciliation formula.
- A local metric value does not become an output metric merely because the asset is upstream.
- A local Assessment status is never copied as a reconciliation Assessment.
- Derived reconciliation Observations retain provenance to every material source Observation and the transformation/reconciliation definition used.
- Material transformation or reconciliation-rule changes require versioned semantics and later historical/reassessment handling.
- No new Reconciliation concept is required: Semantic Definition/check definition supplies meaning, Lineage supplies relationship context, Observation owns derived evidence, Expectation owns normative relationships, and Assessment owns evaluation.
