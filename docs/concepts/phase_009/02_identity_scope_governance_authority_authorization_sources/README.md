# Phase 009 Group 02 — Identity, Scope, Semantics, Governance, Authority & Authorization Sources

**Status:** Not started

## Goal

Apply the Group 01 integration contract to source capabilities for Entity Identity, Monitoring Scope, Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority and Capability Authorization.

## Primary questions

- Which surfaces provide stable source-local identifiers, aliases, environment/version distinctions and rename/delete/recreate history?
- Which joins can establish ecosystem Entity Identity without relying on names alone?
- Which sources can assert monitoring responsibility/scope and with what historical applicability?
- Which metadata systems can provide semantic, responsibility, classification and policy assertions, and for which categories are they actually authoritative?
- How are conflicting assertions and authority rules represented across Unity Catalog, Collibra, repository configuration or other systems?
- Which sources establish action/disclosure permission, and how do current versus historical authorization differ?
- What restricted metadata may be used internally versus disclosed through Explanation/`inspectBasis`?
- What happens when optional systems such as Collibra or Immuta are absent?

## Boundary

A governance source being available does not make it authoritative for every category. A security/policy system does not automatically create legal/compliance truth, and missing metadata does not create benign defaults.

## Handoff

Group 03 uses resolved identities/governance/authorization boundaries to evaluate cross-system change, deployment, execution and version evidence.
