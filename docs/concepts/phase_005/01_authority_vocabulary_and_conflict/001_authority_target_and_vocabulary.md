# AUTH-001 — Authority Target Binding and Vocabulary

**Status:** Accepted — Phase 005 Group 01

## Purpose

Bind every authority determination to the exact assertion category/facet, subject scope, context, and time for which standing is being resolved.

## Contract

An authority question is not `Which source is authoritative?` in the abstract. It is a question such as:

> Which source/actor has authoritative standing for the **business-definition facet** of **Metric M** in **production/external-reporting context** at **effective time T**, using authority state known by **knowledge cutoff K**?

The authority target should identify, as applicable:

- owning concept/assertion category;
- facet, scheme, responsibility type, expectation/metric class, or other bounded assertion subtype;
- identified subject or explicit subject scope;
- environment/tenant/purpose/use/jurisdiction/business context/consumer where relevant;
- effective interval/time;
- knowledge cutoff for historical/as-known resolution when required.

## Core vocabulary

- **source assertion** — a provenance-bearing assertion contributed by a source/actor to its owning concept, regardless of authority standing;
- **authority target** — the bounded assertion category/facet/scope/context/time for which standing is resolved;
- **authority holder** — source/actor/role/governed process referenced by an authority rule;
- **authority rule** — provenance-bearing rule defining holder standing/conditions for an authority target;
- **authoritative assertion** — applicable source assertion whose source/actor has authoritative standing under an accepted applicable rule;
- **advisory assertion** — applicable assertion that may inform/enrich/challenge but does not displace authoritative state;
- **authoritative resolution** — the owning concept's resolution using the applicable assertions plus accepted authority standing;
- **authority unknown/conflicting/unavailable** — explicit non-success states rather than excuses to choose a convenient source.

## Invariants

- Authority is category/facet/context/time specific.
- A source can be authoritative for one facet and advisory or unknown for another.
- Multiple context-specific authorities can legitimately coexist.
- Different schemes/vocabularies are not conflicts merely because their labels differ.
- The authority target must be resolved before precedence rules can be applied.
- No globally authoritative vendor/source is implied.

## Example

Unity Catalog can be authoritative for a technical schema facet while a business governance process is authoritative for the business definition. Neither authority automatically transfers to the other facet.
