# AUTH-020 — Metric Applicability, Baseline Use, and Structural-Change Review Authority

**Status:** Accepted — Phase 005 Group 03

## Purpose

Govern who may approve or revise the intended applicability of metrics, checks, Expectations, and comparison profiles after schema/grain/key or other structural change without allowing authority to manufacture empirical comparability.

## Contract

A structural-change review may govern:

- whether a metric/check remains intended for the changed context;
- whether a metric definition/profile version must be revised or retired;
- whether an Expectation must be revised prospectively;
- whether a Baseline is eligible to remain under review/use pending comparability evidence;
- whether a replacement Baseline should be derived once sufficient post-change evidence exists;
- which downstream consumers/dimensions require separate review.

## Critical separation

**governed applicability/use decision ≠ empirical Baseline comparability.**

Authority can decide that an old Baseline must no longer be used, or that a metric/profile requires review. It cannot declare evidence comparable when Phase 004/006 comparability conditions are not met.

Likewise, the framework may detect strong evidence that a Baseline is non-comparable without thereby gaining authority to redefine the normative Expectation or approve a new business threshold.

## Invariants

- Structural change triggers scoped review, not a mandatory global reset.
- Unaffected metrics/Baselines may remain applicable when their meaning/comparability is preserved.
- A changed grain/key/type can invalidate selected count/null/uniqueness/distribution/join relationships while leaving freshness or execution dimensions unaffected.
- A planned Change Intent can prompt review but not make the review outcome authoritative by itself.
- Metric/Profile retirement does not erase historical evidence.
- A new Baseline is derived from post-change evidence, never from an approved target value or planned effect.
- Phase 006 defines detailed comparability semantics; this contract defines governance standing for use/review decisions only.