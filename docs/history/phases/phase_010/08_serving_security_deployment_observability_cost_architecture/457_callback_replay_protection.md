# ARCH-457 — Callback Replay Protection

**Status:** Accepted

Material callbacks use bounded timestamps/nonces/event IDs/idempotency or equivalent replay defenses supported by the protocol, and duplicate delivery is retained as attempt provenance where useful.

Replayed control callbacks cannot create a new semantic decision or enforcement event.