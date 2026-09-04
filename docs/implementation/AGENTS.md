# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; NEXT CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR-A is complete; **CKR-B is next/ready**. Product implementation remains blocked until CKR-K.

## Authority

Use, in order:

1. current semantic owner selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`;
2. accepted stable-ID semantics / frozen architecture;
3. root `AGENTS.md` and ADF authority/scope/security policies;
4. live CKR and implementation status;
5. active implementation package/group after CKR unlock;
6. implementation ADRs that do not change accepted semantics.

`legacy_authoritative` / `candidate_ready` keep the legacy owner current. `canonicalized` uses the `docs/canonical/` target. History is provenance after cutover, not alternate current authority.

## Current boundary

- CKR-A — **COMPLETE / ACCEPTED**;
- CKR-B — **NEXT / READY**;
- Implementation 001-A — **BLOCKED ON CKR-K**.

Do not create product source, schemas, product tests or deployment configuration as CKR work unless a separate explicit task authorizes it.

## Context and actions

Use:

`root AGENTS → live CKR authority → ownership inventory when unclear → current semantic owner → matching skill/overlay → exact IDs/contracts`.

OKF is routing only. Do not reconstruct a canonicalized rule from chronological phases.

A1–A4 remains unchanged. Completing one CKR group does not authorize starting the next.

## Residuals / vendor guidance

ADF-EX-17 remains deferred; `ADF-G-XT01` is open and Cursor/Claude Code/Codex remain runtime-`unverified`.

`DBX-SKILL-RUN-01` remains a future 001-A obligation. Reviewed Databricks skills remain core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect; vendor guidance is never DMTZ semantic/authorization authority.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

A path migration is not permission to reinterpret a contract. Preserve Observation ≠ Assessment, Expectation ≠ Baseline, execution success ≠ freshness/data health, current ≠ historical/as-known, missing evidence ≠ negative truth, Lineage ≠ exposure ≠ Impact ≠ cause, Assertion Authority ≠ Capability Authorization, and deterministic truth/authority/control boundaries.
