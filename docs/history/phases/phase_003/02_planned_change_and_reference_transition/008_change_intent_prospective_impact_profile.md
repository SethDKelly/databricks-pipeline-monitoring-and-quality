# SYN-008 — Change Intent + Lineage → Prospective Impact Profile

**Status:** Accepted — Phase 003 Group 02 addendum discovered during Group 03 review; refined by Phase 007 Group 03

## Outcome

Allow planned changes to be reviewed for downstream blast radius before realization by identifying plausible downstream candidates and risk-relevant context without claiming actual exposure, downstream effect, or business consequence.

## Participating concepts and actions

- **Change Intent** — `resolvePlannedAt`.
- **Lineage** — `traverseAt` for currently applicable topology.
- **Impact** — `identifyCandidates` using the planned change as originating condition.
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, and **Policy Context** — optional context enrichment where authorized.

## Trigger / initiating condition

A Change Intent is registered/revised or an actor requests pre-deployment blast-radius review.

## Preconditions

The intended-change target resolves to Entity Identity. Planned topology additions/removals remain Change Intent state until realization and are never passed off as active Lineage.

## Coordination semantics

1. Resolve the relevant Change Intent and target/context.
2. Traverse authorized current Lineage downstream from affected targets at the relevant known topology time.
3. Treat any topology proposed only by Change Intent as a distinct planned path; do not merge it with active Lineage.
4. Use Impact candidate semantics to record plausible downstream reachability.
5. Enrich candidates with authorized criticality/business meaning/responsibility/classification/policy context where available.
6. Return a prospective profile that distinguishes active-topology candidates, planned-only candidates, path completeness, restricted/opaque dependencies, and evidence gaps.
7. The profile may inform change review, analyst attention, testing focus, or Propagation Safeguard proposal, but it does not create actual exposure/effect/consequence state.

## State and evidence effects

Change Intent owns the plan; Lineage owns active relationship state; Impact owns candidate/reachability state. The synchronization owns no independent risk truth and does not manufacture a probability or severity score.

## Phase 007 Group 03 refinement

OPS-021–OPS-033 refine this synchronization without changing its truth ownership:

- the profile binds the exact Change Intent revision/component, rollout slice, review evaluation time and knowledge cut;
- `current Lineage` is interpreted through OPS-001–OPS-009 effective/historical topology and question-bound relevance, not generic graph reachability;
- explicit planned additions, removals and relationship/scope modifications form a **derived prospective scenario topology** while remaining Change Intent state;
- a planned removal creates a path-loss/change candidate rather than making the currently effective consumer disappear before realization;
- candidate basis distinguishes effective-path, planned-added-path, path-loss/change and indeterminate cases;
- field/key/population/interface/consumer/version scope can narrow asset-level candidates;
- proposal-bound compatibility consumes HLTH-009–HLTH-018 and remains distinct from realized compatibility;
- metric/profile/Expectation/Baseline/reconciliation/readiness/control assumptions receive scoped review rather than global invalidation or active-control state;
- analytical review relevance ≠ governed review obligation ≠ approval ≠ control/enforcement;
- criticality can prioritize review but is not probability, evidence strength or actual Impact;
- incomplete/conflicting/restricted topology preserves non-exhaustive/indeterminate results;
- mixed rollout remains slice-specific and historical prospective review remains non-rewriting.

These refinements supersede any interpretation of `traverse current Lineage` as sufficient by itself for an exhaustive or semantically relevant blast radius.

## Ambiguity / failure propagation

Incomplete Lineage yields an incomplete profile, not `no blast radius`. Restricted consumers may remain opaque. Conflicting identity/topology remains conflict. A missing criticality/classification value does not become low risk.

A missing or insufficient Change Intent/planned-state description limits the prospective basis; it does not prove no possible change risk.

## Temporal semantics

The profile records when it was produced and which Lineage/Change Intent versions were known then. Later topology discovery can revise the retrospective profile without rewriting what was available during change review.

For partial rollout, observed evidence from already-active slices may inform review of remaining slices but does not become realized fact for those future slices.

## Provenance / traceability

Every candidate remains traceable to a Lineage path or explicitly planned Change Intent relationship plus any contextual metadata used for prioritization. Phase 007 additionally retains whether the basis is an effective path, planned-added path, path-loss/change condition or indeterminate/restricted path.

## Security / authorization

Prospective blast-radius review can reveal sensitive consumers or future architecture. The profile may disclose aggregate/opaque downstream risk without revealing restricted identities or planned logic.

## Invariants

- prospective Impact ≠ actual Impact;
- reachable candidate ≠ exposed consumer;
- criticality ≠ probability of harm;
- planned topology ≠ active Lineage;
- planned removal ≠ relationship already absent;
- review relevance ≠ obligation/approval/control;
- proposed compatibility ≠ realized compatibility;
- missing topology ≠ no dependency;
- no numeric/universal qualitative risk score is invented without an accepted evidence model;
- pre-change analysis does not establish causality.

## Scenarios

**A→C blast radius:** a planned change to A traverses current Lineage to C and client-facing consumers, producing a prospective candidate set before deployment.

**Planned new edge:** Change Intent says A will also feed D. D is shown as planned-only prospective path until realization evidence creates active Lineage.

**Planned relationship removal:** Change Intent says A will no longer feed C. C remains a path-loss/change candidate because its current dependency is the relationship being proposed for removal.

**Restricted client:** the viewer sees that one critical restricted consumer is in the prospective blast radius without its name.

**Incomplete Lineage:** the profile explicitly states that downstream coverage is incomplete rather than implying the enumerated set is exhaustive.

**Partial rollout:** a canary slice is active while another remains prospective; observed canary evidence may inform review but is not projected as fact onto the unactivated slice.

## Non-goals

Actual exposure confirmation, causal attribution, quantitative/universal qualitative risk scoring, deployment approval workflow, active CI/control gating, or graph implementation.

## Deferred questions

Concrete source support/coverage belongs to Phase 009. Technical graph/static-analysis/UI architecture belongs to Phase 010. Any later qualitative/quantitative risk model requires explicit proposition/evidence/governance design rather than being assumed here.
