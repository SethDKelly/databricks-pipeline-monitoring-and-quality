# OPS-081 — Business Use, Decision & Customer Consequence Provenance

**Status:** Accepted — Phase 007 Group 06

## Purpose

Require explicit evidence when Impact extends from technical/analytical state into human/process/customer use.

## Contract

Business/process consequence assertions identify, where material:

- the report/application/result/process actually used;
- user/process/customer/client context at the allowed disclosure level;
- use/decision/action/delivery event or interval;
- consequence proposition and source evidence;
- whether evidence is system-recorded, derived, authoritative assertion or attributed human Annotation;
- limitations and knowledge time.

A human statement such as `the client used this report` remains attributed evidence unless independently corroborated under the relevant proposition.

`No business consequence` requires domain-appropriate opportunity and coverage; absence of a complaint or Annotation is insufficient.

## Invariants

- report publication ≠ human use.
- human view ≠ decision reliance.
- decision reliance ≠ adverse consequence unless separately evidenced.
- missing complaint/report ≠ no business consequence.
- business consequence evidence does not automatically attribute the consequence to the originating issue.
