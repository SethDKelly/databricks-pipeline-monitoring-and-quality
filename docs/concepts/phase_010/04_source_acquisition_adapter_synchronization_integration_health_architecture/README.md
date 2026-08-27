# Phase 010 Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Status:** Next — not started

## Goal

Design source capability discovery, adapters/connectors, polling/streaming/hybrid acquisition, checkpoints, pagination, retries, quota handling, lag tracking, schema/API drift handling, integration health, and graceful degradation.

## Accepted entry contract from Groups 01–03

Group 04 consumes **ARCH-001–ARCH-132** and must preserve:

- deployment-bound capability instances and unknown preservation;
- Group 02 canonical evidence/provenance/time persistence and lifecycle semantics;
- tenant-scoped canonical Entity/Principal IDs plus evidence-bearing source identity bindings;
- Monitoring Scope as organization-owned expected coverage, not connector discoverability;
- Assertion Authority as explicit organization-owned rules, not source availability/role/title;
- Capability Authorization as principal/action/subject/context/detail specific;
- current authorization ≠ historical authorization ≠ actual retained authorization decision;
- service-principal processing permission ≠ requester disclosure permission;
- disclosure-dimensional exact/coarse/redacted/opaque/withheld projection semantics;
- retained/archived/stub evidence ≠ permission;
- unknown scope membership ≠ exclusion.

## Primary Phase 009 gaps

Primary ownership includes GAP-009-32–GAP-009-37 and GAP-009-39–GAP-009-40, plus acquisition responsibilities supporting all source-specific gaps.

## Connector rules

A source adapter must emit source-local identity, provenance, capability-instance context, collection coverage and integration-health facts into the accepted architecture. It must not:

- create canonical cross-system identity from names/timestamps;
- infer Monitoring Scope from whatever it can currently list;
- treat permission denial as source/domain absence;
- treat empty/partial pagination as strong negative evidence;
- promote source roles/permissions into Assertion Authority;
- silently fall back to a lower-authority source;
- expose collected evidence merely because the integration service principal can read it.

## Boundary

Source collection failure, throttling, permissions, lag, partial pagination, parser/schema errors, retention expiry, and optional-source absence remain integration-health states rather than monitored-domain negative facts.

Group 04 owns synchronization/acquisition mechanics, not the identity/authority truth model.