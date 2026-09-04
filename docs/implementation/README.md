# DMTZ Implementation Program

**Status:** BLOCKED — CKR-A COMPLETE; CKR-B IN EXECUTION

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Authority and current gate

This directory owns implementation-program progression. Product implementation remains blocked while the **Canonical Knowledge & Documentation Authority Retrofit (CKR)** moves current documentation authority out of chronology-first phase ownership before code/test traceability begins.

The accepted ADF exit remains valid and is not reopened by CKR.

Current required work:

- **CKR-A — COMPLETE / ACCEPTED**;
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: IN EXECUTION**;
- **Implementation 001-A — NOT ACTIVE / BLOCKED until CKR-K exit acceptance**.

CKR-B currently has nine `candidate_ready` foundation/glossary records. Until atomic cutover, their inventoried legacy owners remain current authority.

Use:

- `../canonical_knowledge_retrofit/README.md` — live CKR progression;
- `../canonical_knowledge_retrofit/canonical_ownership_inventory.json` — current semantic ownership;
- `../canonical_knowledge_retrofit/ckr_b_semantic_conservation_matrix.md` — CKR-B comparison/evidence;
- `../canonical/README.md` — target/current canonical namespace;
- `../design_history/README.md` — provenance/history role;
- root `AGENTS.md` — shared behavior/authority instructions.

## Documentation authority during CKR

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current truth;
- `canonicalized` → inventoried `docs/canonical/` target is sole current owner;
- `history_only` → provenance/rationale only.

Do not reconstruct a canonicalized current rule from design chronology. Conversely, do not promote a candidate before accepted cutover.

Accepted stable-ID ranges remain unchanged: SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270, ARCH-001–500.

## ADF / Databricks residuals

ADF-EX-17 remains **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**; `ADF-G-XT01` remains open and Cursor/Claude Code/Codex remain runtime-`unverified`.

The accepted Databricks vendor set remains core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. `DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation after CKR unlocks implementation. Model/AI skills and managed Databricks MCP servers remain deferred.

## Implementation sequence

1. 001 — Executable Foundations & Walking Skeleton
2. 002 — Identity, Scope, Authority & Authorization Runtime
3. 003 — Source Acquisition, Capability & Evidence Reliability
4. 004 — Runtime Provenance, Health, Quality, Change & Lineage
5. 005 — Investigation, Impact Reasoning & Historical Replay
6. 006 — Serving, Explanation, Basis Inspection & UX
7. 007 — Operationalization, Security, Resilience, SLO & Cost
8. 008 — MVP Pilot Validation & Release Candidate
9. 009 — Enterprise Expansion, Scale & Optional Integrations
10. 010 — Active Control & Enterprise Control Plane — conditional
11. 011 — Production Graduation & Operational Acceptance

Completion profiles remain unchanged: MVP 001–008; enterprise passive monitoring 001–009 + 011; full active-control enterprise 001–011.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof, target Databricks capability or production readiness.
