# 005 — Architectural Principles

## Scope

These are **constraints on future architecture**, not an architecture selection. They describe qualities that technical designs must preserve once implementation design begins.

## AP-01 — Conceptual architecture precedes technical architecture

Technical modules must emerge from accepted product concepts and synchronizations rather than the reverse.

No current document should infer that one concept becomes one microservice, one table, one class, or one API.

## AP-02 — The ecosystem is the reasoning boundary

The system must reason across repository, job, workspace, pipeline, and domain boundaries while preserving those boundaries for provenance and ownership.

A cross-repository dependency is not an edge case; it is a core use case.

## AP-03 — Time and history are first-class

The system must eventually support point-in-time questions such as:

- What did this asset look like before the degradation?
- What lineage/topology existed when the affected run occurred?
- What deployment was active then?
- When did the first abnormal observation appear?
- Has the issue happened before?

Current-state-only architecture would violate the product thesis.

## AP-04 — Evidence is preserved separately from interpretation

Observed facts, derived assessments, hypotheses, attributions, and confirmed causes must remain distinguishable.

A business-friendly summary may compress evidence, but it must not erase the evidence chain.

## AP-05 — Provenance is part of every material fact

Ownership, classifications, descriptions, lineage relationships, quality observations, baselines, deployments, and assessments should retain source and temporal provenance appropriate to their use.

Synchronized metadata must not silently become authoritative merely because it is convenient to query.

## AP-06 — Lineage is typed

The design must distinguish at least:

- data derivation lineage;
- pipeline/operational dependency;
- deployment/code lineage;
- downstream consumption/impact relationships.

These relationships may intersect but should not be collapsed into an ambiguous generic edge.

## AP-07 — Monitoring models degradation, not only failure

A successful job can yield degraded data. Architecture must therefore support measurements and assessments independent of execution success/failure.

## AP-08 — Expectations and observations are separate

What should happen and what did happen are separate facts with separate provenance and ownership.

This enables changes in expectations to be audited and historical observations to be reinterpreted without rewriting history.

## AP-09 — Historical comparisons must be reproducible

Where practical, a historical assessment should be explainable from the evidence and definitions that applied at the time, including known changes to expectations and topology.

## AP-10 — Security boundaries follow data authority, not monitoring convenience

The framework should not gain or redistribute raw-data access merely because it monitors an asset.

Metadata, aggregates, samples, and derived explanations must each be treated according to their sensitivity and source authorization.

## AP-11 — Data minimization is a design requirement

Prefer metadata, aggregate metrics, checks, fingerprints, and other minimally necessary evidence over copying row-level sensitive data into the monitoring system.

If later functionality genuinely requires sample values, that must be an explicit security/design decision rather than a default ingestion behavior.

## AP-12 — Governance metadata participates in reasoning

Business semantics, ownership, stewardship, criticality, and policy classifications should not be decorative catalog links. They should affect impact analysis, explanations, escalation, and presentation where appropriate.

## AP-13 — Policy transparency is not compliance certification

The architecture may present policy classifications, applicable expectations, access evidence, or control status. It must not mechanically transform these into a legal compliance claim.

## AP-14 — Tool integration is replaceable at the concept boundary

Databricks, GitHub/GitHub Actions, Collibra, Immuta, DQX, and Metric Views should be evaluated as providers or realizations of product concepts.

An optional integration must not become an implicit required dependency unless that decision is deliberate and documented.

## AP-15 — Databricks-native capabilities are favored, not worshipped

When Databricks-native capabilities meet the accepted product concept cleanly, prefer them over unnecessary duplication. When they do not, preserve the concept and add only the missing functionality.

## AP-16 — Question answering is a view over evidence

The conversational/question-answering experience must not become an independent knowledge source. Answers should be grounded in authorized evidence, semantics, and historical context.

## AP-17 — Unknown is a valid result

The architecture must support incomplete, stale, conflicting, unavailable, or unauthorized evidence without inventing certainty.

## AP-18 — Human confirmation has explicit semantics

If a person confirms a cause, waives an anomaly, changes an expectation, or annotates an incident, that action must remain distinguishable from machine-derived observations.

## AP-19 — Business and engineering views share the same underlying state

Do not create separate truth stores for executive/business reporting and engineering analysis. Different projections may expose different authorized detail, but they must derive from the same evidence model.

## AP-20 — The product remains useful with optional systems absent

The core product should be able to function without Collibra or Immuta. Their presence may enrich authoritative semantics/policy information, but absence should degrade enrichment rather than invalidate the whole system.
