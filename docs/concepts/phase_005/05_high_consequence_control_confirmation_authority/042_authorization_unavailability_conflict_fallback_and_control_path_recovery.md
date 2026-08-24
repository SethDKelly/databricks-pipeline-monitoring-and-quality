# AUTH-042 — Authorization Unavailability, Conflict, Fallback, and Control-Path Recovery

**Status:** Accepted — Phase 005 Group 05

## Purpose

Define how production-critical high-consequence paths behave when authorization evidence is unknown, conflicting, unavailable, expired, or revoked without rewriting the underlying Capability Authorization state.

## Contract

For each high-consequence action class, a governed operational fallback may specify what an implementation should do when authorization cannot resolve positively, such as refuse, preserve current protective state, escalate, use a separately authorized fallback principal, or apply another bounded behavior.

The fallback rule should bind:

- affected action/control class;
- unresolved authorization states to which it applies;
- target/environment/incident scope;
- fallback action or non-action;
- fallback principal/capability if one exists;
- expiry/recovery/reconciliation behavior;
- provenance and effective interval.

## Invariants

- `unknown`, `conflicting`, and `unavailable` remain authorization truth states; operational fallback does not rewrite them to `denied` or `allowed`.
- There is no universal fail-open, fail-closed, `always hold`, `always release`, or `always escalate` rule across all high-consequence actions.
- Preserving an already enforced protective state during an authorization outage is different from obtaining new authority to activate that state.
- A separately authorized fallback principal must be explicitly governed; the most convenient administrator does not inherit capability because the primary source is unavailable.
- Recovery from an authorization outage uses the authority/permission known at the actual recovery time; later evidence does not backdate approvals.
- Revoked or expired capability cannot be silently reused because a control path is degraded.
- Authorization availability requirements for production-critical actions are later architecture/SLO concerns; Group 05 defines semantics, not implementation.

## Example

A gate-override authorization source becomes unavailable while a gate is holding C. The configured policy may preserve the existing hold and escalate rather than inventing override permission. Another gate class could have a different explicitly governed fallback; no global policy is inferred.