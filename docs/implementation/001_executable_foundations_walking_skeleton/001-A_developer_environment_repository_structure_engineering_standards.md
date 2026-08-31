# 001-A — Developer Environment, Repository Structure & Engineering Standards

**Status:** Planned

## Goal

Turn the documentation-first repository into a reproducible software-development repository without adding domain shortcuts.

## Deliverables

### Repository/package foundation

Create:

- `pyproject.toml` with pinned supported Python range and project metadata;
- lockfile according to selected package manager;
- `src/dmtz/` package;
- standardized test hierarchy;
- `resources/schemas/`;
- `databricks/` resource/code area;
- `databricks.yml` bundle skeleton;
- developer bootstrap commands/scripts;
- environment/configuration loading convention;
- local sample configuration containing no secrets.

### Engineering quality baseline

Select and configure:

- formatter/linter;
- static type checker;
- pytest and coverage;
- pre-commit or equivalent local quality hooks;
- dependency/security scanning consistent with enterprise standards;
- documentation consistency check already present in the repository;
- CI quality workflow skeleton.

Exact tools are implementation ADR choices. The expected default is a conventional typed Python toolchain.

### Environment model

Define explicit configuration profiles for at least:

- local/unit-test;
- development Databricks target;
- CI integration-test target.

Do not introduce `prod` credentials or production data access in 001.

### Developer authentication

For local development, support enterprise-approved Databricks authentication without credentials in source.

For CI/CD, design toward GitHub OIDC/workload identity federation to a least-privilege Databricks service principal.

### Initial module boundaries

Create empty/minimal modules only where needed by 001:

```text
contracts
temporal
evidence
persistence
acquisition.databricks
health
explanation
configuration
```

Do not scaffold every future microservice.

## Engineering standards

- all material Python public functions/classes typed;
- UTC/offset-aware timestamps only at domain boundaries;
- canonical IDs never represented as unvalidated display names;
- no vendor response dicts passed beyond adapter normalization boundary;
- logging is structured and must not emit secrets/raw sensitive payloads by default;
- deterministic code paths have no network/model dependency;
- tests should not depend on execution order;
- database/schema migrations are source controlled;
- implementation ADR required for any non-trivial tool choice that affects future compatibility.

## Acceptance gates

A fresh developer clone can, from documented commands:

1. install the project;
2. run formatter/lint checks;
3. run static type checks;
4. run unit test smoke suite;
5. render/check documentation consistency;
6. validate the Databricks bundle configuration for the dev profile once credentials are present;
7. show that no credential is stored in tracked files.

## Exit artifacts

- engineering/tooling ADR(s);
- repository structure committed;
- bootstrap README section/script;
- first CI workflow passing quality checks;
- environment capability checklist ready for 001-E/G.
