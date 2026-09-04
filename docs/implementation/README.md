# DMTZ Implementation Program

**Status:** BLOCKED — CKR-A COMPLETE; CKR-B CUTOVER COMPLETE / CLOSURE VALIDATION PENDING

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Authority and current gate

This directory owns implementation-program progression. Product implementation remains blocked while CKR completes current-documentation authority migration before code/test traceability begins.

CKR-B has canonicalized its nine foundation/glossary records; group closure validation is still required before CKR-B can be marked complete.

Current required work:

- CKR-A — COMPLETE / ACCEPTED;
- CKR-B — IN EXECUTION / CUTOVER COMPLETE / CLOSURE VALIDATION PENDING;
- Implementation 001-A — NOT ACTIVE / BLOCKED until CKR-K exit acceptance.

Use `../canonical_knowledge_retrofit/README.md`, its ownership inventory, `../canonical/README.md`, and root `AGENTS.md` for current authority.

## Documentation authority

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner;
- `canonicalized` → inventoried `docs/canonical/` target;
- `history_only` → provenance/rationale only.

CKR-B foundation/glossary records are canonicalized. All 24 concepts and stable-ID families remain unchanged for later CKR groups.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals

ADF-EX-17 remains deferred; `ADF-G-XT01` remains open and Cursor/Claude/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Reviewed Databricks vendor skills remain operational guidance; model/AI skills and managed MCP remain deferred.

## Implementation sequence

001 Executable Foundations & Walking Skeleton → 002 Identity/Scope/Authority/Authorization → 003 Acquisition/Evidence Reliability → 004 Runtime/Health/Quality/Change/Lineage → 005 Investigation/Impact/Replay → 006 Serving/Explanation/UX → 007 Operations/Security/SLO/Cost → 008 MVP Pilot → 009 Enterprise Expansion → 010 optional Active Control → 011 Production Graduation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not product/runtime readiness.
