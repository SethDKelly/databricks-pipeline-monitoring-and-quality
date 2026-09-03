# Implementation 001 — Executable Foundations & Walking Skeleton

**Status:** PLANNED / READY AFTER AGENTIC FOUNDATION EXIT

## Objective

Create the smallest executable DMTZ spine that proves the frozen architecture can be built without semantic shortcuts.

001 should end with one real, deterministic, evidence-grounded question flowing from a bounded Databricks evidence source through canonical Delta history and accepted health semantics into Statement IR with historical/as-known behavior.

The target question is:

> **Is this monitored asset stale at the requested time, and what evidence supports that statement?**

001 is not a mini-version of the whole product. It deliberately builds the reusable foundation underneath later implementations.

## Entry dependencies

- Phase 010 COMPLETE / ARCH-001–ARCH-500 frozen;
- Phase 010 implementation handoff accepted;
- Agentic Development Foundation execution exit accepted under its documented gate/waiver rule;
- Databricks Agent Skills pre-exit addendum accepted with the reviewed initial vendor profile;
- representative non-production Databricks target available or scheduled for 001-E/001-G;
- repository access and a developer able to implement Python/Databricks testable code.

## 001-A Databricks developer-environment check

001-A owns the first actual local Databricks vendor-skill materialization proof (`DBX-SKILL-RUN-01`). After establishing a compatible Databricks CLI development environment, run:

```bash
python3 scripts/agentic/materialize_databricks_skills.py --execute
```

The helper materializes only the reviewed vendor set under ignored `.databricks/agent-skills/` and verifies exact selected names/versions. If local materialization is already present, the non-executing helper form validates it:

```bash
python3 scripts/agentic/materialize_databricks_skills.py
```

A materialization failure is an agent/developer convenience degradation, not permission to change DMTZ semantics. Review the CLI/upstream profile and use official Databricks documentation/manual procedures until repaired.

No workspace call, deployment, governance change or credential-bearing action is authorized merely by this environment check.

## Group sequence

1. **001-A — Developer Environment, Repository Structure & Engineering Standards** — includes Databricks CLI compatibility and reviewed Agent Skills materialization/version verification.
2. **001-B — Canonical Type System, Contract Schemas & Versioning**
3. **001-C — Executable Invariants, Golden Fixtures & Architecture Conformance Tests**
4. **001-D — Minimal Canonical Delta Persistence & Historical Semantics**
5. **001-E — Databricks Acquisition Walking Slice & Integration Health**
6. **001-F — First Health Question: Freshness Observation → Assessment → Statement IR**
7. **001-G — Deployment, CI/CD & Development-Environment Validation**
8. **001-H — Implementation 001 Consolidation / Exit Review**

The groups are dependency-oriented. B/C can overlap after A establishes package/testing conventions. D requires stable primitive contracts. E can develop against the adapter contract while D matures. F composes B–E. G makes the path reproducible in the actual development environment. H freezes the executable foundation.

## Databricks workflow composition

Use DMTZ-owned overlays as the project boundary and the reviewed Databricks vendor skills only for the relevant platform mechanics:

- environment/capability: `dmtz-databricks-environment-discovery`;
- acquisition: `dmtz-databricks-acquisition`;
- persistence: `dmtz-databricks-persistence`;
- Lineage: `dmtz-databricks-lineage`;
- runtime provenance: `dmtz-databricks-runtime-provenance`;
- governance: `dmtz-databricks-governance`.

Initial reviewed vendor skills include Databricks core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI implementation skills remain deferred. Managed Databricks MCP servers are not part of this entry dependency.

## Expected repository shape after 001

```text
src/dmtz/
  contracts/
  temporal/
  evidence/
  persistence/
  acquisition/databricks/
  health/
  explanation/
  configuration/
tests/
  unit/
  contract/
  persistence/
  adapters/
  scenarios/
  integration/
  fixtures/
resources/schemas/
databricks/
pyproject.toml
databricks.yml
```

Later packages add identity/governance/Lineage/reasoning/serving modules rather than creating parallel foundations.

## Mandatory 001 semantic coverage

001 must already prove:

- opaque canonical IDs are distinct from source-local IDs;
- event/effective time and framework knowledge/recorded time are distinct;
- later evidence cannot become known in an earlier knowledge cut;
- correction/supersession preserves prior recorded state;
- missing acquisition evidence cannot become a negative fact;
- Expectation is normative, Observation evidential, Assessment interpretive;
- successful execution is not used as a freshness proxy;
- Statement IR identifies proposition, subject, time perspective, status, basis and limitations;
- deterministic rendering does not require an LLM;
- raw Databricks response objects do not become canonical domain models;
- reviewed Databricks vendor guidance cannot override DMTZ contract semantics or A1–A4 authorization.

## Explicitly outside 001

- complete enterprise identity/governance runtime;
- production user authentication/authorization;
- GitHub acquisition beyond optional fixture/interface scaffolding;
- full health/quality metric suite;
- complete Lineage/Impact;
- Investigation/Causal Claims;
- public API/UI;
- model/vector/search implementation and deferred Databricks model/AI Agent Skills;
- graph database;
- Collibra/Immuta;
- managed Databricks MCP-server adoption;
- Gate/Safeguard active control;
- production deployment.

Where 001 requires a future capability seam, use an explicit test/dev stub with a narrow interface and mark it non-production; do not invent simplified semantics.

## Exit demonstration

The exit demo must show at least four cases:

1. asset fresh / expectation satisfied;
2. asset stale / expectation violated;
3. evidence unavailable or incomplete → result unknown/unavailable rather than stale/fresh invention;
4. late-arriving evidence changes a retrospective answer while an earlier `known by K` answer remains unchanged.

At least one case must execute against the actual development Databricks target, not only fixtures.

## 001 exit gate

001 is accepted only when:

- clean-clone bootstrap works;
- `DBX-SKILL-RUN-01` records exact reviewed Databricks skill materialization/version evidence or a clearly documented degraded fallback;
- unit/contract/persistence/scenario suites pass;
- Databricks bundle validation/development deployment path works for the selected slice;
- no long-lived Databricks secret is required in CI when workload federation is available;
- minimal Delta history supports explicit knowledge-cut replay without Delta time travel as the sole mechanism;
- acquisition failure/partial coverage cannot emit false negative evidence;
- freshness question returns Statement IR with exact evidence references and limitations;
- design-to-test traceability exists for implemented contracts;
- remaining work is clearly handed to Implementation 002/003 rather than hidden as TODO semantics.
