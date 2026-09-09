# INTG-120 — Unity Catalog Table-Lineage Event Surface

**Status:** Accepted — Phase 009 Group 05

`system.access.table_lineage` is a bounded observational source for Unity Catalog/path read/write lineage events and associated Databricks entities. It does not represent every read/write event; records exist only where lineage can be inferred.

A captured event can support an observed relationship/read/write proposition for its exact source/target/entity/time context. Non-return cannot establish no lineage, no use or non-exposure without coverage evidence.
