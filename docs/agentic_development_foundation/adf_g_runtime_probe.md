# ADF-G Runtime Probe Contract

**Status:** ACCEPTED — ADF-G execution contract

## Purpose

Provide one repeatable, tool-neutral runtime exercise for Cursor, Claude Code and Codex without allowing the test harness to replace repository authority or fabricate runtime evidence.

A provider runtime result is accepted only when an actual installed runtime performs the bounded exercise in a real checkout. Static repository validation and vendor documentation are necessary inputs but are not runtime proof.

## Representative bounded task

Use the same harmless task in each supported coding-agent runtime:

> Inspect the repository's current Agentic Development Foundation state. Resolve `AUTH-034` using the repository's stable-reference discipline. Identify the canonical `run-conformance` workflow and the command it requires. Do not edit files. Do not begin another ADF group. Report the authority sources used, the stable-ID candidate/owner reasoning, the validation command, and any unavailable native feature.

This is intentionally an **A1 read/review/plan** task. A runtime fails the exercise if it edits the repository, invents current status from memory, treats the first stable-ID occurrence as canonical by search order, starts ADF-H, or requires a provider-specific semantic fork.

## Required observations

For each runtime capture:

1. product/tool name;
2. product version/build when exposed;
3. execution date;
4. invocation mode and working directory;
5. whether shared project instructions were observed;
6. whether current ADF status was resolved from repository authority;
7. whether `knowledge/index.md` was reachable without whole-corpus preload;
8. whether `AUTH-034` was resolved using accepted range + exact occurrence + canonical owner discipline;
9. whether the `run-conformance` workflow was discoverable or its documented bridge worked;
10. whether the canonical command was reported as `python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md`;
11. whether the runtime remained A1/read-only;
12. whether it stopped at the requested task;
13. supported/degraded/unverified/unsupported result;
14. any convenience-only workaround.

## Runtime-specific verification aids

### Cursor

Expected project surfaces:

- root `AGENTS.md`;
- scoped `.cursor/rules/*.mdc`;
- project `.agents/skills/*/SKILL.md`.

Record the Cursor product/CLI build when available and whether project instructions/rules/skills appear to be applied. Native skill discovery is ergonomic evidence only; manual reading of the canonical skill is an acceptable degraded fallback.

### Claude Code

Expected project surfaces:

- `.claude/CLAUDE.md`;
- imported `../AGENTS.md`;
- `.claude/commands/run-conformance.md` bridge to the canonical `.agents/skills/run-conformance/SKILL.md`.

Use `/context` to confirm the project memory file when available. Existing `.claude/commands/` remain a supported compatibility mechanism; DMTZ intentionally does not duplicate the full portable skill corpus into `.claude/skills/`.

### Codex

Expected project surfaces:

- root `AGENTS.md`;
- canonical `.agents/skills/*/SKILL.md`;
- normal repository read/search/command tools.

Record the Codex CLI/app build when available. Model identity is not a DMTZ compatibility requirement.

## Evidence format

Runtime evidence is recorded in `runtime_compatibility_evidence.json`. A tool entry may move from `unverified` to `supported` or `degraded` only with an actual runtime exercise. Documentation review alone may update `documentation_verified_on` but not `runtime_verified_on`.

## Degraded mode

A missing native skill picker, path-scoped feature, diagnostic command or UI surface may produce `degraded` rather than failure when the runtime can still:

- read shared authority;
- reach canonical knowledge/workflows manually;
- preserve A1–A4 boundaries;
- run repository validation when the selected task permits it;
- avoid semantic duplication.

## Failure conditions

Mark the runtime unsupported for the current profile if it cannot perform ordinary repository read/search/edit/test work under human direction without requiring a conflicting semantic instruction set.

Mark it unverified when the runtime cannot be exercised because the binary, authentication, license, network capability or target environment is unavailable. **Unverified is not unsupported and is not PASS.**
