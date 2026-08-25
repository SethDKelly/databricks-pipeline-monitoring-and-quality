# Phase 009 Group 01 — Integration Contract Vocabulary, Source Roles & Capability Matrix

**Status:** Next — not started

## Goal

Define the reusable integration-contract vocabulary and evaluation matrix that every later Phase 009 source review must populate.

## Primary questions

- What is the smallest useful identity for a source capability: system, exact surface, object/event/query class and version/edition context?
- How is a source mapped to one or more accepted propositions without making the integration another truth owner?
- How do proposition-specific source authority, evidence relevance, evidence sufficiency and disclosure authorization remain separate?
- Which source-local identifiers and joins are required to bind evidence to Entity Identity, run, deployment, version, consumer, path, control and historical context?
- What event/effective and recorded/knowledge timestamps does the source actually expose?
- What positive evidence can the source establish, and what opportunity/population/path coverage is needed before it can support a strong negative?
- How should availability, latency, retention, corrections/backfills, mutability, quotas/cost and integration observability be recorded?
- How are `supported`, partial/gapped, unsupported, unknown and not-applicable integration outcomes represented without becoming proposition truth states?

## Expected outputs

- Phase 009 `INTG-###` contract template/vocabulary;
- reusable source capability matrix dimensions;
- evidence-role and authority-applicability rules;
- temporal/join/coverage rules;
- negative-evidence and duplicate/common-derivation rules;
- explicit integration-gap vocabulary;
- scenario matrix for source ambiguity, outages, late evidence, conflicting sources, insufficient coverage and restricted access.

## Boundary

This group defines evaluation semantics only. It must not choose adapter interfaces, source ingestion jobs, storage schemas, queues, polling intervals, streaming mechanisms or vendor SDKs.

## Handoff

Group 02 applies the accepted matrix first to identity, scope, governance, authority and authorization source families.
