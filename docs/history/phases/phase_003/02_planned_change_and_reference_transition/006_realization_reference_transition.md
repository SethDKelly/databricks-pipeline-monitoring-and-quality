# SYN-006 — Realization Evidence → Reference Transition

**Status:** Accepted — Phase 003 Group 02

## Outcome

Move Expectation applicability and Baseline comparability into the realized operating context at the evidence-supported transition boundary, while preserving that activation/context transition is not proof of intended effect, health, or causation.

## Participating concepts and actions

- **Change Intent** — `resolvePlannedAt` for prospective context where available.
- **Deployment** — `resolveActiveAt`, `recordActivation`, `supersede`.
- **Change** — `resolveWindow`, `recordOccurred`, `derive` as evidence of realized structural/state transition.
- **Expectation** — `resolveApplicable` over the resulting context/time; prospective versions may already have been `establish`ed/`revise`d under SYN-004.
- **Baseline** — `markNonComparable`, `resolveComparable`.

## Trigger / initiating condition

Evidence indicates that a target may have crossed from one operating/reference context into another: e.g., a structural configuration becomes active, a realized schema/topology/population logic change is established, or rollback/reversion changes the active context again.

## Preconditions

- the relevant subject/target/dimension/context is identified;
- sufficient realization evidence exists for the **reference context being transitioned**, not merely a successful workflow timestamp;
- any prospective Expectation/Baseline links are resolvable when they exist.

## Coordination semantics

1. Resolve the active Deployment/configuration and/or realized Change evidence relevant to the subject/dimension/context.
2. Establish a reference transition boundary only when evidence is sufficient to show that the changed operating context became effective.
   - Trustworthy Deployment activation evidence may be sufficient where it establishes that the structural/configuration state itself became active.
   - Realized Change evidence may establish the structural boundary when Deployment evidence is absent or insufficient.
   - Both may contribute where available.
3. If a prospective Baseline break was registered for that context, `Baseline.markNonComparable` makes the old Baseline non-comparable **for the post-boundary changed context**. The Baseline remains historical evidence for its prior context.
4. If an explicitly established prospective Expectation was defined to apply when that changed context becomes active, `Expectation.resolveApplicable` may now select it from the transition boundary forward. Pre-boundary evidence continues to resolve the prior applicable Expectation.
5. If no prospective Expectation exists, do not create one from Change Intent or observed effect. Normative context may remain missing/conflicting.
6. A realized structural Change with no Change Intent can still make an old Baseline non-comparable. Planned context remains absent.
7. Actual effect magnitude does not determine whether the reference transition occurred. A filter logic state can become active even if downstream volume unexpectedly fails to move; effect/conformance is later evidence/reasoning.
8. Rollback/reversion creates another context boundary. Earlier Baseline/Expectation versions may become candidates again only if `resolveComparable`/`resolveApplicable` and their own context/time semantics justify reuse; rollback does not automatically restore them.
9. In canary/phased/partial rollout, boundaries resolve per affected target/cohort/context. One target's transition cannot globally switch unrelated reference context.

## State and evidence effects

Deployment and Change own realization evidence/history. Baseline owns comparability limitations. Expectation owns normative applicability. Change Intent remains planned context. The synchronization owns no standalone “reference version” or “transition state” concept.

## Ambiguity / failure propagation

- Deployment attempt only → no realization boundary;
- activation ambiguous/conflicting → intent-linked prospective break remains pending unless independent realized Change evidence establishes the context transition;
- realized Change established but planned context absent → transition descriptive reference context only; no intent/Expectation is fabricated;
- prospective Expectation conflict → preserve conflict after boundary rather than select by synchronization order;
- post-change effect differs from intent → transition can still be real; conformance/health remains separate;
- restricted activation/change details may support an opaque transition result without disclosing sensitive configuration.

## Temporal semantics

The reference boundary uses the best-supported event/effective time of the changed operating context. Recorded/knowledge time remains distinct. If evidence discovered later shows activation occurred earlier, retrospective comparability/applicability can be corrected from the true event boundary while preserving the references/Assessments that were actually used at earlier knowledge time.

## Provenance / traceability

The product must trace which Deployment activation and/or realized Change evidence justified the transition, which prospective Baseline break/Expectation version was linked, and any later correction/rollback boundary.

## Security / authorization

Reference transition can reveal sensitive configuration/business rules. A caller may receive “reference context changed” or an updated Assessment basis without receiving the protected implementation detail that justified it.

## Invariants

- workflow success ≠ realization boundary;
- realization boundary ≠ intended effect realized;
- transition ≠ health/cause;
- Baseline non-comparability is context/time scoped, not deletion;
- old Expectation remains historically resolvable before boundary;
- unregistered Change may transition Baseline context but cannot manufacture planned/normative context;
- rollback ≠ automatic reference restoration;
- one target/context transition does not globally propagate.

## Scenarios

**Filter activates:** R2 containing the filter is proven active in production; old volume Baseline becomes non-comparable after the boundary and prepared post-change Expectation becomes applicable.

**Deployment active, effect absent:** structural configuration is active but C volume has not moved. Reference context can still transition; later Assessment/Investigation determines whether the intended effect occurred.

**Unregistered source break:** source semantics/population changes with no intent/deployment; realized Change can mark the old Baseline non-comparable, but no revised Expectation is invented.

**Rollback:** R2 is superseded by restored R1-like context. Earlier references are reconsidered for comparability/applicability rather than silently reinstated.

**Late activation correction:** later evidence moves activation from 10:05 to 09:55; retrospective reference interpretation uses the corrected boundary while preserving the prior knowledge state.

## Non-goals

Assessment, causal inference, intent conformance verdict, Baseline derivation, deployment implementation, automatic normative-rule creation.

## Deferred questions

Evidence threshold by structural-change type, partial-rollout context representation, and policy for reusing prior Baselines after restoration.
