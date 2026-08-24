# AUTH-039 — Delegation, Temporary Grant, Expiry, and Revocation of High-Consequence Capability

**Status:** Accepted — Phase 005 Group 05

## Purpose

Govern temporary or delegated high-consequence capability without assuming that possession of a capability includes the right to delegate it or that delegation propagates transitively.

## Contract

A delegation/temporary grant should bind:

- grantor or governing authority;
- delegate principal;
- exact delegated capability/action class;
- subject/environment/incident scope;
- effective start and expiry/termination condition;
- whether re-delegation is permitted;
- approval/separation conditions;
- revocation authority and provenance;
- recorded/knowledge time.

## Invariants

- Ability to exercise a capability does not automatically include ability to delegate or grant it.
- A governing grant-maker may be authorized to grant a capability without being intended to exercise it; do not infer grant semantics from exercise semantics.
- Delegation cannot silently broaden target, environment, action class, or time scope.
- Re-delegation is prohibited unless explicitly allowed by the governing rule.
- Temporary grants expire prospectively and preserve historical authorization state.
- Revocation changes future/current authorization from its effective point; it does not rewrite actions legitimately authorized earlier.
- A delegated capability remains subject to the same evidence/control constraints as the original capability.
- Delegation of gate authority does not imply safeguard, raw-data, or causal-confirmation authority.

## Example

An incident lead receives a two-hour delegated capability to approve safeguard activation for one production incident. The grant expires automatically and cannot be reused for another incident or delegated onward unless the rule explicitly permits it.