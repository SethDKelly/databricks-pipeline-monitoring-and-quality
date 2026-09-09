# HLTH-040 — Historical Criterion/Rule Binding, Correction & Reassessment

## Purpose

Preserve non-rewriting normative evaluation across rule changes, waivers, corrected evidence and later knowledge.

## Rule

Every normative Assessment retains the exact Expectation/criterion version, warning/tolerance structure, waiver/exception state, Observation evidence, reference/Baseline version where applicable, evaluation logic/version, evaluated time and framework knowledge/evaluation time.

Later changes produce new prospective rules or reassessments rather than mutating earlier conclusions.

## Invariants

- Current thresholds are not projected backward into historical incidents.
- A later corrected Observation can justify a new reassessment while preserving the original Assessment and why it was reached.
- A later authority correction can change retrospective rule resolution without fabricating what was known/authoritative then.
- Waiver expiry/revocation does not retroactively remove an earlier valid waiver.
- A new Baseline/reference version does not silently replace the one used by a historical relative criterion.
- Historical replay can distinguish actual retained Assessment from a reconstructed as-known-then evaluation and current retrospective evaluation.

## Non-goals

- persistence/event-store design;
- historical disclosure authorization;
- incident workflow.