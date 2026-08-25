# INTG-126 — Lineage Rename & Identity-Continuity Gap

**Status:** Accepted — Phase 009 Group 05

Databricks does not preserve Unity Catalog lineage through object/column renames as universal continuity. Historical cross-rename traversal therefore requires explicit Entity Identity reconciliation or another retained mapping.

A new name does not erase prior lineage; the source simply cannot be assumed to connect the identities automatically.
