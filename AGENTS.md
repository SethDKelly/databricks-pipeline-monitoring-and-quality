# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A; IN EXECUTION DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A is complete/accepted and DPTN-B is IN EXECUTION by explicit human selection. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is still selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. DPTN-B changes history/provenance paths only; it does not move a current semantic owner. All accepted semantic families through ARCH remain canonicalized.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. The user explicitly selected DPTN-B. That authorizes MOVE-001 through MOVE-006 and directly necessary history-role/routing/validation changes only. It does not authorize DPTN-C canonical promotion, DPTN-D mixed-lifecycle decomposition, later routing convergence/rebinding, or product implementation.

## Canonical routing during DPTN-B

Use `human task → current canonical owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain the deterministic current canonical locator `owner_path::ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the current canonical owner. The accepted DPTN move map, history namespace, proposed target paths, OKF, search order, recency, Git history, vendor guidance and model/tool memory never establish semantic authority.

Do not preload the full stable-ID corpus, OKF bundle or DPTN move map when a bounded current owner is already known.

## DPTN-B boundary

Read `docs/documentation_topology_normalization/README.md` for live topology-program status. During DPTN-B:

- only the six accepted historical relocations MOVE-001 through MOVE-006 may execute;
- `docs/history/` is explicitly provenance-only and non-current;
- `docs/canonical/` remains the current semantic root;
- no canonical ownership target or current stable-ID locator may move;
- mixed ADF/CKR directories remain in place for DPTN-D;
- Implementation 001-A remains blocked.

## CKR exit boundary

The ownership-inventory lifecycle remains `ckr_complete`. CKR acceptance proves documentation authority/routing/provenance closure only. It is not product implementation evidence, source-integration evidence, deployment readiness or production readiness.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN topology-normalization blocker. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
