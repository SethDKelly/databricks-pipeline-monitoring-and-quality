# ARCH-179 — Query Selectivity & Partitioning

**Status:** Accepted

Bulk/table collection uses bounded predicates, partition/window strategies and source-supported incremental semantics to avoid oversized queries and unnecessary compute.

Partitioning must preserve coverage accounting so omitted partitions cannot disappear silently.
