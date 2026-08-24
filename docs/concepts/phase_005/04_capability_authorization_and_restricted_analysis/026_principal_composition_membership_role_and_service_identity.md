# AUTH-026 — Principal Composition, Membership, Role, and Service Identity

**Status:** Accepted — Phase 005 Group 04

## Purpose

Resolve capability assertions contributed through users, groups, roles, service principals, or other governed principal relationships without hidden identity or entitlement precedence.

## Contract

Authorization reasoning should preserve:

- the direct requesting principal;
- relevant group/role/service-principal relationships;
- provenance and effective time of membership/association;
- the capability assertion contributed through each relationship;
- the accepted combination/precedence rule, if any;
- unresolved identity/membership/conflict limitations.

## Invariants

- Group membership is evidence-bearing state, not assumed from title, repository activity, team naming, or organizational proximity.
- A group or role grant applies only when the principal's applicable membership/assumption is established for the relevant time/context.
- Direct user authorization does not automatically override group/role authorization.
- Group/role authorization does not automatically override a direct decision.
- Explicit deny does not automatically override explicit allow unless the accepted authorization rule says so.
- Role hierarchy, group nesting, service-principal impersonation/delegation, or membership inheritance is never implicit.
- A service principal may have processing/operational capabilities that a human requester does not, and vice versa.
- Current membership must not be projected backward into historical authorization.

## Authority boundary

Which authorization source or combination rule has governing standing is itself provenance-bearing governance state. Assertion Authority may resolve source/rule standing for the bounded authorization target; source count, convenience, or synchronization order may not.
