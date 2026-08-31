# Phase 010 Group 09 — Security / Trust Boundary View

**Status:** ACCEPTED

Security architecture enforces accepted identity, Capability Authorization, disclosure, tenant/residency and active-control semantics; it does not replace them with network/IAM convenience.

## Trust boundary A — Human / external application caller

Untrusted until authenticated and bound to a canonical Principal/request context.

Required controls:

- target-approved identity federation/authentication;
- session/token validation;
- tenant binding;
- purpose/delivery/action/detail context where policy requires it;
- request limits and correlation identity.

Authentication only answers who/what is presenting a credential. It does not establish DMTZ Capability Authorization or Assertion Authority.

## Trust boundary B — Serving/API façade

Trusted to orchestrate authorized DMTZ operations but not trusted to invent truth.

Required controls:

- current requester Capability Authorization/disclosure evaluation;
- bounded query/replay/basis/control commands;
- authorization-sensitive cache partitioning/revalidation;
- response epistemic envelope;
- export/onward-use checks where policy requires;
- audit correlation.

The API identity used to read internal data cannot be inherited by the caller.

## Trust boundary C — Internal workload plane

Acquisition, evaluation, reasoning, archive and control workloads use distinct least-privilege identities where practical.

Rules:

- prefer short-lived federated/OAuth/OIDC workload credentials when verified target capability supports them;
- long-lived/static secrets are exceptions with governed storage/rotation;
- secrets are referenced, not copied into canonical evidence/logs/traces;
- workers receive only the data/tool scope required for their role;
- optional model/search tools do not receive unrestricted database credentials.

## Trust boundary D — Canonical governed data plane

Canonical Delta/evidence/policy stores are high-trust integrity assets.

Controls include:

- governed catalog/storage permissions;
- tenant/residency partitioning;
- controlled write paths;
- schema/migration versioning;
- encryption/storage controls supplied by the deployment platform;
- backup/restore policy;
- auditability of privileged access and material policy changes.

Direct UI mutation and unrestricted general-user access are rejected.

## Trust boundary E — Source systems

Databricks, GitHub and optional external systems remain separate security/authority domains.

Each adapter binds:

- exact capability instance;
- workload identity/credential;
- network endpoint;
- source permissions;
- source query/surface;
- minimization and retention policy;
- observed integration health.

A 401/403/observer-relative 404 is not domain absence.

## Trust boundary F — External callbacks / control edges

Webhooks, attestations, GitHub deployment protection callbacks and other control signals cross an untrusted network/application boundary.

Material callbacks require protocol-appropriate authenticity/integrity verification, expected opportunity/request binding, replay/idempotency protection and durable attempt/correlation provenance.

Callback receipt does not prove downstream enforcement unless the exact source/control evidence establishes it.

## Trust boundary G — Optional model/search provider

Evidence minimization and authorization occur **before** sensitive content/metadata is exposed to optional retrieval/model paths where the metadata itself can leak protected facts.

The model/provider may:

- parse ambiguous language;
- suggest leads;
- retrieve candidates;
- render authorized Statement IR.

It may not establish domain facts, Assertion Authority, negative coverage, causal confirmation, Impact, authorization or control decisions.

## Trust boundary H — Archive / backup / DR

Cold/backup copies retain the same tenant/residency/disclosure constraints as recent material.

Archive location does not declassify evidence. Restore permissions and operations are audited. A restored record preserves original evidence identity/time semantics and does not retroactively change prior availability-by-K.

## Active-control privilege boundary

SC-06 control components are high-consequence workloads. The architecture requires:

- exact Capability Authorization for normal/override/fallback/control actions where applicable;
- bounded decision applicability horizons;
- revalidation for revocation-sensitive delayed irreversible action when policy requires;
- separation between decision authority, delivery and actual enforcement evidence;
- explicit degraded-dependency behavior;
- no model/search-generated control decision.

## Tenant and residency invariant

Tenant/residency boundaries apply to:

- canonical data;
- governance metadata;
- derived graphs/search/vector stores;
- response caches;
- logs/traces/metrics;
- model grounding packets;
- archive/backups.

A shared service is allowed only when logical/physical controls prevent unauthorized cross-boundary visibility, including counts, identifiers and hidden basis metadata.

## Threats explicitly blocked by architecture

- service-principal privilege inherited by end user;
- cached privileged response served to another requester;
- hidden basis counts/source names leaked through UI or retrieval metadata;
- model/vector corpus containing records the requester/model path was never authorized to see;
- spoofed/replayed control callback creating a semantic decision;
- long-lived credential becoming the universal runtime identity;
- raw secrets copied into manifests/logs/Explanations;
- archive or backup bypassing current disclosure policy;
- current membership/authorization backfilled into historical truth;
- network isolation being treated as a substitute for application authorization.
