# AUTH-038 — Multi-Party Approval, Separation of Duties, and Conditional Authorization

**Status:** Accepted — Phase 005 Group 05

## Purpose

Represent high-consequence actions that require one or more independent approvals, role/identity separation, or other preconditions without introducing a generic workflow concept or approval-engine architecture.

## Contract

A conditional high-consequence authorization may require:

- one or more approval actions from explicitly eligible principal classes;
- distinct-principal or distinct-role requirements where separation of duties is intended;
- a quorum or ordered approval condition where explicitly defined;
- bounded subject/action/environment scope;
- evidence that approvals were current and applicable at execution time;
- expiry, revocation, or invalidation conditions;
- approval provenance and knowledge time.

Approval actions contribute evidence to Capability Authorization resolution for the exact requested action. They do not themselves become the target concept's operational state.

## Invariants

- Multi-party approval is never assumed merely because an action is high consequence; the requirement must be explicit.
- A `two approvals required` rule means two qualifying approvals under the rule, not two copies of the same approval or two identities that fail an independence requirement.
- Self-approval is neither universally allowed nor universally prohibited; the applicable rule decides.
- Approval by silence, timeout, or absence is not valid unless an explicit rule defines such behavior.
- A completed approval set can make an authorization condition satisfied; it does not prove the action was issued or enforced.
- Revoked/expired approvals cannot be silently reused for a later action opportunity.
- Separation of duties may differ by action: gate override, safeguard release, causal confirmation, and job cancellation need not share one policy.

## Example

A production gate override may require one incident lead approval plus one data-platform approval from distinct principals. Once both are evidenced, an authorized operator may execute the override. The approvals do not themselves override the gate.