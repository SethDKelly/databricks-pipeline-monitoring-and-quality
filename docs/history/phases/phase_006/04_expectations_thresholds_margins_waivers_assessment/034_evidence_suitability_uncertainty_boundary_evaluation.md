# HLTH-034 — Evidence Suitability, Uncertainty & Boundary Evaluation

## Purpose

Constrain normative conclusions when current evidence is sparse, approximate, sampled, incomplete or otherwise uncertain.

## Rule

A criterion evaluation considers whether the available Observation evidence is suitable for the intended `meets` or `violates` conclusion, including as applicable:

- measurement coverage/completeness;
- denominator/population size;
- approximation/sampling error or method limitation;
- temporal alignment/current-cycle identity;
- source availability and correction state;
- required structural/reference comparability;
- distance from the normative boundary relative to material uncertainty.

## Invariants

- Authoritative criterion + unsuitable evidence does not produce pass/fail.
- Missing telemetry is not a violation unless sufficient opportunity/coverage establishes the prohibited/required absence.
- Approximate values far enough from a boundary may support a conclusion when the method limitations cannot plausibly change the outcome.
- When material uncertainty spans the boundary, preserve an indeterminate/insufficient-evidence result unless the criterion explicitly defines a valid uncertainty treatment.
- Low-volume evidence can be sufficient for a literal count criterion while insufficient for a stable rate/distribution inference; suitability is conclusion-relative.
- Do not hide uncertainty inside a generic confidence score.

## Non-goals

- selecting statistical confidence intervals or libraries;
- weakening Phase 004 evidence standards;
- alert-routing policy.