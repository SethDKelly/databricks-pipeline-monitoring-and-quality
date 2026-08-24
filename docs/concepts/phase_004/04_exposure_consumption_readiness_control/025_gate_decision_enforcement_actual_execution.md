# REF-025 — Execution Gate Decision, Enforcement, and Actual Execution

**Status:** Accepted — Phase 004 Group 04

## Purpose

Preserve the distinction among a gate's readiness evaluation, its admission/hold/override decision, actual enforcement of that decision, and the downstream execution that may or may not follow.

## Distinct propositions

The framework must be able to answer separately:

1. what readiness result was evaluated;
2. what gate decision/action was recorded or requested (`hold`, `admit`, `override`, expiry/fallback where applicable);
3. whether the intended control decision was actually enforced for the relevant downstream opportunity;
4. whether the downstream execution actually started/completed.

## Rules

- A readiness Assessment is not a gate decision.
- A gate decision/request is not automatically enforcement proof when an external control plane implements the decision.
- **Hold asymmetry:** if an applicable `hold` is recorded and sufficiently reliable Execution History proves the downstream execution started during the protected opportunity without an authorized override/release, that materially contradicts full hold enforcement.
- Absence of a downstream run supports hold enforcement only when the relevant execution opportunity and Execution History coverage are sufficient. Missing execution telemetry cannot prove enforcement.
- **Admit asymmetry:** `admit` means the gate barrier was removed/permitted. A downstream run not starting does not by itself prove admission failed; scheduling, compute, or other independent conditions may explain non-execution.
- A downstream run after `admit` can corroborate the sequence but does not by itself prove the gate admission caused the run.
- `override` permits proceeding despite the underlying readiness state; it does not rewrite readiness.
- Execution History remains the owner of actual run facts.

## Temporal behavior

Decision time, enforcement-effective time, downstream start time, framework knowledge time, and later correction time remain distinguishable where material.

## Non-goals

- choosing control-plane technology;
- defining timeout/fallback policy;
- treating admission as execution success;
- causal attribution for delay or execution.
