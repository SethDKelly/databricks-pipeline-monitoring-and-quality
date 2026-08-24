# AUTH-045 — Result, Basis, Provenance, and Detail-Level Disclosure Separation

**Status:** Accepted — Phase 005 Group 06

## Purpose
Allow an audience to receive an authorized conclusion without assuming entitlement to every metric, threshold, schema field, source identity, actor identity, evidence item, or authority rule underlying it.

## Contract
Disclosure is independently resolvable for:
- result/conclusion state;
- exact measured value and comparison basis;
- threshold/Expectation/Baseline detail;
- source/evidence identity;
- authority/authorization basis;
- actor/reviewer/confirmer/approver identity;
- rationale/provenance detail;
- uncertainty, restriction, and coverage limitations.

## Invariants
- Result visibility does not imply basis visibility.
- Basis restriction does not make the basis absent.
- When hidden basis materially limits how the visible result should be interpreted, an authorized limitation must remain visible at a safe abstraction.
- Disclosure may preserve `supported`, `confirmed`, `held`, `overridden`, `waived`, or similar state while hiding restricted basis details, but must not imply a stronger meaning because the basis is hidden.
- Visible provenance may be abstracted only when the abstraction itself is authorized and does not falsely attribute the state.
- Internal statement-to-basis traceability remains required even when the audience cannot inspect the basis.
