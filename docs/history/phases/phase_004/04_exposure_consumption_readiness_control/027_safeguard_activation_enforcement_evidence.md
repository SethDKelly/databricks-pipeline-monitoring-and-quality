# REF-027 — Propagation Safeguard Activation and Enforcement Evidence

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define when a Propagation Safeguard can be treated as actually active/enforced at its intended output/publication/consumption boundary rather than merely proposed, configured, or requested.

## Enforcement binding

Safeguard evidence is bound to:

- the protected subject/output/version or missing-output context;
- the exact propagation/consumption boundary;
- the intended consumer/path scope;
- the effective protected interval;
- the safeguard action/state being asserted;
- the enforcement source and knowledge time.

## Rules

- Proposal, policy/configuration, activation request, or operator intent is not enough to establish external enforcement.
- `Active` requires sufficient evidence that the intended boundary was actually placed into the protected state for the relevant scope/time.
- Enforcement at one boundary or consumer set does not silently prove enforcement at every downstream/alternate path.
- If a safeguard protects publication of current output while an older state remains available, the current-version protection and stale-delivery condition are evaluated separately.
- Missing output does not become a quarantined object; evidence may instead establish that a downstream advancement/publication boundary was actively held.
- Release request is distinct from effective release when an external control source must actually remove the protection.
- Conflicting or unavailable enforcement evidence remains explicit.
- Safeguard state does not prove data defect, health, exposure, or business consequence.

## Temporal behavior

Activation request time, enforcement-effective time, release-effective time, framework knowledge time, and later correction time remain distinguishable where material.

## Non-goals

- choosing quarantine/hold implementation;
- safeguard authority definition;
- treating control configuration as enforcement;
- health or causal determination.
