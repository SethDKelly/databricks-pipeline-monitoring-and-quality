# OPS-051 — Investigation Lifecycle, Scope Revision, Closure & Reopen

**Status:** Accepted — Phase 007 Group 05

## Purpose

Define a minimal Investigation lifecycle without turning Investigation into ticketing, remediation or causal status.

## Contract

A functional lifecycle may distinguish:

- `open` — inquiry exists and has a bounded question;
- `active` — evidence/candidates/localization are being evaluated;
- `paused` — inquiry intentionally not progressing while preserving unresolved state;
- `closed` — inquiry is complete for its stated current purpose.

Reopening creates a new active interval linked to the prior closure; it does not erase that closure.

Lifecycle state is independent of whether any Causal Claim is proposed, supported, confirmed, rejected or unresolved.

## Closure record

A closure records:

- investigation purpose at closure;
- closure disposition/reason;
- remaining material gaps/restrictions;
- linked Causal Claim states, if any, as references rather than Investigation-owned truth;
- closure actor/process provenance where applicable;
- knowledge time.

## Invariants

- closed ≠ root cause found.
- closed ≠ Causal Claim confirmed.
- paused ≠ evidence unavailable by definition.
- reopened ≠ prior closure was invalid.
- operational mitigation/completion can coexist with unresolved causality.
