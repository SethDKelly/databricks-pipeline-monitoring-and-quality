@../AGENTS.md

# Claude Code adapter

This file exists only to bridge Claude Code to DMTZ's shared repository authority.

- Use `knowledge/index.md` for portable discovery when the relevant canonical resource is not already known.
- Keep Claude auto-memory, chat context, and tool-native state advisory only; correctness-critical facts belong in repository artifacts.
- Do not add Claude-specific semantic rules here. Shared behavior belongs in `AGENTS.md`; task-specific procedures belong in the portable workflow/skill layer introduced by ADF-D.
- Do not use subagents or agent teams for repository implementation under the current human-directed foundation; that remains deferred autonomous scope.
