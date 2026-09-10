# Agentic / Documentation Authority Conformance Policy

**Status:** ACCEPTED ADF CONFORMANCE — EXTENDED CKR / DPTN-F ROUTING

## Purpose

Provide one deterministic repository-owned conformance path for the accepted Agentic Development Foundation, completed CKR and active Documentation Physical Topology Normalization without turning repository configuration health into DMTZ domain health or provider/runtime certification.

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
6. live ADF / CKR / DPTN status-mirror drift;
7. CKR ownership-inventory/current semantic-owner validation;
8. CKR-B–K accepted semantic/routing/provenance baselines through bounded accepted-era compatibility where necessary;
9. DPTN-A–F topology/conservation/rebinding validation;
10. ADF/addendum/CKR/DPTN fixture catalog integrity;
11. deterministic context budgets;
12. ADF-G runtime-compatibility evidence integrity;
13. reviewed Databricks Agent Skills dependency/profile/materialization-boundary validation;
14. high-confidence checked-in agentic secret/sensitive-file scan;
15. ADF-H security/trust/lifecycle governance and review-horizon validation;
16. negative controls proving seeded defects are rejected.

This remains separate from future product/runtime tests.

## Current authority checks

The CKR ownership inventory selects the sole current semantic owner for each record and stable-ID family. Current semantic roots are first-class `docs/<family>/` paths. Deterministic exact-ID lookup uses `scripts/agentic/resolve_stable_id.py <ID>` and returns one current `owner_path::ID`; `--history` is separate provenance discovery.

DPTN validation additionally enforces:

- `docs/index.md` is repository-native discovery;
- generated `knowledge/` is OKF compatibility only;
- current agent/rule/validator routing does not depend on Phase-era, history or `docs/canonical/<family>` compatibility paths;
- completed CKR validators may reconstruct accepted-era paths only inside the dedicated ephemeral compatibility wrapper;
- semantic owner tree identities/counts/ranges remain conserved;
- Implementation 001-A remains blocked until DPTN-G exit acceptance.

These checks protect documentation authority/topology. They do not prove product behavior or deployment capability.

## Failure semantics

A failed conformance check means a repository configuration, routing, workflow, status, reference, context-budget, compatibility-evidence, reviewed vendor dependency, security/lifecycle or documentation-authority invariant is not conformant.

It does **not** mean a monitored pipeline/data source/DMTZ runtime/provider runtime/Databricks workspace is unhealthy or failed. Conversely, PASS does not prove application behavior, provider compatibility, Databricks target capability, causal truth or production readiness.

## Negative controls

Repository negative controls use temporary copies and inject bounded defects across status mirrors, generated OKF metadata, stable-ID/current-owner routing, context budgets, provider runtime evidence, vendor skill boundaries, security review horizons, DPTN conservation, discovery routing and implementation gating. A negative control is useful only when its intended validator rejects the seeded defect.

## Databricks boundary

Databricks vendor skills remain reviewed operational dependencies under the accepted addendum. Local ignored materialization remains future implementation-environment work. Managed Databricks MCP servers remain outside the accepted boundary.

## Secret-scanning boundary

The checked-in agentic secret scanner remains a high-confidence repository guard, not organization-wide DLP/secret management.

## Drift report

`run_conformance.py` reports deterministic PASS/FAIL checks, current provider compatibility state, generated-knowledge lifecycle state, CKR/DPTN documentation-authority notes, the ADF-G deferred-runtime condition, vendor-skill/materialization boundaries, and the non-domain-health disclaimer.

## CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant agentic, current semantic-owner, routing, implementation and topology-normalization changes. The job requires only repository checkout and Python; it intentionally does not require coding-agent runtimes, Databricks credentials/workspace connectivity, production data or external mutation.
