# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN exit: ACCEPTED — Implementation 001-A NEXT / READY / NOT STARTED.**

ADF, CKR and Documentation Physical Topology Normalization (DPTN) have exited successfully. **Implementation 001-A has not started.** It is now the next eligible implementation package and still requires an explicit human-selected implementation task before any implementation work begins.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. The ownership ledger selects the current owner for every semantic question and stable ID; `docs/history/` and generated OKF never become semantic owners.

Authority order: current semantic owner → root `AGENTS.md` → current implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`. Completion of a foundation, retrofit or topology program does not authorize autonomous continuation. Starting Implementation 001-A requires a separate explicit human-selected task.

## Current routing

Use `human task → docs/index.md when location is unknown → current ownership ledger/current owner → exact IDs/tests as needed`.

For a known stable ID, run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::ID`; use `--history` only for explicit provenance/rationale/history work. Historical occurrences and generated OKF never compete with current ownership.

`knowledge/index.md` is generated OKF v0.2 compatibility only. Repository-native agents/tools should use `docs/index.md` for unknown-location discovery unless a generic OKF interface is specifically required.

The completed DPTN record is preserved under `docs/history/retrofits/dptn/` as provenance only. Current routing must use the first-class semantic-owner roots and permanent discovery/implementation surfaces rather than retired compatibility or migration paths.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output/currentness/health; Lineage/reachability ≠ encounter/exposure; exposure ≠ effect ≠ consequence ≠ cause; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; model/graph/search output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Neither was closed by DPTN exit.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Current conformance validates the durable final documentation topology rather than replaying DPTN phase progression. Historical DPTN evidence and phase tooling remain available under the DPTN history archive when provenance is explicitly needed.
