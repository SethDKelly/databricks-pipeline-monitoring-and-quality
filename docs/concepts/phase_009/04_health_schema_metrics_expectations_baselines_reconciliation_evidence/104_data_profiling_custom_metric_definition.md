# INTG-104 — Data-Profiling Custom Metric Definition

**Status:** Accepted — Phase 009 Group 04

Data profiling supports aggregate, derived and drift custom metrics with explicit names, definitions, input columns and output types.

Custom metrics can implement framework metric definitions only when semantic identity/version/authority and measurement context are governed. Derived/drift outputs retain dependence on their underlying aggregate/source metrics rather than becoming independent corroboration.
