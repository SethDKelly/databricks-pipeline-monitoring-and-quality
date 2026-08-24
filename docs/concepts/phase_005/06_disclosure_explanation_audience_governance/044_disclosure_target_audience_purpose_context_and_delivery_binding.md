# AUTH-044 — Disclosure Target, Audience, Purpose, Context, and Delivery Binding

**Status:** Accepted — Phase 005 Group 06

## Purpose
Bind every material disclosure decision to the exact audience/requester, information class/detail, purpose/context, subject, time perspective, and delivery scope so an audience label or generally permitted fact does not become universal disclosure permission.

## Contract
A material disclosure target should identify, where relevant:
- requester or receiving audience/principal set;
- requested statement/information class and detail level;
- subject/entity/context/environment;
- purpose/use context;
- temporal perspective and current disclosure time;
- delivery scope, such as private investigation, internal operational communication, business summary, client/external communication, or retained audit/review artifact;
- applicable Capability Authorization and disclosure/review conditions.

## Invariants
- `technical`, `business`, `executive`, `client`, `auditor`, or similar audience labels do not themselves grant disclosure capability.
- Permission to view information privately does not automatically grant permission to publish, forward, export, or disclose it to another audience.
- Permission in one environment, tenant, incident, purpose, or time does not silently transfer to another.
- The same underlying truth can support several authorized projections without creating several truth models.
- Delivery/channel technology is not selected here; the contract binds disclosure scope functionally.
- Current requester/disclosure authorization governs current disclosure even when the requested subject is historical.
