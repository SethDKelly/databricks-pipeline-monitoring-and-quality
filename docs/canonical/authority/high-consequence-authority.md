# High-Consequence Action, Control & Causal-Confirmation Authority

**Canonical key:** `auth.high-consequence-authority`

**Kind:** AUTHORITY

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.AUTH`

**Owns current question:** How are causal confirmation and operational/control actions authorized without collapsing approval, issuance, enforcement and outcome?

**Stable IDs:** AUTH-033–AUTH-043

## Current semantics

### AUTH-033 — High-Consequence Action Target and Lifecycle Decomposition
Request/propose, approve/authorize, execute/issue, override/release/cancel and review are separately governable lifecycle actions.

### AUTH-034 — Causal-Confirmation and High-Consequence Causal Status Authority
Causal confirmation is claim-class/context/profile scoped and jointly REF-017 evidence-gated plus authorization-gated. No title, model, service principal or incident role self-authorizes confirmation.

### AUTH-035 — Job and Run Operational Action Authority
Trigger/retry/restart/cancel and bounded operational modifications are granular and independent from raw-data, deployment, Gate and Safeguard authority.

### AUTH-036 — Execution Gate Configuration, Operation, and Override Authority
Gate registration/configuration, readiness/fallback policy, enable/disable, normal HOLD/ADMIT, override and retirement may require different capabilities. Override never rewrites readiness or proves enforcement.

### AUTH-037 — Propagation Safeguard Proposal, Activation, Release, and Recovery Authority
Proposal, approval, activation, extension, cancellation, release and retirement/expiry are independently governable. Release does not prove health/recovery and activation authority does not prove effective protection.

### AUTH-038 — Multi-Party Approval, Separation of Duties, and Conditional Authorization
Quorum, ordering, independence and self-approval restrictions are explicit conditions on exact capabilities. Approval completion does not execute the action.

### AUTH-039 — Delegation, Temporary Grant, Expiry, and Revocation of High-Consequence Capability
Exercise authority does not imply delegation. Delegated grants are exact-scope, time-bounded, expiring/revocable and non-transitive unless explicitly governed.

### AUTH-040 — Emergency / Break-Glass High-Consequence Authorization
Break-glass is explicit, scoped, time-bounded emergency authorization. It cannot manufacture raw-data permission, readiness, health, evidence sufficiency or causality beyond its governed capability.

### AUTH-041 — Automated and Service-Principal High-Consequence Authority
Automation requires exact explicit grants and cannot bypass required human review. Technical capability/model recommendation is not authority.

### AUTH-042 — Authorization Unavailability, Conflict, Fallback, and Control-Path Recovery
Authorization outage behavior is action-specific; no universal fail-open/fail-closed/always-hold/always-release rule exists. Existing protective state and authority to change it are separate.

### AUTH-043 — Action, Approval, Enforcement, Outcome, and Historical Audit Separation
Where material preserve request → authorization/approval → issuance → control-plane acceptance → enforcement/effect → resulting state/outcome as separate provenance-bearing facts.

## Invariants / boundaries

Permission/approval ≠ action issuance ≠ enforcement ≠ success/outcome. Gate/Safeguard proof remains REF-owned; domain concepts retain actual state.

## Provenance

- `docs/concepts/phase_005/05_high_consequence_control_confirmation_authority/README.md`
