# AUTH-036 — Execution Gate Configuration, Operation, and Override Authority

**Status:** Accepted — Phase 005 Group 05

## Purpose

Decompose high-consequence Execution Gate authority so registration/configuration, enablement, opportunity-specific operation, override, fallback policy, and retirement are not collapsed into one gate-admin permission.

## Contract

Execution Gate capabilities may independently include:

- register a target/prerequisite relationship;
- configure readiness criteria and approved control-eligible Expectation references;
- configure timeout/fallback/escalation policy where later defined;
- enable/disable a gate prospectively;
- issue/execute opportunity-specific hold/admit decisions when a control principal is permitted to do so;
- override an applicable readiness result for a bounded execution opportunity;
- cancel/expire an opportunity-specific control action where represented;
- retire the gate configuration.

Each capability binds target, environment, prerequisite/control profile version, effective interval, approval conditions, and provenance.

## Invariants

- AUTH-023 control-use eligibility for a metric/Expectation does not authorize gate configuration or operation.
- Authority to configure a gate does not imply override authority.
- Authority to override does not imply authority to change the gate's normal readiness criteria.
- An override never changes `not ready`, `unknown`, `conflicting`, or `unavailable` evidence into `ready`.
- A service principal that evaluates/executes the normal gate policy requires its own exact capability; it does not borrow the human approver's identity.
- Permission to issue a hold/admit/override is not evidence that the external control plane enforced it.
- Gate authorization rules do not create a universal fail-open/fail-closed policy for unavailable readiness or authorization evidence.
- Gate configuration/operation authority does not imply safeguard authority or raw-data access.

## Example

A governance authority may approve the readiness profile, a platform team may configure the gate, a service principal may execute ordinary hold/admit decisions, and a distinct incident role may hold time-bounded override authority. These capabilities remain separate.