# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-H; IN EXECUTION CKR-I; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-A–H are complete/accepted. CKR-I is in execution/cutover validation. Product implementation remains blocked until CKR-K.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`: `canonicalized` → inventoried `docs/canonical/` owner; `legacy_authoritative` / `candidate_ready` → inventoried legacy owner; `history_only` → provenance/rationale only.

Foundation/glossary, all 24 concepts, SYN-001–035, authority vocabulary, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 are canonicalized. Phase 001–010 sources are provenance for migrated meanings. The frozen reference architecture resolves to `docs/canonical/architecture/reference-architecture.md`.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 bounded change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit authorization; A4 semantic/architecture change requires explicit change control. CKR-I migration preserves accepted Phase 010 architecture; it does not authorize CKR-J or product implementation.

## Context and semantic conservation

Use `human task → live CKR authority → ownership inventory when unclear → current owner → exact IDs/tests as needed`. `knowledge/index.md` is optional routing only; search order, recency, path presence, vendor guidance, tool memory or synchronization order never establish authority.

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; copied evidence ≠ independent corroboration; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; Monitoring Scope ≠ accessibility ≠ authorization ≠ successful observation; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output existence ≠ currentness/freshness ≠ health; Lineage/reachability ≠ encounter/consumption ≠ exposure; exposure ≠ effect ≠ consequence ≠ causal attribution; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; graph/search/vector/model output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained actual communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery; cache/SLO/cost convenience cannot strengthen truth or weaken evidence/control obligations.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
