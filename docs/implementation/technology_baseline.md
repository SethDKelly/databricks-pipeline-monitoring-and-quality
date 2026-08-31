# Implementation Technology Baseline

**Status:** Reference baseline — concrete versions are selected/pinned in Implementation 001-A

This document defines a pragmatic default stack. These are implementation selections, not new semantic architecture. An enterprise team may substitute equivalent tools by implementation ADR if all accepted contracts and gates remain satisfied.

## Core language/runtime

**Default:** Python for the initial DMTZ core.

Why:

- native fit with Databricks/PySpark/Delta workflows;
- strong typed-model/validation/testing ecosystem;
- suitable for source adapters, deterministic reasoning, persistence and service code;
- avoids a multi-language core before product boundaries are executable.

The exact Python minor version must be compatible with the selected Databricks Runtime and enterprise support policy and must be pinned in `pyproject.toml`/lockfile and CI.

## Packaging and repository

Use a standard `src/` Python package layout and a single repository initially:

```text
src/dmtz/
  contracts/
  temporal/
  evidence/
  identity/
  governance/
  persistence/
  acquisition/
  health/
  lineage/
  investigation/
  reasoning/
  explanation/
  serving/
  ops/
tests/
  unit/
  contract/
  persistence/
  adapters/
  integration/
  scenarios/
  e2e/
  fixtures/
resources/schemas/
databricks/
docs/
```

Start as a modular package/application. Separate deployable services only where latency, security, scale or failure-domain evidence justifies it.

## Typed contracts

Reference implementation:

- Python type hints;
- Pydantic v2 or an equivalent strongly validated schema library for boundary/domain DTOs;
- generated JSON Schema/OpenAPI where applicable;
- opaque strongly typed canonical IDs rather than raw strings throughout domain code.

Domain models must not expose source-vendor response objects as canonical types.

## Testing

Reference baseline:

- `pytest`;
- property-based testing where useful for invariants/state machines;
- coverage reporting;
- lint/format/type checking in CI;
- deterministic fixture factories and golden scenario manifests.

The exact lint/type tools may follow enterprise standards; the gate is zero ambiguous quality baseline, not a specific vendor.

## Databricks packaging/deployment

Use Databricks **Declarative Automation Bundles** for Databricks application/job/pipeline resource packaging and environment targets unless a target limitation proves unsuitable.

Keep bundles small/focused as the deployment topology evolves rather than creating one universal bundle for every enterprise component.

Use Terraform or the enterprise cloud/IaC standard for account/workspace/network/external infrastructure that sits outside bundle ownership.

## CI/CD identity

Prefer GitHub Actions with OIDC/workload identity federation to a Databricks service principal. Do not store long-lived Databricks PATs/client secrets when federation is available.

Use environment/repository constraints on federation trust and least-privilege service-principal permissions.

## Persistence

Canonical structured state is Delta-first per Phase 010. Reference implementation uses:

- Unity Catalog managed Delta tables when verified/appropriate;
- governed object/volume storage for selective payloads and archives;
- derived/read-model stores only when justified later.

Do not use Delta time travel alone as DMTZ historical knowledge semantics.

## API/UI

Do not select a heavyweight application platform in 001. Implementation 006 owns the final initial API/UI framework choice.

001 may expose a CLI/test harness or thin internal function boundary to prove Statement IR. Any temporary interface must not become an accidental public contract.

## Search/graph/model

No specialized graph database, vector database or LLM is required for 001–008 core acceptance.

Use Delta-backed/rebuildable graph-shaped projections first. Introduce specialized search/graph/model infrastructure only after measured need and behind non-authoritative interfaces.

## Version pinning

Before the first executable commit, record:

- Python minor;
- Databricks Runtime target(s);
- Databricks CLI/SDK minor range;
- Spark/Delta compatibility;
- schema library major/minor;
- test/lint/type tooling;
- bundle schema/tooling;
- any API versions used by adapters.

Upgrade work must run contract/scenario suites before promotion.
