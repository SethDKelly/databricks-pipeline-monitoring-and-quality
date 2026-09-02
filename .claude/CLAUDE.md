@../AGENTS.md

# Claude Code adapter

This file exists only to bridge Claude Code to DMTZ's shared repository authority.

- Use `knowledge/index.md` for portable discovery when the relevant canonical resource is not already known.
- Canonical human-directed workflows live in `.agents/skills/<name>/SKILL.md`.
- Invoke the DMTZ workflow names through the thin `.claude/commands/<name>.md` bridges; those commands add no workflow semantics of their own.
- Keep Claude auto-memory, chat context, and tool-native state advisory only; correctness-critical facts belong in repository artifacts.
- Do not add Claude-specific semantic rules here. Shared behavior belongs in `AGENTS.md`; shared workflow meaning belongs in `.agents/skills/`.
- Do not create duplicate DMTZ workflows under `.claude/skills/`; Cursor also discovers Claude skill directories, so duplicate names would create avoidable ambiguity.
- Do not use subagents or agent teams for repository implementation under the current human-directed foundation; that remains deferred autonomous scope.
