# OPS-065 — Analyst / Automation Research, Provenance & Evidence Parity

**Status:** Accepted — Phase 007 Group 05

## Purpose

Ensure human and automated investigation assistance participate in the same concept/evidence model without granting either hidden truth or confirmation authority.

## Contract

An analyst or automated process may:

- open/refine Investigation scope when authorized;
- suggest leads and localization queries;
- link existing evidence;
- produce reproducible facts that are recorded through Observation/Change or another owning concept;
- propose Causal Claims;
- provide attributed commentary through Annotation.

The origin of a lead/research result is provenance. It is not evidence strength by itself.

Automated ranking, model confidence, analyst intuition, majority agreement or incident-role seniority do not become universal causal confidence/authority.

If a generated result cannot be reproduced or bound to an owning concept, it remains attributed research/context rather than silently entering structured operational truth.

## Invariants

- human assertion ≠ fact by title.
- model output ≠ fact by automation.
- same evidence must not be counted independently merely because both analyst and automation restate it.
- confirmation requires REF/AUTH semantics regardless of who generated the claim.
