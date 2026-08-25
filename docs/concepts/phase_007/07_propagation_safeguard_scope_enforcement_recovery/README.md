# Phase 007 Group 07 — Propagation Safeguard Scope, Enforcement, Release & Recovery

**Status:** Review complete — accepted

## Goal

Refine how Propagation Safeguard protects exact suspect states and consumer paths, how enforcement/prevented-exposure claims are evidenced, and how extension, expiry, release and post-protection recovery interact with downstream freshness, delivery and Impact without merging control state with health or causality.

## Group result

Group 07 accepts **OPS-086–OPS-104**. No new concept is required. **Propagation Safeguard** remains the protection-control truth owner. Impact retains encounter/exposure/effect/consequence truth; Capability Authorization retains permission truth; Causal Claim retains broader control-effect attribution.

The accepted protection chain is:

**bound protected state/surface → proposal/authorization context → activation request/issuance → evidence-established enforcement → path/opportunity-specific protection → REF-028 prevented-exposure determination → extension/expiry/release → independently evidenced post-protection state/recovery**.

No link automatically manufactures the next.

## Accepted OPS contracts

1. [`OPS-086 — Safeguard Proposition: Protected State, Surface & Scope`](086_safeguard_proposition_protected_state_surface_scope.md)
2. [`OPS-087 — Safeguard Lifecycle & Action-Fact Decomposition`](087_safeguard_lifecycle_action_fact_decomposition.md)
3. [`OPS-088 — Protection Surface Placement & Semantic Boundary`](088_protection_surface_placement_and_semantic_boundary.md)
4. [`OPS-089 — Safeguard Applicability, Effective Scope & Interval`](089_safeguard_applicability_effective_scope_interval.md)
5. [`OPS-090 — Activation, Enforcement & Material Path Control`](090_activation_enforcement_material_path_control.md)
6. [`OPS-091 — Partial Enforcement Across Consumers, Cohorts & Paths`](091_partial_enforcement_consumer_cohort_path_matrix.md)
7. [`OPS-092 — Alternate Paths, Bypass & Protection Coverage`](092_alternate_paths_bypass_and_protection_coverage.md)
8. [`OPS-093 — Prevented Exposure Determination Using Group 06 + REF-028`](093_prevented_exposure_determination_group06_ref028.md)
9. [`OPS-094 — No-Opportunity / Incidental Safeguard Non-Prevention`](094_no_opportunity_incidental_safeguard_nonprevention.md)
10. [`OPS-095 — Safe Prior State, Stale Serving, Hold & Non-Delivery During Protection`](095_safe_prior_state_stale_serving_hold_non_delivery.md)
11. [`OPS-096 — Missing Output & Current-Cycle Advancement Protection`](096_missing_output_current_cycle_advancement_protection.md)
12. [`OPS-097 — Extension, Renewal, Scope Revision & Supersession`](097_extension_renewal_scope_revision_and_supersession.md)
13. [`OPS-098 — Expiry, Scheduled End & Effective End of Protection`](098_expiry_scheduled_end_and_effective_end.md)
14. [`OPS-099 — Release Request, Effective Release & Path Reopening`](099_release_request_effective_release_and_path_reopening.md)
15. [`OPS-100 — Post-Release Recovery State & Independent Observation`](100_post_release_recovery_state_and_observation.md)
16. [`OPS-101 — Safeguard Telemetry Conflict, Unavailability & Fallback Discipline`](101_control_telemetry_conflict_unavailable_fallback_discipline.md)
17. [`OPS-102 — Overlapping Safeguards, Composition & Attribution`](102_overlapping_safeguards_composition_and_attribution.md)
18. [`OPS-103 — Safeguard-Induced Effects, Impact & Causal Handoff`](103_safeguard_induced_effects_impact_causal_handoff.md)
19. [`OPS-104 — Historical Safeguard Replay, Ownership & Group 08 Handoff`](104_historical_safeguard_replay_ownership_group08_handoff.md)

## Exact protection proposition

Every safeguard is bound to the suspect/protected state or missing-output/current-cycle context, exact propagation surface, consumer/path/cohort/environment scope and effective interval. A safeguard can protect one version or consumer path without making an entire asset globally `quarantined`.

Protection surfaces remain functional and implementation-neutral: output/version publication, current-state presentation, consumer/interface paths, downstream advancement/refresh opportunities, or bounded cohorts can be protected where supported. Group 07 chooses no table/view/ACL/routing/quarantine implementation.

## Lifecycle and enforcement

Group 07 deliberately separates:

**proposal → authorization/approval → activation request/issuance → control acceptance → effective enforcement → resulting publication/consumption behavior**.

Likewise, extension, expiry and release have request/authorization and effective-control facts rather than one administrative lifecycle transition. `Active` means the intended protected state is actually evidenced as enforced for the relevant scope/time under REF-027; it is not merely configured/requested.

Partial enforcement is first-class across consumers, paths, regions, cohorts, versions and intervals. No universal protection percentage is accepted as a truth substitute.

## Alternate paths and bypass

Protection is path-specific. One controlled publication path does not prove another API, cache, replica, export or consumer route was controlled. Material alternate paths from Group 06 must be covered before a global prevention conclusion is justified.

An unresolved/restricted alternate path limits strong prevention. A theoretical route is not automatically a bypass; actual/sufficiently evidenced use outside intended protection is.

## Prevented exposure

`Prevented exposure` is **not** a Propagation Safeguard lifecycle state. It is a derived cross-concept determination requiring REF-028 plus Group 06 evidence:

- exact suspect state and consumer/use proposition;
- applicable encounter opportunity or materially operative opportunity;
- path through the protected surface;
- evidence-established enforcement;
- negative suspect-state encounter evidence for the controlled path;
- sufficient material alternate-path coverage.

Therefore **Safeguard active + consumer not exposed ≠ Safeguard prevented exposure** by default. If no encounter opportunity occurred, the safeguard can still be validly active without receiving causal credit for prevention.

## Safe stale state, missing output and protection consequences

A successfully protected consumer may remain on safe V-1 while freshness/current-cycle requirements fail, may receive delayed delivery, or may receive no delivery. Those are Observation/Assessment/Impact facts rather than safeguard failure or success labels.

If no qualifying current output exists, there is no nonexistent object to quarantine. A safeguard can instead hold downstream advancement/current-state presentation or another relevant boundary so an older state is not silently represented as current.

## Extension, expiry and release

Extension/renewal/scope revision is separately authorized/evidenced and preserves prior scope/interval history. Scheduled expiry is not automatically effective expiry unless applicable control semantics/evidence establish that protection ended.

Release similarly preserves:

**release rationale → authorization → release request → control acceptance → effective removal of protection → reopened paths/opportunities**.

Release can be partial and **does not prove health, freshness, causal resolution or downstream recovery**.

## Recovery after protection

Propagation Safeguard owns protection and its removal; it does **not** own `recovered` truth. After release/expiry, independently resolve the actual published/served state, consumer encounter, freshness/currentness, health/readiness, delivery and consequences through their owning concepts.

A released path may expose recovered state, safe-but-stale state, suspect state, unknown state or nothing at all.

## Telemetry, overlapping controls and causal effects

REF-029 remains binding: missing/conflicting enforcement telemetry does not prove success, failure, fail-open, fail-closed, preserved hold or automatic release. Configured fallback is not actual fallback application.

Multiple safeguards can overlap. Each keeps its own scope/enforcement/release history; first-activated or most-visible control is not automatically the material protector.

Safeguard-induced delay, stale serving, non-delivery or business effect remains separate Impact/runtime evidence. Broader statements that a safeguard caused/contributed to such an outcome require Causal Claim semantics under REF-013–REF-020. The narrowly bounded prevented-exposure determination remains governed by REF-028/OPS-093.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **SG07-01–SG07-36**, including active-without-enforcement proof, alternate-path bypass, safe stale fallback, no-opportunity protection, missing-output advancement hold, partial cohorts, degraded telemetry, expiry/extension, release-before-recovery, overlapping safeguards, control-induced delay, restricted evidence and Gate/Safeguard separation.

## Durable boundaries

- protected/suspect ≠ defective.
- proposal/configuration/authorization/request ≠ effective enforcement.
- active safeguard ≠ global path protection.
- partial enforcement ≠ global success/failure.
- one protected path ≠ no alternate path.
- `not exposed` ≠ `prevented by Safeguard`.
- no encounter opportunity ≠ prevention evidence.
- prevented exposure requires REF-028 + Group 06 path/opportunity/negative evidence.
- blocked suspect state ≠ fresh/current/healthy delivery.
- missing output ≠ quarantined object.
- scheduled expiry ≠ effective expiry by convenience.
- release request ≠ effective release.
- release ≠ recovery/health/currentness.
- Safeguard owns protection, not post-release recovered truth.
- safeguard effect ≠ causal attribution by proximity.
- control telemetry missing ≠ fail-open/fail-closed result.
- Propagation Safeguard ≠ Execution Gate.
- historical retrospective prevention ≠ what operators knew then.

## Architecture boundary

Group 07 does not select quarantine tables/views/aliases, ACLs, publication routing, storage locations, control services, consumer instrumentation, enforcement integrations, fallback implementation, event schemas/stores or technical architecture. Source capabilities belong to Phase 009 and implementation placement to Phase 010.

## Group exit gate

**Satisfied.** OPS-086–OPS-104 and SG07-01–SG07-36 establish exact protection propositions, lifecycle/enforcement decomposition, path/alternate-path control, REF-028 prevention, no-opportunity discipline, safe stale/missing-output protection, extension/expiry/release, independent recovery, degraded telemetry, overlapping safeguards and control-effect handoff without a 25th concept.

**Next: Phase 007 Group 08 — Execution Gate, Fallback/Override & Control-Induced Operational Effects.**
