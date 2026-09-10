# Agentic / Documentation Authority Conformance Policy

**Status:** ACCEPTED ADF CONFORMANCE — CKR COMPLETE — FINAL DOCUMENTATION TOPOLOGY

## Purpose

Provide one deterministic repository-owned conformance path for the accepted Agentic Development Foundation, completed CKR and normalized documentation topology without turning repository configuration health into DMTZ domain health or provider/runtime certification.

## Canonical command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The command is safe and non-destructive. Fixing failures requires the surrounding human task to authorize A2 changes.

## Current validation order

1. documentation phase consistency;
2. generated OKF v0.2 compatibility validation;
3. Cursor / Claude Code / Codex adapter structure and normalized discovery routing;
4. canonical portable skill structure, including DMTZ Databricks overlays;
5. current agent-facing links and deterministic stable-ID references;
6. live ADF / CKR status drift;
7. CKR ownership-inventory/current semantic-owner validation;
8. CKR-B–K accepted semantic/routing/provenance baselines through bounded accepted-era compatibility where necessary;
9. **durable final documentation-topology validation and negative controls**;
10. ADF/addendum/CKR/DPTN historical fixture-catalog integrity;
11. deterministic context budgets;
12. ADF-G runtime-compatibility evidence integrity;
13. reviewed Databricks Agent Skills dependency/profile/materialization-boundary validation;
14. high-confidence checked-in agentic secret/sensitive-file scan;
15. ADF-H security/trust/lifecycle governance and review-horizon validation;
16. cross-cutting negative controls proving seeded defects are rejected.

This remains separate from future product/runtime tests.

## Current authority and topology checks

The CKR ownership inventory selects the sole current semantic owner for each record and stable-ID family. Current semantic roots are first-class `docs/<family>/` paths. Deterministic exact-ID lookup uses `scripts/agentic/resolve_stable_id.py <ID>` and returns one current `owner_path::ID`; `--history` is separate provenance discovery.

`validate_documentation_topology.py` enforces the durable post-DPTN structure:

- `docs/index.md` is repository-native discovery;
- generated `knowledge/` is OKF compatibility only and matches its generator;
- current semantic-owner roots remain first-class directories selected by the CKR ledger;
- retired compatibility/migration namespaces do not reappear as current paths;
- current agent/rule/implementation routing does not depend on retired paths;
- the completed DPTN program and phase tooling remain preserved under history as provenance only;
- the accepted 24-concept / 1,237-stable-ID / ARCH-001–500 baseline remains intact;
- Implementation 001-A is **NEXT / READY / NOT STARTED**, not implicitly started by DPTN exit.

Phase-specific DPTN validators/guards are historical execution evidence and are no longer part of the active conformance path. This avoids keeping migration scaffolding as a permanent second operating framework.

Completed CKR validators may reconstruct accepted-era paths only inside the dedicated ephemeral compatibility wrapper. That compatibility projection is test reproducibility, not current routing or authority.

## Failure semantics

A failed conformance check means a repository configuration, routing, workflow, status, reference, context-budget, compatibility-evidence, reviewed vendor dependency, security/lifecycle or documentation-authority invariant is not conformant.

It does **not** mean a monitored pipeline/data source/DMTZ runtime/provider runtime/Databricks workspace is unhealthy or failed. Conversely, PASS does not prove application behavior, provider compatibility, Databricks target capability, causal truth or production readiness.

## Negative controls

`test_documentation_topology_guards.py` protects the final topology against reintroduced compatibility/migration roots, lost DPTN exit provenance, semantic/stable-ID count drift, weakened history boundaries, generated-OKF misrouting, restored phase tooling, stale canonical-path routing and accidental implementation start.

`test_conformance_guards.py` remains the cross-cutting negative-control suite for shared authority, CKR/semantic, adapter, runtime-evidence, vendor-skill and stable-reference failures.

## Databricks boundary

Databricks vendor skills remain reviewed operational dependencies under the accepted addendum. Local ignored materialization remains future implementation-environment work. Managed Databricks MCP servers remain outside the accepted boundary.

## Secret-scanning boundary

The checked-in agentic secret scanner remains a high-confidence repository guard, not organization-wide DLP/secret management.

## Drift report

`run_conformance.py` reports deterministic PASS/FAIL checks, current provider compatibility state, generated-knowledge lifecycle state, CKR documentation-authority notes, final-topology state, the ADF-G deferred-runtime condition, vendor-skill/materialization boundaries, and the non-domain-health disclaimer.

## CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant agentic, current semantic-owner, routing, implementation and history/compatibility changes. The job requires only repository checkout and Python; it intentionally does not require coding-agent runtimes, Databricks credentials/workspace connectivity, production data or external mutation.
