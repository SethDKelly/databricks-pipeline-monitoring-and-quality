# EXPL-041 — Deployment Attempt, Activation & Active-State Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Was it deployed?`, `is the new version live?`, and `what was active?` must distinguish Deployment attempt/outcome, target/facet activation and active-state interval.

## Rules

- deployment attempt ≠ successful attempt ≠ activation;
- successful CI/workflow evidence does not automatically prove runtime activation;
- activation is target/facet/slice specific;
- active state can be composite across source/build, job/transformation definition, configuration, schema/interface and target context;
- activation does not prove downstream effect or run-specific version use;
- rollback/supersession creates new effective intervals without erasing history.

`Live` must be resolved to the exact activation proposition rather than used as a generic success label.