# SYN-030 — Capability Authorization + Concept State → Authorized Analytical Projection

**Status:** Accepted — Phase 003 Group 05

## Outcome

Give an analyst or other actor the maximum useful monitoring/RCA context explicitly permitted for the task even when direct data access is denied, while preventing restricted rows, values, metadata, topology, policy details, or operational-control authority from leaking through the analytical view.

## Participating concepts and actions

- **Capability Authorization** — `resolveFor`, optionally `explainBasis`.
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, **Policy Context** — authorized meaning/governance context.
- **Execution History**, **Observation**, **Assessment**, **Change** — authorized runtime/health evidence.
- **Lineage**, **Investigation**, **Causal Claim**, **Impact**, **Propagation Safeguard**, **Annotation** — authorized reasoning/context state.
- Operational capabilities such as job/run action or safeguard control may be resolved and displayed separately but are not executed by this synchronization.

## Trigger / initiating condition

A principal requests monitoring analysis, RCA context, downstream Impact, governance/policy context, or another evidence view for a subject/question/time.

## Preconditions

The requesting principal, requested purpose/context, relevant subject(s), requested evidence facets/capabilities, and temporal perspective are identified enough to resolve authorization.

## Coordination semantics

1. Resolve Capability Authorization independently for the requested evidence/capability categories and relevant subjects/path segments.
2. Do not use raw-data read permission as a proxy for metadata, health, Lineage/RCA, Explanation, job-operation, or safeguard authority.
3. Assemble only concept state that is permitted for the actor/context. Each concept retains its own truth and provenance; the projection owns no new truth.
4. Where an authoritative capability/disclosure rule permits a safe abstraction, expose the narrowest useful form, for example:
   - `completeness expectation violated` while hiding the exact threshold/raw offending values;
   - `one restricted upstream dependency materially limits confidence` while hiding identity/path details;
   - team-level responsibility while hiding individual contact details;
   - applicable special-handling restriction summary while hiding restricted policy text;
   - supported upstream contributor status while hiding underlying protected evidence.
5. A safe abstraction is allowed only when the abstracted statement itself is authorized and already supported by concept state; restricted evidence must not be fetched merely to synthesize an otherwise unauthorized conclusion.
6. Denied/unknown/conflicting facets remain omitted/redacted/opaque with an explicit limitation where disclosure permits; they are never converted to reassuring absence.
7. Partial analytical projections remain valid and should preserve enough provenance/status to show what is known, what is hidden, and what cannot be determined.
8. Resolve job-operation/safeguard capabilities separately if relevant to the actor's next actions. Displaying that a capability exists does not execute an operation or prove an attempted action succeeds.
9. For historical questions, historical Capability Authorization may be evidence about what a past actor could know/do then, but current disclosure to the requester is still constrained by the requester's current applicable authorization.

## State and evidence effects

Capability Authorization owns permission decisions. Participating concepts own all substantive state. `Authorized analytical projection` is a synchronization result/view, not a new persisted truth-owning concept.

## Ambiguity / failure propagation

Unknown/conflicting authorization is not permission. If a safe abstraction cannot be established without disclosing restricted information, omit it and report the limitation. Partial evidence authorization can leave a causal or Impact conclusion less specific without forcing it to false/unknown globally.

## Temporal semantics

Authorization resolves for the requested capability/subject/context/time. The projection records composition/knowledge time and, where historical reasoning is requested, the evidence-time perspective. Current disclosure rules cannot be bypassed by asking for a historical view.

## Provenance / traceability

Every projected statement remains traceable internally to the underlying authorized concept state plus the Capability Authorization decision/abstraction rule used to expose it.

## Security / authorization

This synchronization is the primary analytical least-privilege boundary. Derived metrics, thresholds, Lineage paths, classifications, policies, responsibility metadata, causal claims, Impact, safeguards, and authorization details can each be sensitive even when raw rows are hidden.

## Invariants

- raw-data denial ≠ analytical denial;
- analytical permission ≠ production-control permission;
- job-operation permission ≠ raw-data permission;
- policy/restriction context ≠ authorization decision;
- responsibility ≠ authorization decision;
- derived/aggregate evidence ≠ automatically unrestricted;
- omitted/restricted ≠ nonexistent;
- safe abstraction ≠ declassification by inference;
- authorization view ≠ source truth mutation;
- permission to act ≠ action succeeded.

## Scenarios

**Restricted-data analyst:** cannot query C rows, but can see approved volume/completeness/freshness/duration Assessments, redacted A+B→C Lineage, policy restriction summary, responsible team, Impact layers, and supported Causal Claims.

**Restricted threshold:** analyst sees the violated health dimension and provenance class but not the numerical threshold or raw violating values.

**Analysis without control:** analyst can investigate and inspect Impact but cannot retry/update a job or activate a safeguard.

**Operation without raw access:** operator can retry/update a job under separate capability while remaining unable to inspect source rows.

**Current versus historical authorization:** a retrospective question can state that an incident responder had broader evidence access at the time, but a current requester does not receive those restricted historical values unless currently authorized.

## Non-goals

IAM enforcement, role-model design, executing job/safeguard actions, data masking implementation, universal declassification rules, or a new persisted projection database.

## Deferred questions

Minimum first-MVP capability/disclosure vocabulary, safe abstraction rules by evidence type, source authority/precedence for capability decisions, and purpose-of-use/just-in-time access semantics.