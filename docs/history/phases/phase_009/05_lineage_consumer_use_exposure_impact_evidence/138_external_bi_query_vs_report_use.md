# INTG-138 — External BI Query vs Report Use

**Status:** Accepted — Phase 009 Group 05

Databricks query/lineage evidence can observe SQL executed by external clients such as Tableau/Power BI when routed through covered compute and can identify the client application where reported.

This supports a data-query encounter, not the external platform's report-view, user-display, export, decision or customer consequence. Those require external instrumentation where material.
