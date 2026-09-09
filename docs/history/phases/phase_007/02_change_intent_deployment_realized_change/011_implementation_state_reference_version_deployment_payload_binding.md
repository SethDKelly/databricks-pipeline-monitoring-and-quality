# OPS-011 — Implementation-State Reference, Version & Deployment Payload Binding

**Status:** Accepted — Phase 007 Group 02

## Purpose

Prevent one convenient identifier such as a Git commit, release tag or job name from being treated as the universal identity of what actually became active in runtime.

## Contract

A Deployment may carry or reference one or more implementation-state facets, including where available:

- source revision/reference;
- build/package/release identity exposed by the source system;
- job/task/logical-process definition version;
- transformation/query/notebook definition version;
- configuration/parameter/feature-setting state;
- schema/interface definition version;
- environment/target-specific binding;
- other source-defined immutable or versioned realization references.

Each reference retains source semantics and provenance. The framework does not invent a globally canonical version string when no source establishes one.

## Deployment payload binding

A deployment-attempt proposition should identify the implementation-state references it was intended to apply to the bounded target. Evidence may later establish that only a subset became active.

A repository revision can be strong provenance for code content while still being insufficient to prove:

- which built/package artifact was deployed;
- which runtime configuration accompanied it;
- which target accepted it;
- whether the target activated it;
- whether a long-running execution used it;
- whether downstream data state changed.

## Composite active state

The active operating state may legitimately be composite, for example:

**code R2 + configuration K7 + schema S3 + transformation T5**.

Those facets may change independently. A single Deployment can affect one or several facets; several Deployments can collectively produce the then-active composite state.

## Invariants

- repository commit ≠ deployed runtime identity unless evidence establishes the mapping;
- release/tag equality ≠ configuration equality;
- same source revision ≠ same operating state when configuration differs;
- same configuration label ≠ same state if source semantics/version changed;
- Deployment payload reference ≠ activation evidence;
- active-at-target ≠ specific execution consumed/used that state;
- there is no mandatory universal deployment/version token.

## Deferred integration detail

Phase 009 maps concrete GitHub Actions/Databricks/source evidence to these functional references. Phase 010 chooses any implementation representation.