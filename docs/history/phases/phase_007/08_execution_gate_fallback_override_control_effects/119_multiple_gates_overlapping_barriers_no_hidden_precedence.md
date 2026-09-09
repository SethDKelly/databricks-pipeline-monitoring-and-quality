# OPS-119 — Multiple Gates, Overlapping Barriers & No Hidden Precedence

**Status:** Accepted — Phase 007 Group 08

## Purpose

Handle multiple Gate configurations applicable to the same execution opportunity without inventing a universal `most restrictive wins` or source-precedence rule.

## Rules

- each Gate retains independent identity, criterion/result, decision, authority and enforcement state;
- ADMIT by one Gate does not prove the execution opportunity is globally unblocked while another applicable barrier may remain;
- HOLD by one Gate does not explain another Gate's state;
- conflicting-looking decisions can both be valid propositions about different barriers;
- effective overall admission behavior requires explicit composition/control semantics and evidence; it is not inferred from list order, Criticality, actor rank or creation time;
- actual execution can contradict the hypothesis that an applicable HOLD barrier was fully enforced while leaving other Gate records intact;
- no aggregate Gate effectiveness/control score is accepted.

Grouped summaries must preserve material Gate-level differences.