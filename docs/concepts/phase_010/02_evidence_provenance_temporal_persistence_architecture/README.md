# Phase 010 Group 02 — Evidence, Provenance, Temporal & Persistence Architecture

**Status:** Next — not started

## Goal

Select the durable representation and persistence architecture for source evidence, proposition/basis identity, provenance, bitemporal coordinates, correction/supersession, common derivation, retention, replay, and durable traceability.

## Accepted entry contract from Group 01

Group 02 consumes **ARCH-001–ARCH-032** and must preserve:

- public/vendor fact ≠ target-environment fact ≠ requirement ≠ assumption ≠ unknown;
- deployment-bound, multidimensional capability instances rather than vendor-wide Booleans;
- proposition/service-class-specific usability;
- capability history/freshness and unknown preservation;
- hard semantic/evidence/security/degraded-state constraints;
- SC-01–SC-06 service classes;
- decision-specific quality tradeoffs with no universal architecture score;
- ADR evidence/alternatives/reversibility discipline;
- explicit MVP/enterprise boundary;
- GAP-009 ownership and treatment.

Persistence options may depend on capability facts only where the target deployment verifies them or the assumption/unknown is explicitly safe and recorded.

## Primary Phase 009 gaps

Primary ownership or persistence responsibility includes GAP-009-25–GAP-009-30 plus persistence implications from GAP-009-03, 06, 07, 12, 13 and 19.

## Primary questions

- What canonical durable evidence/provenance representation best preserves accepted source identity and statement-to-basis semantics?
- Which data belongs in relational/lakehouse/object/graph/search representations, if multiple are used?
- What is the system of record for immutable/raw source evidence versus normalized/derived architecture state?
- How are event/effective, source-recorded/available, collection/knowledge, correction/supersession and communication times represented?
- How are common derivation and duplicate evidence retained without false corroboration?
- How does retention differ by service class and product commitment?
- How are source deletions/truncation/encryption/expiry represented while stable provenance references survive?
- How are schema evolution, migrations, archival, compaction and restoration handled without historical rewriting?
- What storage/indexing choices support reasoning graph traversal without making graph traversal truth?
- How do cost, quota, portability, security/residency and operational simplicity affect the persistence choice?

## Boundary

Persistence technology must conform to accepted time/evidence semantics; it cannot redefine them. Copied evidence remains source-owned and does not become newly authoritative or independent.

Group 02 must not assume that a Databricks/GitHub/Collibra/Immuta surface is present in every deployment because the public documentation describes it.
