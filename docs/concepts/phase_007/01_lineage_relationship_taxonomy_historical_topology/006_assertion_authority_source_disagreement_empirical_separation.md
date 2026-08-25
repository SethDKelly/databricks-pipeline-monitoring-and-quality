# OPS-006 — Assertion Authority, Source Disagreement & Empirical Separation

**Status:** Accepted — Phase 007 Group 01

## Purpose

Handle disagreement among code, catalog, platform, human and runtime Lineage sources without inventing hidden precedence or confusing authoritative declaration with empirical fact.

## Contract

Lineage source assertions participate in the accepted Phase 005 Assertion Authority model when authoritative standing is relevant to the proposition.

An authority target may be scoped by relationship family, semantic role, subject, environment/context, interface/version and effective interval.

Examples of different propositions that must not be collapsed:

- **declared logical dependency** — which source has standing to say P depends on Q by design/configuration?;
- **effective Lineage relationship** — is that dependency actually applicable for the questioned version/interval?;
- **specific runtime encounter/use** — did run R or consumer U actually use version V? This remains execution/Impact evidence and is not manufactured by declaration authority.

## No universal source hierarchy

Phase 007 does not accept defaults such as:

- runtime always beats catalog;
- catalog always beats code;
- code always beats human assertion;
- latest record wins;
- most sources wins;
- more specific source wins;
- Databricks/Unity Catalog/GitHub/another platform is inherently authoritative.

Concrete source roles and support are deferred to Phase 009.

## Authority and evidence remain separate

An authoritative assertion can still be empirically wrong, stale or later corrected. Conversely, a strong empirical observation may establish a bounded runtime fact while lacking authority to redefine the governed logical relationship for future contexts.

When apparently contradictory evidence actually answers different propositions, preserve both rather than forcing conflict. When assertions/evidence genuinely disagree about the same bounded relationship proposition and no accepted resolver/evidence conclusion applies, preserve `conflicting`.

## Correction and history

Later authority-rule changes or source corrections can alter current retrospective resolution without rewriting:

- the assertions available earlier;
- the authority state known then;
- the topology resolution used by an earlier Investigation/Explanation/control decision.

## Invariants

- Assertion Authority ≠ evidence sufficiency.
- Authoritative standing ≠ factual infallibility.
- Source availability ≠ authority.
- Repository ownership/job creator/platform administrator ≠ topology authority.
- Capability Authorization to view/edit topology ≠ authority over the relationship assertion.
- Ingestion order ≠ precedence.

## Handoff

OPS-007 consumes resolved/evidenced relationship state for traversal. Phase 009 later maps concrete systems to these proposition/authority roles.