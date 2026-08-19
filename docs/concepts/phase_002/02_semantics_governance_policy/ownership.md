# Concept: Ownership

**Status:** Candidate

## Purpose

Let users know who is responsible, accountable, or stewarding an identified subject for a defined responsibility.

## Operational principle

An investigation identifies a degraded table. The system resolves the technical owner responsible for remediation, the business owner accountable for fitness for use, and the data steward responsible for semantics, each as distinct responsibility assignments with provenance and effective time.

## Actors

- Data Engineer
- Business Owner
- Data Steward
- Data Platform Administrator
- Business Analyst

## State

- responsibility assignments between an identified subject and person/team/organizational role;
- responsibility type;
- effective time/lifecycle status;
- provenance/authority context;
- conflicts or gaps.

## Actions

### `assign`
Records or synchronizes a responsibility assignment.

### `transfer`
Supersedes an assignment while retaining history.

### `resolve`
Returns applicable responsible parties by responsibility type and time.

## Invariants / behavioral expectations

- Technical owner, business owner, steward, security/privacy authority, and platform administrator are not interchangeable.
- Ownership does not imply authorization to view underlying data.
- An owner is not automatically authoritative for all metadata categories.
- Historical ownership remains queryable for incident-time analysis.

## Ambiguity and missing evidence

Multiple owners may be valid for different responsibilities. Conflicting assignments remain provenance-bearing. `unowned`/`unknown owner` are legitimate findings.

## Synchronizations

- Asset Identity supplies the owned subject.
- Expectation may reference an owner/steward without duplicating ownership state.
- Investigation and Impact use Ownership to route attention.
- Explanation can surface appropriate contacts subject to authorization.

## Security / privacy / governance considerations

Ownership metadata contains organizational/person information and may need controlled visibility.

## Evidence / provenance considerations

Assignments retain their asserting source/actor, responsibility type, and effective interval. Resolved ownership must be traceable back to those assignments rather than appearing as an unexplained current value.

## Representative scenarios

### Happy path
An investigation resolves a technical owner and business steward for the affected asset.

### Degraded path
No current technical owner can be resolved; the framework reports an ownership gap.

### Conflicting evidence
Two systems claim different business owners; both remain visible until authority rules resolve the conflict.

### Unauthorized evidence
A user may receive a team-level contact while individual identity details remain restricted.

## Non-goals

- semantic definition;
- authorization;
- incident assignment workflow;
- compliance accountability determination beyond recorded responsibility assertions.

## Open questions

- Which responsibility types are required for MVP?
- Can ownership inherit from domain/product/container relationships, and if so how explicitly?
