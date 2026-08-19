# Concept: Policy Context

**Status:** Candidate — introduced in Phase 002

## Purpose

Let users understand which declared policies, handling expectations, restrictions, or governance obligations are relevant to an identified subject in a given context without claiming enforcement or compliance.

## Operational principle

An affected asset is classified as PHI. The system resolves that an authoritative policy source associates the asset/context with specific handling and reporting restrictions. The explanation communicates the relevant policy context but does not claim that the monitoring framework has proven those requirements are satisfied.

## Actors

- Privacy / Security stakeholder
- Data Governance / Steward
- Business Analyst
- Data Engineer
- Monitoring framework

## State

- policy-context assertions and source references;
- subject/scope/context to which the assertion applies;
- effective time;
- handling/restriction metadata appropriate for monitoring use;
- provenance/authority context;
- conflicts, unknowns, and stale policy context.

## Actions

### `associate`
Associates a policy/handling context with an identified subject/context.

### `supersede`
Changes effective policy context while retaining historical applicability.

### `resolveAt`
Returns applicable policy context for a subject/time/audience context, or unknown/conflicting/unavailable.

## Invariants / behavioral expectations

- Policy context does not itself grant or deny access.
- Policy context does not prove compliance.
- Classification may inform policy applicability but is not identical to policy.
- Source authority and effective time are preserved.
- The monitoring framework must not broaden sensitive data access merely to explain policy context.

## Ambiguity and missing evidence

Unknown policy context should not be interpreted as unrestricted. Conflicting policies remain visible until authority/resolution semantics are defined.

## Synchronizations

- Classification may contribute to determining relevant policy context.
- Asset Identity provides the subject.
- Explanation uses Policy Context to constrain/supplement audience-facing communication.
- Later authorization concepts/mechanisms may synchronize with Policy Context but remain semantically separate.

## Security / privacy / governance considerations

Policy metadata can reveal sensitive organizational practices and may itself be protected.

## Evidence / provenance considerations

Policy context must retain the source policy/reference, applicability basis, effective time, and any known dependency on classification or organizational context. Derived summaries must remain traceable to the originating policy assertions.

## Representative scenarios

### Happy path
A PHI-classified asset resolves to an applicable handling policy and the explanation communicates the relevant constraints.

### Degraded path
Policy context is stale or unavailable; the framework reports that policy interpretation is incomplete.

### Conflicting evidence
Two policy authorities appear applicable with different handling requirements; the conflict is not silently flattened.

### Unauthorized evidence
The system can enforce safe omission in an explanation without revealing restricted policy metadata to the viewer.

## Non-goals

- access-control enforcement;
- legal interpretation;
- compliance certification;
- classification assignment.

## Open questions

- Is Policy Context a required MVP concept or a later enrichment?
- Which policy facts are useful to business analysts versus only privacy/security stakeholders?
