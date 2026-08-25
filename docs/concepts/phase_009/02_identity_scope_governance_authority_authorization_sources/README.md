# Phase 009 Group 02 — Identity, Scope, Semantics, Governance, Authority & Authorization Sources

**Status:** Next — not started

## Goal

Apply the accepted Group 01 integration contract (**INTG-001–INTG-022**) to source capabilities for Entity Identity, Monitoring Scope, Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority and Capability Authorization.

## Group 01 entry contract

For each material source surface, Group 02 must record exact surface/version identity, proposition mapping, evidence role, authority applicability, identity/join semantics, temporal coordinates, grain/context, positive/negative capability, coverage, availability/latency, retention/replay, correction behavior, disclosure, derivation/independence, quota/cost, integration observability and support classification/residual gaps.

Source availability does not establish authority; authority does not establish sufficiency; retrievability does not establish disclosure permission.

## Primary questions

- Which surfaces provide stable source-local identifiers, aliases, environment/version distinctions and rename/delete/recreate history?
- Which joins can establish ecosystem Entity Identity without relying on names alone?
- Which sources can assert monitoring responsibility/scope and with what historical applicability?
- Which metadata systems can provide semantic, responsibility, classification and policy assertions, and for which categories are they actually authoritative?
- How are conflicting assertions and authority rules represented across Unity Catalog, Collibra, repository configuration or other systems?
- Which sources establish action/disclosure permission, and how do current versus historical authorization differ?
- What restricted metadata may be used internally versus disclosed through Explanation/`inspectBasis`?
- What happens when optional systems such as Collibra or Immuta are absent?

## External-fact requirement

Group 02 must verify current vendor/platform documentation for evaluated surfaces and record meaningful edition/feature/permission/history limitations. Undocumented behavior cannot be treated as a guaranteed capability.

## Boundary

A governance source being available does not make it authoritative for every category. A security/policy system does not automatically create legal/compliance truth, and missing metadata does not create benign defaults.

## Handoff

Group 03 uses resolved identities/governance/authorization boundaries to evaluate cross-system change, deployment, execution and version evidence.