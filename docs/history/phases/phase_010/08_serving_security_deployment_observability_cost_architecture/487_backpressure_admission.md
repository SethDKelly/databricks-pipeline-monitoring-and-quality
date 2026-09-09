# ARCH-487 — Backpressure & Admission

**Status:** Accepted

Overload uses bounded queues/concurrency, backpressure, shedding of eligible optional work and explicit unavailable/deferred responses rather than uncontrolled fan-out or silent evidence omission.

Required control and evidence behavior follows service-class policy.