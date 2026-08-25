# INTG-132 — Query Source, Client Application & Consumer Context

**Status:** Accepted — Phase 009 Group 05

Query-history `query_source` can identify Databricks dashboard/job/notebook/Genie/query context; `client_application` can identify clients such as Tableau or Power BI when provided by the client.

These fields support consumer-mode context. Client-application labels are not stable ecosystem identity or proof that a human viewed/relied on the corresponding report.
