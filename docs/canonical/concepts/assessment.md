# Assessment

**Canonical key:** `concept.assessment`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.assessment`

**Owns current question:** What does authorized Observation evidence mean relative to explicit normative and/or descriptive reference context for one subject/dimension/context/time?

**Stable IDs:** N/A

## Current semantics

Assessment owns dimension-scoped interpretation: subject/dimension/time, basis type, exact Observation and Expectation/Baseline versions, basis-appropriate result, rationale, evidence/reference sufficiency, conflict/limitations, evaluation rule identity, reassessment history, and disclosure context.

## Actions

- `assess` — interpret evidence against explicit reference context.
- `reassess` — append a new conclusion after late/corrected evidence/reference context without rewriting the earlier conclusion.
- `explainBasis` — expose authorized basis, evaluation context, and limitations.

## Invariants / boundaries

- Assessment never mutates Observation, Expectation, or Baseline.
- Normative and descriptive results remain distinguishable: criterion met/violated ≠ typical/atypical.
- Typical does not imply normative health; atypical does not imply defect/degradation.
- Missing Observation is not automatically a violation; strong non-occurrence conclusions require sufficient negative evidence.
- No applicable Expectation and no comparable Baseline means insufficient/unassessed reference—not healthy.
- Assessment does not establish cause or downstream Impact.
- Historical Assessments retain the exact basis known/used then.
- Assessments are dimension-scoped by default. No implicit majority/average/universal health rollup is accepted; any composite requires explicit components/rule and cannot hide severe child state.
- Unknown, insufficient, conflicting, non-comparable, not-applicable, unauthorized, and unavailable are legitimate results.

## Ambiguity / evidence

Restricted audiences may see a derived conclusion without every threshold/value, but the visible basis/limitations must remain trustworthy and non-leaking.

## Synchronizations / related canonical resources

Observation supplies evidence; Expectation normative criteria; Baseline descriptive context; Investigation may consume material/unresolved Assessments without treating them as cause; Explanation communicates authorized results/basis.

## Non-goals

Measurement, normative rule definition, Baseline derivation, causal reasoning, Impact, incident workflow, or universal quality score.

## Provenance

- `docs/concepts/phase_002/03_health_evaluation/assessment.md`
- `docs/concepts/phase_006/`
