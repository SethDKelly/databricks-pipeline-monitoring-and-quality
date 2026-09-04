# Measurement Vocabulary, Profiles & Applicability

**Canonical key:** `health.measurement-applicability`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** How are measurement identity, metric families, profile roles, applicability, availability and evidence provenance represented without turning measured values into health conclusions?

**Stable IDs:** HLTH-001–HLTH-008

## Current semantics

### HLTH-001 — Measurement Target, Scope, Grain, Window & Version Binding
A measurement binds subject, metric/check definition and version, grain/population, evaluation window, relevant output/data/schema/current-cycle context and material temporal provenance. A value without those bindings is not safely reusable across contexts.

### HLTH-002 — Metric, Check, Observation, Assessment & Result Vocabulary
Metric/check definitions express measurement meaning; measured numeric/categorical/boolean/structural facts are Observation; comparative or normative interpretation is Assessment. A metric value is not itself a health pass/fail.

### HLTH-003 — Canonical Metric-Family Taxonomy
Functional families include operational/output, temporal/freshness, structural/schema, volume/population, completeness, uniqueness/key integrity, validity/domain, distribution/shape, relational/transformation integrity and business-semantic measurement. The taxonomy classifies useful measurement, not mandatory implementation modules.

### HLTH-004 — Metric Definition Identity, Version & Semantic Binding
Metric identity includes material formula, denominator, unit, filter, grain/population, window and approximation semantics. Material meaning changes create an explicit definition/version boundary and require later comparability review; same display name does not establish continuity.

### HLTH-005 — Metric Profile Structure & Profile Roles
A governed metric profile selects purposeful measurements for a subject/context and may distinguish core operational/table, critical-field/business, transformation-specific reconciliation and diagnostic/on-demand roles. Profile membership is governance structure, not a new truth concept.

### HLTH-006 — Applicability, Selection, Computability & Availability Separation
Semantic applicability, governed profile selection, technical support/computability, current evidence availability and Assessment outcome are independent. `not applicable`, `not selected`, `unsupported`, `unavailable`, `pending` and `meets/pass` must not collapse.

### HLTH-007 — Metric Anti-Bloat, Routine/Diagnostic Use & Lifecycle Principle
Technical availability never requires routine collection. Metrics remain purpose-driven, lifecycle-governed and removable; diagnostic/on-demand evaluation does not silently create permanent profile membership.

### HLTH-008 — Metric/Check Observation Provenance & Evidence Binding
Material measurements retain subject/definition/version, grain/population/window, source/evidence provenance, collection/evaluation timing, method/approximation and known limitation context sufficient for later REF evidence evaluation and historical replay.

## Invariants / boundaries

- metric definition ≠ Observation ≠ Assessment;
- semantic applicability ≠ profile selection ≠ computability ≠ availability ≠ Assessment outcome;
- metric available ≠ metric useful;
- local metric usefulness ≠ downstream propagation;
- readiness, Impact, causality, authorization, control enforcement and compliance are not metric families.

## Synchronizations / related canonical resources

Semantic Definition and Entity Identity own meaning/identity; Observation owns measured facts; Assessment owns interpretation; Expectation and Baseline remain normative and descriptive reference bases respectively. AUTH-017 governs profile selection and AUTH-023 separately governs high-consequence-use eligibility.

## Provenance

- `docs/concepts/phase_006/01_measurement_vocabulary_metric_profiles/README.md`
- Phase 006 Group 01 accepted HLTH-001–HLTH-008.
