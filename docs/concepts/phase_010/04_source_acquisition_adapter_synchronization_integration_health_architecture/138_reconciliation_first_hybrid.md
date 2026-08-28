# ARCH-138 — Reconciliation-First Hybrid Acquisition

**Status:** Accepted

The reference architecture uses durable reconciliation as the completeness/recovery foundation and permits incremental, stream, webhook or export channels as freshness accelerators.

A low-latency channel does not replace reconciliation where bounded coverage or missed-event recovery matters.
