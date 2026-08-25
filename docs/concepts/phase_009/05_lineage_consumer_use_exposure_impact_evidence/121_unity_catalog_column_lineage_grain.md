# INTG-121 — Unity Catalog Column-Lineage Grain

**Status:** Accepted — Phase 009 Group 05

`system.access.column_lineage` can support source-column→target-column/read relationships when captured. Missing column lineage can reflect unsupported constructs, path references, UDFs or other capture limitations rather than absence of a field relationship.

Column names remain source-local identifiers; rename/recreate continuity still requires Entity Identity evidence.
