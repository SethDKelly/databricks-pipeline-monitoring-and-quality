# SYN-008 — Change Intent + Lineage → Prospective Impact Profile

**Status:** Accepted — Phase 003 Group 02 addendum discovered during Group 03 review

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

## Ambiguity / failure propagation

Incomplete Lineage yields an incomplete profile, not `no blast radius`. Restricted consumers may remain opaque. Conflicting identity/topology remains conflict. A missing criticality/classification value does not become low risk.

## Temporal semantics

The profile records when it was produced and which Lineage/Change Intent versions were known then. Later topology discovery can revise the retrospective profile without rewriting what was available during change review.

## Provenance / traceability

Every candidate remains traceable to a Lineage path or explicitly planned Change Intent relationship plus any contextual metadata used for prioritization.

## Security / authorization

Prospective blast-radius review can reveal sensitive consumers or future architecture. The profile may disclose aggregate/opaque downstream risk without revealing restricted identities or planned logic.

## Invariants

- prospective Impact ≠ actual Impact;
- reachable candidate ≠ exposed consumer;
- criticality ≠ probability of harm;
- planned topology ≠ active Lineage;
- missing topology ≠ no dependency;
- no numeric risk score is invented without an accepted evidence model;
- pre-change analysis does not establish causality.

## Scenarios

**A→C blast radius:** a planned change to A traverses current Lineage to C and client-facing consumers, producing a prospective candidate set before deployment.

**Planned new edge:** Change Intent says A will also feed D. D is shown as planned-only prospective path until realization evidence creates active Lineage.

**Restricted client:** the viewer sees that one critical restricted consumer is in the prospective blast radius without its name.

**Incomplete Lineage:** the profile explicitly states that downstream coverage is incomplete rather than implying the enumerated set is exhaustive.

## Non-goals

Actual exposure confirmation, causal attribution, quantitative risk scoring, deployment approval workflow, or graph implementation.

## Deferred questions

Whether later phases require qualitative risk tiers, probability/severity models, test-plan generation, or mandatory pre-deployment review rules for high-criticality paths.
