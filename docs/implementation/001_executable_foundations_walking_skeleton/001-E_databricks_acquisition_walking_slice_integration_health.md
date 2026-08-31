# 001-E — Databricks Acquisition Walking Slice & Integration Health

**Status:** Planned

## Goal

Implement one bounded real Databricks acquisition path while proving that source/API health is distinct from domain facts.

## Step 1 — Target capability discovery

Before selecting the source surface, record the development target's actual:

- cloud/region/workspace/account context;
- Unity Catalog/system-table availability;
- relevant API/system-table permissions;
- retention/publication-lag facts if discoverable;
- selected Databricks Runtime/CLI/SDK compatibility;
- service-principal/workload-identity capability.

Public documentation is possibility evidence, not deployment proof.

## Step 2 — Adapter contract

Create a vendor-neutral acquisition result envelope containing:

- source capability/surface revision;
- request/query/window/page identity;
- records returned;
- pagination/continuation state;
- coverage bounds;
- source publication/availability metadata where known;
- auth/permission/throttle/timeout/schema/parser status;
- retryability;
- checkpoint candidate;
- acquisition timestamps.

The adapter emits evidence + collection facts, not health/quality conclusions.

## Step 3 — First source family

Select one stable bounded Databricks evidence family from the pilot environment. Preferred candidates are job/run/task evidence or another surface with clear identity/time semantics.

The first adapter does **not** need to collect every source required by the final product.

## Step 4 — Normalization

Map source records into versioned DMTZ evidence/provenance contracts. Preserve the original source identity and material fields needed for replay/audit. Quarantine unknown/breaking schema shapes instead of silently dropping them.

## Step 5 — Integration health

Persist/emit distinct states for:

- successful complete acquisition;
- successful partial acquisition;
- no matching source records with sufficient coverage;
- permission denied;
- authentication failure;
- throttle/rate limit;
- timeout/outage;
- publication delay/known lag;
- partial pagination;
- schema/parse incompatibility;
- unsupported/unavailable capability.

None of those error states may be translated into `no run`, `no data`, `fresh`, `stale`, or other domain proposition automatically.

## Checkpoint safety

Advance a durable high-water mark only when the contract proves the relevant window/page coverage was safely handled. Retry/redelivery must be idempotent.

## Acceptance gates

Tests + development integration prove:

- one real Databricks source surface can be acquired and persisted;
- 401/403/throttle/timeout/schema-error simulations remain integration-health states;
- partial pagination cannot advance an unsafe checkpoint;
- redelivery does not duplicate canonical evidence;
- source lag is visible separately from framework processing lag;
- adapter code contains no health/causal/business conclusions.
