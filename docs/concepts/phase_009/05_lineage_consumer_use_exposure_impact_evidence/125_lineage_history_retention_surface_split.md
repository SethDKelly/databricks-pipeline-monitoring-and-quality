# INTG-125 — Lineage History & Retention Surface Split

**Status:** Accepted — Phase 009 Group 05

Lineage system tables provide a rolling one-year event history. Catalog Explorer/lineage API can retain captured lineage after 2024-09-01 beyond that window, with different programmatic/detail semantics.

Historical Lineage replay is therefore source-surface/time-window bound; the indefinite catalog view does not restore system-table fields that aged out.
