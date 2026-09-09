# SYN-007 — Post-Transition Observation → Baseline Establishment

**Status:** Accepted — Phase 003 Group 02

## Outcome

Establish a new empirical descriptive reference after a realized operating-context transition using sufficient comparable post-transition Observations, while allowing immediate normative Assessment to proceed independently through any applicable Expectation.

## Participating concepts and actions

- **Observation** — `retrieve` (source evidence was previously `record`ed/corrected by the concept).
- **Baseline** — `derive`, `refresh`, `resolveComparable`.
- **Change** and/or **Deployment** — provide the established transition/context boundary from SYN-006.
- **Expectation** — `resolveApplicable` remains an independent immediate normative reference; it does not supply Baseline values.

## Trigger / initiating condition

A reference transition has become effective and enough post-transition evidence may now exist to characterize the new descriptive operating behavior.

## Preconditions

- the relevant transition/context boundary is sufficiently established;
- post-transition Observations can be identified for the same subject/dimension/context;
- evidence sufficiency/comparability is adequate for the proposed Baseline derivation.

## Coordination semantics

1. Use the realized transition boundary/context to identify candidate post-transition Observations.
2. Exclude pre-transition evidence from the new reference population unless a later explicit comparability rule establishes it belongs to the same operating context; this synchronization does not assume such equivalence.
3. Evaluate evidence coverage, representativeness, context consistency, and other functional sufficiency limitations.
4. If sufficient, call `Baseline.derive`/`refresh` to create a new version with the supporting Observation population and comparison context.
5. If insufficient, return `insufficient evidence`/no comparable new Baseline. Do not fill the gap with Change Intent's anticipated values or with the prospective Expectation.
6. While the Baseline is unavailable, current Observations may still be assessed normatively against an applicable Expectation in Group 03.
7. Do not silently adapt the old Baseline by mixing changed-context observations into its historical population.
8. If later corrections invalidate part of the evidence population, derive/refresh a corrected Baseline version while preserving the earlier Baseline and the knowledge state that produced it.
9. After rollback/restoration, an older Baseline may be reused only when `resolveComparable` establishes that its context is again suitable; otherwise derive a refreshed reference from the restored-context evidence.

## State and evidence effects

Observation owns evidence facts/corrections. Baseline owns the new empirical reference version, supporting population/window, limitations, and provenance. Expectation remains an independent normative reference. Synchronization owns no statistical model or “learning state.”

## Ambiguity / failure propagation

- too few post-transition Observations → insufficient Baseline evidence, not a guessed range;
- mixed rollout contexts → separate/ambiguous populations rather than one blended Baseline;
- conflicting measurements → preserve conflict unless correction/authority resolves them;
- restricted observations may support an authorized abstract Baseline/comparison result without exposing raw values;
- uncertain transition boundary may prevent clean evidence partitioning and therefore keep the new Baseline unavailable.

## Temporal semantics

Baseline derivation time is distinct from the event times of its supporting Observations and from the earlier transition boundary. A Baseline becomes known only when it is actually derived; later derivation does not imply the product had that reference for the first post-change runs.

## Provenance / traceability

The new Baseline must identify the transition/context it follows, the Observation population/window used, derivation meaning, sufficiency limitations, and any correction/refresh relationship to later versions.

## Security / authorization

Post-change Baseline evidence may reveal sensitive volumes/business cycles. Use minimized/authorized observations and permit safe comparative abstraction where detailed values are restricted.

## Invariants

- intended/planned value ≠ Baseline evidence;
- Expectation threshold ≠ Baseline value;
- new Baseline requires empirical comparable evidence;
- insufficient history remains insufficient;
- old Baseline is not silently trained/adapted across a structural break;
- first post-change run need not wait for a Baseline if an applicable Expectation exists;
- late correction creates traceable new reference history.

## Scenarios

**New normal learned:** after several comparable post-filter runs, a new C-volume Baseline is derived from those observations.

**Immediate validation:** first post-change run is evaluated against a prepared Expectation while Baseline remains insufficient.

**Mixed canary:** half the population remains old logic; evidence is not blended into one new Baseline unless comparability/context rules justify it.

**Corrected measurement:** one early row-count Observation is later corrected; Baseline is refreshed with provenance rather than silently mutated.

**Rollback:** restored context may use an older comparable Baseline or derive a refreshed one depending on evidence/context, not merely the rollback label.

## Non-goals

Statistical algorithm selection, automatic Expectation generation, health Assessment semantics, causal reasoning, persistence/model-serving design.

## Deferred questions

First-MVP evidence sufficiency criteria, seasonality/context classes, and stability/adaptation policy.
