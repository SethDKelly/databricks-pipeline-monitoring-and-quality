# Phase 009 Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence

**Status:** Next — not started

## Goal

Map concrete source evidence for Change Intent, repository/configuration revision, Deployment association/attempt/activation, Execution History, run lifecycle, dependency sequence, retries/reruns/backfills and run-specific implementation/input/output versions.

## Group 02 entry contract

Group 03 may consume accepted source-local identities and explicit cross-system crosswalks from Group 02, including repository identity, Unity Catalog object identity, principal provenance, bounded governance authority, current authorization/disclosure limits and known historical-retention gaps.

Those facts do **not** establish operational association. Repository path/name, CODEOWNERS, Unity Catalog ownership, Collibra responsibility, active Deployment names or timestamp proximity cannot prove which repository revision was deployed or which implementation/input/output version a run actually used.

## Primary questions

- What Git/GitHub evidence identifies proposed/approved/merged Change Intent and exact revision?
- What GitHub Actions evidence establishes workflow/deployment attempt and outcome, and what does it not establish about Databricks activation?
- What Databricks runtime/job/workflow evidence establishes actual execution opportunity, run/attempt lifecycle and execution identity?
- Which explicit identifiers can join repository revision → deployment → activated target → run-specific implementation state?
- How are input/output dataset/table/version identifiers established for a run rather than inferred from latest state?
- Which sources support actual precedence, waiting or dependency evidence versus configured dependency only?
- How are retry, restart, rerun and backfill semantics represented by each source?
- What lifecycle/history is retained, how late can evidence arrive, and what clock uncertainty exists?
- What evidence is required for strong no-run/no-output/no-consumption conclusions?

## External-fact requirement

Verify current GitHub/GitHub Actions and Databricks Jobs/Workflows/runtime/system-table documentation for every material source surface. Record edition/feature/permission/retention constraints and distinguish documented guarantees from environment-specific configuration.

## Boundary

Temporal/name similarity is not a cross-system join. Git revision, workflow success, Deployment activation, execution occurrence and realized Change remain separate.

## Handoff

Group 04 uses run/version/runtime binding to evaluate measurement, schema, quality and health evidence accurately.