# AUTH-009 — Semantic Facet and Schema-Meaning Authority

**Status:** Accepted — Phase 005 Group 02

## Purpose

Apply Assertion Authority to Semantic Definition facets, including technical schema meaning, without conflating governed declarations with observed physical schema state or normative schema-health requirements.

## Contract

Authority resolves independently for semantic facets such as:

- business definition;
- technical description;
- grain;
- unit;
- population/inclusion meaning;
- calculation meaning;
- domain/interpretation guidance;
- column/field semantic role;
- identifier/key role;
- governed technical schema or schema-contract declaration where one exists.

A source can be authoritative for one facet and advisory/unknown for another. Business and technical facets may legitimately have different authorities.

## Schema separation

Preserve three distinct truths:

1. **declared/governed schema meaning** — Semantic Definition assertion, resolved through Assertion Authority;
2. **normative schema contract** — Expectation describing what structure/compatibility should be acceptable;
3. **realized/observed schema** — Observation/Change evidence describing what actually exists or changed.

A Git/repository schema specification may eventually be authoritative for a declared contract while Databricks/Unity Catalog metadata provides evidence of realized structure. Neither role is selected universally in Phase 005.

## Invariants

- Authoritative schema meaning does not prove the physical schema actually matches it.
- Observed schema metadata does not by itself establish authoritative business meaning.
- Column name/type/nullability/key-role assertions remain facet-specific; they are not silently merged into one universal schema truth.
- A declared primary/business-key role is semantic context; actual uniqueness/null behavior requires Observation/Assessment evidence.
- A column rename cannot be inferred as semantic identity merely because one column disappeared and another appeared; Change Intent, Entity Identity, Semantic Definition, or other evidence must support that interpretation.
- Names, code, DDL, SQL usage, or schemas may provide assertions/evidence but do not create business-semantic authority by themselves.
- Current semantic authority does not rewrite historical schema meaning.

## Example

A governed contract declares `customer_id` as the customer business key. A runtime catalog shows the column exists but duplicate-rate evidence is elevated. The semantic key role remains authoritative while uniqueness health can independently fail an Expectation.
