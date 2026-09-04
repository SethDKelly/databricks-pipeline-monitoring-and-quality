# Capability Authorization

**Canonical key:** `concept.capability_authorization`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.capability_authorization`

**Owns current question:** Is an identified principal permitted to perform a named capability on a bounded subject/context/time?

**Stable IDs:** N/A

## Current semantics

Capability Authorization owns principal, capability, subject/set, environment/purpose/use/consumer context, permitted/denied/conditional/unknown/conflicting/unavailable decision, constraints, authoritative source/provenance, effective interval, knowledge time, revocation/correction history, and safe basis disclosure. Capability classes remain independently resolvable, including raw/sensitive data access, metadata/semantic/governance visibility, health/Assessment visibility, Lineage/RCA/evidence inspection, job/run operation, Change Intent/Expectation authoring, Safeguard actions, Gate registration/config/control/override, and Explanation/report access.

## Actions

- `recordDecision` — preserve a bounded authorization decision/entitlement.
- `supersedeDecision` — revoke/replace/correct prospectively while retaining history.
- `resolveFor` — return decision/conditions/conflict/unknown/unavailable for principal+capability+subject+context+time.
- `explainBasis` — return authorized decision basis/reference where permitted.

## Invariants / boundaries

- Authentication ≠ Capability Authorization ≠ Assertion Authority.
- Raw-data read ≠ metadata/health visibility ≠ Lineage/RCA visibility ≠ job operation ≠ Safeguard authority ≠ Gate authority ≠ causal-confirmation authority.
- Responsibility Assignment, Classification, Policy Context, Monitoring Scope, repository ownership, creator identity, administrator title, or Assertion Authority do not automatically grant capability permission.
- Permission to see a derived Assessment does not imply access to all underlying Observations/thresholds/raw values.
- Permission to perform Investigation does not imply complete evidence visibility.
- Permission to operate a job/Gate/Safeguard does not imply data-read permission, readiness, or successful enforcement/action outcome.
- Service processing permission is not the same as requester visibility/disclosure.
- Capability Authorization is decision/entitlement truth, not enforcement proof.
- Missing authorization evidence is not allow; unknown remains unknown.
- Current authorization does not overwrite historical authorization.

## Ambiguity / evidence

Conflicting access authorities remain conflict until accepted resolution. Metadata and control state may themselves be sensitive; safe decision exposure need not reveal full policy/entitlement detail.

## Synchronizations / related canonical resources

Entity Identity supplies subjects; all other concepts consume task-specific permissions without ceding their truth. Explanation composes only a requester-authorized projection. Assertion Authority remains independently resolved.

## Non-goals

Authentication/IdP selection, RBAC/ABAC implementation, direct enforcement, responsibility, assertion standing, compliance, or vendor permission-model selection.

## Provenance

- `docs/concepts/phase_002/addenda/capability_authorization.md`
- `docs/concepts/phase_005/`
