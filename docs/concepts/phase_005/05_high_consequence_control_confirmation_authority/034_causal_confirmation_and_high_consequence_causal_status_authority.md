# AUTH-034 — Causal-Confirmation and High-Consequence Causal Status Authority

**Status:** Accepted — Phase 005 Group 05

## Purpose

Define who or what may perform high-consequence causal status actions—especially `confirmed`—for a bound claim class/context without weakening REF-013–REF-020 evidence standards.

## Contract

Causal-confirmation authorization should bind:

- exact Causal Claim or claim class;
- subject, effect, causal role, environment/context, and material scope;
- applicable confirmation profile/standard and version;
- permitted action such as confirm, reject under a governed high-consequence standard, or reopen/review where separately controlled;
- authorized confirmer principal/class;
- whether human review is required, permitted automation is allowed, or both;
- any multi-party/independence conditions;
- effective interval, expiry/review conditions, and provenance.

## Invariants

- Evidence sufficiency for confirmation remains mandatory; authorization cannot promote an insufficient claim.
- `supported` does not become `confirmed` because an authorized confirmer prefers the claim.
- A job owner, data owner, administrator, incident commander, model, or service principal has no confirmation authority unless explicitly granted for the bound claim class/context.
- Confirmation authority may differ by claim class. A deterministic direct-control claim may have a different confirmation profile and authorized confirmer set than a diffuse business-impact causal claim.
- Human review may be mandatory for some claim classes and optional for others only when an explicit rule says so.
- Automated confirmation is permitted only where an explicit authorization rule, confirmation profile, and exact service identity allow it; automation identity alone is not authority.
- A confirmation action preserves evidence cut, confirmer, profile, time, and prior status history.
- Later evidence may challenge a confirmed claim without erasing that historical confirmation.

## Example

A service principal may be authorized to confirm a narrowly deterministic proposition that a specific enforced gate suppressed a specific execution opportunity when the confirmation profile is fully satisfied. The same service principal may be restricted to `supported` for a multi-system business-impact causal proposition requiring human confirmation.