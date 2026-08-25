# OPS-053 — Investigation Evidence Assembly, Roles, Contradiction & Gap Tracking

**Status:** Accepted — Phase 007 Group 05

## Purpose

Organize source-owned evidence around an Investigation without copying it into an Investigation truth store or filtering out inconvenient contradiction.

## Contract

Investigation may link evidence with an inquiry-specific role such as:

- outcome/symptom evidence;
- topology/relevance context;
- execution/version context;
- realized Change/deployment context;
- health/structural/Baseline/Expectation context;
- reconciliation/localization evidence;
- prospective-review context;
- supporting relevance for a lead;
- contradicting/discriminating evidence;
- negative/exclusion evidence;
- evidence gap/restriction/conflict.

The role describes relevance to the inquiry; it never changes the source concept's semantics.

Evidence assembly retains proposition applicability, provenance, event/effective time, knowledge time, coverage, common derivation and restrictions under REF-001–REF-012.

## Invariants

- linked evidence ≠ copied truth.
- evidence role ≠ causal status.
- contradiction cannot be discarded because it weakens the leading theory.
- missing evidence ≠ contradicting evidence.
- duplicated/common-derived evidence ≠ independent corroboration.
- Investigation relevance does not grant authorization to inspect restricted evidence.
