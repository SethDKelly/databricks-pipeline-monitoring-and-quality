# Phase 006 Group 05 — Transformation Reconciliation & Metric Propagation

**Status:** Next — not yet started

## Goal

Define when upstream/downstream metrics have meaningful transformation-aware relationships rather than recursively copying statistics or local health statuses through Lineage.

## Accepted handoff from Groups 01–04

- HLTH-001–HLTH-008 bind local metric/check identity, profile role, applicability, availability and provenance;
- HLTH-009–HLTH-018 bind structural/interface/key/grain compatibility and scoped consequences;
- HLTH-019–HLTH-029 bind Baseline reference membership, empirical comparability, distribution context, normalization and uncertainty;
- HLTH-030–HLTH-040 bind exact normative criteria, warning/tolerance semantics, evidence-suitability gates, criterion outcomes, waivers, severity and historical reassessment;
- a local upstream `violates` or `atypical` result does not propagate automatically to downstream C;
- a downstream criterion can reference upstream/current-cycle evidence only when an explicit transformation/dependency relationship gives that comparison meaning;
- local measurement, related upstream context, derived reconciliation measurement and downstream normative Assessment remain separate;
- schema/key/grain transitions can change which reconciliation relationships are meaningful;
- relative/reference rules preserve exact reference identity and evidence limitations;
- uncertainty/availability limitations propagate as evidence limitations where relevant, not as fabricated pass/fail;
- waiver of one local criterion does not automatically waive a downstream reconciliation criterion.

## Review scope

- local metric versus related upstream evidence versus derived reconciliation measure;
- join semantics: eligible input populations, matched/unmatched populations, fan-out/cardinality shape, key completeness and duplicate effects;
- filters: included/excluded populations and intentional reduction;
- aggregations: total/balance conservation where semantically valid and non-conservation where not;
- deduplication: input/output relationship, selected-record semantics and uniqueness consequences;
- unions/merges: source contribution and overlap/duplicate semantics;
- null introduction/removal/defaulting through transformations;
- freshness/current-cycle dependency alignment;
- distribution/quantile relationships only when transformation semantics preserve meaning;
- normalization/reconciliation denominators and grain alignment;
- multiple upstream contributors without forced causal attribution;
- downstream consumer/path-specific relevance;
- propagation of metric definition/provenance/uncertainty/restriction limitations without blind metric inheritance;
- how reconciliation Observations become independently assessable under explicit Expectations.

## Questions to resolve

1. What is the precise difference between an upstream local metric, downstream-relevant context and a derived reconciliation metric?
2. Which transformation types support conservation/equality/range relationships, and which do not?
3. How do joins express expected match rate, unmatched population and fan-out without assuming row-count conservation?
4. How do filter, aggregation, dedupe and union semantics change valid metric relationships?
5. When can null/completeness or distribution behavior be related across a transformation without pretending it is inherited?
6. How should current-cycle/freshness alignment be represented for multi-input pipelines?
7. How do uncertainty, non-comparability and unavailable evidence constrain reconciliation results?
8. How should multiple abnormal upstream contributors remain relevant evidence without becoming causal attribution?

## Boundaries

- A+B→C never implies generic row-count arithmetic.
- Lineage alone never propagates metric values, Baseline status, warning, violation, severity or waiver.
- Upstream anomaly/violation does not automatically become downstream failure or cause.
- Group 05 defines functional reconciliation semantics; Phase 007 later refines Lineage-aware operational/change propagation.
- Do not define composite/overall health or control-readiness timing yet; Group 06 owns those.
- Do not select Spark implementation, DQX/Metric Views realization, SQL templates, graph engine, storage or compute architecture.

**Group 05 has not started.**