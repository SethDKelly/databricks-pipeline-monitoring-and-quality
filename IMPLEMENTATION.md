# DMTZ Implementation — Start Here

Phase 010, the Agentic Development Foundation, its execution exit, and the Databricks Agent Skills Integration Addendum are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; NEXT CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

A later **Canonical Knowledge & Documentation Authority Retrofit (CKR)** now blocks product implementation until CKR-K. CKR-A established the authority/migration model; CKR-B is next/ready. The accepted ADF exit is not reopened.

## Start here

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR progression.
2. `docs/canonical_knowledge_retrofit/authority_model.md` — current knowledge vs design history.
3. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — record-specific current ownership.
4. `docs/canonical/README.md` — target current-truth namespace.
5. `docs/design_history/README.md` — provenance/history layer.
6. `docs/implementation/README.md` — blocked implementation authority.
7. `AGENTS.md` — shared repository instructions.
8. `knowledge/index.md` — optional routing only.

## Current semantic ownership

- `legacy_authoritative` / `candidate_ready` → use the inventoried legacy owner;
- `canonicalized` → use the inventoried `docs/canonical/` target;
- `history_only` → provenance/rationale only.

Do not use phase chronology, search order, OKF summaries or mere canonical-path presence to manufacture authority. CKR owner-path changes must preserve accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meaning unless a separate A4 change is explicitly accepted.

## Current work

**CKR-A — COMPLETE / ACCEPTED.**

**CKR-B — Foundation, Terminology & Cross-Cutting Invariants: NEXT / READY.**

**Implementation 001-A — BLOCKED until CKR-K exit acceptance.**

`ADF-G-XT01` remains open provider-runtime verification debt. `DBX-SKILL-RUN-01` remains a future 001-A environment obligation after CKR unlocks implementation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS describes repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof, target Databricks capability or production readiness.

## Boundaries

- no autonomous task selection or group continuation;
- no product implementation during CKR;
- reviewed Databricks skills remain operational guidance, not DMTZ authority;
- model/AI skills and managed Databricks MCP servers remain deferred;
- design history is retained rather than rewritten to look like current truth;
- genuine semantic conflicts discovered during canonicalization require explicit change control.
