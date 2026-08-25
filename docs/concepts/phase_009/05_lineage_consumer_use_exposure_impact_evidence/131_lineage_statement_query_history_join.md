# INTG-131 — Lineage `statement_id` ↔ Query-History Join

**Status:** Accepted — Phase 009 Group 05

For SQL-warehouse lineage events, lineage `statement_id` is an explicit foreign key to `system.query.history`. This is a strong association from a captured source read/write event to the exact statement execution.

The join strengthens encounter provenance but does not create missing exact data-version identity, downstream business use or causal attribution.
