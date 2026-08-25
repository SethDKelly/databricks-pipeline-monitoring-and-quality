# OPS-107 — Readiness Suitability, Readiness Result & Gate Decision Basis

**Status:** Accepted — Phase 007 Group 08

## Purpose

Preserve the complete separation between evidence suitability, readiness truth and the later Gate decision.

## Contract

For the exact opportunity, the Gate may consume:

1. source-owned facts/Assessments;
2. HLTH-063 exact-use suitability where health/result evidence is used;
3. REF-024 readiness evaluation for the declared criterion;
4. authorization/context needed to operate the Gate.

The readiness result remains one of the criterion-supported outcomes such as ready, not ready, unknown, conflicting, unavailable or unauthorized/undecidable where applicable.

A Gate decision records its **basis**, including normal criterion evaluation, authorized override, or explicitly applied fallback. Decision basis does not replace the underlying readiness result.

## Invariants

**health outcome ≠ evidence suitability ≠ readiness result ≠ Gate decision ≠ enforcement ≠ execution**.

A fresh violation can be suitable evidence for `not ready`; a stale `meets` result can be unsuitable. Neither suitability nor readiness grants Gate operating authority.