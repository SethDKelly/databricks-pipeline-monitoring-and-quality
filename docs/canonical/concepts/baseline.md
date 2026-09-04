# Baseline

**Canonical key:** `concept.baseline`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.baseline`

**Owns current question:** What descriptive reference behavior is supported by comparable historical evidence for a subject/dimension/context?

**Stable IDs:** N/A

## Current semantics

Baseline owns empirical reference populations/windows, comparison context, derived characteristics, derivation meaning, evidence coverage/sufficiency, version, comparability limitations, prospective break context, provenance, and ambiguity.

## Actions

- `derive` — create a reference from sufficient comparable evidence.
- `refresh` — derive a new reference version without rewriting earlier use.
- `registerProspectiveBreak` — record that a Change Intent may make the reference non-comparable if realized.
- `markNonComparable` — close/limit future comparable use after a justified structural break.
- `resolveComparable` — return comparable candidates, insufficient evidence, non-comparable, ambiguous, unauthorized, or unavailable.

## Invariants / boundaries

- Baseline is descriptive, not normative.
- Typical ≠ healthy/acceptable; atypical ≠ degraded/defective/unacceptable.
- Change Intent may anticipate a break but cannot end/rewrite the active Baseline itself.
- Post-change Baselines are derived from post-change Observation evidence, never manufactured from planned values.
- Repeated abnormal behavior does not become an approved criterion through repetition.
- Sparse/non-representative evidence must not produce false precision.
- Refresh creates a new version and does not rewrite historical Assessments.
- Structural breaks/seasonality/calendar/population changes may make abundant history non-comparable.

## Ambiguity / evidence

Multiple plausible reference populations remain explicit. Missing history is insufficient evidence, not a default Baseline.

## Synchronizations / related canonical resources

Observation supplies evidence; Semantic Definition supplies grain/unit/context; Assessment compares current evidence descriptively; Expectation remains independent normative truth; Change Intent/Deployment/Change provide prospective/realized comparability context.

## Non-goals

Normative criteria, health declaration, anomaly algorithm selection, causal inference, or silent adaptation.

## Provenance

- `docs/concepts/phase_002/03_health_evaluation/baseline.md`
- `docs/concepts/phase_003/02_planned_change_and_reference_transition/`
