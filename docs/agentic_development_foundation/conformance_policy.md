# Agentic / Documentation Authority Conformance Policy

**Status:** ACCEPTED ADF CONFORMANCE — EXTENDED FOR CKR

## Purpose

Provide one deterministic repository-owned conformance path for the accepted Agentic Development Foundation and the Canonical Knowledge & Documentation Authority Retrofit without turning repository configuration health into DMTZ domain health or provider/runtime certification.

## Canonical command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The command is safe and non-destructive. Fixing failures requires the surrounding human task to authorize A2 changes.

## Validation order

1. documentation phase consistency;
2. OKF v0.2 / DMTZ knowledge-profile validation;
3. Cursor / Claude Code / Codex adapter structure;
4. canonical portable skill structure, including DMTZ Databricks overlays;
5. agent-facing links and stable-ID references;
6. live ADF status-mirror drift;
7. **canonical knowledge authority / CKR ownership-inventory validation**;
8. **live CKR status / implementation-blocking drift**;
9. ADF/addendum/CKR fixture catalog integrity;
10. deterministic context budgets;
11. ADF-G runtime-compatibility evidence integrity;
12. reviewed Databricks Agent Skills dependency/profile/materialization-boundary validation;
13. high-confidence checked-in agentic secret/sensitive-file scan;
14. ADF-H security/trust/lifecycle governance and review-horizon validation;
15. negative controls proving seeded defects are rejected.

This remains separate from future product/runtime tests.

## CKR authority checks

`validate_canonical_knowledge.py` enforces the CKR migration contract, including:

- the canonical structural namespace exists;
- all 24 accepted concepts have unique ownership records and unique canonical targets;
- every accepted stable-ID family is represented with the frozen range, current legacy root, target canonical domain and migration group;
- ARCH-001–ARCH-500 is partitioned across the eight accepted Phase 010 architecture groups;
- inventoried legacy/current sources exist;
- targets are under `docs/canonical/`;
- `candidate_ready` targets are explicitly non-authoritative;
- `canonicalized` targets exist and explicitly declare canonical current authority;
- a `legacy_authoritative` target cannot simultaneously claim canonical authority;
- substantive canonical documents cannot appear outside the ownership inventory.

`validate_ckr_status.py` enforces contiguous CKR-A–K progression and keeps Implementation 001-A blocked until CKR-K exit.

These checks protect documentation authority. They do not prove semantic equivalence of a future candidate by themselves; each migration group still performs domain-specific semantic-conservation review before cutover.

## Failure semantics

A failed conformance check means a repository configuration, routing, workflow, status, reference, context-budget, compatibility-evidence, reviewed vendor dependency, security/lifecycle or documentation-authority invariant is not conformant.

It does **not** mean a monitored pipeline/data source/DMTZ runtime/provider runtime/Databricks workspace is unhealthy or failed.

Conversely, PASS does not prove application behavior, provider compatibility, Databricks target capability, causal truth or production readiness.

## Negative controls

`scripts/agentic/test_conformance_guards.py` copies the repository into a temporary directory and injects bounded defects. Current controls cover:

- malformed OKF metadata;
- provider-specific portable-skill metadata;
- accidental `alwaysApply: true` Cursor routing;
- persistent-context overflow;
- stale ADF status;
- broken OKF resource routing;
- unaccepted `ARCH-501` citation;
- fabricated provider runtime support;
- checked-in high-confidence credential;
- expired provider security-review horizon;
- automatic Databricks vendor-skill expansion;
- deferred model skill entering the initial vendor profile;
- **fabricated CKR canonicalization without canonical target evidence**;
- **canonical target moved outside `docs/canonical/`**;
- **stale CKR implementation-blocking status**.

The temporary checkout is discarded.

## Databricks boundary

Databricks vendor skills remain reviewed operational dependencies under the accepted addendum. Local ignored materialization remains a future Implementation 001-A environment check after CKR unlocks implementation. Managed Databricks MCP servers remain outside the accepted boundary.

## Secret-scanning boundary

The checked-in agentic secret scanner remains a high-confidence repository guard, not organization-wide DLP/secret management.

## Drift report

`run_conformance.py` reports:

- PASS/FAIL for deterministic checks;
- current provider compatibility state;
- OKF stale/deprecated counts;
- explicit CKR documentation-authority notes;
- the ADF-G deferred-runtime condition;
- Databricks vendor-skill/materialization boundaries;
- the non-domain-health disclaimer.

## CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant ADF, CKR, canonical-knowledge, design-history routing, implementation-routing and agentic changes.

The job requires only repository checkout and Python. It intentionally does not require coding-agent runtimes, Databricks credentials/workspace connectivity, production data or external mutation.
