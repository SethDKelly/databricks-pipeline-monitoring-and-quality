# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-F; NEXT DPTN-G; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A through DPTN-F are complete/accepted. DPTN-G is NEXT / READY / NOT STARTED and requires explicit human selection. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. The ownership ledger selects the current owner for every semantic question and stable ID; `docs/history/`, generated OKF and compatibility redirects never become semantic owners.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. DPTN-F acceptance authorizes no autonomous continuation. DPTN-G exit work and product implementation each require their own explicit human-selected task.

## Current routing after DPTN-F

Use `human task → docs/index.md when location is unknown → current ownership ledger/current owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work. Historical occurrences, generated OKF and compatibility redirects never compete with current ownership.

`knowledge/index.md` is generated OKF v0.2 compatibility only. Repository-native agents/tools should use `docs/index.md` for unknown-location discovery unless a generic OKF interface is specifically required.

## DPTN-F accepted boundary

MOVE-019 rebound current stable-reference, agent/rule/link and drift-analysis consumers to the normalized topology:

- durable CKR routing mechanics name first-class `docs/<family>/` owners and `docs/history/` provenance;
- canonical workflows use `docs/index.md` for repository-native discovery;
- scoped Cursor rules route to first-class current semantic owners and current implementation packages rather than Phase 010/pre-DPTN paths;
- current link validation requires real current targets and does not substitute history;
- generated-OKF impact analysis derives current body-link scope from the CKR ownership inventory;
- completed CKR checks alone retain a bounded ephemeral accepted-era compatibility projection.

No semantic content, stable-ID meaning, concept count, accepted range, architecture contract or implementation state changed.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN topology blocker.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

DPTN-G owns final conservation audit, legacy-path retirement, migration-scaffolding disposition and exit review. Do not begin it without explicit human selection.
