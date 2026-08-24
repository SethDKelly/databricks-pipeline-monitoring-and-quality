# AUTH-017 — Metric Profile Selection, Purpose, and Critical-Metric Authority

**Status:** Accepted — Phase 005 Group 03

## Purpose

Govern which metrics/checks are selected for an asset/context and which are designated core, critical-field, transformation-specific, business-critical, or diagnostic without treating metric availability as a reason to compute or elevate everything.

## Contract

A governed metric profile is a provenance-bearing selection/applicability structure over existing metric/Expectation/Assessment dimensions. It is not a new operational truth concept.

Profile governance should be able to identify:

- subject or bounded scope;
- metric/check identity or semantic definition reference;
- purpose and monitored failure mode/business use;
- applicability context and lifecycle state;
- profile role such as core, critical-field, transformation-specific, business-critical, or diagnostic/on-demand;
- authority/provenance for inclusion, revision, and retirement;
- optional review cadence/cost-latency constraints as governance metadata without choosing implementation.

## Invariants

- A metric being technically available does not justify profile inclusion.
- Metric-profile authority is separate from authority over the metric's business meaning, calculation semantics, threshold, severity, or control use.
- Marking a metric business-critical does not prove current business Impact or consequence.
- Criticality Classification can inform prioritization/profile review but does not automatically add every available metric.
- A new column does not automatically receive null-rate, quantile, cardinality, or other checks merely because they can be computed.
- Removing a metric from a profile does not erase historical Observations/Assessments.
- A profile can require review after schema/grain/key changes without deciding whether a historical Baseline remains empirically comparable.
- Phase 006 defines the metric taxonomy and statistical/health meaning; Group 03 only governs selection/standing.

## Anti-bloat rule

Every governed retained metric/check should have an identifiable purpose, applicable context, expected use/audience, authority/owner, and lifecycle/retirement path. Availability alone is insufficient.