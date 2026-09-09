# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; IN EXECUTION DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A and DPTN-B are complete/accepted. DPTN-C is IN EXECUTION by explicit human selection. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. During the DPTN-C cutover, only an atomic ownership-ledger + physical-tree promotion may change a current owner path. `docs/history/` remains provenance-only and cannot compete with current ownership.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. The user explicitly selected DPTN-C. That authorizes MOVE-007 through MOVE-014 and directly necessary ownership/resolver/validation compatibility work only. It does not authorize DPTN-D decomposition, DPTN-E routing convergence, full DPTN-F rebinding/retirement, or product implementation.

## Canonical routing during DPTN-C

Use `human task → current ownership ledger → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work. Historical occurrences and legacy compatibility redirects never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may still route through one bounded domain concept. Until DPTN-F completes broad route rebinding, legacy canonical paths may exist only as explicitly non-authoritative compatibility redirects. The ownership ledger—not redirect presence, path name, search rank, OKF, recency, Git history, vendor guidance or model/tool memory—selects current authority.

## DPTN-C boundary

DPTN-C may promote exactly these current semantic trees by path-only atomic cutover:

- `docs/canonical/concepts` → `docs/concepts`;
- `docs/canonical/architecture` → `docs/architecture`;
- `docs/canonical/authority` → `docs/authority`;
- `docs/canonical/contracts` → `docs/contracts`;
- `docs/canonical/experience` → `docs/experience`;
- `docs/canonical/invariants` → `docs/invariants`;
- `docs/canonical/policies` → `docs/policies`;
- `docs/canonical/reference` → `docs/reference`.

The CKR ownership inventory must rebind current `target_owner` / stable-family target paths in the same cutover. `docs/canonical/README.md` remains only as an orientation/compatibility surface pending DPTN-E. Redirects beneath `docs/canonical/`, if present, are non-owner compatibility routes pending DPTN-F/G.

No semantic content, stable-ID meaning, concept count, accepted range, architecture contract or implementation state may change.

## DPTN-B accepted boundary

MOVE-001 through MOVE-006 remain preserved as exact-tree historical relocations under `docs/history/`. The old historical first-class roots remain history-only/non-authoritative after any DPTN-C reuse of `docs/concepts` or `docs/reference`.

Completed CKR provenance checks may use validation-only compatibility projection. It leaves no persistent authority behind and cannot satisfy current lookup.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither is a DPTN topology-normalization blocker. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
