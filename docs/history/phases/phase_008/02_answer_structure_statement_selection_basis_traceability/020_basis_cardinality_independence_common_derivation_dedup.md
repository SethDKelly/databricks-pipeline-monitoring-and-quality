# EXPL-020 — Basis Cardinality, Independence, Common Derivation & Deduplication

**Status:** Accepted — Phase 008 Group 02

## Requirement

Retain the provenance relationships necessary to distinguish multiple basis items from multiple independent evidentiary sources.

Answer composition must account for:

- duplicate telemetry/events;
- repeated projections of the same source fact;
- common-derived facts produced from one upstream record;
- independently sourced corroborating propositions;
- source conflict.

## Invariants

- evidence count ≠ evidence strength/confidence;
- duplicate/common-derived basis ≠ independent corroboration;
- repeated mentions of the same fact do not strengthen the answer;
- the framework does not create a universal corroboration or confidence score from basis cardinality.

This contract inherits REF/OPS common-derivation discipline into Explanation traceability.
