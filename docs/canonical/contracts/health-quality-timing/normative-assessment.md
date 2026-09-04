# Expectations, Thresholds, Waivers & Normative Assessment

**Canonical key:** `health.normative-assessment`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** How is evidence evaluated against exact normative criteria while preserving Baseline context, uncertainty, warning bands, conflict, waivers and severity as distinct dimensions?

**Stable IDs:** HLTH-030–HLTH-040

## Current semantics

### HLTH-030 — Normative Criterion Binding & Evaluation Basis
A normative criterion binds subject/dimension, exact metric/check/structural definition, grain/population/window/context, operator/direction, boundary semantics, unit/denominator and any required reference basis.

### HLTH-031 — Threshold Direction, Boundary, Unit & Denominator Semantics
Threshold meaning includes comparison direction, inclusive/exclusive boundary, unit and denominator/population. Display labels and vendor defaults cannot fill missing semantics by implication.

### HLTH-032 — Warning Bands, Tolerance Margins & Proximity Semantics
Warning/proximity/tolerance semantics are explicit secondary regions or response rules. `meets + warning` can be valid; warning is not automatically violation, severity or waiver.

### HLTH-033 — Relative / Reference-Based Criterion Semantics
Relative criteria explicitly bind the reference identity/version and formula. Using a Baseline in a criterion does not make Baseline normative generally; an unusable required reference can make that evaluation indeterminate rather than selecting another convenient Baseline.

### HLTH-034 — Evidence Suitability, Uncertainty & Boundary Evaluation
Authoritative criteria do not overcome sparse, approximate, unavailable or misaligned evidence. If material uncertainty spans a boundary, preserve indeterminate/insufficient evidence unless an explicit valid uncertainty treatment applies.

### HLTH-035 — Normative Assessment Result Vocabulary & Basis Separation
For one bound criterion preserve at least `meets`, `violates`, `indeterminate/insufficient evidence`, `conflicting`, `unavailable` and `not applicable`. Warning, Baseline typicality, severity and waiver remain separate attributes/basis results.

### HLTH-036 — Baseline and Expectation Coexistence in Assessment
Descriptive and normative results coexist independently: typical+meets, atypical+meets, typical+violates and atypical+violates are all legitimate. An independent Expectation can be evaluated without a mature Baseline when evidence otherwise suffices.

### HLTH-037 — Multiple Expectations, Composition & Normative Conflict
Distinct dimension/context rules can coexist. Same-proposition conflict remains explicit absent accepted authority/composition semantics; strictest, loosest, newest, business, technical or highest-severity is never an implicit winner.

### HLTH-038 — Waiver, Exception, Suspension & Response-Disposition Semantics
`violates + waived response` remains a violation. A bounded exception that makes a criterion non-applicable is different. Waiver/exception/suspension cannot rewrite Observation/Baseline evidence or automatically waive other response/control classes.

### HLTH-039 — Severity, Priority & Escalation Separation from Criterion Outcome
Severity, priority and escalation are separate from criterion truth. Low-severity violations remain violations; high-criticality criteria can currently meet. Criticality does not manufacture Impact or threshold meaning.

### HLTH-040 — Historical Criterion/Rule Binding, Correction & Reassessment
Assessments retain exact rule/version, warning/tolerance, waiver, evidence/reference versions and temporal provenance. Corrections create reassessment/supersession without projecting current rules backward or rewriting earlier results.

## Invariants / boundaries

Expectation/criterion ≠ Observation evidence ≠ Baseline comparison ≠ normative Assessment outcome ≠ warning/proximity ≠ severity/priority ≠ waiver/response disposition ≠ composite health.

Missing telemetry is not a violation unless sufficient opportunity/coverage establishes the relevant negative proposition under REF rules.

## Provenance

- `docs/concepts/phase_006/04_expectations_thresholds_margins_waivers_assessment/README.md`
- Phase 006 Group 04 accepted HLTH-030–HLTH-040.
