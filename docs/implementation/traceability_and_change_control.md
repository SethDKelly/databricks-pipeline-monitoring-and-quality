# Traceability & Change Control

## Why this exists

DMTZ has a large accepted contract stack. Implementation must make those contracts discoverable from code/tests without forcing developers to reread every phase for every change.

## Required traceability

Every material implementation epic/group should record:

- incoming SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH ranges or exact IDs;
- code module(s) realizing the behavior;
- schema/table/API artifacts involved;
- executable tests proving the contract;
- environment assumptions/capability facts;
- unresolved gaps/limitations.

Traceability may be stored as Markdown plus machine-readable YAML/JSON once code begins.

## Contract tags

Tests and ADRs should use stable tags where practical, for example:

```text
ARCH-017
REF-004
AUTH-034
HLTH-030
OPS-067
EXPL-101
INTG-145
```

Tags are references, not implementation package IDs.

## Implementation ADRs

Use implementation ADRs for choices such as:

- exact Python/runtime version;
- schema library;
- bundle layout;
- table partitioning/clustering;
- API framework;
- event/queue technology;
- cache/search/graph product;
- secrets/IAM realization;
- observability platform.

An ADR may select **how** a frozen contract is realized. It may not change **what the contract means**.

## Architecture change request threshold

Raise an architecture change request only when all are true:

1. a specific accepted architecture contract cannot be realized in the target deployment;
2. reasonable implementation alternatives were attempted or evaluated;
3. narrowing the deployment capability/product promise is unacceptable;
4. added instrumentation/attestation cannot solve it; and
5. the proposed change does not merely optimize developer convenience.

The request must state affected ARCH/earlier contracts and scenario consequences.

## Functional semantics reopening

Functional semantics are reopened only when the product requirement intentionally changes or an unavoidable real-world scenario proves the accepted concept model unable to represent required truth.

Vendor limitations alone normally cause capability narrowing or architecture adaptation, not semantic rewriting.
