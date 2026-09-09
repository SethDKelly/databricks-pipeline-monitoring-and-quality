# INTG-042 — Databricks Audit / Information-Schema History Boundary

**Status:** Accepted — Phase 009 Group 02

Unity Catalog Information Schema is a current, privilege-aware metadata projection. It is not a complete historical ledger. The Databricks audit system table provides historical operational/security events with documented scope and retention, but event availability must be verified per proposition.

The system audit table currently has a documented 365-day free retention period and Public Preview status; long-horizon replay requires an external retention strategy if needed.
