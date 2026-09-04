# Implementation 001 — Executable Foundations & Walking Skeleton

**Status:** PLANNED / BLOCKED ON CANONICAL KNOWLEDGE RETROFIT EXIT

## Objective

Create the smallest executable DMTZ spine that proves the frozen architecture can be built without semantic shortcuts.

001 should end with one real, deterministic, evidence-grounded question flowing from a bounded Databricks evidence source through canonical Delta history and accepted health semantics into Statement IR with historical/as-known behavior.

The target question is:

> **Is this monitored asset stale at the requested time, and what evidence supports that statement?**

001 is not a mini-version of the whole product. It deliberately builds the reusable foundation underneath later implementations.

## Entry dependencies

- Phase 010 COMPLETE / ARCH-001–ARCH-500 frozen;
- Phase 010 implementation handoff accepted;
- Agentic Development Foundation execution exit ACCEPTED;
- ADF-EX-17 accepted only as DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT, with `ADF-G-XT01` carried forward;
- Databricks Agent Skills addendum accepted with the reviewed initial vendor profile;
- **Canonical Knowledge & Documentation Authority Retrofit CKR-A through CKR-K COMPLETE / EXIT ACCEPTED**;
- current implementation references resolve through the post-CKR canonical knowledge layer rather than phase chronology;
- representative non-production Databricks target available or scheduled for 001-E/001-G;
- repository access and a developer able to implement Python/Databricks testable code.

**CKR is currently in progress, therefore 001-A is not active.**

## 001-A Databricks developer-environment check

Once CKR-K unlocks implementation, 001-A owns the first actual local Databricks vendor-skill materialization proof (`DBX-SKILL-RUN-01`). After establishing a compatible Databricks CLI development environment, run:

```bash
python3 scripts/agentic/materialize_databricks_skills.py --execute
```

The helper materializes only the reviewed vendor set under ignored `.databricks/agent-skills/` and verifies exact selected names/versions. If local materialization is already present, the non-executing helper form validates it:

```bash
python3 scripts/agentic/materialize_databricks_skills.py
```

A materialization failure is an agent/developer convenience degradation, not permission to change DMTZ semantics. No workspace call, deployment, governance change or credential-bearing action is authorized merely by this environment check.

## Group sequence

1. **001-A — Developer Environment, Repository Structure & Engineering Standards** — **BLOCKED ON CKR-K**; when unlocked includes Databricks CLI compatibility and reviewed Agent Skills materialization/version verification.
2. **001-B — Canonical Type System, Contract Schemas & Versioning**
3. **001-C — Executable Invariants, Golden Fixtures & Architecture Conformance Tests**
4. **001-D — Minimal Canonical Delta Persistence & Historical Semantics**
5. **001-E — Databricks Acquisition Walking Slice & Integration Health**
6. **001-F — First Health Question: Freshness Observation → Assessment → Statement IR**
7. **001-G — Deployment, CI/CD & Development-Environment Validation**
8. **001-H — Implementation 001 Consolidation / Exit Review**

The groups remain dependency-oriented; CKR does not alter their implementation semantics.

## Documentation authority after CKR

Implementation code, tests, schemas, ADRs and traceability should reference the canonical current owner for the relevant semantic record. Design-history phase files remain available for rationale/provenance but should not be the routine implementation contract surface once their records have canonicalized.

Stable IDs remain the durable semantic identifiers across the documentation path migration.

## Databricks workflow composition

Use DMTZ-owned overlays as the project boundary and reviewed Databricks vendor skills only for relevant platform mechanics:

- environment/capability: `dmtz-databricks-environment-discovery`;
- acquisition: `dmtz-databricks-acquisition`;
- persistence: `dmtz-databricks-persistence`;
- Lineage: `dmtz-databricks-lineage`;
- runtime provenance: `dmtz-databricks-runtime-provenance`;
- governance: `dmtz-databricks-governance`.

Initial vendor skills remain Databricks core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI implementation skills and managed Databricks MCP servers remain deferred.

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

## Mandatory 001 semantic coverage

001 must prove:

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
- reviewed vendor guidance cannot override DMTZ semantics or A1–A4 authorization.

## Explicitly outside 001

Complete enterprise identity/governance runtime, production auth, full health/Lineage/Impact/Investigation, public API/UI, model/vector/search, graph database, optional enterprise integrations, managed Databricks MCP adoption, active control and production deployment remain outside 001 unless separately planned.

## Exit demonstration

The exit demo must show at least:

1. asset fresh / expectation satisfied;
2. asset stale / expectation violated;
3. evidence unavailable/incomplete → unknown/unavailable rather than invented stale/fresh;
4. late evidence changes retrospective answer while an earlier `known by K` answer remains unchanged.

At least one case must execute against the actual development Databricks target.

## 001 exit gate

001 is accepted only when clean-clone bootstrap, reviewed Databricks skill environment evidence/degraded fallback, executable suites, development deployment path, historical knowledge-cut semantics, acquisition failure discipline, Statement IR evidence/limitations and canonical design-to-test traceability all pass without hiding remaining semantic work as TODOs.
