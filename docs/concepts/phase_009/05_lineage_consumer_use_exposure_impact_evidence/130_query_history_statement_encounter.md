# INTG-130 — Query-History Statement Encounter

**Status:** Accepted — Phase 009 Group 05

`system.query.history` provides statement execution identity, actor/executed-as principal, timing, status, query source, client application and read/produced metrics for covered SQL warehouse/serverless queries.

A successful statement plus matching source-read evidence is strong query/read encounter evidence. Query execution alone does not identify every table/version consumed.
