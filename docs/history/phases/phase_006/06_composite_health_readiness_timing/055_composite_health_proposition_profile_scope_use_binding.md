# HLTH-055 — Composite Health Proposition, Profile, Scope & Use Binding

**Status:** Accepted — Phase 006 Group 06

## Purpose

Define composite health as a derived Assessment over an explicit bounded set of component Assessments rather than as an intrinsic scalar property of an asset.

## Binding

A composite health proposition binds, where material:

- subject/output/interface identity;
- consumer or intended operational/business use;
- composite profile/version;
- component dimensions/checks/reconciliation Assessments and their roles;
- required, optional, conditional or alternative component semantics;
- effective/current-cycle/window context;
- evaluation and knowledge time.

## Rules

- `Table C is healthy` without a profile/use/context is too broad for a high-confidence conclusion.
- Different consumers or uses may legitimately have different composite profiles while sharing the same underlying component truth.
- Composite health is a derived **Assessment**, not a new concept or independent truth model.
- Component profile membership remains governed under the accepted Phase 005 metric/profile authority rules.
- Diagnostic/on-demand results do not silently enter a routine composite profile.
- Current profile versions do not rewrite historical composite results.

## Non-goals

- universal health score;
- UI badge design;
- choosing computation/storage architecture.