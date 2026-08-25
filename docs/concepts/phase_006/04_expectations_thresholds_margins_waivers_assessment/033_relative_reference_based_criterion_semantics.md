# HLTH-033 — Relative / Reference-Based Criterion Semantics

## Purpose

Define normative criteria whose boundary is expressed relative to another value/reference without turning that reference into normative truth by implication.

## Rule

A relative criterion must explicitly bind:

- the target measurement;
- the reference type and exact reference identity/version where required;
- comparison formula and direction;
- denominator/base-value semantics;
- handling of zero/near-zero/negative references where material;
- reference comparability and evidence requirements.

Examples include `within 10% of Baseline B`, `no more than 5 minutes later than upstream completion`, or `reconciled total within 0.5% of authorized source total`.

## Invariants

- Baseline remains descriptive even when an Expectation explicitly adopts a relative relationship to it.
- If the referenced Baseline is non-comparable, ambiguous, unavailable or insufficient for the required claim, the normative evaluation may become indeterminate; another convenient Baseline is not silently substituted.
- Relative thresholds do not erase the provenance or uncertainty of the referenced value.
- Ratio/percentage comparison must preserve direction and denominator semantics.
- A reference revision does not retroactively rewrite historical Assessments made against the earlier referenced version.

## Non-goals

- transformation reconciliation formulas owned by Group 05;
- authority for choosing the reference;
- automatic Baseline-to-Expectation promotion.