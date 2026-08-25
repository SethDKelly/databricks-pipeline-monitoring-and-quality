# OPS-105 — Execution Gate Proposition: Target, Opportunity, Configuration & Knowledge Cut

**Status:** Accepted — Phase 007 Group 08

## Purpose

Bind every gate decision to the exact downstream start/admission opportunity it controls rather than treating a gate as a timeless job-wide status.

## Contract

A Gate proposition identifies, where material:

- gate identity and exact configuration/profile revision;
- downstream execution target and environment/slice;
- specific execution opportunity, trigger/window/cycle or other bounded admission context;
- applicable prerequisite/criterion profile revision;
- evaluation/decision time and knowledge cut;
- authorization/control-principal context;
- relevant limitations or restricted details.

## Invariants

- gate configuration ≠ execution opportunity;
- enabled configuration ≠ decision for every future opportunity;
- schedule expectation ≠ actual opportunity unless the applicable control semantics/evidence establish one;
- current configuration is not projected backward into historical opportunities;
- one decision cannot silently apply to another target/environment/cycle.

Execution History remains the owner of actual execution identity; Gate owns only admission-control propositions.