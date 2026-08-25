# OPS-118 — Multiple Prerequisites, Criterion Composition & Membership

**Status:** Accepted — Phase 007 Group 08

## Purpose

Support multi-input readiness without inventing implicit all-upstream-ready semantics.

## Contract

A Gate criterion/profile explicitly defines:

- prerequisite/member identities and historical applicability;
- each member predicate and required evidence;
- composition logic sufficient to determine readiness;
- treatment of unknown/conflicting/unavailable members;
- criterion/profile revision and effective interval.

Composition may use explicit logical structures such as all-required, any-sufficient, conditional branches or another declared rule. No composition is assumed from graph shape.

## Rules

- Lineage fan-in does not automatically define Gate membership;
- one ready prerequisite does not imply composite readiness unless the declared logic allows it;
- one false predicate can legitimately decide an all-required criterion while unresolved members remain preserved as limitations/context;
- no universal percentage-ready score is accepted;
- changing prerequisite membership/logic creates a new criterion/profile revision rather than rewriting history.