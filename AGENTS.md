# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR-A and CKR-B are complete/accepted; CKR-C is the next eligible group but is not active until explicitly selected. Product implementation remains blocked until CKR-K.

Current DMTZ semantic ownership is determined record-by-record by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`:

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current;
- `canonicalized` → inventoried `docs/canonical/` target is current;
- `history_only` → provenance/rationale only.

CKR-B canonicalized product definition, actors/stakeholders, foundational terminology, Concept Design method, AP-01–AP-32, SP-01–SP-15/security-governance, ecosystem lifecycles, MVP boundary and shared glossary. Their Phase-001/legacy glossary sources are provenance. The 24 concepts and all stable-ID families remain with their later-group current owners.

Authority order: current semantic owner → this `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Current-truth vs history

For a `canonicalized` record, answer current questions from its canonical owner. Use phase/decision/scenario/exit records for provenance, rationale, historical comparison or explicit semantic-change review. Search order, recency, OKF summaries, canonical-path presence and tool memory do not establish authority.

CKR migration follows `docs/canonical_knowledge_retrofit/authority_model.md` and `migration_contract.md`. Genuine semantic conflicts require A4 adjudication.

## Human-directed action classes

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 in-scope change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit task authorization; A4 semantic/architecture change requires explicit change control.

Completing one group does not authorize the next. Do not autonomously select backlog work, delegate repository implementation, merge/deploy unattended, or reopen architecture.

## Context and references

Use the shortest path:

`human task → live CKR/implementation authority → known current owner/path/ID; otherwise ownership inventory or one OKF route → current semantic owner → exact IDs/tests as needed`.

Do not preload phases/contracts/knowledge/vendor skills/history. `knowledge/` is routing only.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500. Their owner paths change only through their assigned CKR groups.

## Semantic conservation

Preserve at minimum Observation ≠ Assessment; Expectation ≠ Baseline; execution success ≠ freshness/data quality; missing evidence ≠ negative truth; current ≠ historical/as-known; later evidence ≠ evidence known then; Lineage ≠ exposure ≠ Impact ≠ cause; authentication ≠ Capability Authorization ≠ Assertion Authority; current disclosure ≠ historical authorization/truth; passive monitoring ≠ active Gate; Gate readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; and model/search output cannot manufacture truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions.

## Residuals / conformance

ADF-EX-17 and `ADF-G-XT01` remain deferred runtime-verification debt. Cursor/Claude/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof, Databricks capability or production readiness.
