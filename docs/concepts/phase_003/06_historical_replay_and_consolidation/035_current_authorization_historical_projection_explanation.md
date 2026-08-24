# SYN-035 — Historical State + Current Authorization → Safe Replay Explanation

**Status:** Accepted — Phase 003 Group 06

## Outcome

Answer historical questions using a clearly labeled contemporaneous, retrospective, or comparative perspective while preserving current requester authorization, historical actor authorization/control state, statement-to-basis traceability, and the difference between actual retained Explanation and a newly generated replay reconstruction.

## Participating concepts and actions

- **Capability Authorization** — `resolveFor`, `explainBasis` where permitted;
- **Explanation** — compose/resolve historical communication state under accepted semantics;
- **SYN-033 historical state reconstruction**;
- **SYN-034 retrospective re-evaluation** where later evidence matters;
- any concept state included in the requested authorized analytical projection.

Historical Capability Authorization, gate/safeguard state, and retained Explanation are evidence inputs; they do not grant current access.

## Trigger / initiating condition

A current requester asks a historical question such as:

- what did we know at incident time?
- what did the responder believe or explain then?
- what do we know now about the same incident?
- why did a gate or safeguard act as it did?
- what changed between the contemporaneous and retrospective conclusion?

## Preconditions

- requested historical perspective/time coordinates are explicit enough to reconstruct;
- current requester identity/capability context is resolvable;
- historical concept state is available at least partially;
- restricted evidence can remain opaque without being treated as absent.

## Coordination semantics

1. Determine the requested perspective:
   - **contemporaneous** — historical event/window under a historical knowledge cutoff;
   - **retrospective** — historical event/window under a later/current knowledge cutoff;
   - **comparison** — contrast two or more knowledge cuts for the same event/window.
2. Use SYN-033 and, where needed, SYN-034 to reconstruct the relevant internal historical state before disclosure.
3. Resolve the **current requester's** applicable Capability Authorization for the requested subject/evidence facets. Historical actor authorization may be reconstructed separately as a historical fact.
4. Produce an Authorized Analytical Projection containing only currently permitted details/abstractions. Restricted historical evidence can contribute internally only according to accepted enforcement/integration semantics; it is never exposed or summarized beyond the current authorized projection.
5. Preserve explicit limitations such as `restricted upstream identity`, `exact threshold hidden`, `historical evidence incomplete`, or `current requester cannot inspect the original basis` where disclosure of that limitation itself is allowed.
6. Distinguish **actual retained Explanation** from **reconstructed Explanation**:
   - if an Explanation was actually generated/retained at the historical knowledge time, it may be returned as `actual historical explanation` subject to current authorization;
   - if no such snapshot exists, the system may compose `reconstructed as-known-then explanation` from the historical state cut, but must never claim that wording or conclusion was actually shown to anyone then.
7. A retrospective Explanation may state how understanding changed: e.g. `At 08:15 exposure was unknown; current evidence establishes exposure.` Both sides remain traceable to their knowledge cuts.
8. Historical authorization/control may be described when currently authorized, e.g. `the incident responder had raw-data access and gate override authority then`; this does not grant those capabilities to the current requester.
9. Current disclosure/redaction rules apply even when a historical actor had broader access.

## State and evidence effects

The synchronization does not mutate historical concept state. If a new replay Explanation is retained, Explanation records it at the current generation time with explicit perspective/knowledge-cut basis and `reconstructed` status where applicable.

## Ambiguity / failure propagation

If current authorization cannot be resolved, do not widen disclosure. If historical Explanation snapshots are missing, say that the view is reconstructed. If historical authorization is unavailable, do not infer that a past actor was or was not permitted.

Redaction may reduce causal/Impact detail without changing the underlying epistemic status. Hidden evidence is not described as nonexistent.

## Temporal semantics

The replay explanation carries at least:

- historical event/window;
- selected knowledge cutoff(s);
- current generation/request time where retained;
- whether each represented statement is actual historical state, retrospective state, or replay-derived reconstruction.

Current requester authorization is resolved according to the current applicable disclosure context unless the user is asking about historical authorization as a fact.

## Provenance / traceability

Every material statement remains traceable to the historical state cut, current authorization projection, epistemic/control status, and any retrospective re-evaluation. Comparison explanations retain the basis for both old and new conclusions.

## Security / authorization

This synchronization is a strict disclosure boundary:

- historical access never becomes current access;
- past privileged evidence is not leaked through paraphrase;
- aggregate/opaque historical statements are used only when independently authorized;
- current requester permission is not inferred from Responsibility Assignment, past incident role, repository ownership, or gate/safeguard authority.

## Invariants

- historical actor authorization ≠ current requester authorization;
- internal replay state ≠ authorized disclosure;
- actual retained historical Explanation ≠ reconstructed as-known-then Explanation;
- retrospective Explanation ≠ contemporaneous Explanation;
- redacted evidence ≠ absent evidence;
- current prose cannot promote Causal Claim/Impact/control state;
- historical replay cannot bypass least privilege.

## Scenarios

### E-20 historical authorization
A responder had raw-data access during the incident. A current analyst lacks it. The analyst can receive an authorized statement that broader evidence existed and influenced the historical investigation, but not the protected values unless currently authorized.

### Restricted RCA comparison
At incident time a restricted upstream contributor was only `candidate`. Later evidence supports a causal claim. A current analyst may see the status transition while the upstream identity/evidence remains opaque if those abstractions are separately authorized.

### Missing historical Explanation snapshot
No answer/report was retained during the incident. The current system generates an `as-known-at-08:15 reconstruction`; it is explicitly not presented as an answer that responders actually saw.

## Non-goals

- selecting UI/report/LLM implementation;
- granting historical impersonation privileges;
- exposing hidden evidence to improve narrative completeness;
- defining legal record-retention requirements;
- claiming reconstructed prose was actually communicated historically.

## Deferred questions

- audience-facing vocabulary for `actual historical`, `reconstructed`, and `retrospective` views;
- which Explanation snapshots must be retained for MVP/audit;
- visible citation/redaction UX;
- deterministic versus generative replay composition rules for high-consequence statements.
