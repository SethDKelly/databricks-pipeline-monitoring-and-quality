# ADF-F — Conformance, Validation, Drift Detection & CI

**Status:** PLANNED / READY TO EXECUTE

## Objective

Make the Agentic Development Foundation reviewable and enforceable through repository checks rather than relying on agent instructions alone.

## Validation layers

### 1. OKF structure validation

Validate the `knowledge/` bundle against the adopted OKF v0.2 structural requirements and the stricter DMTZ producer profile.

Checks should include:

- every concept document has parseable YAML frontmatter;
- `type` is present and non-empty;
- DMTZ-required profile fields are present;
- root `index.md` declares `okf_version: "0.2"` if the bundle uses that declaration;
- reserved `index.md` / `log.md` structures are valid;
- cross-links/resources resolve when repository-relative;
- status values are valid;
- stale/deprecated entries are surfaced in generated reports.

### 2. Authority/reference validation

Check that agent-facing artifacts do not become the only location for a material requirement.

Useful mechanical checks:

- referenced canonical paths exist;
- stable contract IDs cited by routing entries exist in `docs/`;
- active implementation package in agent-routing artifacts matches `docs/implementation/README.md`;
- no tool adapter declares a contradictory project phase/status;
- no generated knowledge entry points to a removed/deprecated resource without explicit lifecycle state.

### 3. Tool adapter validation

At minimum, lint/parse:

- Cursor `.mdc` frontmatter and relevant globs;
- Claude `CLAUDE.md` import/reference path and `.claude/rules` frontmatter where used;
- portable `SKILL.md` frontmatter/profile;
- any generated native skill adapters;
- Bugbot or review-policy references.

Where a vendor provides a local validation command, the execution plan may use it, but repository-owned structural validation remains the portable baseline.

### 4. Context-budget checks

Track simple deterministic measures such as lines/bytes for always-loaded instruction surfaces. CI should flag accidental expansion beyond agreed thresholds rather than allowing gradual return to monolithic prompts.

Context size is an engineering signal, not a semantic correctness score.

### 5. Workflow conformance

Each portable workflow should have scenario fixtures that verify required steps and boundaries at the artifact level.

Examples:

- `resolve-context` returns canonical sources rather than invented summaries;
- `implement-group` requires affected tests/traceability and does not chain to the next group;
- `exit-review` cannot mark a missing mandatory gate complete;
- review workflow flags a deliberately seeded semantic boundary violation.

These tests may begin as deterministic fixtures/checklists before deeper tool-in-the-loop evaluation is justified.

## CI integration

ADF execution should add a fast agentic-conformance job early in the repository CI sequence:

```text
parse/structure
  → OKF/profile/link validation
  → adapter/skill validation
  → authority/status drift checks
  → context-budget checks
  → normal repository tests
```

A failure in agentic metadata should block merging the broken agentic configuration but must not be represented as a DMTZ domain-health failure.

## Tool-in-the-loop compatibility tests

Because Cursor/Claude/Codex behavior changes independently, keep tool-in-the-loop smoke checks separate from deterministic CI where licensing/network/runtime makes them unsuitable for every PR.

Run them:

- during ADF-G compatibility acceptance;
- after material adapter changes;
- after supported-tool major/minor behavior changes when relevant;
- before declaring a tool compatibility profile current.

## Drift report

Provide one compact command/report showing:

- OKF validation status;
- broken resources/contract references;
- adapter versions last verified;
- context-budget exceptions;
- stale/deprecated knowledge entries;
- skill/native-adapter divergence where generated copies are used.

## Deliverables

- repository-owned agentic validation script(s);
- CI job/workflow integration;
- fixtures for structural and boundary failures;
- context-budget configuration;
- compatibility smoke-test checklist;
- human-readable drift report.

## Acceptance scenarios

ADF-F passes when:

- malformed OKF/skill/rule metadata is caught before merge;
- an intentionally stale implementation-status copy is detected;
- a broken stable-ID/path reference is surfaced;
- accidental growth of universal instruction files beyond the agreed threshold is visible/failing according to policy;
- normal product tests remain distinct from agentic-config conformance;
- a tool upgrade can be marked unverified without making another tool unusable.
