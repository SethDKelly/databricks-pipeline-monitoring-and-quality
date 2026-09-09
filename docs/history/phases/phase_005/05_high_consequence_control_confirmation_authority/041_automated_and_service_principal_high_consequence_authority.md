# AUTH-041 — Automated and Service-Principal High-Consequence Authority

**Status:** Accepted — Phase 005 Group 05

## Purpose

Allow narrowly scoped automated high-consequence actions only when an exact service/control principal, action class, governing rule, and conditions are explicitly authorized.

## Contract

Automated high-consequence authorization should bind:

- exact service/control principal identity;
- permitted action class and target scope;
- applicable normative/control/confirmation profile version;
- evidence/readiness prerequisites and any human-approval conditions;
- rate, time, incident, environment, or blast-radius constraints where governed;
- fallback/escalation behavior when authorization/evidence/control state is unresolved;
- effective interval, revocation/disable path, and provenance.

## Invariants

- Service-principal identity, code deployment, scheduler ownership, or model output does not self-authorize high-consequence action.
- Automation may be authorized to propose, approve, execute, or confirm only for the exact stages explicitly granted.
- A recommendation or model-generated action proposal is not execution authority.
- Automated causal confirmation is allowed only for claim classes whose confirmation profile and authorization explicitly permit it and only when REF-013–REF-020 are satisfied.
- Automated gate/safeguard operation is allowed only when the exact control action is authorized; monitoring status alone is not permission.
- Human approval requirements, when specified, cannot be bypassed because the automation has technical ability to act.
- Revoking the service principal's capability changes future authorization without rewriting earlier legitimate actions.
- Automation authority does not prove that the action was delivered, enforced, or successful.

## Example

A service principal may be authorized to execute ordinary hold/admit decisions for one gate according to a versioned readiness profile, while all overrides require human approval. A separate deterministic causal profile may allow automated confirmation for one direct-control claim class but not for broader business-impact causality.