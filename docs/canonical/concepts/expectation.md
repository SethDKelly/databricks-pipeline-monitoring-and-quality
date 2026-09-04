# Expectation

**Canonical key:** `concept.expectation`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.expectation`

**Owns current question:** What normative condition should be considered acceptable for a subject/dimension/context/time?

**Stable IDs:** N/A

## Current semantics

Expectation owns provenance-bearing normative criteria, their subject/dimension/context, effective/lifecycle state, authority standing, bounded exceptions/suspensions, revisions/retirement, and conflicts.

## Actions

- `establish` — record a normative criterion.
- `revise` — prospectively replace a criterion while retaining prior versions.
- `exceptFor` — record a bounded suspension/non-applicability without mutating evidence.
- `retire` — end future applicability.
- `resolveApplicable` — return applicable assertions, none known, conflicting, unauthorized, or unavailable.

## Invariants / boundaries

- Expectation is normative; Baseline is descriptive.
- Historical/common behavior does not become an Expectation through repetition.
- Change Intent anticipated effects do not become normative automatically.
- Applicability follows accepted effective/realization semantics rather than guessed plan-registration time.
- Expectation does not measure actual state or decide whether a criterion was met; Assessment does.
- Missing Expectation does not mean healthy/acceptable.
- A waiver/exception changes applicability/response, not Observation and not a false `pass`.
- Business criticality, responsibility, Classification, Policy Context, source availability, or metric ownership do not automatically grant normative authority.
- Control eligibility/authority/enforcement remain separate from normative truth.

## Ambiguity / evidence

Co-authoritative incompatible criteria remain normative conflict; no implicit strictest/latest precedence. Historical replay uses the criterion/exception state known/applicable at the requested cut.

## Synchronizations / related canonical resources

Observation provides evidence; Assessment evaluates it; Baseline remains descriptive; Change Intent can trigger explicit review; Deployment/Change can establish effective transition context; Gate/Safeguard may consume an explicitly eligible criterion without gaining authority from it.

## Non-goals

Measurement, Baseline derivation, health interpretation, causality, vendor rule syntax, or production-control capability.

## Provenance

- `docs/concepts/phase_002/03_health_evaluation/expectation.md`
- `docs/concepts/phase_005/03_expectation_metric_threshold_severity_governance/`
