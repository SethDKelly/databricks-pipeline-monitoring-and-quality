# DMTZ Canonical Knowledge

**Authority state:** PARTIALLY CANONICALIZED — CKR MIGRATION IN PROGRESS

This directory is the namespace for DMTZ **current accepted meaning** once a record has been explicitly cut over.

Semantic authority changes only through:

- [`../canonical_knowledge_retrofit/authority_model.md`](../canonical_knowledge_retrofit/authority_model.md)
- [`../canonical_knowledge_retrofit/migration_contract.md`](../canonical_knowledge_retrofit/migration_contract.md)
- [`../canonical_knowledge_retrofit/canonical_ownership_inventory.json`](../canonical_knowledge_retrofit/canonical_ownership_inventory.json)

A resource here is current authority only when its inventory state is `canonicalized` and its file declares `CANONICAL CURRENT AUTHORITY`.

## Canonicalized in CKR-B

The first substantive cutover established current canonical owners for nine foundation/glossary records:

- product definition;
- actors/stakeholders;
- foundational terminology;
- Concept Design method;
- AP-01–AP-32 architectural principles;
- SP-01–SP-15 security/governance policy;
- ecosystem lifecycles;
- MVP boundary;
- shared glossary.

Use [`reference/`](reference/), [`invariants/`](invariants/), and [`policies/`](policies/) for these resources.

## Still migrating

The 24 accepted concept definitions, SYN/REF/AUTH/HLTH/OPS/EXPL/INTG stable-ID families, authority vocabulary, experience contracts, and ARCH-001–ARCH-500 remain with their inventory-selected legacy owners until their assigned CKR groups.

## Knowledge families

- [`concepts/`](concepts/) — independently understandable accepted concepts;
- [`contracts/`](contracts/) — cross-cutting/domain/stable-ID contracts;
- [`policies/`](policies/) — normative policy rules;
- [`invariants/`](invariants/) — durable semantic separations/non-collapse rules;
- [`authority/`](authority/) — authority, authorization, governance and disclosure boundaries;
- [`experience/`](experience/) — questioning, Explanation and user-facing contracts;
- [`architecture/`](architecture/) — accepted technical architecture contracts;
- [`reference/`](reference/) — terminology and compact reference surfaces.

## Lookup rule

For a `canonicalized` record, answer current semantic questions from its canonical owner here. Consult design history only for provenance/rationale or explicit historical/change work.

For records not yet canonicalized, follow the ownership inventory to their current legacy owners.
