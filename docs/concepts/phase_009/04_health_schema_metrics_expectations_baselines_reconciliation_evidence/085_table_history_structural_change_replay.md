# INTG-085 — Table-History Structural Change & Replay

**Status:** Accepted — Phase 009 Group 04

Delta/Iceberg table history can provide versioned operation/time/provenance evidence and support bounded structural-change reconstruction when the relevant history is retained.

Default log-history retention and time-travel retention differ. Missing older table versions after retention expiry remains an evidence gap rather than proof that no structural change occurred.
