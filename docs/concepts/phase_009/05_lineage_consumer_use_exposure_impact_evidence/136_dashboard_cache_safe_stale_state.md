# INTG-136 — Dashboard Cache & Safe/Stale State

**Status:** Accepted — Phase 009 Group 05

AI/BI dashboards can serve dashboard-cache results up to 24 hours old without running a warehouse query, and underlying data changes do not automatically invalidate that cache.

A viewer may therefore encounter a safe prior state, an affected cached state or an unknown cached state. `No current query` does not establish no dashboard encounter, and stale-safe state remains separate from freshness health.
