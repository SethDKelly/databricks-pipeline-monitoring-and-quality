# Agentic Conformance Policy

**Status:** ACCEPTED — ADF-F

## Purpose

Provide one deterministic repository-owned conformance path for the Agentic Development Foundation without turning agent configuration health into DMTZ domain health.

## Canonical command

Run:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The command is safe and non-destructive. It may run under the A1 `run-conformance` workflow. Fixing failures requires the surrounding human task to authorize A2 changes.

## Validation order

1. documentation phase consistency;
2. OKF v0.2 / DMTZ knowledge-profile validation;
3. Cursor / Claude Code / Codex adapter structure;
4. canonical portable skill structure;
5. agent-facing canonical links and stable-ID references;
6. live ADF status-mirror drift;
7. ADF scenario fixture catalog integrity;
8. deterministic context budgets;
9. negative controls proving that important seeded defects are rejected.

This order is intentionally separate from future product/runtime tests. Agentic conformance may be an early CI gate, but it does not replace unit, integration, scenario, deployment, or production validation.

## Failure semantics

A failed agentic check means an agent-facing repository configuration, routing, workflow, status, reference, or context-budget invariant is not currently conformant.

It does **not** mean:

- a monitored pipeline is unhealthy;
- data quality failed;
- source evidence is unavailable;
- DMTZ runtime behavior failed;
- production readiness failed;
- any causal or health proposition is true.

Conversely, an agentic PASS does not prove DMTZ application behavior.

## Negative controls

`scripts/agentic/test_conformance_guards.py` copies the repository into a temporary directory and injects bounded defects. Each mutated checkout must cause the targeted validator to fail.

Current negative controls cover:

- malformed OKF metadata;
- provider-specific metadata in a portable skill;
- accidental `alwaysApply: true` Cursor routing;
- persistent-context budget overflow;
- stale ADF status copy;
- broken canonical OKF resource routing;
- an unaccepted stable-ID citation (`ARCH-501`).

The temporary checkout is discarded and no canonical repository file is mutated by the negative-control run.

## Drift report

`run_conformance.py` produces a human-readable report containing:

- PASS/FAIL for each deterministic check;
- current per-tool compatibility status from `tool_compatibility.json`;
- stale/deprecated OKF knowledge counts;
- the explicit non-domain-health disclaimer.

Tool compatibility states such as degraded or unverified are reported independently. One tool becoming degraded must not make another tool unusable or create DMTZ domain-health state.

## CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant pull requests and pushes to `main`.

The job requires only a repository checkout and Python. It intentionally does not require Cursor, Claude Code, Codex, credentials, Databricks connectivity, or external mutation.

ADF-G owns tool-in-the-loop smoke exercises. ADF-H owns long-term security/trust/lifecycle governance and compatibility review horizons.
