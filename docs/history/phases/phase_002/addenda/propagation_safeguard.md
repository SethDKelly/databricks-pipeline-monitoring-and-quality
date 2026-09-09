# Concept: Propagation Safeguard

**Status:** Accepted — Phase 002 post-exit addendum discovered during Phase 003 Group 03

## Purpose

Let an authorized actor or accepted response rule protect downstream consumers by placing a defined data-output or consumption boundary into a temporary hold/quarantine state and later releasing it, without changing the underlying evidence or asserting that the data is defective, causal, or safe.

## Operational principle

Table C produces an output whose completeness Assessment violates a requirement and whose downstream Impact context includes client-facing deliverables. The ecosystem can propose a safeguard at C's publication boundary or another justified downstream boundary. If authorized enforcement evidence establishes that the safeguard became active, affected consumption is held while Investigation proceeds. The safeguard does not rewrite the Observation, Assessment, or Causal Claims. If later evidence supports release, release is recorded explicitly and does not imply that every health dimension is healthy.

If C fails to produce an output at all, there is no nonexistent object to quarantine. A safeguard may instead hold downstream advancement, prevent a stale prior output from being represented as the current cycle, or protect a specific consumer boundary where the product/environment supports that behavior.

Where dependency-readiness control is enabled, an **Execution Gate** may separately prevent a downstream job from starting before a required current upstream state is ready. That start-admission control can reduce stale-recomputation risk, but it does not replace Propagation Safeguard: safeguards still own output/publication/consumption protection when a suspect state exists, no qualifying output exists, or protection is needed at a consumer boundary.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Data Owner / accountable business party
- Data Steward / Governance Steward
- Incident responder / on-call engineer
- Business Analyst / authorized operator
- Monitoring framework
- Authorized external control/enforcement source

## State

- safeguard identity;
- identified protected subject, output instance/version/execution context, or propagation boundary;
- safeguard kind, such as hold or quarantine, without prescribing implementation;
- intended downstream protection scope;
- lifecycle state, including proposed, active, released, cancelled, expired, or unresolved where useful;
- originating rationale/evidence references, such as Assessment, Investigation, Impact, Change Intent, Execution Gate context, or operator decision;
- authorizing actor/source/rule and authority context;
- effective/activation time and recorded/knowledge time;
- enforcement/confirmation evidence when activation is external to the monitoring product;
- expiry/review context when applicable;
- release rationale/provenance;
- supersession/correction/conflict history;
- security/redaction context.

## Actions

### `propose`
Records that a protective hold/quarantine should be considered at a defined boundary without asserting that propagation has actually been blocked.

### `activate`
Establishes that the safeguard is active for the defined boundary/context when sufficient authority and enforcement/activation evidence exist. A violated Assessment alone does not automatically activate a safeguard unless an accepted response rule explicitly authorizes that behavior.

### `release`
Ends an active safeguard while preserving the protected interval and release evidence. Release does not itself assert that all related data is healthy or that a cause was resolved.

### `cancel`
Withdraws a proposal that never became active.

### `resolveAt`
Returns safeguard state for a subject/output/boundary at a relevant time: proposed, active, released/not active, conflicting, unauthorized, unavailable, or unknown with allowed provenance.

## Invariants / behavioral expectations

- Propagation Safeguard is a protective control state, not a quality Assessment.
- A safeguard may be precautionary; active quarantine does not prove the data is defective.
- A violated Expectation or atypical Baseline result does not automatically imply quarantine.
- Proposed safeguard is not active safeguard.
- Release is not a health conclusion.
- Safeguard does not mutate Observation, Assessment, Baseline, Expectation, Change, Investigation, Impact, Causal Claim, or Execution Gate state.
- Safeguard placement is explicit and context-specific; source-level quarantine is not always the safest or least disruptive location.
- A safeguard may protect one output version, execution, environment, cohort, downstream boundary, or consumer set without silently applying everywhere.
- Missing output is not represented as a quarantined data object; downstream advancement/consumption can instead be held when appropriate.
- Safeguard activation can itself create operational delay or downstream non-delivery and therefore remains visible to runtime health reasoning.
- **Execution Gate controls whether a downstream execution starts; Propagation Safeguard controls whether output/current state propagates or is consumed.** Neither concept silently substitutes for the other.
- A gate-held downstream run does not automatically mean publication/consumption is safely protected; if an older state could still be presented or consumed, a separate safeguard may still be warranted.
- Conversely, an active safeguard does not determine whether a future downstream execution should be admitted.
- Monitoring Scope and user authorization do not automatically grant safeguard authority.
- Safeguard authority and Execution Gate control/override authority are separately resolved through Capability Authorization.
- Safeguard is not a substitute for source-system access control or policy enforcement.
- Event/effective time and recorded/knowledge time remain distinguishable.

## Ambiguity and missing evidence

A system may know that a safeguard was requested while lacking proof that the external runtime actually enforced it. That remains proposed/activation-unknown rather than active. Conflicting control sources remain explicit. Restricted safeguard details may be abstracted while still allowing an authorized audience to know that delivery/consumption is intentionally held.

Execution Gate state may also be unavailable or unknown. The product must not infer that a safeguard exists merely because a gate held a run, or infer that propagation is safe because the gate admitted one.

## Synchronizations

- **Entity Identity** supplies protected subject/boundary referents.
- **Assessment** may motivate a reactive safeguard but does not activate it automatically.
- **Investigation** may organize evidence and human review associated with proposing, maintaining, or releasing a safeguard.
- **Lineage** and **Impact** can help identify candidate placement/protection scope and likely downstream exposure without making the placement decision automatically.
- **Change Intent** and a prospective Impact profile may motivate a proactive safeguard proposal for high-risk planned transitions.
- **Execution Gate** may prevent a downstream execution from starting before prerequisites are ready; safeguard logic remains independently applicable to output/publication/consumption boundaries.
- **Execution History** and **Observation** can establish whether held/released state changed runtime timing or delivery behavior.
- **Responsibility Assignment** may help route an authorization/review decision without granting universal authority.
- **Policy Context** may identify relevant handling obligations but does not itself prove that a safeguard should activate.
- **Capability Authorization** separately resolves safeguard proposal/activation/release authority and Execution Gate control/override authority.
- **Explanation** can communicate that data is intentionally held, why, how that differs from an execution gate, and what remains uncertain subject to authorization.

## Security / privacy / governance considerations

Safeguard state can reveal sensitive incidents, client dependencies, protected data flows, or security controls. Visibility and activation authority must therefore be separately governed. Automatic activation, if ever supported, requires an explicit accepted response/authority rule.

A user may be permitted to know that a publication boundary is protected while being denied the restricted prerequisite identities or gate-control details that led to related operational decisions.

## Evidence / provenance considerations

Proposal, activation, enforcement evidence, scope, authority, expiry, release, and correction history remain provenance-bearing. Historical replay distinguishes when protection was effective from when the monitoring ecosystem learned or corrected that state. Where a related Execution Gate existed, its hold/admission/override history remains separately referenced rather than collapsed into safeguard history.

## Representative scenarios

### Reactive quarantine
C violates a completeness Expectation and downstream client reports are exposed. An authorized responder activates a safeguard at C's publication boundary while Investigation proceeds.

### Missing output
C produces no qualifying output for the cycle and absence evidence is sufficient. A downstream delivery boundary is held so the prior cycle is not silently presented as current.

### Proactive change safeguard
A Change Intent on A has a broad prospective blast radius into critical consumers. A safeguard is proposed for the first production activation window; it becomes active only under explicit authority/enforcement semantics.

### Boundary-specific hold
A suspect C output is safe for an internal exploratory consumer but not for a regulated client delivery. The safeguard targets the client publication boundary rather than globally blocking all access.

### Execution Gate plus safeguard
C is held by an Execution Gate until A's current output is ready. During the wait, the client publication boundary is separately safeguarded so the prior-cycle C output is not misrepresented as current. Gate admission later permits C to run; safeguard release remains a separate decision/evidence state.

### Gate without safeguard
A gate successfully prevents C from starting with stale A. No suspect C output exists and no consumer boundary needs a separate hold, so no Propagation Safeguard is required merely because gating occurred.

### False alarm / release
A corrected Observation removes the original concern. The safeguard is explicitly released; the earlier protected interval remains historical evidence.

### Safeguard causes delay
Quarantine correctly blocks suspect output but causes a delivery-latency Expectation to be violated. Both truths remain visible; protection does not hide operational consequence.

## Non-goals

- deciding data health;
- root-cause determination;
- performing Investigation;
- deciding whether a downstream execution should start;
- replacing Execution Gate;
- defining organization-wide incident response policy;
- granting user/data access;
- selecting a quarantine storage pattern, table design, workflow engine, scheduler, or enforcement product;
- automatically rolling back code;
- deleting suspect data.

## Deferred questions

- which safeguard kinds and lifecycle states are required for MVP;
- which actors/sources may propose, activate, or release safeguards;
- whether any conditions support pre-authorized automatic activation;
- how enforcement evidence is obtained from representative Databricks/consumer patterns;
- how to choose the least disruptive effective placement across complex Lineage;
- when a gate hold should be paired with a publication/consumption safeguard to prevent stale prior-state delivery;
- whether safeguard expiry/review deadlines need their own normative Expectations;
- how client-delivery obligations interact with a protective hold.

## Later refinement — Phase 007 Group 07

Phase 007 Group 07 accepts [`OPS-086–OPS-104`](../../phase_007/07_propagation_safeguard_scope_enforcement_recovery/README.md) as the operational refinement of Propagation Safeguard.

The refinement establishes:

- exact suspect/protected state, missing-output/current-cycle context, protection surface, path/cohort/environment scope and effective interval;
- proposal/authorization/request/enforcement/extension/expiry/release facts as separate provenance-bearing propositions rather than one scalar lifecycle;
- `active` only when REF-027 evidence establishes effective protection for the bounded scope/time;
- partial enforcement across consumers, paths, regions and cohorts without global success/failure collapse;
- explicit alternate-path/bypass coverage before broad protection/prevention claims;
- `prevented exposure` as a derived REF-028 + Group 06 determination rather than a Propagation Safeguard lifecycle state;
- active/no-opportunity cases that do not receive prevention credit merely from coincident non-exposure;
- safe-prior-state serving, staleness, held advancement and non-delivery as separate Impact/health facts;
- missing-output protection through downstream advancement/current-state presentation rather than quarantine of a nonexistent object;
- extension, scheduled/effective expiry and release as independently authorized/evidenced, non-rewriting actions;
- post-release recovery as source-owned Observation/Assessment/Impact truth rather than Safeguard state;
- REF-029 discipline for conflicting/unavailable control telemetry and configured versus actual fallback;
- overlapping safeguards with independent materiality/release history;
- broader safeguard-induced delay/business-effect attribution through Causal Claim while REF-028 retains the narrowly scoped prevention determination;
- bitemporal historical enforcement/prevention/release reconstruction.

Accordingly, the earlier convenience lifecycle labels remain valid only as summaries of the accepted evidence-backed action facts. `Released` never means `recovered`, and `not exposed` never means `prevented by this safeguard` unless the applicable REF-028/OPS-093 burden is satisfied.
