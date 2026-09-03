# Agentic Conformance Policy

**Status:** ACCEPTED — ADF-F / EXTENDED THROUGH ADF-H AND DATABRICKS AGENT SKILLS ADDENDUM

## Purpose

Provide one deterministic repository-owned conformance path for the Agentic Development Foundation without turning agent configuration health into DMTZ domain health or provider-runtime certification.

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
4. canonical portable skill structure, including registered DMTZ Databricks overlays;
5. agent-facing canonical links and stable-ID references;
6. live ADF status-mirror drift;
7. ADF and pre-exit addendum scenario fixture catalog integrity;
8. deterministic context budgets;
9. ADF-G runtime-compatibility evidence integrity;
10. reviewed Databricks Agent Skills dependency/profile/materialization-boundary validation;
11. high-confidence checked-in agentic secret/sensitive-file scan;
12. ADF-H security/trust/lifecycle governance and review-horizon validation;
13. negative controls proving important seeded defects are rejected.

This order is intentionally separate from future product/runtime tests. Agentic conformance may be an early CI gate, but it does not replace unit, integration, scenario, deployment, provider runtime, Databricks workspace, or production validation.

## Failure semantics

A failed agentic check means an agent-facing repository configuration, routing, workflow, status, reference, context-budget, compatibility-evidence, reviewed vendor dependency, or security/lifecycle invariant is not currently conformant.

It does **not** mean:

- a monitored pipeline is unhealthy;
- data quality failed;
- source evidence is unavailable;
- DMTZ runtime behavior failed;
- a provider coding-agent runtime failed unless actual provider evidence says so;
- a Databricks workspace/vendor skill runtime failed unless actual environment evidence says so;
- production readiness failed;
- any causal or health proposition is true.

Conversely, an agentic PASS does not prove DMTZ application behavior, coding-agent runtime compatibility, or target Databricks capability.

## Negative controls

`scripts/agentic/test_conformance_guards.py` copies the repository into a temporary directory and injects bounded defects. Each mutated checkout must cause the targeted validator to fail.

Current negative controls cover:

- malformed OKF metadata;
- provider-specific metadata in a portable DMTZ skill;
- accidental `alwaysApply: true` Cursor routing;
- persistent-context budget overflow;
- stale ADF status copy;
- broken canonical OKF resource routing;
- an unaccepted stable-ID citation (`ARCH-501`);
- fabricated provider runtime support without actual exercise evidence;
- a seeded high-confidence credential in an agentic instruction surface;
- an expired provider security-review horizon;
- automatic addition of newly published Databricks vendor skills;
- a deferred Databricks model/AI skill entering the initial selected set.

The temporary checkout is discarded and no canonical repository file is mutated by the negative-control run.

## Databricks vendor-skill boundary

`validate_databricks_agent_skills.py` validates the repository review profile and DMTZ overlay composition. Vendor skills themselves are materialized locally under ignored `.databricks/agent-skills/` using `aitools --path`; they are not copied into canonical `.agents/skills/`.

If a local materialization exists, exact reviewed names/versions and absence of extra skills are validated. Absence of that local ignored tree is allowed in CI and remains an Implementation 001-A environment verification.

Managed Databricks MCP servers are outside the addendum and require separate G3/G4 review.

## Secret scanning boundary

`scan_agentic_secrets.py` is intentionally a **high-confidence agentic-surface guard**. It checks known credential/private-key forms, structured non-placeholder secret assignments and secret-bearing filenames under checked-in agentic surfaces.

It is not a replacement for organization-wide repository secret scanning, dependency review, DLP, credential rotation or incident response.

## Drift report

`run_conformance.py` produces a human-readable report containing:

- PASS/FAIL for each deterministic check;
- current per-tool documented/runtime compatibility state;
- stale/deprecated OKF knowledge counts;
- the explicit non-domain-health disclaimer;
- the explicit ADF-G deferred-verification note;
- the Databricks vendor-skill/materialization boundary.

Tool compatibility states such as degraded or unverified are reported independently. One tool becoming degraded must not make another tool unusable or create DMTZ domain-health state.

## CI contract

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant pull requests and pushes to `main`.

The job requires only a repository checkout and Python. It intentionally does not require Cursor, Claude Code, Codex, credentials, Databricks CLI/workspace connectivity, production data or external mutation.

ADF-G provider runtime evidence remains independently recorded. ADF-H governs security/trust/lifecycle policy and provider review horizons. The Databricks Agent Skills addendum governs the curated vendor-skill review/materialization boundary without turning vendor guidance into DMTZ authority.
