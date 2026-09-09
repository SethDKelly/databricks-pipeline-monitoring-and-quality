# OPS-087 — Safeguard Lifecycle & Action-Fact Decomposition

**Status:** Accepted — Phase 007 Group 07

## Purpose

Keep safeguard proposal, authorization, issuance, enforcement, maintenance and removal facts separate rather than compressing them into one scalar lifecycle label.

## Contract

Where material distinguish:

- proposal;
- activation approval/authorization context;
- activation request/issuance;
- effective enforcement established;
- partial/failed/conflicting/unavailable enforcement;
- extension/renewal/scope revision;
- cancellation before enforcement;
- scheduled expiry and effective expiry;
- release request/authorization;
- effective release;
- supersession/retirement.

Existing convenience labels such as `active`, `released`, `cancelled` or `expired` summarize only the applicable evidence-backed facts.

## Invariants

- proposal ≠ authorization ≠ request ≠ enforcement.
- authorization ≠ external action acceptance/effect.
- `active` requires applicable enforcement evidence under REF-027.
- release request ≠ effective release.
- expiry configuration ≠ effective end of protection unless the applicable control semantics/evidence establish it.
- historical intervals are non-rewriting.
