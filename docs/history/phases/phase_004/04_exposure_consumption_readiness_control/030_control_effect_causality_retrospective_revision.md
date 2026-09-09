# REF-030 — Control-Effect Causality and Retrospective Revision

**Status:** Accepted — Phase 004 Group 04

## Purpose

Apply the accepted causal and temporal standards to claims that a gate or safeguard caused, contributed to, or prevented an operational outcome, while preserving late evidence and actual historical control actions.

## Rules

- Direct control-mechanism evidence may support a causal claim quickly when the proposition is tightly bound and the applicable REF-013–REF-020 profile is satisfied.
- `Gate held C` does not automatically prove `gate caused missed delivery`; other scheduler, compute, upstream, or downstream conditions may be material alternatives.
- `Safeguard active` does not automatically prove `safeguard caused no client exposure`; use REF-028 for the scoped prevented-exposure determination and Causal Claim for broader consequences.
- When reliable evidence shows the downstream start was blocked throughout a hold interval and began only after the gate barrier was removed, that sequence can strongly support a gate-delay proposition, subject to alternative/coverage review.
- When enforcement is unknown, causal claims about control effects cannot outrun the enforcement evidence.
- Late enforcement, execution, refresh, or consumption evidence may strengthen, weaken, reject, or otherwise revise current causal/exposure conclusions.
- Retrospective revision never rewrites the actual gate decision, safeguard action, downstream execution, or explanation that existed at the historical knowledge time.
- Historical confirmed/support statuses remain reconstructable even when later evidence changes the current status.

## Non-goals

- counterfactual simulation;
- automatic causal confirmation;
- quantitative delay attribution;
- control remediation workflow.
