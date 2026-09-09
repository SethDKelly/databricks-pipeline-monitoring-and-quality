# INTG-009 — Temporal Coordinate Contract

For each material field/event, record which temporal coordinates the surface actually supplies and what they mean.

Potential coordinates include source event/occurrence time, effective/valid interval, source recorded/committed time, correction/supersession time, first reliably retrievable/available time, and extraction/retrieval time.

These coordinates are not interchangeable. A historical event timestamp returned today does not establish that the record was known or available at the historical knowledge cut.

Clock domain, precision, timezone, ordering guarantees and known skew/uncertainty are recorded when material to joins, sequencing or cutoff reasoning.