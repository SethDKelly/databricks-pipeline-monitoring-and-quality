# HLTH-051 — Reconciliation Evidence, Provenance, Uncertainty & Restriction Propagation

## Rule

A reconciliation Observation must preserve the material evidence limitations of its inputs and derivation. Derivation does not upgrade evidence quality.

Retain, as applicable:

- source Observation identities and versions;
- transformation/reconciliation definition version;
- input/output versions, grain/population/window/current-cycle context;
- source coverage/completeness limitations;
- sampling/approximation method and material uncertainty;
- non-comparability or ambiguous context affecting the derivation;
- restriction/sensitivity state and disclosure limitations;
- evaluation/knowledge time.

## Invariants

- If a required input is unavailable, the reconciliation cannot silently substitute zero or pass.
- If input uncertainty materially spans a reconciliation boundary, the derived normative Assessment remains indeterminate unless the rule explicitly provides a valid treatment.
- Copied/mirrored upstream evidence does not become independent corroboration through reconciliation.
- A derived aggregate can remain sensitive even when raw rows are hidden.
- Authorized processing of restricted inputs can produce an authorized analytical projection, but derivation is not declassification.
- Derived reconciliation evidence cannot be more temporally current than the material evidence it actually relies upon.
