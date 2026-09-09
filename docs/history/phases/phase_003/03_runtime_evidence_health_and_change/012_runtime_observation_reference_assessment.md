# SYN-012 — Runtime Observation + Time-Valid Reference → Assessment

**Status:** Accepted — Phase 003 Group 03

## Outcome

Evaluate runtime/data Observations against the correct applicable Expectation and/or comparable Baseline for their actual subject/dimension/context/time, including reference transitions established in Group 02.

## Participating concepts and actions

- **Observation** — `retrieve`.
- **Expectation** — `resolveApplicable`.
- **Baseline** — `resolveComparable`.
- **Assessment** — `assess`, `reassess`.

## Trigger / initiating condition

A runtime or data Observation becomes available, including execution duration, completion timing, freshness, volume, completeness, schema/distribution, or other supported dimensions.

## Preconditions

Subject/dimension/measurement semantics are sufficient for comparison. Reference ambiguity is preserved rather than guessed.

## Coordination semantics

1. Resolve the Observation and its event/context time.
2. Resolve the time-valid normative Expectation branch and descriptive Baseline branch independently.
3. Respect Group 02 reference transitions: do not use the most recent stored Baseline when it is non-comparable for the new operating context.
4. Assess each basis explicitly; one branch may be available while the other is not.
5. Ordinary run-to-run variation remains represented by the Baseline distribution/range/comparison semantics; raw difference alone is not atypicality.
6. A Baseline-only atypical result remains descriptive. Normative violation requires an applicable Expectation.
7. Late/corrected observations or reference context produce linked reassessment, not silent replacement.

## State and evidence effects

Assessment owns the interpretation and exact basis references; source concepts retain their own state.

## Ambiguity / failure propagation

Insufficient post-change Baseline history, conflicting Expectations, partial Observations, or non-comparable context yield appropriate unresolved results rather than forced pass/fail.

## Temporal semantics

Assessment uses the reference context applicable to the Observation event time and records assessment/knowledge time separately.

## Provenance / traceability

Every result retains exact Observation and Expectation/Baseline versions plus evaluation logic provenance.

## Security / authorization

Safe derived status may be exposed while restricted thresholds/reference values remain hidden.

## Invariants

- small difference ≠ anomaly;
- atypical ≠ normative violation;
- normative violation ≠ cause;
- one dimension's success ≠ whole-ecosystem health;
- old Baseline ≠ automatically comparable after structural change;
- execution success ≠ duration/freshness/quality success.

## Scenarios

A 55-minute run is atypical versus a 20–30-minute Baseline but still meets a 60-minute completion Expectation; C volume is valid under a revised post-change Expectation while completeness fails; first post-change run has Expectation but insufficient Baseline.

## Non-goals

Alerting policy, Investigation decision, safeguard activation, or causal attribution.
