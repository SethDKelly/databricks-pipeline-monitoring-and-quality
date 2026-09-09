# AUTH-011 — Classification-Scheme and Criticality Authority

**Status:** Accepted — Phase 005 Group 02

## Purpose

Apply Assertion Authority to Classification while keeping each scheme/vocabulary/context independently governed and treating business/operational criticality as classification context rather than impact evidence.

## Contract

Authority is resolved for a named classification scheme or bounded classified facet. Examples may include sensitivity, confidentiality, PHI/PII, operational tier, business criticality, client-delivery criticality, or other governed vocabularies.

Criticality remains a Classification under an explicit scheme/context unless later scenarios expose behavior requiring a separate concept.

## Invariants

- A source authoritative for one classification scheme is not automatically authoritative for another.
- Different labels from different schemes can coexist without conflict.
- A crosswalk/normalization between schemes is itself a provenance-bearing governed assertion and requires its own authority standing.
- `critical`, `tier 1`, or similar labels have meaning only within their named scheme/context; no universal criticality score is assumed.
- Business criticality, operational criticality, consumer criticality, and delivery criticality may legitimately differ.
- Criticality influences prioritization/context; it does not establish exposure, downstream effect, consequence, health failure, or causal severity by itself.
- Missing classification is `unknown`, not `unclassified` or low criticality.
- Schema, column names, data values, or downstream reachability do not manufacture authoritative Classification.

## Example

Table C may be `Restricted` in a confidentiality scheme, `Tier 1` in an operational-criticality scheme, and `Client Critical` only for one external-reporting consumer context. These are distinct assertions rather than one flattened criticality/sensitivity truth.