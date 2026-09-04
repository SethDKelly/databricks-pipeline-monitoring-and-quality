# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR-B has completed its nine-record foundation/glossary authority cutover and is awaiting closure validation. Product implementation remains blocked until CKR-K.

Current DMTZ semantic ownership is determined record-by-record by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`:

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current;
- `canonicalized` → inventoried `docs/canonical/` target is current;
- `history_only` → provenance/rationale only.

The CKR-B product/foundation/glossary records are now `canonicalized`. Their Phase-001/legacy glossary sources are provenance, not alternate current owners. All 24 concepts and all stable-ID families remain with their later-group legacy owners.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## CKR-B boundary

CKR-B owns only the nine foundation/glossary records listed in the CKR README. Its cutover may improve locality/wording and remove obsolete future-phase language from current resources; it may not absorb CKR-C–I semantics or create product implementation.

Current foundation lookup now begins under:

- `docs/canonical/reference/`;
- `docs/canonical/invariants/architectural-principles.md`;
- `docs/canonical/policies/`.

Use `docs/foundation/` and the old glossary for provenance/history, not routine current truth.

## Human-directed action classes

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 in-scope change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit task authorization; A4 semantic/architecture change requires explicit change control.

Completing one group does not authorize the next. Do not autonomously select backlog work, delegate repository implementation, merge/deploy unattended, or reopen architecture.

## Context and references

Use the shortest path:

`human task → live CKR/implementation authority → known current owner/path/ID; otherwise ownership inventory or one OKF route → current semantic owner → exact IDs/tests as needed`.

Do not preload phases/contracts/knowledge/vendor skills/history. `knowledge/` is routing only.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500. Their owner paths do not change until their assigned CKR groups.

## Semantic conservation

Preserve at minimum Observation ≠ Assessment; Expectation ≠ Baseline; execution success ≠ freshness/data quality; missing evidence ≠ negative truth; current ≠ historical/as-known; later evidence ≠ evidence known then; Lineage ≠ exposure ≠ Impact ≠ cause; authentication ≠ Capability Authorization ≠ Assertion Authority; current disclosure ≠ historical authorization/truth; passive monitoring ≠ active Gate; Gate readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; and model/search output cannot manufacture truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions.

Genuine contradictions discovered in migration require A4 adjudication.

## Residuals / conformance

ADF-EX-17 and `ADF-G-XT01` remain deferred runtime-verification debt. Cursor/Claude/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof, Databricks capability or production readiness.
