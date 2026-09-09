# INTG-014 — Availability, Latency, Freshness & Knowledge Eligibility

Contracts distinguish source/service availability, retrieval success, observation/event production latency, publication/indexing latency, and the age of retrieved evidence.

Latency determines when evidence can legitimately participate in a knowledge cut; it does not change the event/effective time of the underlying fact.

An outage, permission failure, throttling or delayed index makes evidence unavailable/late for the affected interval. It cannot be converted into a negative product fact.

Where latency is variable or only bounded empirically, the contract records that limitation rather than inventing deterministic freshness.