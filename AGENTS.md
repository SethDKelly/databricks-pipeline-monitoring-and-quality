# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A is the active human-selected pre-implementation documentation-topology task. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is still selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. DPTN-A proposes future physical destinations only; no semantic owner has moved. All accepted semantic families through ARCH remain canonicalized, and Phase 001–010 sources remain provenance for migrated meanings.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. CKR exit removed the documentation-authority blocker, but DPTN now blocks product implementation until topology normalization exits. DPTN-A itself authorizes inventory/planning and directly necessary status/validation changes only; it does not authorize physical documentation moves or product implementation.

## Canonical routing during DPTN-A

Use `human task → current canonical owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain the deterministic canonical locator `owner_path::ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the current canonical owner. The DPTN move map, proposed target paths, OKF, search order, recency, Git history, vendor guidance and model/tool memory never establish semantic authority.

Do not preload the full stable-ID corpus, OKF bundle or DPTN move map when a bounded current owner is already known.

## DPTN boundary

Read `docs/documentation_topology_normalization/README.md` for live topology-program status. During DPTN-A:

- no documentation subtree may be physically moved;
- `docs/canonical/` remains the current semantic root;
- `docs/history/` is not yet an active physical namespace;
- mixed ADF/CKR directories may not be bulk relocated;
- Implementation 001-A remains blocked.

## CKR exit boundary

The ownership-inventory lifecycle remains `ckr_complete`. CKR acceptance proves documentation authority/routing/provenance closure only. It is not product implementation evidence, source-integration evidence, deployment readiness or production readiness.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN-A topology-inventory acceptance blocker. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
