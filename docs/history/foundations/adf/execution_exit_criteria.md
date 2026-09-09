# Agentic Development Foundation — Execution Exit Criteria

**Status:** COMPLETE / ADJUDICATED — see `execution_exit_review.md`

The design exit review is complete. This file defines the **implementation exit gate** that was adjudicated in `execution_exit_review.md` before Implementation 001-A became eligible.

## Required gates

### Authority / scope

- **ADF-EX-01** — root/shared authority is consistent across supported tools.
- **ADF-EX-02** — human-directed action boundaries are explicit and tested by representative prompts/tasks.
- **ADF-EX-03** — no tool adapter can silently supersede DMTZ semantic/change-control authority.

### Knowledge plane

- **ADF-EX-04** — `knowledge/` is structurally valid under OKF v0.2 and the DMTZ producer profile.
- **ADF-EX-05** — progressive disclosure resolves current project status, active package and representative domain architecture without preloading the full design corpus.
- **ADF-EX-06** — OKF trust/lifecycle fields are documented/tested as separate from DMTZ authority/health/evidence semantics.
- **ADF-EX-07** — broken/deprecated/stale knowledge routing is surfaced explicitly.

### Tool adapters

- **ADF-EX-08** — Cursor loads the expected shared/scoped guidance for representative files/tasks.
- **ADF-EX-09** — Claude Code consumes shared repository authority through a thin `CLAUDE.md` adapter and does not require a semantic copy.
- **ADF-EX-10** — Codex can operate from shared `AGENTS.md`, knowledge and workflow sources without a separate DMTZ rulebook.

### Workflows / skills

- **ADF-EX-11** — `resolve-context`, `implement-group`, `resolve-contract`, `run-conformance`, `review-change`, `update-traceability` and `exit-review` (or an accepted reduced set) are represented in the canonical portable workflow source.
- **ADF-EX-12** — human invocation/scope remains explicit; workflows do not automatically continue to unrelated work.
- **ADF-EX-13** — tool-native workflow adapters preserve required steps or clearly document degraded/manual fallback.

### Context / validation

- **ADF-EX-14** — deterministic validation catches malformed agentic metadata, broken canonical references and stale duplicated status.
- **ADF-EX-15** — context-budget checks prevent accidental return to monolithic always-loaded instructions.
- **ADF-EX-16** — one drift/conformance report summarizes agentic configuration health without presenting it as DMTZ domain health.

### Developer compatibility

- **ADF-EX-17** — one representative bounded task is successfully exercised with Cursor, Claude Code and Codex using the same repository acceptance criteria.
- **ADF-EX-18** — a non-agent developer can follow the same canonical docs/tests without requiring AI-specific knowledge.

### Security / lifecycle

- **ADF-EX-19** — secrets/sensitive data are excluded from checked-in agentic artifacts and tool memory is explicitly noncanonical.
- **ADF-EX-20** — supported-tool compatibility assumptions have current verification metadata and a defined degraded/unverified state.

## Exit evidence

The execution exit review includes:

- files/artifacts created;
- validation commands/checks run;
- representative cross-tool test state;
- context-size measurements for persistent instruction surfaces;
- known degraded or unverified tool features;
- unresolved risks/debt;
- explicit confirmation that autonomous backlog items remain deferred.

## Exit decision rule

Implementation 001-A becomes the normal next work only when all mandatory ADF-EX gates pass or a specific gate is explicitly waived with a bounded reason that does not alter DMTZ semantic/security authority.

A tool-specific convenience gap may be accepted as degraded. A shared-authority, canonical-reference, security or human-directed-boundary failure may not be silently waived.

## Adjudicated disposition

See [`execution_exit_review.md`](execution_exit_review.md) for the evidence-backed decision:

- ADF-EX-01–ADF-EX-16 — **PASS**;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**; `ADF-G-XT01` carried forward;
- ADF-EX-18–ADF-EX-20 — **PASS**;
- Databricks Agent Skills Integration Addendum — **ACCEPTED**;
- `DBX-SKILL-RUN-01` — **OPEN / IMPLEMENTATION 001-A**;
- autonomous development — **DEFERRED / NOT AUTHORIZED**.
