# REF-011 — Dependent Re-evaluation and Investigation Reopen Materiality

**Status:** Accepted — Phase 004 Group 02

## Purpose

Define when late/corrected evidence should cause dependent reasoning to be reevaluated and when a closed Investigation should become a reopen candidate, without reopening everything automatically.

## Dependency principle

A retained derived conclusion is a reevaluation candidate when the new/corrected evidence is part of, contradicts, changes the applicability of, or materially changes coverage for the basis used by that conclusion.

Potentially affected state includes Assessment, Baseline comparability, Change, Causal Claim support/status, Impact exposure/effect/consequence, gate/safeguard interpretation, Investigation outcome, and Explanation.

## Materiality classes

### No relevant dependency
The new evidence does not bear on the retained conclusion. No reevaluation is required merely because evidence arrived elsewhere in the ecosystem.

### Basis affected; outcome demonstrably unchanged
The evidence changes part of the basis/coverage, but the applicable evaluation rule establishes that the conclusion remains the same. A traceable `reviewed/no conclusion change` result may be appropriate where audit significance warrants it.

### Conclusion may change
The new evidence could legitimately alter status, applicability, support/contradiction, exposure, consequence, or another material statement. Re-evaluation is required before the current retrospective conclusion is treated as settled.

### High-consequence historical conclusion materially challenged
If corrected/new evidence materially undermines a closed Investigation outcome, confirmed/high-consequence Causal Claim, business consequence statement, safeguard/gate rationale, or retained Explanation, the state becomes a **review/reopen candidate** under the owning concept's later authority/workflow rules.

## Investigation reopen boundary

- late evidence does not automatically reopen every closed Investigation;
- closure does not immunize an Investigation from materially new evidence;
- Group 02 identifies a reopen/review candidate but does not invent who may reopen or the workflow implementation;
- causal confirmation challenge semantics are specialized in Group 03;
- actual historical control actions remain unchanged even when their rationale is retrospectively reevaluated.

## Provenance

Every reevaluation records the evidence change that triggered it, the earlier basis/conclusion, the new knowledge/evaluation time, and whether the conclusion changed, remained unchanged, or remains unresolved.

## Non-goals

- notification architecture;
- incident-ticket workflow;
- automatic reprocessing of all downstream state;
- causal confirmation rules;
- source-authority resolution.
