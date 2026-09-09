# SYN-034 — Late/Corrected Evidence → Retrospective Re-evaluation

**Status:** Accepted — Phase 003 Group 06

## Outcome

Allow late-arriving or corrected evidence to change the **current retrospective understanding** of a past event while preserving what was actually known, assessed, believed, controlled, and explained at earlier knowledge times.

## Participating concepts and actions

Potentially all evidence-bearing and derived concepts participate. Common participants include:

- **Entity Identity**, governance-context concepts, **Capability Authorization**;
- **Observation**, **Expectation**, **Baseline**, **Assessment**;
- **Change Intent**, **Deployment**, **Execution History**, **Lineage**, **Change**;
- **Execution Gate**, **Propagation Safeguard**;
- **Investigation**, **Causal Claim**, **Impact**, **Annotation**, **Explanation**.

## Trigger / initiating condition

A material source fact/assertion is recorded late, corrected, superseded, revoked, or newly associated with an earlier event-time context such that one or more historical interpretations may now differ.

## Preconditions

- the new/corrected state belongs to an accepted concept and retains provenance/effective time/knowledge time;
- the historical subject/window is identifiable enough to determine potentially affected reasoning;
- prior derived state, when it existed, remains historically addressable rather than silently overwritten.

## Coordination semantics

1. Record the late/corrected fact in the concept that owns it. Preserve prior source state and the new knowledge time.
2. Identify historical reasoning that may be materially affected, such as:
   - reference applicability/comparability;
   - Assessment;
   - realized Change;
   - Investigation evidence set;
   - Causal Claim support/contradiction/status;
   - Impact exposure/effect/consequence;
   - safeguard/gate interpretation;
   - Explanation.
3. Reconstruct the earlier contemporaneous cut with SYN-033 when needed to preserve `what was known then`.
4. Re-evaluate affected derived reasoning using the later knowledge cut. Any newly retained Assessment/Change/claim/Impact/Explanation receives its actual new evaluation/record time and links to the historical event-time context.
5. Preserve prior conclusions as historical knowledge. A later reassessment may supersede them for the current retrospective view but does not erase them.
6. **Do not replay control actions counterfactually.** If later evidence shows a gate would now be evaluated differently, the actual historical hold/admit/override remains what happened. The system may explain that the action was based on incomplete/incorrect evidence, but it does not replace the action with what should have occurred.
7. **Do not backfill prospective knowledge.** Later realized Lineage/Impact or causal evidence cannot be inserted into an earlier Prospective Impact Profile as though it was known before deployment.
8. If new evidence materially challenges a closed Investigation or a Causal Claim, preserve the challenge and allow reopening/status evolution under accepted later rules; closure never immunizes a conclusion from evidence.
9. If the evidence change does not materially affect a conclusion, retain that fact as a traceable re-evaluation result rather than forcing a different status.

## State and evidence effects

Source concepts retain corrections/supersessions. Derived concepts retain new versions/re-evaluations according to their own actions and histories. The synchronization itself owns no `latest truth` record.

## Ambiguity / failure propagation

Late evidence can reduce, increase, or merely relocate uncertainty. New conflicts remain conflicts. If dependency evidence is still incomplete, a prior unresolved conclusion may remain unresolved even after re-evaluation.

A corrected source does not automatically invalidate every downstream conclusion; only conclusions whose basis is materially affected are candidates for reassessment.

## Temporal semantics

At least two valid views can coexist:

- **contemporaneous:** event/window `T`, knowledge cutoff `K1`;
- **retrospective:** same event/window `T`, later knowledge cutoff `K2`.

The difference between them is itself explainable evidence about how understanding evolved.

## Provenance / traceability

Every retrospective change links to the new/corrected evidence, affected prior conclusion, prior knowledge cut where relevant, new knowledge cut, and reason the re-evaluation changed or preserved the conclusion.

## Security / authorization

Re-evaluation may use evidence that the current requester cannot see directly. Disclosure still uses SYN-035 and Capability Authorization; a current Explanation cannot expose hidden corrected evidence merely because it affected the internal retrospective conclusion.

## Invariants

- correction/supersession ≠ deletion of prior knowledge;
- retrospective conclusion ≠ contemporaneous conclusion;
- later evidence ≠ evidence known then;
- control replay ≠ counterfactual control rewrite;
- later actual Impact ≠ earlier Prospective Impact;
- Investigation closure ≠ evidence immunity;
- later support ≠ automatic causal confirmation;
- current retrospective truth does not rewrite historical Explanation snapshots.

## Scenarios

### E-10 historical correction
Late consumption logs prove a downstream report consumed the affected C version. The incident-time Impact remains `exposure unknown`; the retrospective Impact becomes `exposed`. Any current Explanation can contrast the two states.

### Causal claim changes
A Deployment-correlated theory was initially supported. Later run evidence proves the outcome began before activation. The claim can be weakened/rejected retrospectively while preserving its earlier supported state and the evidence available then.

### Gate decision with late readiness evidence
C was held because A readiness was unknown. Later evidence shows A was actually ready at the decision time. The retrospective readiness interpretation changes, but the historical gate hold remains the actual action and its delay consequence remains historical fact.

## Non-goals

- automatically reopening every Investigation after any late event;
- defining statistical significance or causal confirmation standards;
- changing historical control actions;
- generating counterfactual alternate timelines;
- choosing event-sourcing/version-storage architecture.

## Deferred questions

- exact materiality rules for triggering automatic reassessment/reopen prompts;
- which retained derived states require explicit supersession links in MVP;
- notification/escalation rules when retrospective conclusions materially change;
- retention of obsolete or superseded Explanation snapshots.
