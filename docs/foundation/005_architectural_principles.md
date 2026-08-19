# 005 — Architectural Principles

## Scope

These are **constraints on future architecture**, not an architecture selection. They describe qualities that technical designs must preserve once implementation design begins.

## AP-01 — Conceptual architecture precedes technical architecture

Technical modules must emerge from accepted product concepts and synchronizations rather than the reverse.

No current document should infer that one concept becomes one microservice, one table, one class, or one API.

## AP-02 — The ecosystem is the reasoning boundary

The system must reason across repository, job, workspace, pipeline, and domain boundaries while preserving those boundaries for provenance and responsibility.

A cross-repository dependency is not an edge case; it is a core use case.

## AP-03 — Time and history are first-class

The system must eventually support point-in-time questions such as:

- What did this asset look like before the degradation?
- What lineage/topology existed when the affected run occurred?
- What deployment was active then?
- Which Expectations and Baselines applied then?
- When did the first abnormal Observation/Assessment appear?
- Has the issue happened before?

Current-state-only architecture would violate the product thesis.

## AP-04 — Evidence is preserved separately from interpretation

Normative Expectations, descriptive Baselines, observed facts, derived Assessments, hypotheses, attributions, and confirmed causes must remain distinguishable.

A business-friendly summary may compress evidence, but it must not erase the evidence chain or silently turn descriptive comparison into normative judgment.

## AP-05 — Provenance is part of every material fact

Responsibility Assignments, classifications, semantic definitions, policy context, lineage relationships, Expectations, quality Observations, Baselines, deployments, and Assessments should retain source and temporal provenance appropriate to their use.

Synchronized metadata must not silently become authoritative merely because it is convenient to query.

## AP-06 — Lineage is typed

The design must distinguish at least:

- data derivation lineage;
- pipeline/operational dependency;
- deployment/code lineage;
- downstream consumption/impact relationships.

These relationships may intersect but should not be collapsed into an ambiguous generic edge.

## AP-07 — Monitoring models degradation, not only failure

A successful job can yield data that violates freshness or quality Expectations. Architecture must therefore support Observations and dimension-specific Assessments independent of execution success/failure.

Baseline deviation alone must not be treated as normative degradation.

## AP-08 — Expectations, Baselines, Observations, and Assessments are separate

What should happen, what comparable reference behavior looks like, what was observed, and what the evidence means are separate states with separate provenance.

This enables Expectations and Baselines to change while historical Observations and Assessments remain reproducible. Typicality must not silently become health, and missing telemetry must not become observed absence.

## AP-09 — Historical comparisons and assessments must be reproducible

Where practical, a historical Assessment should be explainable from the exact Observation evidence, Expectation/Baseline versions, evaluation context, and definitions that applied at the time.

Late or corrected evidence should create traceable reassessment rather than rewriting the earlier conclusion invisibly.

## AP-10 — Security boundaries follow data authority, not monitoring convenience

The framework should not gain or redistribute raw-data access merely because it monitors an asset.

Metadata, aggregates, samples, Baselines, Assessments, and derived explanations must each be treated according to their sensitivity and source authorization.

## AP-11 — Data minimization is a design requirement

Prefer metadata, aggregate metrics, checks, fingerprints, and other minimally necessary evidence over copying row-level sensitive data into the monitoring system.

If later functionality genuinely requires sample values, that must be an explicit security/design decision rather than a default ingestion behavior.

## AP-12 — Governance metadata participates in reasoning

Business semantics, Responsibility Assignments, criticality, Classification, and Policy Context should not be decorative catalog links. They should affect impact analysis, explanations, escalation, and presentation where appropriate without taking ownership of health evidence.

## AP-13 — Policy transparency is not compliance certification

The architecture may present Classifications, Policy Context, applicable Expectations, access evidence, or control status. It must not mechanically transform these into a legal compliance claim.

## AP-14 — Tool integration is replaceable at the concept boundary

Databricks, GitHub/GitHub Actions, Collibra, Immuta, DQX, and Metric Views should be evaluated as providers or realizations of product concepts.

An optional integration must not become an implicit required dependency unless that decision is deliberate and documented.

## AP-15 — Databricks-native capabilities are favored, not worshipped

When Databricks-native capabilities meet the accepted product concept cleanly, prefer them over unnecessary duplication. When they do not, preserve the concept and add only the missing functionality.

## AP-16 — Question answering is a view over evidence

The conversational/question-answering experience must not become an independent knowledge source. Answers should be grounded in authorized evidence, semantics, historical context, and explicit Assessment basis.

## AP-17 — Unknown is a valid result

The architecture must support incomplete, insufficient, non-comparable, conflicting, unavailable, or unauthorized evidence/reference context without inventing certainty.

## AP-18 — Human intervention has explicit semantics

If a person establishes/revises an Expectation, records a bounded exception, marks a Baseline non-comparable, confirms a later causal claim, or annotates an incident, that action must remain distinguishable from machine-derived Observations.

## AP-19 — Business and engineering views share the same underlying state

Do not create separate truth stores for executive/business reporting and engineering analysis. Different projections may expose different authorized detail, but they must derive from the same evidence and Assessment basis.

## AP-20 — The product remains useful with optional systems absent

The core product should be able to function without Collibra or Immuta. Their presence may enrich authoritative semantics/policy information, but absence should degrade enrichment rather than invalidate the whole system.
