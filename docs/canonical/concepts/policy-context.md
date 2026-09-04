# Policy Context

**Canonical key:** `concept.policy_context`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.policy_context`

**Owns current question:** Which declared policies, restrictions, handling expectations, or governance obligations are asserted applicable to a subject/context/time?

**Stable IDs:** N/A

## Current semantics

Policy Context records policy/applicability assertions, policy reference, bounded use/environment/jurisdiction/consumer context, monitoring-appropriate obligation/restriction summary, applicability basis, effective interval, provenance/authority, revisions, staleness, conflicts, and availability limitations.

## Actions

- `associate` — record an applicability assertion with context/basis.
- `supersede` — prospectively replace/end applicability while preserving history.
- `resolveAt` — return applicable assertions, unknown, conflicting, stale, unauthorized, or unavailable.

## Invariants / boundaries

- Policy Context does not grant/deny access, prove enforcement/compliance, or perform legal interpretation.
- Authority for policy text/reference may differ from authority for subject/context applicability.
- Classification may inform applicability but cannot manufacture it.
- Missing policy context is unknown, not unrestricted.
- Multiple policies may simultaneously apply without conflict.
- Applicability is context/time specific and does not become global by convenience.
- Responsibility, Classification, schema tags, parent-domain state, or Lineage do not automatically derive Policy Context.

## Ambiguity / evidence

Stale/unavailable policy metadata remains marked as such. Co-authoritative applicability conflicts remain conflict. Safe disclosure may expose only that special handling applies.

## Synchronizations / related canonical resources

Entity Identity supplies subject; Assertion Authority supplies standing; Classification may provide evidence; Capability Authorization remains separate permission truth; Explanation may communicate authorized policy context and limitations.

## Non-goals

Access enforcement, legal interpretation, compliance certification, Classification assignment, or proof that controls operated.

## Provenance

- `docs/concepts/phase_002/02_semantics_governance_policy/policy_context.md`
- `docs/concepts/phase_005/02_semantic_responsibility_classification_policy_criticality_governance/`
