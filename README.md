# infiniteleverage-plugin

> ⚠️ **Superseded — frozen.** This repo (and the `infiniteleverage-8-plugin` mirror) is replaced by
> the v2 plugin that ships directly from the canonical template repo:
> **https://github.com/talentedgeai/infiniteleverage-8-agents-template**
>
> No new features land here. Only critical safety fixes are accepted until all installs
> have migrated to v2, after which this repo will be archived.

## Why superseded

This repo was a hand-copied snapshot of the template repo's `setup-skills/`, mirrored by CI to a
third repo. The copies drifted (this repo still shipped skills deleted upstream), the mirror
workflow never ran, and the plugin's `hooks.json` pointed at `~/.claude/hooks/*` instead of
`${CLAUDE_PLUGIN_ROOT}` — so plugin updates never took effect without a manual copy step.

v2 collapses all of it into one repo that ships the plugin itself, with a bare-minimum payload
(2 skills, 2 opt-in telemetry hooks, no global writes). See the cleanup plan in the template repo.

## Migration

1. Remove this plugin/marketplace from your Claude Code settings.
2. Add the template repo as the marketplace and install `infiniteleverage` v2.
3. The v2 plugin's first session run cleans up residue that v1's `init`/`patch` copied into
   `~/.claude/` (agents, skills, hooks, rules, the `Bash(*)` permission grant).
