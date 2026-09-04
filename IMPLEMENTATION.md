# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture, ADF-A through ADF-H, the Databricks Agent Skills Integration Addendum, and the **Agentic Development Foundation Execution Exit Review** are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: IN EXECUTION CKR-A; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

A post-ADF **Canonical Knowledge & Documentation Authority Retrofit (CKR)** is now the active pre-implementation program. It separates current semantic authority from preserved chronological design history before source code/test traceability begins. The ADF exit remains accepted; CKR adds a later implementation-entry dependency.

## Start here

1. [`docs/canonical_knowledge_retrofit/README.md`](docs/canonical_knowledge_retrofit/README.md) — live CKR program/status authority.
2. [`docs/canonical_knowledge_retrofit/authority_model.md`](docs/canonical_knowledge_retrofit/authority_model.md) — canonical knowledge vs design-history authority.
3. [`docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`](docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json) — current owner/migration ledger.
4. [`docs/canonical/README.md`](docs/canonical/README.md) — target current-truth namespace; structural only until record cutover.
5. [`docs/design_history/README.md`](docs/design_history/README.md) — logical provenance/history layer.
6. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program authority and blocked state.
7. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — Implementation 001 package authority.
8. [`docs/agentic_development_foundation/execution_exit_review.md`](docs/agentic_development_foundation/execution_exit_review.md) — accepted foundation exit and residual debt.
9. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
10. [`knowledge/index.md`](knowledge/index.md) — portable discovery when needed; routing only.
11. [`.agents/skills/`](.agents/skills/) — canonical DMTZ workflows and Databricks overlays.
12. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path/platform bridge.

## Documentation authority during CKR

For a semantic record, consult `canonical_ownership_inventory.json` when ownership is unclear:

- `legacy_authoritative` — inventoried legacy owner remains current truth;
- `candidate_ready` — canonical candidate is review-only; legacy owner still wins;
- `canonicalized` — canonical target under `docs/canonical/` is current truth and legacy source becomes provenance/history for that record;
- `history_only` — provenance/rationale only.

There is no accepted dual-current-authority state. CKR changes owner paths and routing without changing accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meaning unless explicit A4 change control separately authorizes a semantic change.

## Foundation exit disposition

The accepted `execution_exit_review.md` remains unchanged:

- ADF-EX-01–ADF-EX-16 — **PASS**;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — **PASS**;
- Databricks Agent Skills Integration Addendum — **ACCEPTED**;
- `ADF-G-XT01` — **OPEN / CARRIED FORWARD**;
- `DBX-SKILL-RUN-01` — **OPEN / FUTURE IMPLEMENTATION 001-A**;
- autonomous development — **DEFERRED / NOT AUTHORIZED**.

Cursor, Claude Code and Codex remain runtime-`unverified`; the waiver is not provider runtime support. Ordinary IDE/CLI development remains supported.

## Current required work

**CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: IN EXECUTION.**

**Implementation 001-A: BLOCKED until CKR-K accepts the documentation authority retrofit.**

`DBX-SKILL-RUN-01` remains owned by 001-A once implementation is unlocked; CKR does not perform or waive it.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This reports repository/agentic/documentation-authority conformance only. It is not DMTZ domain health, data quality, target Databricks capability, provider-runtime certification or production readiness.

## Databricks skill composition

- vendor dependency authority: `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_vendor_skills_profile.json`;
- canonical DMTZ overlays: `.agents/skills/dmtz-databricks-*`;
- local vendor materialization: ignored `.databricks/agent-skills/` through `scripts/agentic/materialize_databricks_skills.py` after implementation unlock;
- reviewed vendor skills: core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect;
- model/AI implementation skills remain deferred;
- automatic vendor-skill expansion is prohibited;
- managed Databricks MCP servers require later explicit security/integration review;
- vendor instructions cannot create workspace permission, semantic authority or A3/A4 authorization.

## Coding-agent boundaries

- skill selection does not create new project scope;
- CKR does not authorize product implementation;
- `ADF-G-XT01` remains future provider-runtime verification debt;
- autonomous task selection, multi-agent implementation delegation, unattended merge/deploy and agent-created backlog work remain out of scope;
- accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH semantics remain authoritative throughout owner-path migration;
- design-scenario PASS, agentic conformance PASS and vendor documentation are not substitutes for executable product/target evidence.
