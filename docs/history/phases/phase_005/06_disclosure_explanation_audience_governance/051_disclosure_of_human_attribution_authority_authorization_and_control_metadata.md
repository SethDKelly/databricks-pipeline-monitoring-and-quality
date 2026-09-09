# AUTH-051 — Disclosure of Human Attribution, Authority, Authorization, and Control Metadata

**Status:** Accepted — Phase 005 Group 06

## Purpose
Treat identities and governance/control metadata as independently sensitive so valid operational or causal state can be disclosed without automatically exposing the people, roles, rules, or security posture behind it.

## Potentially sensitive detail

- Annotation author and text;
- Assertion Authority holder/rule/basis;
- Capability Authorization source or membership path;
- causal confirmer/reviewer identity;
- gate/safeguard approver or operator identity;
- delegation/grantor/delegate details;
- break-glass principal, reason, bypassed conditions, or compensating controls;
- automated/service-principal identity and control scope.

## Invariants

- Permission to see a state such as `confirmed`, `held`, `overridden`, or `break-glass used` does not imply permission to see actor identity or rule details.
- Actor identity may be replaced by an authorized role/category abstraction only when that abstraction is truthful and permitted.
- Hiding an actor does not make the action unattributed internally; provenance remains retained.
- An Annotation surfaced without its author identity must still be identified as human-provided context if that distinction is material.
- Authority/authorization opacity must not be worded as though no governing rule or authorized actor existed.
- Disclosure of security/control metadata does not itself grant the corresponding capability.
