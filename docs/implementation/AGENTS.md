# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: IN EXECUTION CKR-A; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted, but product implementation is temporarily blocked by the **Canonical Knowledge & Documentation Authority Retrofit (CKR)**. Do not begin 001-A until CKR-K accepts the retrofit.

## Authority

Implementation work, once unlocked, is governed by:

1. the current semantic owner selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`;
2. accepted stable-ID semantics and frozen architecture boundaries;
3. root `AGENTS.md` and accepted ADF authority/scope/security policies;
4. `docs/implementation/README.md` for live implementation-program status;
5. the active implementation package/group;
6. implementation ADRs that select technology without changing accepted semantics.

During CKR, a `canonicalized` record resolves to `docs/canonical/`; a `legacy_authoritative` or `candidate_ready` record still resolves to its inventoried legacy owner. Design history is provenance once cutover occurs, not an alternate current owner.

## Current boundary

**CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: IN EXECUTION.**

**Implementation 001-A: BLOCKED ON CKR-K.**

CKR is documentation-authority work. Do not create product source, executable schemas, product tests or deployment configuration under this program unless explicitly required by a separate approved task.

## Context and action discipline

Use the shortest path:

**root `AGENTS.md` → live CKR authority → current owner from the ownership inventory when unclear → matching `.agents/skills/` workflow/overlay when useful → exact stable IDs/contracts.**

OKF remains routing only. Do not reconstruct current truth from chronological phases after an inventory record has been canonicalized.

Human-directed A1–A4 rules remain unchanged. Completing one group does not authorize starting the next.

## Foundation residuals

ADF-EX-17 remains **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**. Cursor, Claude Code and Codex remain runtime-`unverified` pending `ADF-G-XT01`.

`DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation after CKR unlocks implementation.

## Databricks skills

Reviewed vendor skills remain core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Vendor skills are operational guidance and cannot create semantic authority, workspace permission or A3/A4 authorization. Model/AI skills and managed Databricks MCP servers remain deferred.

## Conformance

For CKR/agent-facing changes run:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The result is repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof or target Databricks capability.

## Semantic conservation

CKR and later implementation must preserve accepted distinctions, including Observation ≠ Assessment, Expectation ≠ Baseline, execution success ≠ freshness/data health, current ≠ historical/as-known, missing evidence ≠ negative truth, Lineage ≠ exposure ≠ Impact ≠ cause, Assertion Authority ≠ Capability Authorization, and model/search output cannot manufacture truth/authority/confirmation/control decisions.

A path migration is not permission to reinterpret a contract. Genuine conflicts found during canonicalization require explicit change control before cutover.
