# infiniteleverage (plugin payload)

> ⚠️ **Superseded — frozen.** See the root README. The v2 plugin ships from
> https://github.com/talentedgeai/infiniteleverage-8-agents-template — no new features land here.

## Contents (v1, for reference)

| Path | Purpose |
|---|---|
| `skills/` | Setup skills (`init`, `patch`, `project`, `validate`) — hand-copied snapshots of the template repo's `setup-skills/` |
| `hooks/session-start` | 4-stage SessionStart hook (init check, version, routing, usage) |
| `hooks/il_telemetry/` | Session effort telemetry (Stop/SessionEnd) |
| `hooks/hooks.json` | Hook registration — points at `~/.claude/hooks/*`, which is the core v1 defect: the files shipped here never run from the plugin |
