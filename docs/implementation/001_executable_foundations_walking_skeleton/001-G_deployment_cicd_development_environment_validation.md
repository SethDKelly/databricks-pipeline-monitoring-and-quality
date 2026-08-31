# 001-G — Deployment, CI/CD & Development-Environment Validation

**Status:** Planned

## Goal

Make the 001 walking skeleton reproducibly testable/deployable by automation rather than a developer-specific workspace setup.

## Databricks packaging

Use Declarative Automation Bundles as the reference packaging/deployment mechanism for Databricks-owned jobs/resources in the 001 slice.

Create focused dev/test targets. Do not create a universal production bundle or production resource topology yet.

## GitHub Actions CI

PR checks should run, at minimum:

```text
checkout
  ↓
dependency install from lockfile
  ↓
format/lint
  ↓
type check
  ↓
unit + contract + fixture tests
  ↓
documentation consistency
  ↓
bundle validate
```

A protected integration workflow may then authenticate to the development Databricks target and run the selected integration/scenario suite.

## CI/CD identity

Prefer OIDC/workload identity federation from GitHub Actions to a dedicated least-privilege Databricks service principal when the target deployment supports it.

Do not store long-lived Databricks PATs in GitHub secrets if federation is available. If federation is not available, record the verified environment limitation and use the enterprise-approved temporary credential strategy with rotation.

## Environment isolation

Use explicit resource naming/catalog/schema prefixes or equivalent isolation so concurrent developer/test runs do not overwrite one another's canonical history unintentionally.

## Deployment validation

Automated deployment should prove:

- bundle validates against the dev target;
- required code/resources deploy;
- selected acquisition job/function can execute;
- canonical Delta tables are reachable with the intended workload identity;
- integration-health telemetry is produced;
- the freshness vertical slice can run from acquired/pilot evidence;
- deployment rollback/redeploy does not rewrite canonical semantic history.

## Supply-chain baseline

Where enterprise tooling permits:

- pin actions/dependencies;
- scan dependencies;
- restrict workflow permissions;
- protect environments/branches used for deployment;
- preserve build/deployment provenance.

## Acceptance gates

A clean merge can be validated/deployed to the development target by CI without a human copying notebooks or pasting credentials, and the 001 end-to-end scenario can be rerun reproducibly.
