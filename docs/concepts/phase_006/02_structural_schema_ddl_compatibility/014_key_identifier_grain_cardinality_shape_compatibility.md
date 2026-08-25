# HLTH-014 — Key, Identifier, Grain & Cardinality-Shape Compatibility

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define structural compatibility for changes that alter record identity, uniqueness assumptions, join semantics, or the grain at which an output represents the world.

## Contract

Structural compatibility may bind:

- declared business/technical key or identifier role;
- composite-key membership/order where semantically meaningful;
- row/entity grain;
- one-to-one, one-to-many, many-to-one, or many-to-many relationship assumptions where part of the contract;
- deduplication or surrogate-key semantics when they determine output identity;
- consumer expectations that rely on key uniqueness, referential use, or grain stability.

## Invariants

- Changing key/grain semantics is structurally material even when the column list and physical types do not change.
- A declared key-role change belongs to Semantic Definition/Change; actual uniqueness/non-null/reference quality remains Observation/Assessment evidence.
- `same columns, different grain` can invalidate row-count Baselines, uniqueness checks, quantiles/distributions, joins, reconciliation formulas and downstream consumer assumptions.
- Adding a key component can make previously unique records intentionally repeat at the old grain; that is not automatically a quality defect.
- Removing a key component can collapse previously distinct records; compatibility depends on the declared contract and consumer semantics.
- Key order is material only when the relevant contract or transformation treats order as semantically significant.
- Surrogate-key replacement does not establish semantic continuity unless Entity Identity/mapping evidence supports equivalence.
- Group 03 later decides historical metric/Baseline comparability after such a change; Group 05 later defines transformation reconciliation under the new grain/key semantics.

## Example

Table C changes from one row per `account_id` to one row per `account_id, business_date`. Every original column may still exist with the same types, yet old row-count and account-level uniqueness expectations are no longer directly comparable.