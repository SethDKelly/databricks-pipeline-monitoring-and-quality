# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-D; NEXT DPTN-E; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A through DPTN-D are complete/accepted. DPTN-E is NEXT / READY / NOT STARTED and requires explicit human selection. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. The ownership ledger selects the current **canonical owner** for every semantic question and stable ID; `docs/history/` and legacy redirects never become canonical owners.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. DPTN-D acceptance authorizes no autonomous continuation. DPTN-E routing convergence, DPTN-F rebinding/retirement, DPTN-G exit work, and product implementation each require their own explicit human-selected task.

## Canonical routing after DPTN-D

Use `human task → current ownership ledger → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work. Historical occurrences and legacy compatibility redirects never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may still route through one bounded domain concept until DPTN-E resolves the discovery-root topology. DPTN-D moved completed CKR evidence to `docs/history/retrofits/ckr/` and completed ADF program evidence to `docs/history/foundations/adf/`; those history paths are never current policy or semantic authority.

## DPTN-D accepted boundary

DPTN-D completed MOVE-015 and MOVE-016 without semantic rewrite:

- durable CKR ownership/routing mechanics remain in `docs/canonical_knowledge_retrofit/`;
- completed CKR reviews, conservation matrices, manifests and fixtures are preserved under `docs/history/retrofits/ckr/`;
- durable ADF authority/context/workflow/conformance/security/compatibility policy remains in `docs/agentic_development_foundation/`;
- completed ADF phase-design, execution/exit reviews and fixtures are preserved under `docs/history/foundations/adf/`;
- ADF-G-XT01 remains deferred verification and its live procedure/evidence remains current.

No semantic content, stable-ID meaning, concept count, accepted range, architecture contract or implementation state changed.

## DPTN-C accepted boundary

The eight current semantic subtrees live at first-class `docs/<family>/` paths. Legacy `docs/canonical/<family>` paths may remain only as non-authoritative compatibility redirects until DPTN-F/G cleanup.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN topology-normalization blocker.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
