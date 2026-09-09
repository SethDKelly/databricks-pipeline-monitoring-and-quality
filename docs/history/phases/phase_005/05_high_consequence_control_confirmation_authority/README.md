# Phase 005 Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority

**Status:** Accepted — AUTH-033–AUTH-043

## Goal

Refine high-consequence authorization for causal confirmation, job/run operations, Execution Gates, Propagation Safeguards, delegation, multi-party approval, break-glass, and automation while preserving Phase 004 evidence/control semantics and Group 04 permission-resolution truth.

## Accepted handoff from Groups 01–04

- Assertion Authority and AUTH-001–AUTH-032 are accepted;
- Capability Authorization is exact principal/capability/subject/context/time permission truth;
- `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` remain distinct from runtime fallback behavior;
- principal composition/inheritance requires explicit rules and historical evidence;
- high-consequence-use eligibility for a metric/Expectation does not grant control authority;
- permission to act does not make the result authoritative or prove action/enforcement/success;
- Causal Claim `confirmed` retains the REF-013–REF-020 evidence gate;
- gate readiness/decision/enforcement/execution remain separate;
- safeguard proposal/configuration/enforcement/prevention remain separate;
- historical authorization is reconstructable but never reusable as current permission.

## Accepted contracts

- **AUTH-033 — High-Consequence Action Target and Lifecycle Decomposition**
- **AUTH-034 — Causal-Confirmation and High-Consequence Causal Status Authority**
- **AUTH-035 — Job and Run Operational Action Authority**
- **AUTH-036 — Execution Gate Configuration, Operation, and Override Authority**
- **AUTH-037 — Propagation Safeguard Proposal, Activation, Release, and Recovery Authority**
- **AUTH-038 — Multi-Party Approval, Separation of Duties, and Conditional Authorization**
- **AUTH-039 — Delegation, Temporary Grant, Expiry, and Revocation of High-Consequence Capability**
- **AUTH-040 — Emergency / Break-Glass High-Consequence Authorization**
- **AUTH-041 — Automated and Service-Principal High-Consequence Authority**
- **AUTH-042 — Authorization Unavailability, Conflict, Fallback, and Control-Path Recovery**
- **AUTH-043 — Action, Approval, Enforcement, Outcome, and Historical Audit Separation**

## Core accepted distinctions

### High-consequence actions are lifecycle-specific

`Propose/request`, `approve/authorize`, `execute/issue`, `override/release/cancel`, and `review` can require different capabilities. One broad `operator` or `admin` permission is not sufficient conceptually.

A principal can legitimately be permitted to approve but not execute, execute an already approved action but not self-approve it, or propose a safeguard while lacking activation authority.

### Causal confirmation remains both evidence- and authority-gated

Confirmation authority is claim-class/context/profile scoped. An authorized confirmer cannot promote insufficient evidence. Human review may be mandatory for some claim classes, while narrowly deterministic classes may permit explicitly authorized automated confirmation.

No role, title, model, service principal, or job owner self-authorizes `confirmed` status.

### Job operations remain independent

Retry, restart, cancel, trigger, scheduling/control action, and bounded operational modification are separately governable. Job-operation authority does not grant raw-data read, gate/safeguard authority, or code/deployment authority, and an authorized operation does not prove a resulting run succeeded.

### Gate authority is decomposed

Gate registration/configuration, readiness/fallback policy configuration, enable/disable, normal opportunity-specific hold/admit execution, override, and retirement can have different capabilities.

Control-use eligibility from Group 03 does not grant these capabilities. Override never converts `not ready`/`unknown` into `ready`, and permission to issue a gate decision never proves enforcement.

### Safeguard activation and release are independently high consequence

Proposal, approval, activation, extension, cancellation, release, and retirement/expiry can be independently authorized. Release is not assumed to be lower risk than activation because it restores propagation/consumption.

Safeguard release does not prove health, and activation permission does not prove the boundary was actually protected.

### Conditional authorization can require multi-party approval

Approval requirements are represented as explicit conditions on the exact Capability Authorization. Distinct-principal/role requirements, quorum, ordering, or self-approval rules exist only when explicitly governed.

Completed approvals make an authorization condition satisfiable; they do not execute the action.

### Delegation is explicit and bounded

Capability exercise does not imply delegation authority. Temporary grants bind exact action/target/context/time and preserve expiry/revocation history. Re-delegation is not assumed.

### Break-glass is governed, not magical

Emergency authorization must be explicit, scoped, time-bounded, and provenance-bearing. It may replace specified ordinary approval conditions when the rule permits, but it does not create raw-data access, readiness, health, causal sufficiency, or control enforcement.

### Automation can be high-consequence only by explicit grant

A service principal may be authorized for narrowly scoped normal gate actions, safeguard actions, or deterministic confirmation profiles, but technical capability or model recommendation is not authority. Human-review requirements remain binding where declared.

### Authorization outage behavior is action-specific

`Unknown`, `conflicting`, and `unavailable` authorization remain truth states. A production-control implementation may preserve a hold, refuse a release, escalate, or use a separately authorized fallback principal only when an explicit rule says so. There is no universal fail-open/fail-closed or `always hold` rule.

### Audit chain preserves every stage

Where material:

**request → authorization/approval → action issuance → control-plane acceptance → enforcement/effect → resulting domain state → downstream outcome**

remain separate facts with their own provenance/time. Authorization never substitutes for enforcement or outcome evidence.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes representative causal-confirmation, job-operation, gate/safeguard, delegation, approval, break-glass, automation, outage, revocation, and audit-chain scenarios.

No new Concept is required. **Capability Authorization remains the permission truth owner; Causal Claim, Execution Gate, Propagation Safeguard, Execution History, Deployment/Change, and other domain concepts retain actual state/outcome ownership. The catalog remains 24 concepts.**

## Boundaries preserved

Group 05 does **not**:

- select IAM/RBAC/ABAC, approval/workflow engine, scheduler/orchestrator, quarantine mechanism, control-plane API, or causal engine;
- define the Phase 006 metric/statistical/schema-health computation model;
- weaken REF-013–REF-030 evidence/control semantics;
- treat Group 03 control-use eligibility as operational permission;
- grant raw-data visibility merely because an operator needs action permission;
- equate authorization/approval with action issuance, enforcement, success, health, or cause;
- decide Group 06 audience/disclosure wording and review policy.

## Exit

**Group 05 is accepted with AUTH-033–AUTH-043. AUTH-001–AUTH-043 are accepted overall. Group 06 — Disclosure, Explanation & Audience Governance is next and has not started.**
