# AUTH-004 — Assertion Disagreement and Authority Conflict

**Status:** Accepted — Phase 005 Group 01

## Purpose

Keep domain assertion disagreement separate from conflict about the authority rules themselves.

## Conflict classes

### Assertion disagreement
Applicable assertions for the same authority target/context/time materially disagree.

### Resolved assertion disagreement
Assertions disagree, but accepted authority standing/precedence selects the authoritative resolution. Lower-standing assertions remain recorded and visible as disagreement where authorized.

### Authoritative assertion conflict
Two or more simultaneously authoritative assertions materially disagree and no accepted resolution rule chooses among them.

### Authority-rule conflict
Applicable authority rules disagree about holder standing, precedence, conditions, scope, or effective interval and no accepted governing rule resolves the rules themselves.

### Authority unknown/unavailable
No applicable accepted authority rule can be established, or required authority-rule evidence/source is unavailable.

## Invariants

- An assertion disagreement does not imply an authority-rule conflict.
- An authority-rule conflict cannot be resolved by applying one of the conflicting rules to itself.
- Conflicting authoritative assertions remain authoritative conflict rather than majority vote.
- Conflict is scoped to the same relevant target/context/time; different facets, schemes, environments, purposes, or intervals may legitimately differ.
- Resolved disagreement does not erase dissenting assertions or rewrite them as never having existed.
- Conflict status itself is historical and may later be resolved while preserving the earlier unresolved state.
