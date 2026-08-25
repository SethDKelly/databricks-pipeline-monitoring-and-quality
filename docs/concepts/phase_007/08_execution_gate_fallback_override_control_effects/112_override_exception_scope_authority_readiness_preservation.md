# OPS-112 — Override, Exception Scope, Authority & Readiness Preservation

**Status:** Accepted — Phase 007 Group 08

## Purpose

Represent opportunity-specific bypass without rewriting prerequisite truth or borrowing authority from ordinary Gate operation.

## Contract

An override binds:

- exact Gate/configuration and execution opportunity;
- readiness result being bypassed;
- exception rationale/scope/time;
- actor/principal and AUTH-036 capability evidence;
- any conditions/expiry attached to the override;
- decision delivery/enforcement evidence.

## Rules

- override authority is separate from Gate configuration/ordinary operation authority;
- `not ready`, `unknown`, `conflicting` or `unavailable` remains unchanged after override;
- override permits this bounded opportunity only; it does not change future criteria/configuration;
- unauthorized override request is not a valid override;
- an enforced override may still be followed by no execution;
- later stale/quality/delivery consequences remain independently evidenced.

Override is not a waiver of evidence truth and not a Propagation Safeguard release.