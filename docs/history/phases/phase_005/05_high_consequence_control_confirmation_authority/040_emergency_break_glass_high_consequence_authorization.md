# AUTH-040 — Emergency / Break-Glass High-Consequence Authorization

**Status:** Accepted — Phase 005 Group 05

## Purpose

Represent explicitly governed emergency authorization that can bypass or replace ordinary approval conditions for a bounded incident without becoming a universal superuser mechanism or rewriting evidence/readiness state.

## Contract

Break-glass authorization should identify:

- exact emergency action class and target scope;
- eligible principal/class;
- qualifying emergency/incident condition;
- which ordinary approval/authorization conditions may be bypassed or substituted;
- maximum duration/expiry and permitted action count where applicable;
- required reason/justification and provenance;
- required notifications, post-action review, or compensating controls where governed;
- revocation/termination behavior.

## Invariants

- Break-glass capability must be established before or explicitly during the emergency under an accepted governing basis; `this is urgent` does not create authority.
- Break-glass is action- and scope-specific, not blanket administrator access.
- It does not grant raw-data visibility unless that exact access is separately included.
- It does not convert an unmet/unknown gate prerequisite into `ready`, a quarantined output into `healthy`, or an insufficient causal claim into `confirmed`.
- Authorization-source unavailability does not automatically activate break-glass.
- A break-glass action remains provenance-bearing and historically distinguishable from ordinary authorization.
- Post-action review can be required without making the action retroactively unauthorized merely because review occurs later.
- Emergency permission does not prove the downstream control/action was enforced or successful.

## Example

During a major outage, an explicitly eligible incident commander may use a time-bounded break-glass capability to approve a specific gate override without the ordinary second approver. The gate still records `override`; the upstream prerequisite remains not-ready/unknown as evidenced.