# DPTN-F — Stable References, Agent Routing & Drift Rebinding — Execution Review

**Status:** ACCEPTED — DPTN-F COMPLETE

## Decision

DPTN-F is accepted as the MOVE-019 in-place routing cutover. DPTN-A–E remain accepted; DPTN-G is the next dependency-safe phase. Implementation 001-A remains BLOCKED / NOT STARTED until DPTN-G exit acceptance and a subsequent explicit human-selected implementation task.

## Accepted result

DPTN-F rebinds current repository-native agent, stable-reference, validator and scoped-rule consumers to the normalized topology established by DPTN-C–E:

- `docs/index.md` is the primary repository-native discovery root;
- generated `knowledge/index.md` remains explicit OKF v0.2 compatibility only;
- exact stable-ID lookup remains deterministic `owner_path::STABLE-ID` against CKR-inventoried current owners;
- `--history` remains separate provenance discovery;
- scoped Cursor rules point to first-class current semantic owners and current implementation packages instead of Phase 010/pre-DPTN routing;
- current link validation requires physical current targets and no longer falls back to DPTN-D-retired history paths;
- routing-impact analysis follows the CKR inventory's `canonical_owner_roots` rather than legacy `docs/canonical/` compatibility paths;
- completed CKR validators retain their dedicated ephemeral accepted-era compatibility projection, which is historical test reproducibility rather than current routing.

## Conservation

No substantive semantic owner tree changed. The accepted DPTN-E tree identities remain:

- `docs/architecture` — `0f1564882f1c8d142c0eb4e5d77eb9ab56e43415`;
- `docs/authority` — `c3f7a1436294dff05729d81edbabcbac180833f5`;
- `docs/concepts` — `67d418f9d71ca9c64169c813853da514a37166ad`;
- `docs/contracts` — `b01663426ff83a79e09a0a05a218638587f86905`;
- `docs/experience` — `6e7b89390426ba651c2735baf6d441fc39dafd9c`;
- `docs/invariants` — `3e2f3ac5f6b201200fd6bce9cb9cbba92243c8ed`;
- `docs/policies` — `4acc2b064198d0a3725d4ff4bdda30e2cb139dff`;
- `docs/reference` — `6a3a361d1275f23c601710ba62089f790ae9f3f8`.

The generated DPTN-E OKF tree remains `8a8ac74f7eb5afcd7245043501103b0b691101f6`. The catalog remains 24 concepts and 1,237 stable IDs across eight families, including ARCH-001–ARCH-500.

## Collision closure

- **COL-009 — RESOLVED BY DPTN-F.** Current stable-ID and cross-surface consumers use first-class owner paths and deterministic current resolution.
- **COL-011 — RESOLVED BY DPTN-F.** Agent, adapter, rule and routing consumers are rebound after physical topology stabilization.
- **COL-012 — REMAINS ACTIVE.** Implementation 001-A remains blocked through DPTN-G exit.

DPTN-F does not execute MOVE-020 and does not retire the physical `docs/canonical/<family>` compatibility redirects or DPTN migration scaffolding. Those are DPTN-G responsibilities.

## Validation contract

Accepted DPTN-F evidence consists of `dptn_f_rebinding_manifest.json`, `fixtures/dptn_f_rebinding_scenarios.yaml`, `scripts/agentic/validate_dptn_f_rebinding.py`, and `scripts/agentic/test_dptn_f_rebinding_guards.py`. The phase adds 24 positive scenarios and 12 negative controls.

This review records repository topology/routing acceptance only. It does not fabricate provider-runtime verification, Databricks deployment capability, product implementation evidence, or production readiness. Where an execution environment cannot run the full repository conformance suite, the absence of an executed PASS must remain explicit rather than being inferred from this acceptance record.

## Handoff

**DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: NEXT / READY / NOT STARTED.**

DPTN-F acceptance does not authorize DPTN-G automatically. Implementation 001-A remains blocked.
