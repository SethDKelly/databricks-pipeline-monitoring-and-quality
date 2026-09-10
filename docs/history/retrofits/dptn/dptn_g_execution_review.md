# DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review

**Status:** ACCEPTED — DPTN EXIT ACCEPTED

## Decision

DPTN-G is accepted as the final Documentation Physical Topology Normalization phase. MOVE-020 is authorized and completed by archiving DPTN execution/provenance, retiring temporary compatibility/migration paths, replacing phase-specific live topology validation with one durable final-topology guard, and releasing Implementation 001-A from the topology blocker to **NEXT / READY / NOT STARTED**.

DPTN exit does **not** start implementation. Product implementation still requires a separate explicit human-selected task.

## Whole-program result

DPTN-A–G normalized documentation lifecycle and routing without changing accepted DMTZ semantics:

- historical design/provenance resides under `docs/history/`;
- current semantic authority resides at first-class `docs/<family>/` owner roots selected by the CKR ownership inventory;
- `docs/index.md` is the single authored repository-native discovery root;
- top-level `knowledge/` is deterministic generated OKF v0.2 compatibility only;
- current stable-ID resolution returns one first-class current `owner_path::ID`, with history explicitly requested through `--history`;
- durable ADF/CKR operating mechanics remain current while completed program evidence is historical;
- current agent/rule/link routing no longer depends on historical Phase paths or retired compatibility namespaces;
- the completed DPTN program and its phase-specific validator tooling are preserved as provenance under `docs/history/retrofits/dptn/`.

## MOVE-020 retirement

DPTN-G retires the migration scaffolding rather than allowing it to become a permanent second documentation framework:

1. the finalized DPTN program tree moves from the live normalization namespace to `docs/history/retrofits/dptn/`;
2. the final compatibility README from the legacy canonical namespace is preserved at `docs/history/routing/canonical-compatibility-pre-dptn-g/README.md`;
3. the live legacy canonical compatibility namespace is removed;
4. phase-specific DPTN A–F validators/guards plus the DPTN progression-status validator move to `docs/history/retrofits/dptn/tooling/`;
5. active conformance retains only `validate_documentation_topology.py` and `test_documentation_topology_guards.py` for durable post-exit topology invariants.

Completed CKR checks may still reconstruct accepted-era paths ephemerally through `run_ckr_with_history_compat.py`. That temporary test projection never recreates a current authority path.

## Conservation audit

The eight substantive semantic-owner tree identities remain exactly the DPTN-F baseline:

- `docs/architecture` — `0f1564882f1c8d142c0eb4e5d77eb9ab56e43415`;
- `docs/authority` — `c3f7a1436294dff05729d81edbabcbac180833f5`;
- `docs/concepts` — `67d418f9d71ca9c64169c813853da514a37166ad`;
- `docs/contracts` — `b01663426ff83a79e09a0a05a218638587f86905`;
- `docs/experience` — `6e7b89390426ba651c2735baf6d441fc39dafd9c`;
- `docs/invariants` — `3e2f3ac5f6b201200fd6bce9cb9cbba92243c8ed`;
- `docs/policies` — `4acc2b064198d0a3725d4ff4bdda30e2cb139dff`;
- `docs/reference` — `6a3a361d1275f23c601710ba62089f790ae9f3f8`.

The accepted catalog remains **24 concepts and 1,237 stable IDs across eight families**, including **ARCH-001–ARCH-500**. No new semantic ID, architecture contract, implementation behavior or product capability is introduced.

The generated OKF tree intentionally changes from its DPTN-E/F identity only because the generated `documentation-topology` project route now points to permanent `docs/index.md` instead of the retired live DPTN namespace. Its pre-retirement post-route-update tree identity is recorded in the exit manifest as `01e2a153191fb258b3823377332ef6bdd0f1f4d9`.

## Residual obligations

DPTN does not close unrelated deferred evidence:

- ADF-EX-17 / ADF-G-XT01 provider-runtime verification remains deferred;
- Databricks target/runtime capability remains deployment evidence, not documentation topology;
- product implementation evidence does not exist merely because implementation is now eligible to begin.

## Implementation handoff

**Implementation 001-A — NEXT / READY / NOT STARTED.**

The topology blocker is removed. The human must explicitly select Implementation 001-A before implementation work begins. DPTN-G does not authorize automatic continuation.

## Verification boundary

The DPTN-G acceptance contract includes the final-topology validator, 24 DPTNG scenarios, 12 durable topology negative controls, retained historical phase fixtures/tooling, semantic-tree identity conservation, deterministic generated-routing validation, and current routing/status rebinding.

An accepted DPTN exit is documentation-topology acceptance only. It does not fabricate provider-runtime proof, product tests, Databricks workspace support or production readiness.
