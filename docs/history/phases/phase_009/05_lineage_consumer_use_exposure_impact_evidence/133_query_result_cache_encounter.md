# INTG-133 — Query Result Cache Encounter

**Status:** Accepted — Phase 009 Group 05

Query history exposes `from_result_cache` and `cache_origin_statement_id`. A cached statement can therefore be linked to the statement that originally populated the result cache where retained.

Cached result receipt remains an encounter with cached state, not proof that the underlying source was freshly read at receipt time.
