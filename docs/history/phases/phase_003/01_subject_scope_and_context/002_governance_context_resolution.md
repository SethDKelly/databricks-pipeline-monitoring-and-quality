# SYN-002 — Identified Subject + Governance Context Resolution

**Status:** Accepted — Phase 003 Group 01

## Outcome

Allow later health, investigation, impact, and explanation behavior to obtain the relevant **meaning, named responsibility, classification, and policy context** for one identified subject/time while preserving each concept's independent provenance, conflict, missing-state, and authorization semantics.

## Participating concepts and actions

- **Entity Identity** — resolved subject from SYN-001 or another justified identity path.
- **Semantic Definition** — relevant resolution action/state.
- **Responsibility Assignment** — relevant responsibility resolution.
- **Classification** — `resolveAt`.
- **Policy Context** — `resolveAt`.

## Trigger / initiating condition

A downstream scenario needs governance/semantic context for an identified subject, facet/context, and relevant time.

## Preconditions

One Entity Identity is sufficiently resolved. The downstream need supplies enough context to avoid pretending all semantic facets, responsibility types, classification schemes, or policies are interchangeable.

## Coordination semantics

1. Use the Entity Identity as the common referent.
2. Resolve Semantic Definition, Responsibility Assignment, Classification, and Policy Context independently for their relevant facets/context/time.
3. Preserve independent result states and provenance per concept/category.
4. Do not require every branch to succeed before valid branches can be used.
5. Do not collapse multiple applicable assertions into one synthetic `governance status` unless a later accepted purpose explicitly requires such a concept.
6. Pass only the authorized projection needed by downstream reasoning/presentation.

The conceptual independence of branches does not prescribe parallel implementation.

## State and evidence effects

No participating concept is mutated merely because context was requested. If an external synchronization writes new assertions, those writes occur through the owning concept's accepted actions/provenance rules, not through this resolution synchronization.

## Ambiguity / failure propagation

- missing semantic definition → meaning unknown, not inferred from name/schema;
- missing responsibility → responsibility gap/unknown, not intentional unassignment;
- missing classification → unknown, not non-sensitive;
- missing Policy Context → unknown, not unrestricted;
- conflict in one category remains category-local unless a downstream conclusion specifically depends on it;
- unauthorized detail may resolve to an allowed abstract/opaque result rather than a false absence;
- synchronization order never resolves authority conflict.

## Temporal semantics

Each governance concept resolves its own applicable effective-time assertions. A historical investigation can therefore use the meaning/responsibility/classification/policy context that applied then. Later corrections remain visible through recorded/knowledge time where material.

## Provenance / traceability

Downstream material statements must identify which semantic facet, responsibility type, classification assertion, or Policy Context assertion they relied on rather than citing an untraceable composite metadata blob.

## Security / authorization

Context aggregation can create inference risk. A downstream projection may disclose less than the internally available authorized reasoning context, but it must not broaden source access or use restricted detail solely to leak a conclusion.

## Invariants

- common Entity Identity does not merge concept state;
- technical responsibility does not become semantic/policy authority;
- classification does not become policy or authorization;
- Policy Context does not become compliance;
- missing context is not a safe default;
- current context does not overwrite historical context.

## Scenarios

**Cross-repository:** C's technical responsibility comes from one repository/team while business accountability/semantic stewardship come from other sources; all remain distinct.

**Partial context:** semantics are known but Policy Context is unavailable. Explanation can use known meaning while disclosing the policy-context gap where relevant.

**Conflict:** two sources disagree on PHI classification. The product retains the conflict rather than using whichever synchronized last.

## Non-goals

Universal authority/source precedence, IAM mechanics, compliance determination, alert routing, creation of a generic governance aggregate concept.

## Deferred questions

Which metadata facets/types are mandatory for the MVP and whether repeated authority behavior later warrants its own concept.
