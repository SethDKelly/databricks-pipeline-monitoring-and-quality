# SYN-016 — Investigation Trigger → Bounded Inquiry

**Status:** Accepted — Phase 003 Group 04

## Outcome

Turn a material Assessment, realized Change, Change-Intent realization concern, safeguard condition, or user question into a bounded Investigation without converting the initiating symptom into a causal conclusion.

## Participating concepts and actions

- **Investigation** — `open`, `refineScope`.
- **Entity Identity** — supplies identified subject referents.
- **Assessment**, **Change**, **Change Intent**, **Propagation Safeguard**, and **Impact** — optional initiating context.
- **Responsibility Assignment** — optional routing/participation context.

## Trigger / initiating condition

An authorized actor requests inquiry, or an explicitly accepted response rule initiates one under SYN-014.

## Preconditions

The initiating question/symptom and relevant subject/time context are sufficiently identifiable. Automatic initiation still requires an explicit accepted response rule; Group 04 does not invent alert severity policy.

## Coordination semantics

1. Record the question or outcome to be explained, not a presumed cause.
2. Resolve the primary subject(s) to Entity Identity.
3. Establish an initial effective/event-time window appropriate to the symptom and preserve the Investigation open/knowledge time separately.
4. Link the initiating Assessment/Change/other evidence by provenance reference.
5. Record material evidence gaps, authorization limits, and known Monitoring Scope boundaries at opening time.
6. Refine subject/time boundaries later when evidence justifies expansion or narrowing; preserve prior scope history.
7. A safeguard may be part of the inquiry context, but its existence does not imply that protected data was defective.

## State and evidence effects

Investigation owns inquiry scope/lifecycle only. Initiating facts remain owned by their source concepts.

## Ambiguity / failure propagation

A question can be investigated even when the initiating Assessment is comparative-only, unresolved, or evidence-limited. Uncertain event time yields a bounded but explicitly uncertain initial window rather than guessed precision.

## Temporal semantics

The symptom's effective/event time, Investigation opening time, later scope revisions, and late-arriving evidence retain distinct knowledge-time history.

## Provenance / traceability

The Investigation retains the initiating actor/rule and exact source evidence that motivated inquiry.

## Security / authorization

Opening an Investigation never broadens evidence access. Restricted initiating evidence can remain opaque while preserving that it materially motivated inquiry.

## Invariants

- symptom ≠ cause;
- Assessment ≠ Investigation;
- safeguard ≠ proof of defect;
- investigation scope ≠ Monitoring Scope;
- Investigation opening time ≠ incident event time;
- automatic initiation requires an accepted response rule.

## Scenarios

A materially atypical client-critical C output is manually investigated despite no normative volume Expectation. A completeness violation opens an Investigation under an accepted response rule. An analyst asks why a successful pipeline missed a delivery deadline and opens an operational-timing Investigation.

## Non-goals

Ticketing, paging, notification routing, incident-severity policy, causal hypothesis generation, or remediation orchestration.
