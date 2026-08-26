# ARCH-048 — Logical Occurrence vs Physical Deduplication

**Status:** Accepted

The architecture MAY deduplicate identical payload bytes/objects physically while retaining distinct logical evidence occurrences when source/time/context identity differs.

Storage deduplication must never collapse materially distinct evidence occurrences or invent source independence.
