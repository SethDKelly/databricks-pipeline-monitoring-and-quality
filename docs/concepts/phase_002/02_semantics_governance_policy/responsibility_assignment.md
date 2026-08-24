# Concept: Responsibility Assignment

**Status:** Accepted — Phase 002 Group 02; authority refined by Phase 005 Group 02

## Purpose

Let users determine who bears a named responsibility for an identified subject at a relevant time without treating responsibility as universal authority or access permission.

## Operational principle

An investigation identifies a degraded table. The system can separately resolve the team responsible for technical remediation, the business party accountable for fitness for use, and the steward responsible for semantic/governance maintenance. Each assignment retains its responsibility type, provenance, effective time, and Assertion Authority context. A technical owner is therefore not silently treated as the authority for business semantics, classification, policy, metrics, schema expectations, or access.

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
- assertion provenance, actor/source, and Assertion Authority context;
- supersession/correction history;
- unresolved or conflicting responsibility assertions.

## Actions

### `assign`
- **Intent:** assert or synchronize that a party bears a named responsibility for a subject.
- **State effect:** records a provenance-bearing assignment with applicable effective time/context.
- **Failure / unknown behavior:** unresolved subject identity or authority standing does not create a guessed assignment.

### `transfer`
- **Intent:** prospectively move a responsibility from one party to another while preserving history.
- **State effect:** ends/supersedes the earlier assignment and records the new assignment without rewriting the past.

### `end`
- **Intent:** record that a known assignment no longer applies after an effective time without asserting who succeeds it.

### `resolveAt`
- **Intent:** return responsibility assignments applicable to a subject, responsibility type, context, and time.
- **Observable result:** applicable assignment(s), unknown, explicitly unassigned when such an authoritative assertion exists, conflicting, unauthorized, or unavailable, with provenance where disclosure is allowed.

## Invariants / behavioral expectations

- Technical ownership, business accountability, stewardship, security/privacy responsibility, operational/on-call responsibility, platform administration, and other responsibility types are distinct.
- Assertion Authority resolves separately by responsibility type/context.
- A responsibility assignment does not grant authorization to inspect data or metadata.
- A responsible party is not automatically authoritative for Semantic Definition, Classification/criticality, Policy Context, Expectations, metric/schema rules, or controls.
- Multiple parties may legitimately hold different responsibilities for the same subject at the same time.
- Multiple parties may share the same responsibility only when the governed assignment/rule explicitly permits that condition; it is not inferred from duplicate sources.
- Missing assignment evidence resolves to `unknown`, not `unassigned`.
- `Unassigned` is meaningful only when an authoritative assertion explicitly establishes the absence of an assignee for that responsibility.
- Current assignments do not overwrite historical responsibility.
- Responsibility inheritance from containers, domains, repositories, pipelines, tables, or upstream assets is never implicit. Explicit governed derivation is required if inheritance is later supported.
- Repository activity, source-code ownership, job creator identity, or on-call membership may be evidence/context but do not manufacture authoritative responsibility.

## Ambiguity and missing evidence

Conflicting assignments remain provenance-bearing until accepted Assertion Authority rules resolve standing/precedence. If two co-authoritative sources name different technical owners and no resolver applies, the authoritative conflict remains. A caller may receive a team-level or opaque contact when individual identity details are restricted.

## Synchronizations

- **Entity Identity** supplies the subject of the responsibility assignment.
- **Assertion Authority** determines which assignment assertions have authoritative/advisory/conflicting standing by responsibility type/context/time.
- **Semantic Definition**, **Classification**, and **Policy Context** may reference relevant responsible/steward parties without transferring authority into Responsibility Assignment.
- **Expectation** may reference a responsible party for maintenance or approval without duplicating assignment state or granting normative authority automatically.
- **Investigation** and **Impact** use Responsibility Assignment to identify appropriate parties for follow-up.
- **Explanation** can surface authorized responsibility/contact context.

## Security / privacy / governance considerations

Responsibility metadata may contain personal or organizational information. Disclosure should support the task without unnecessarily exposing individual details. Responsibility Assignment must not become an authorization bypass or a reason to retrieve otherwise restricted data.

## Evidence / provenance considerations

Every assignment should retain its asserting source/actor, responsibility type, relevant context, assertion time, effective time, and authority standing/basis when known. Transfers and corrections must remain historically reconstructable.

## Representative scenarios

### Happy path
An affected table has a current technical owner, business accountable party, and data steward, each represented as separate responsibility assignments.

### Missing responsibility
No current technical-owner assertion is known. The product reports the gap as `unknown`; it does not invent a maintainer from repository activity.

### Conflicting assertions
Two co-authoritative governance sources identify different business owners. The authoritative conflict remains visible until an accepted resolver applies.

### Transfer over time
A pipeline moves from Team A to Team B. Historical incident replay before the transfer resolves Team A; later incidents resolve Team B.

### Cross-repository responsibility
A downstream pipeline depends on an upstream data asset maintained by another repository/team. Each entity retains its own assignments; repository membership or Lineage does not implicitly transfer responsibility.

### Responsibility without semantic authority
Team A is the technical owner of Table C but has only advisory standing for C's business definition and criticality scheme. Ownership does not promote its other assertions.

### Unauthorized evidence
A business user can see an approved team contact for an incident without being shown restricted individual contact details.

## Non-goals

- defining semantic meaning;
- granting access or evaluating authorization;
- granting assertion authority by assignment alone;
- incident ticket assignment/workflow;
- inferring responsibility solely from commit history, job creator, repository ownership, containment, or Lineage;
- legal/compliance accountability determinations beyond recorded assertions.

## Deferred questions

- Which responsibility types are required for MVP?
- Should responsibility inheritance ever be supported as an explicit governed derivation, and from which parent relationships?
- Which responsibility types permit multiple concurrent assignees?
- Which concrete sources/actors hold authority for each responsibility type in the deployment environment?
