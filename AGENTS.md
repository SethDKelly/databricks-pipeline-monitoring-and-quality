# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; NEXT DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A and DPTN-B are complete/accepted. DPTN-C is NEXT / READY / NOT STARTED and requires explicit human selection before any canonical promotion occurs. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership remains selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`; `docs/canonical/` remains the current semantic root. DPTN-B relocated history only. `docs/history/` is provenance-only and cannot compete with current ownership.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. DPTN-B acceptance authorizes no autonomous continuation. DPTN-C canonical promotion, DPTN-D decomposition, later routing convergence/rebinding and product implementation all require their own explicit human-selected task.

## Canonical routing before DPTN-C starts

Use `human task → current canonical owner → exact IDs/tests as needed`. For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the current canonical `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the current canonical owner. `docs/history/`, cleared first-class paths, the DPTN move map, OKF, search order, recency, Git history, vendor guidance and model/tool memory never establish semantic authority.

## DPTN-B accepted boundary

- MOVE-001 through MOVE-006 are complete and preserved by exact-tree relocation under `docs/history/`;
- `docs/concepts/`, `docs/reference/` and `docs/decisions/` are vacant/unassigned, not current owners;
- `docs/canonical/` remains current;
- mixed ADF/CKR directories remain in place for DPTN-D;
- permanent historical-reference/agent rebinding remains later DPTN work;
- Implementation 001-A remains blocked.

Completed CKR provenance checks may use the validation-only ephemeral history compatibility projection. That projection leaves no repository path behind and cannot satisfy current lookup.

## CKR exit boundary

The ownership-inventory lifecycle remains `ckr_complete`. CKR acceptance proves documentation authority/routing/provenance closure only; it is not product implementation, source-integration, deployment or production evidence.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN topology-normalization blocker. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
