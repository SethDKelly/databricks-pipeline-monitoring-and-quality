# Decision Records — Phase 005 Group 05 High-Consequence Action, Control & Causal-Confirmation Authority

Continues after D-217.

### D-218 — Group 05 requires no new concept
**Status:** Accepted — Phase 005 Group 05
Capability Authorization owns permission/conditional approval state. Causal Claim, Execution Gate, Propagation Safeguard, Execution History, Deployment/Change, and other domain concepts retain actual action/state/outcome ownership. No generic high-consequence workflow concept is required.

### D-219 — High-consequence authorization is action- and lifecycle-stage specific
**Status:** Accepted — Phase 005 Group 05
Proposal/request, approval/authorization, execution/issuance, override/release/cancel, and review can require separate capabilities. Broad `operator`, `admin`, or owner labels do not grant every stage.

### D-220 — Causal confirmation remains jointly evidence- and authority-gated
**Status:** Accepted — Phase 005 Group 05
Confirmation requires the applicable REF-013–REF-020 evidence profile plus explicit confirmer Capability Authorization/authority for the bound claim class/context. Authorization cannot promote insufficient evidence.

### D-221 — Human versus automated causal confirmation is claim-profile scoped
**Status:** Accepted — Phase 005 Group 05
Some claim classes may require human confirmation; others may permit narrowly authorized automated confirmation. Neither human title nor service/model identity self-authorizes confirmation.

### D-222 — Job operational capabilities remain granular and independent from data access
**Status:** Accepted — Phase 005 Group 05
Retry/restart/trigger/cancel/scheduling/bounded operational actions can be independently authorized. Job-operation permission does not grant raw-data read, gate/safeguard authority, or prove resulting execution success.

### D-223 — Execution Gate authority is decomposed
**Status:** Accepted — Phase 005 Group 05
Registration/configuration, readiness/fallback policy configuration, enable/disable, ordinary hold/admit execution, override, and retirement may have different authorized principals. Control-use eligibility does not grant these capabilities.

### D-224 — Gate override never rewrites readiness
**Status:** Accepted — Phase 005 Group 05
A valid override authorizes execution despite the applicable readiness state. It does not change `not ready`, `unknown`, `conflicting`, or `unavailable` evidence into `ready` and does not prove enforcement.

### D-225 — Safeguard proposal, activation, and release are independently governable
**Status:** Accepted — Phase 005 Group 05
Proposal does not imply activation; activation does not imply release. Release can be independently high consequence because it restores propagation/consumption. Neither activation nor release authority proves enforcement or health.

### D-226 — Multi-party approval and separation of duties are explicit conditional-authorization semantics
**Status:** Accepted — Phase 005 Group 05
Quorum, distinct-principal/role requirements, ordering, and self-approval rules exist only when explicitly governed. Approval completion can satisfy Capability Authorization conditions but does not execute the high-consequence action.

### D-227 — Delegation is separately authorized, bounded, and non-transitive by default
**Status:** Accepted — Phase 005 Group 05
Exercise authority does not imply delegation authority. Temporary/delegated grants bind exact capability/target/context/time; re-delegation requires explicit permission; expiry/revocation preserve historical state.

### D-228 — Break-glass is explicit emergency authorization, not a universal superuser state
**Status:** Accepted — Phase 005 Group 05
Emergency authority must bind action, target, qualifying condition, duration, bypassed ordinary conditions, provenance, and any review/compensating controls. Urgency or authorization-source failure does not create break-glass authority.

### D-229 — Break-glass never manufactures evidence, readiness, health, or causality
**Status:** Accepted — Phase 005 Group 05
Emergency authorization can alter who may perform a specific action under governed conditions, but it cannot make prerequisites ready, data healthy, evidence sufficient, or a causal claim confirmed without the applicable evidence standard.

### D-230 — Automated high-consequence action requires exact service-principal authorization
**Status:** Accepted — Phase 005 Group 05
Technical ability, scheduler ownership, deployed code, or model recommendation does not authorize automation. Service principals may act only for explicitly granted stages/classes/targets/conditions, including any human-approval requirement.

### D-231 — Authorization-outage fallback is high-consequence-action specific
**Status:** Accepted — Phase 005 Group 05
There is no universal fail-open, fail-closed, always-hold, always-release, or administrator-fallback rule. `unknown/conflicting/unavailable` authorization remains truth while an explicit operational fallback may prescribe bounded action/non-action.

### D-232 — Existing protective state and authority to change it are separate
**Status:** Accepted — Phase 005 Group 05
An already enforced gate hold or safeguard can remain an actual control state during an authorization outage even when no new activation/override/release permission can be established. Continuing state is not a new authorization grant.

### D-233 — Authorization, approval, action issuance, external acceptance, enforcement, and outcome remain separate
**Status:** Accepted — Phase 005 Group 05
A complete audit chain preserves each material stage and its provenance/time. Approved does not mean executed; issued does not mean enforced; enforced does not mean desired outcome/health; control/operation authority never substitutes for operational evidence.

### D-234 — Group 05 exit gate satisfied; Group 06 next
**Status:** Accepted
Phase 005 Group 05 is complete with AUTH-033–AUTH-043. AUTH-001–AUTH-043 are accepted overall. Group 06 — Disclosure, Explanation & Audience Governance is next and has not started.
