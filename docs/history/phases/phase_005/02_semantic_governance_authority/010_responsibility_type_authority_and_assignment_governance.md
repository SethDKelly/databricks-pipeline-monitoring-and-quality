# AUTH-010 — Responsibility-Type Authority and Assignment Governance

**Status:** Accepted — Phase 005 Group 02

## Purpose

Apply Assertion Authority to Responsibility Assignment without allowing technical ownership, stewardship, accountability, or organizational role to become universal authority or permission.

## Contract

Authority is resolved per responsibility type and context, including examples such as:

- technical owner / maintainer;
- business accountable party;
- semantic/data steward;
- security/privacy/compliance contact;
- operational/on-call responsibility;
- platform administration responsibility.

The source or actor authoritative for one responsibility type need not be authoritative for another.

## Invariants

- Repository ownership, commit activity, job creator identity, team membership, or on-call participation do not establish Responsibility Assignment authority by themselves.
- Responsibility inheritance from domain, repository, pipeline, table, or parent container is not implicit. If supported later, it requires an explicit authority/synchronization rule.
- Multiple concurrent responsible parties are valid only when the responsibility assertion/rule permits them.
- `unknown responsibility` is distinct from an authoritative assertion of `unassigned`.
- A responsibility holder does not automatically gain Assertion Authority for semantics, Classification, Policy Context, criticality, Expectations, metrics, or controls.
- A responsibility holder does not automatically gain Capability Authorization.
- Transfers/corrections preserve historical responsibility and historical authority state.

## Example

Team A is the authoritative technical owner of Table C. A business-governance process, not Team A, is authoritative for C's business definition and criticality classification. Team A's remediation responsibility does not confer those other authorities.