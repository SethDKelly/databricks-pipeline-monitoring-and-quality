# 001-B — Canonical Type System, Contract Schemas & Versioning

**Status:** Planned

## Goal

Make the most important cross-cutting DMTZ distinctions impossible—or at least difficult—to accidentally collapse in code.

## Core primitive types

Define strongly typed opaque identifiers for at least:

- `EntityId`;
- `PrincipalId` seam for future 002 use;
- `EvidenceId`;
- `SourceRecordId` / source locator;
- `ExpectationId` and revision;
- `ObservationId`;
- `AssessmentId`;
- `StatementId`;
- acquisition run/attempt/request/page/checkpoint IDs;
- schema/version IDs.

Source-local IDs remain data inside provenance structures; they are not interchangeable with canonical IDs.

## Temporal model

Create explicit types/fields for the material time coordinates needed by 001:

- event/effective time or interval;
- source-produced/observed time where available;
- source-first-available time where available;
- framework retrieved/collected time;
- framework recorded/knowledge time;
- correction/supersession time;
- requested knowledge cut `K`.

Do not use one generic `timestamp` field where semantics differ.

## Evidence/provenance envelope

Define a reusable evidence envelope containing, as applicable:

- evidence identity;
- source system/surface/version;
- source-local locator;
- subject/context/grain;
- temporal coordinates;
- acquisition provenance;
- payload/reference/hash/minimization state;
- correction/supersession linkage;
- known source limitations/coverage metadata.

## Health walking-skeleton contracts

Define versioned schemas for:

- freshness Expectation revision;
- freshness Observation;
- freshness Assessment;
- statement/basis reference;
- Statement IR minimum subset.

Statement IR minimum fields should include:

- statement/proposition identity/type;
- subject;
- temporal perspective / knowledge cut;
- status/outcome;
- exact basis references;
- limitations/coverage state;
- schema/rendering revision metadata.

## Status vocabulary

Represent states explicitly. Do not overload null/Boolean for states such as:

- supported / partial / unsupported / unavailable;
- known / unknown / conflicting;
- pass / fail / pending / not-applicable where the owning contract allows them;
- fresh / stale as Assessment outcomes only after the normative criterion is evaluated.

## Schema versioning policy

Each persisted/external contract carries:

- schema name/type;
- schema version;
- compatibility policy;
- migration/upcast strategy where required.

Rules:

- adding optional fields may be backward-compatible;
- semantic reinterpretation of an existing field requires a new version;
- enum/status changes require explicit compatibility review;
- persisted historical records retain the schema version under which they were recorded;
- migration may change representation, not historical meaning.

## Acceptance gates

Tests prove:

- canonical/source IDs cannot be freely substituted;
- naive/ambiguous datetimes are rejected at domain boundaries;
- a record cannot claim a knowledge time before framework recording without an explicit accepted historical import mechanism;
- Statement IR cannot omit its subject/time/status/basis/limitation envelope when those are required;
- schema round-trip serialization is deterministic;
- incompatible schema versions fail explicitly rather than silently coercing.
