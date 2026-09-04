# CKR-E Semantic Conservation Matrix

**Status:** CUTOVER STATE — CLOSURE VALIDATION PENDING

CKR-E changes documentation ownership only. Acceptance requires preservation of HLTH-001–HLTH-066 and the Phase 006 exit model without importing OPS/EXPL/INTG/ARCH ownership.

| Domain | Must remain true after cutover | Canonical owner |
|---|---|---|
| Measurement identity | metric definition ≠ Observation ≠ Assessment; same display name does not guarantee definition continuity | `health-quality-timing/measurement-applicability.md` |
| Applicability/profile | semantic applicability ≠ profile selection ≠ computability ≠ current availability ≠ Assessment outcome; unavailable/not-selected/not-applicable are not pass | `measurement-applicability.md` |
| Structural health | declared/governed schema meaning ≠ structural Expectation ≠ proposed/planned state ≠ realized Observation/Change ≠ compatibility Assessment | `structural-compatibility.md` |
| Baseline/comparability | Observation ≠ reference membership ≠ Baseline ≠ comparative Assessment ≠ normative Expectation; typical ≠ acceptable | `baseline-comparability.md` |
| Normative assessment | criterion ≠ evidence ≠ Baseline comparison ≠ outcome ≠ warning ≠ severity ≠ waiver ≠ composite health | `normative-assessment.md` |
| Reconciliation | local Observation ≠ downstream relevance ≠ reconciliation rule ≠ derived Observation ≠ reconciliation Assessment ≠ Causal Claim; Lineage does not propagate status | `transformation-reconciliation.md` |
| Composite health | component Assessment ≠ bounded composite health; no universal score/majority/weighted/worst-child rule | `composite-health-readiness-timing.md` |
| Timing/suitability | evaluation time ≠ evidence freshness; no universal TTL; maturity follows evidence rather than elapsed time | `composite-health-readiness-timing.md` |
| Readiness/control | eligible ≠ suitable ≠ ready ≠ control authorization ≠ Gate decision ≠ enforcement ≠ execution | `composite-health-readiness-timing.md` |
| History | current rules are never projected backward; late/corrected evidence creates reassessment without rewriting prior state | all six resources |

## Phase-wide reasoning chain

Preserve distinct layers:

**definition/applicability → Observation/evidence → structural compatibility/comparability context → Baseline-relative and/or normative Assessment → transformation reconciliation where applicable → profile-bound composite health → freshness/maturity/suitability → readiness criterion under REF-024 → separate Gate/control decision, enforcement and execution under REF-025+.**

A valid result at one layer never manufactures the next.

## Scope isolation

CKR-E must not canonicalize or redefine OPS-001–123, EXPL-001–160, INTG-001–270 or ARCH-001–500. It may reference canonical concepts/SYN/REF/AUTH and later-family semantics only as boundaries.

CKR-E introduces no new concept, SYN, REF, AUTH or HLTH-067; selects no DQX/Metric View/Spark SQL/Unity Catalog/GitHub Actions/storage/streaming/cache/scheduler/control architecture; and introduces no universal health, confidence, anomaly or comparability score.

## Provenance

- `docs/concepts/phase_006/README.md`
- `docs/concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`
- Phase 006 Groups 01–06 remain detailed design history/provenance after cutover.
