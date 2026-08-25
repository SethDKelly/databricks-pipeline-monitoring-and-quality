# EXPL-002 — Requested Conclusion Type & Question Family

**Status:** Accepted — Phase 008 Group 01

## Requirement

Record the kind of conclusion the requester is actually seeking so evidence and source-owned propositions can be routed correctly.

Useful descriptive families include, without creating a closed universal enum:

- state/status/health;
- change/difference;
- execution/timing/version use;
- causality/`why`;
- downstream Impact/exposure/effect/consequence;
- control state/effect such as Gate or Safeguard;
- meaning/governance/responsibility/policy;
- authorization/capability;
- historical/comparative;
- mixed/compound.

The exact requested conclusion remains authoritative over the family label.

## Semantics

A family is routing and answer-contract metadata. It is not:

- a source of truth;
- an authority rule;
- a confidence level;
- an evidence-sufficiency rule by itself;
- permission to collapse distinct source propositions.

A question can legitimately belong to more than one descriptive family when it contains independent requested conclusions.

## Examples

`Why was report R stale?` potentially spans Assessment/freshness, Execution History, Investigation and Causal Claim. The `why` family does not let Explanation infer cause from timing.

`Was the change planned?` requests a Change Intent/realization proposition. Absence of a matching registered intent is not automatically proof that humans did not plan the change.

`Can I rerun it?` requests Capability Authorization, not Responsibility Assignment or historical execution state.
