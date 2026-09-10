# Implementation 001 — Executable Foundations & Walking Skeleton

**Status:** READY — **001-A NEXT / READY / NOT STARTED**

## Objective

Create the smallest executable DMTZ spine that proves the accepted architecture can be realized without semantic shortcuts.

Implementation 001 should end with one real, deterministic, evidence-grounded question flowing from a bounded Databricks evidence source through canonical historical persistence and accepted health semantics into Statement IR with historical/as-known behavior.

The target question is:

> **Is this monitored asset stale at the requested time, and what evidence supports that statement?**

001 is not a miniature version of the full product. It establishes reusable foundations for later packages while keeping unsupported enterprise capability outside its boundary.

## Entry gate

Implementation 001 may begin when a human explicitly selects 001-A. Before code changes, the implementing agent/developer must:

- read root `AGENTS.md`, `docs/implementation/AGENTS.md`, and this package boundary;
- resolve current semantic and architecture owners through `docs/index.md` and the ownership inventory;
- resolve applicable stable IDs with `scripts/agentic/resolve_stable_id.py` rather than using historical/search order;
- identify local tool/runtime limitations separately from product requirements;
- preserve ADF-EX-17 / `ADF-G-XT01` as deferred provider-runtime verification until actually executed and recorded;
- keep target-environment capability claims evidence-based.

A representative non-production Databricks target is required for the package's environment-dependent acquisition/deployment evidence, but lack of that target at an earlier local-only group must be reported as an environment dependency rather than converted into a semantic shortcut.

## 001-A — Developer environment, repository structure & engineering standards

001-A is the first implementation group. It establishes the local/toolchain baseline, executable repository skeleton, engineering conventions, and the first actual Databricks vendor-skill materialization proof (`DBX-SKILL-RUN-01`) without yet claiming workspace functionality.

After establishing a compatible Databricks CLI development environment, use:

```bash
python3 scripts/agentic/materialize_databricks_skills.py --execute
```

The helper materializes only the reviewed vendor set under ignored `.databricks/agent-skills/` and verifies the selected names/versions. If local materialization already exists, the non-executing form validates it:

```bash
python3 scripts/agentic/materialize_databricks_skills.py
```

Materialization failure is a developer-tooling degradation. It is not permission to change DMTZ semantics and does not by itself prove or disprove Databricks workspace capability.

## Group sequence

1. **001-A — Developer Environment, Repository Structure & Engineering Standards** — **NEXT / READY / NOT STARTED**
2. **001-B — Canonical Type System, Contract Schemas & Versioning**
3. **001-C — Executable Invariants, Golden Fixtures & Architecture Conformance Tests**
4. **001-D — Minimal Canonical Delta Persistence & Historical Semantics**
5. **001-E — Databricks Acquisition Walking Slice & Integration Health**
6. **001-F — First Health Question: Freshness Observation → Assessment → Statement IR**
7. **001-G — Deployment, CI/CD & Development-Environment Validation**
8. **001-H — Implementation 001 Consolidation / Exit Review**

The sequence is dependency-oriented. Completion of one group does not authorize automatic continuation into the next.

## Documentation and contract authority

Implementation code, tests, schemas, ADRs, and traceability reference the current semantic owner for the proposition being implemented. Start at `docs/index.md` when the owner is unknown; use the stable-ID resolver for exact IDs.

Historical material under `docs/history/` is available for rationale and provenance but is not the routine implementation contract surface. Generated `knowledge/` content is OKF compatibility routing only.

Implementation ADRs choose how accepted contracts are realized. They do not silently redefine what those contracts mean.

## Databricks workflow composition

Use DMTZ-owned workflows as the project boundary and reviewed Databricks vendor skills only for relevant platform mechanics:

- environment/capability — `dmtz-databricks-environment-discovery`;
- acquisition — `dmtz-databricks-acquisition`;
- persistence — `dmtz-databricks-persistence`;
- Lineage — `dmtz-databricks-lineage`;
- runtime provenance — `dmtz-databricks-runtime-provenance`;
- governance — `dmtz-databricks-governance`.

Vendor guidance remains subordinate to DMTZ semantics, authorization, and target-environment verification. Model/AI implementation skills and managed Databricks MCP adoption remain outside this package unless separately authorized.

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

This is a target shape, not permission to create unused scaffolding. Create only what the selected group requires.

## Mandatory semantic coverage

By the end of Implementation 001, executable evidence must preserve at least these boundaries:

- opaque canonical IDs are distinct from source-local IDs;
- event/effective time and framework knowledge/recorded time are distinct;
- later evidence cannot become known in an earlier knowledge cut;
- correction/supersession preserves prior recorded state;
- missing acquisition evidence cannot become a negative fact;
- Expectation is normative, Observation evidential, Assessment interpretive;
- successful execution is not a freshness proxy;
- Statement IR identifies proposition, subject, time perspective, status, basis, and limitations;
- deterministic rendering does not require an LLM;
- raw Databricks response objects do not become canonical DMTZ domain models;
- reviewed vendor guidance cannot override DMTZ semantics or human-directed authorization.

## Explicitly outside 001

Complete enterprise identity/governance runtime, production authentication, full health/Lineage/Impact/Investigation capability, public API/UI, model/vector/search, graph-database infrastructure, optional enterprise integrations, managed Databricks MCP adoption, active control, and production graduation remain outside 001 unless a governed change explicitly alters the package boundary.

## Exit demonstration

The 001 exit demonstration must show at least:

1. asset fresh / expectation satisfied;
2. asset stale / expectation violated;
3. evidence unavailable or incomplete → unknown/unavailable rather than invented stale/fresh;
4. late evidence changes a retrospective answer while an earlier `known by K` answer remains unchanged.

At least one applicable case must execute against the actual development Databricks target before Implementation 001 can claim environment-backed exit evidence.

## Exit gate

Implementation 001 is accepted only when its clean-clone bootstrap, developer/tooling evidence or explicit degraded fallback, executable suites, development deployment path, historical knowledge-cut semantics, acquisition failure discipline, Statement IR evidence/limitations, and design-to-test traceability satisfy the package's accepted contracts without hiding mandatory semantic work as TODOs.
