# INTG-075 — Lakeflow Pipeline Update Identity & Lifecycle

**Status:** Accepted — Phase 009 Group 03

Lakeflow pipeline configuration/update system surfaces provide a distinct pipeline/update execution identity and lifecycle source family. Pipeline update is not silently normalized into a Jobs run.

Pipeline deployment/configuration provenance and run-specific source/input/output versions require their own supported fields/correlation. Pipeline success alone does not prove output health or exact input consumption.
