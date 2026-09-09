# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-E; NEXT DPTN-F; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A through DPTN-E are complete/accepted. DPTN-F is NEXT / READY / NOT STARTED and requires explicit human selection. Implementation 001-A remains NOT STARTED and may not begin until DPTN-G accepts the normalization exit and a subsequent human-selected implementation task authorizes work.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. The ownership ledger selects the current **canonical owner** for every semantic question and stable ID; history, redirects and generated OKF never become canonical owners.

Authority order: current semantic owner → root `AGENTS.md` → live DPTN/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. DPTN-E acceptance authorizes no autonomous continuation. DPTN-F rebinding, DPTN-G exit work, and product implementation each require their own explicit human-selected task.

## Discovery and exact routing after DPTN-E

For unknown-location discovery, begin at `docs/index.md`. Top-level `knowledge/` is generated OKF v0.2 compatibility output and must not be hand-edited or treated as semantic authority.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work.

Current semantic owners remain first-class `docs/<family>/` paths. Completed CKR evidence is under `docs/history/retrofits/ckr/`, completed ADF evidence under `docs/history/foundations/adf/`, and the pre-DPTN-E authored OKF tree under `docs/history/routing/okf-pre-dptn-e/`; all are history only.

## DPTN-E accepted boundary

DPTN-E completed MOVE-017 and MOVE-018 without semantic rewrite:

- `docs/index.md` is the single authored discovery root;
- `docs/README.md` remains design-phase progression authority;
- top-level `knowledge/` is generated from `docs/routing/okf_projection.json` plus repository-owned catalogs;
- pre-DPTN-E authored `knowledge/` is preserved exactly in history;
- `docs/canonical/README.md` is compatibility/orientation only;
- broad stable-reference, agent/rule/link rebinding remains DPTN-F.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search/generated routing output ≠ truth or authority; Gate ≠ Safeguard.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
