# OPS-024 — Semantic Scope Narrowing & Candidate Relevance

**Status:** Accepted — Phase 007 Group 03

## Purpose

Prevent asset-level blast radius from over-generalizing a proposed change to consumers whose fields, populations, interfaces or uses are not actually implicated.

## Contract

Prospective relevance composes OPS-003/OPS-007 relationship scope with the proposed change scope. Material dimensions may include:

- changed field/path/semantic role;
- key or grain;
- population/cohort/partition;
- transformation role;
- interface/contract version;
- consumer/use;
- environment/region;
- proposed version/effective context.

For one candidate/change question, relevance is:

- relevant;
- not relevant where the semantic path is sufficiently excluded;
- indeterminate where scope cannot be composed;
- conflicting/unavailable where applicable.

## Examples

A change to `A.internal_note` need not make a report that consumes only `A.customer_id` relevant when field-level derivation evidence is sufficient. If only table-level A→C Lineage is known, the report remains indeterminate rather than being declared unaffected.

A stable consumer-facing view can insulate a consumer from a backing-table structural change when the interface contract and planned state support that conclusion.

## Invariants

- asset reachability ≠ field relevance;
- same table dependency ≠ every field/population dependency;
- `not relevant` is a bounded negative conclusion requiring sufficient semantic/path evidence;
- missing fine-grained Lineage does not broaden certainty;
- relevance does not establish compatibility, exposure, Impact or cause.

## Handoff

OPS-025 evaluates structural/interface compatibility for candidates where the proposed change reaches a material contract surface.