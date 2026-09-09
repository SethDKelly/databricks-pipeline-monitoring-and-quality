# HLTH-008 — Metric/Check Observation Provenance & Evidence Binding

**Status:** Accepted — Phase 006 Group 01

## Purpose

Ensure every material metric/check Observation can be traced to the definition, inputs, scope and evidence limitations that produced it.

## Contract

A material metric/check Observation should retain or reference, where applicable:

- metric/check definition identity and version;
- measured subject/field/relationship;
- input source/evidence references and relevant output/data/schema versions;
- evaluation population, grain and window;
- unit and denominator/reference population where applicable;
- event/effective time represented by the measurement;
- source production/availability time when material;
- framework collection/knowledge time;
- derived evaluation time;
- sampling/approximation/partial-population status where material;
- bounded coverage/quality limitations relevant to interpretation;
- calculation/evaluation status and failures;
- restriction/sensitivity state needed for Authorized Analytical Projection;
- provenance relation when the same underlying telemetry is copied or re-expressed by multiple sources.

## Invariants

- A metric Observation is evidence, not self-proving truth beyond its bound proposition.
- Copied/mirrored representations of the same measurement do not become independent corroboration.
- Approximate/sampled metrics are not automatically invalid, but the approximation/sample context must remain available to later comparability/threshold reasoning when material.
- Missing provenance needed to identify subject/window/definition can make a metric unusable for a conclusion even if a numeric value exists.
- Restricted provenance may be hidden from a requester under Phase 005 disclosure rules while remaining internally bound if the framework is authorized to process it.
- Observation provenance does not confer Assertion Authority, Capability Authorization, profile inclusion, threshold standing or downstream propagation.
- Later correction of a metric Observation or its source preserves the historical value/knowledge cut and follows Phase 004 correction semantics.

## Handoff

Group 03 will use provenance to decide Baseline/reference comparability. Group 04 will use it when determining whether a metric can support an Assessment. Group 05 will use it when deriving transformation-aware reconciliation evidence. Group 06 will use it when deciding whether a result is mature/fresh enough for composite/readiness/control use.
