# ARCH-142 — Webhook / Push Acceleration

**Status:** Accepted

Webhook delivery identifiers, signatures, event types and delivery attempts are retained where available, and webhook processing is idempotent.

Push delivery is a latency accelerator; failed/missed deliveries and finite redelivery windows require reconciliation rather than an assumption of complete event history.
