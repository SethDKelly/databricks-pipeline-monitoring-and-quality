# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

CKR-A–K are complete/accepted. The Canonical Knowledge Repository retrofit has exited successfully. DPTN-A is now the active pre-implementation documentation-topology task. Implementation 001-A is **BLOCKED ON DPTN EXIT**; DPTN itself is not product implementation.

Current semantic ownership remains selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. All accepted semantic families through ARCH remain canonicalized under the existing CKR paths during DPTN-A; Phase 001–010 sources remain provenance for migrated meanings.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. CKR exit removed the documentation-authority blocker, but DPTN now intentionally interposes a bounded physical-topology normalization before product implementation. DPTN-A authorizes inventory/planning only: no existing documentation path move/rename/delete, semantic rewrite, stable-ID change, architecture change, or product implementation.

## Canonical routing

Use `human task → current canonical owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain the deterministic canonical locator `owner_path::ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the canonical owner. OKF, DPTN planning metadata, the resolver, search order, recency, Git history, vendor guidance and model/tool memory never establish semantic authority.

Do not preload the full stable-ID corpus or OKF bundle.

## CKR / DPTN boundary

The CKR ownership-inventory lifecycle remains `ckr_complete`. CKR acceptance proves documentation authority/routing/provenance closure only. DPTN changes physical topology and routing paths only; it cannot change accepted meaning merely by moving a file.

During DPTN-A the existing CKR/current paths remain authoritative and physically unchanged. Later DPTN groups may relocate them only through the accepted collision-safe move map and validated cutovers.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is DPTN-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
