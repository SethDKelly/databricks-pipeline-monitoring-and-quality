# OPS-089 — Safeguard Applicability, Effective Scope & Interval

**Status:** Accepted — Phase 007 Group 07

## Purpose

Resolve whether a safeguard applies to a particular suspect state, consumer/path and opportunity at a particular time.

## Contract

Applicability is evaluated against:

- exact protected/suspect state or missing-output context;
- protection surface and target scope;
- effective Lineage/consumer path at the relevant time;
- consumer/cohort/region/interface constraints;
- activation/enforcement interval;
- exclusions/exceptions where explicitly governed;
- knowledge limitations.

A safeguard may be applicable to one opportunity and irrelevant to another even while its broader record is `active`.

## Invariants

- configured scope ≠ effective scope unless enforcement supports it.
- active interval overlap ≠ material applicability by timing alone.
- one cohort/region ≠ global scope.
- restricted path detail may limit visible applicability without making the path absent.
