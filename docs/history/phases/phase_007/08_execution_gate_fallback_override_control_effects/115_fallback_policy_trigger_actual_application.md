# OPS-115 — Fallback Policy, Trigger & Actual Application

**Status:** Accepted — Phase 007 Group 08

## Purpose

Prevent configured unavailable/timeout behavior from being mistaken for actual runtime behavior.

## Contract

A fallback policy binds:

- Gate/profile revision and applicable opportunity classes;
- exact trigger condition, such as readiness unavailable, control integration unavailable, timeout or another declared condition;
- authorized fallback action, such as hold, admit, escalate or cancel/expire where allowed;
- authority/effective interval;
- provenance and visibility constraints.

Actual fallback application separately binds trigger recognition, selected action, opportunity, time and enforcement evidence.

## Rules

- configured fallback ≠ trigger occurred;
- trigger occurred ≠ fallback action applied;
- fallback action issued ≠ enforced;
- fallback admission does not turn unknown/not-ready into ready;
- fallback hold does not prove a run was actually suppressed without REF-026 evidence;
- fallback is policy-driven behavior, not an opportunity-specific human override;
- no universal fail-open/fail-closed fallback is accepted.