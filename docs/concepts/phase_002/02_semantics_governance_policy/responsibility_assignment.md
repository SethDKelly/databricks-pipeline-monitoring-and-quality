# Concept: Responsibility Assignment

**Status:** Accepted — Phase 002 Group 02

## Purpose

Let users determine who bears a named responsibility for an identified subject at a relevant time without treating responsibility as universal authority or access permission.

## Operational principle

An investigation identifies a degraded table. The system can separately resolve the team responsible for technical remediation, the business party accountable for fitness for use, and the steward responsible for semantic/governance maintenance. Each assignment retains its responsibility type, provenance, and effective time. A technical owner is therefore not silently treated as the authority for business semantics, classification, policy, or access.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Owner
- Data Steward / Governance Steward
- Security / Privacy / Compliance Stakeholder
- Data Platform Administrator
- Business Analyst
- Monitoring framework

## State

- identified subject;
- responsible party reference, such as person, team, organizational role, or system-managed group;
- responsibility type;
- optional responsibility scope/context;
- effective interval or lifecycle status;
- assertion provenance, actor/source, and authority context;
- supersession/correction history;
- unresolved or conflicting responsibility assertions.

## Actions

### `assign`
- **Intent:** assert or synchronize that a party bears a named responsibility for a subject.
- **State effect:** records a provenance-bearing assignment with applicable effective time/context.
- **Failure / unknown behavior:** unresolved subject identity or insufficient assertion authority does not create a guessed assignment.

### `transfer`
- **Intent:** prospectively move a responsibility from one party to another while preserving history.
- **State effect:** ends/supersedes the earlier assignment and records the new assignment without rewriting the past.

### `end`
- **Intent:** record that a known assignment no longer applies after an effective time without asserting who succeeds it.

### `resolveAt`
- **Intent:** return responsibility assignments applicable to a subject, responsibility type, context, and time.
- **Observable result:** applicable assignment(s), unknown, explicitly unassigned when such an assertion exists, conflicting, unauthorized, or unavailable, with provenance where disclosure is allowed.

## Invariants / behavioral expectations

- Technical ownership, business accountability, stewardship, security/privacy responsibility, platform administration, and other responsibility types are distinct.
- A responsibility assignment does not grant authorization to inspect data or metadata.
- A responsible party is not automatically authoritative for every other concept or metadata category.
- Multiple parties may legitimately hold different responsibilities for the same subject at the same time.
- Multiple parties may share the same responsibility only when the governing assertion explicitly permits or records that condition; it is not inferred from duplicate sources.
- Missing assignment evidence resolves to `unknown`, not `unassigned`.
- `Unassigned` is meaningful only when an authoritative assertion explicitly establishes the absence of an assignee for that responsibility.
- Current assignments do not overwrite historical responsibility.
- Responsibility inheritance from containers, domains, repositories, or pipelines is never implicit in this concept.

## Ambiguity and missing evidence

Conflicting assignments remain provenance-bearing until an accepted authority rule resolves them. If two sources name different technical owners, synchronization order must not decide the winner. A caller may receive a team-level or opaque contact when individual identity details are restricted.

## Synchronizations

- **Entity Identity** supplies the subject of the responsibility assignment.
- **Semantic Definition**, **Classification**, and **Policy Context** may reference relevant responsible/steward parties without transferring authority into Responsibility Assignment.
- **Expectation** may reference a responsible party for maintenance or approval without duplicating assignment state.
- **Investigation** and **Impact** use Responsibility Assignment to identify appropriate parties for follow-up.
- **Explanation** can surface authorized responsibility/contact context.
- A later authority concept or integration contract may determine which source is authoritative for a responsibility type; that rule is not hidden inside this concept.

## Security / privacy / governance considerations

Responsibility metadata may contain personal or organizational information. Disclosure should support the task without unnecessarily exposing individual details. Responsibility Assignment must not become an authorization bypass or a reason to retrieve otherwise restricted data.

## Evidence / provenance considerations

Every assignment should retain its asserting source/actor, responsibility type, relevant context, assertion time, and effective time when known. Transfers and corrections must remain historically reconstructable. Any later effective-resolution rule must be explainable from the underlying assertions rather than presenting an unexplained current owner.

## Representative scenarios

### Happy path
An affected table has a current technical owner, business accountable party, and data steward, each represented as separate responsibility assignments.

### Missing responsibility
No current technical-owner assertion is known. The product reports an ownership/responsibility gap as `unknown`; it does not invent a maintainer from repository activity.

### Conflicting assertions
Two governance sources identify different business owners. Both assertions remain visible with provenance until an accepted authority rule resolves the conflict.

### Transfer over time
A pipeline moves from Team A to Team B. Historical incident replay before the transfer resolves Team A; later incidents resolve Team B.

### Cross-repository responsibility
A downstream pipeline depends on an upstream data asset maintained by another repository/team. Each entity retains its own assignments; repository membership does not implicitly transfer responsibility.

### Unauthorized evidence
A business user can see an approved team contact for an incident without being shown restricted individual contact details.

## Non-goals

- defining semantic meaning;
- granting access or evaluating authorization;
- determining which source is universally authoritative;
- incident ticket assignment/workflow;
- inferring responsibility solely from commit history, job creator, or repository ownership;
- legal/compliance accountability determinations beyond recorded assertions.

## Deferred questions

- Which responsibility types are required for MVP?
- Should responsibility inheritance ever be supported as an explicit synchronization, and if so from which parent relationships?
- Which responsibility types permit multiple concurrent assignees?
- What source-precedence rules apply by responsibility type?
