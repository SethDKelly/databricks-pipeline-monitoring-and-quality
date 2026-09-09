# ARCH-218 — Exact Table-Version Consumption

**Status:** Accepted

Exact Delta/Iceberg table version consumption is accepted only when query/runtime instrumentation or authoritative source evidence binds that version to the execution.

Table history/latest version and timestamp proximity cannot manufacture the consumed version.