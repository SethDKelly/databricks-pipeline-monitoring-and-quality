# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

CKR-A–K are complete/accepted. The Canonical Knowledge Repository retrofit has exited successfully. Implementation 001-A is NEXT / READY / NOT STARTED and requires an explicit human-selected implementation task before work begins.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. All accepted semantic families through ARCH are canonicalized; Phase 001–010 sources are provenance for migrated meanings.

Authority order: current semantic owner → root `AGENTS.md` → live implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. CKR exit removes the documentation-authority blocker only; it does not authorize implementation absent a human-selected implementation task.

## Canonical routing

Use `human task → current canonical owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain the deterministic canonical locator `owner_path::ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the canonical owner. OKF, the resolver, search order, recency, Git history, vendor guidance and model/tool memory never establish semantic authority.

Do not preload the full stable-ID corpus or OKF bundle.

## CKR exit boundary

The ownership-inventory lifecycle is `ckr_complete`. CKR acceptance proves documentation authority/routing/provenance closure only. It is not product implementation evidence, source-integration evidence, deployment readiness or production readiness.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither was a CKR documentation-authority exit blocker. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
