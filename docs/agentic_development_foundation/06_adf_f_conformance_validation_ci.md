# ADF-F — Conformance, Validation, Drift Detection & CI

**Status:** COMPLETE / ACCEPTED

## Objective

Make the Agentic Development Foundation reviewable and enforceable through repository checks rather than relying on agent instructions alone.

ADF-F is realized by the accepted policy in [`conformance_policy.md`](conformance_policy.md), the unified runner `scripts/agentic/run_conformance.py`, the repository CI workflow `.github/workflows/agentic-conformance.yml`, the ADF-F fixture set, and the execution evidence recorded in [`adf_f_execution_review.md`](adf_f_execution_review.md).

## Validation layers

### 1. OKF structure validation

Validate the `knowledge/` bundle against OKF v0.2 structural requirements and the stricter DMTZ producer profile, including required fields, local resources/links, lifecycle state, and stale/deprecated reporting.

### 2. Authority/reference validation

Validate agent-facing canonical links and accepted stable-ID citations without turning search order into semantic authority. Live ADF status mirrors are checked against the ADF README authority.

### 3. Tool adapter validation

Validate Cursor scoped rules, the Claude shared-authority bridge, absence of competing root semantic adapters, and the portable Agent Skills workflow structure.

### 4. Context-budget checks

Enforce the deterministic UTF-8 byte budgets accepted in ADF-E. Context budget failure is agentic configuration drift, not DMTZ domain health.

### 5. Workflow/fixture conformance

Validate the ADF-A–ADF-F scenario catalogs structurally and execute bounded negative controls proving that seeded configuration defects are rejected by their owning validators.

## CI integration

The canonical sequence is:

```text
documentation consistency
  → OKF/profile/link validation
  → adapter/skill validation
  → canonical reference validation
  → ADF status drift
  → fixture catalog
  → context budgets
  → negative controls
  → future normal repository/product tests
```

`.github/workflows/agentic-conformance.yml` runs this sequence for relevant pull requests and pushes to `main`.

A failure in agentic metadata blocks the broken agentic configuration but must not be represented as a DMTZ domain-health, data-quality, source-health, or production-readiness failure.

## Tool-in-the-loop compatibility tests

Cursor/Claude Code/Codex runtime smoke checks remain separate because they may require installed/licensed/networked tool environments. [`compatibility_smoke_checklist.md`](compatibility_smoke_checklist.md) defines the ADF-G checklist.

## Drift report

The unified runner produces one human-readable Agentic Conformance Report containing:

- deterministic check results;
- current per-tool compatibility status;
- stale/deprecated knowledge counts;
- explicit non-domain-health semantics.

## Negative controls

`scripts/agentic/test_conformance_guards.py` mutates a temporary checkout only and requires failure detection for:

- malformed OKF metadata;
- provider-specific portable-skill metadata;
- accidental `alwaysApply: true` Cursor routing;
- persistent-context overflow;
- stale ADF status;
- broken canonical knowledge routing;
- unaccepted stable-ID citation.

## Deliverables

- repository-owned unified conformance runner;
- dedicated GitHub Actions CI job;
- authority/status/reference/context/fixture validators;
- bounded negative-control suite;
- ADF-F scenario catalog;
- compatibility smoke-test checklist for ADF-G;
- human-readable drift report.

## Acceptance result

ADF-F passes when the real repository checkout passes the unified conformance job and each seeded negative control is detected. See [`adf_f_execution_review.md`](adf_f_execution_review.md) for the actual run evidence and any residual obligations.
