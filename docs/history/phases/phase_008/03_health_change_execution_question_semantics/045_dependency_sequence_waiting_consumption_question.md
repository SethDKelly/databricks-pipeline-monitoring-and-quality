# EXPL-045 — Dependency Sequence, Waiting & Consumption Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Did C wait for B?`, `what ran first?`, and `did C use B's output?` remain separate runtime propositions.

Preserve the ladder:

**effective dependency → expected/scheduled order → actual temporal precedence → evidenced waiting/hold relationship → run-specific version consumption**.

## Rules

- Lineage/dependency does not prove actual sequence;
- temporal precedence does not prove waiting;
- waiting does not prove version consumption;
- cross-source clock limits can leave ordering indeterminate;
- exact version consumption requires its own basis;
- these propositions do not establish causality by timing alone.