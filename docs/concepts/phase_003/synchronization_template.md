# Phase 003 Synchronization Specification Template

## Synchronization

**ID:** `SYN-XXX`

**Status:** Candidate / Accepted / Deferred / Reopened

## Outcome

What user/ecosystem result does this synchronization enable that no participating concept owns alone?

## Participating concepts and actions

List only accepted concepts and the relevant actions/results. External sources/actors may initiate a chain but do not become concepts merely by participating.

## Trigger / initiating condition

What condition causes the coordination to be considered? A trigger is not a causal assertion.

## Preconditions

What must already be resolved or known before the synchronization can proceed safely?

## Coordination semantics

Describe the semantic sequence or partial ordering. State explicitly when branches are independent and need not block each other.

## State and evidence effects

For each participating concept, state what it owns/records/returns. Synchronization itself should not become a hidden state-owning concept.

## Ambiguity / failure propagation

Describe behavior for unknown, ambiguous, conflicting, stale/non-comparable, insufficient-evidence, unavailable, and unauthorized results where applicable. Do not replace uncertainty with defaults just to complete the chain.

## Temporal semantics

State effective/event-time and recorded/knowledge-time behavior where material, including historical replay expectations.

## Provenance / traceability

State how resulting conclusions remain traceable to participating concept state and source evidence.

## Security / authorization

State what may be resolved internally versus disclosed to the requesting audience. Synchronization never broadens authorization.

## Invariants

List the boundaries the synchronization must preserve.

## Scenarios

Include happy, degraded/partial, conflicting, unauthorized, and historical scenarios where material.

## Non-goals

Explicitly exclude architecture assumptions and neighboring concept responsibilities.

## Deferred questions

Record open issues that do not block acceptance of the synchronization semantics.
