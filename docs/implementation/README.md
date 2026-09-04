# DMTZ Implementation Program

**Status:** BLOCKED — CKR-A–CKR-B COMPLETE; CKR-C IN EXECUTION

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Authority and current gate

This directory owns implementation-program progression. Product implementation remains blocked while CKR completes current-documentation authority migration before code/test traceability begins.

Current required work:

- CKR-A–B — COMPLETE / ACCEPTED;
- CKR-C — Concept Catalog: IN EXECUTION / CANDIDATE REVIEW;
- Implementation 001-A — NOT ACTIVE / BLOCKED until CKR-K exit acceptance.

CKR-B foundation/glossary records are canonical. CKR-C has candidate targets for the 24 concepts plus SYN-001–SYN-035; Phase 002/003 remain current authority while those records are `candidate_ready`.

Use `../canonical_knowledge_retrofit/README.md`, its ownership inventory, `../canonical/README.md`, and root `AGENTS.md` for current authority.

## Documentation authority

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner;
- `canonicalized` → inventoried `docs/canonical/` target;
- `history_only` → provenance/rationale only.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500. CKR-C may move SYN only; later stable families remain legacy-authoritative.

## Residuals

ADF-EX-17 remains deferred; `ADF-G-XT01` remains open and Cursor/Claude/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Reviewed Databricks vendor skills remain operational guidance.

## Implementation sequence

001 Executable Foundations & Walking Skeleton → 002 Identity/Scope/Authority/Authorization → 003 Acquisition/Evidence Reliability → 004 Runtime/Health/Quality/Change/Lineage → 005 Investigation/Impact/Replay → 006 Serving/Explanation/UX → 007 Operations/Security/SLO/Cost → 008 MVP Pilot → 009 Enterprise Expansion → 010 optional Active Control → 011 Production Graduation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not product/runtime readiness.