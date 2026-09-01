# Claude Code Hooks Reference (distilled)

Distilled September 2026 from the canonical documentation — verify against it when anything surprises:

- https://code.claude.com/docs/en/hooks — full reference
- https://code.claude.com/docs/en/hooks-guide — tutorial

## Where hooks live

| Location | Scope |
| --- | --- |
| `~/.claude/settings.json` | All projects on the machine |
| `.claude/settings.json` | One project, committed |
| `.claude/settings.local.json` | One project, gitignored |
| Plugin `hooks/hooks.json` | While the plugin is enabled |
| Skill / subagent frontmatter `hooks:` | After skill invoked / while subagent runs |

Hooks from all sources merge; identical handlers are deduped. `disableAllHooks: true` turns everything off.

## Configuration shape

```json
{
  "hooks": {
    "<EventName>": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "node", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/x.mjs"] }
        ]
      }
    ]
  }
}
```

Three levels: event → matcher group → handlers.

## Events (the ones that matter most)

| Event | Fires | Exit 2 blocks? |
| --- | --- | --- |
| `PreToolUse` | Before a tool call | Yes — blocks the call |
| `PostToolUse` | After a tool call succeeds | No (tool already ran; stderr shown to Claude) |
| `PostToolUseFailure` | After a tool call fails | No |
| `UserPromptSubmit` | Before Claude sees a prompt | Yes — erases the prompt |
| `Stop` / `SubagentStop` | When Claude / a subagent finishes | Yes — forces continuation |
| `SessionStart` | Session begins/resumes | — (stdout becomes context) |
| `SessionEnd` | Session terminates | — (1.5s total budget) |
| `Notification` | Claude Code notifies | — |
| `PreCompact` / `PostCompact` | Around context compaction | — |
| `PermissionRequest` | Tool call needs permission decision | No — use decision object |
| `ConfigChange` | A settings file changes mid-session | Yes |
| `FileChanged` | A watched file changes (matcher = filenames) | — |

Many more exist (SubagentStart, TaskCreated/Completed, PreModelSwitch, WorktreeCreate, StopFailure, …) — see the canonical docs.

## Matchers

- `"*"`, `""`, or omitted → match everything.
- Plain names / `|` lists → exact tool match: `Bash`, `Edit|Write`.
- Anything else → JS regex, unanchored: `mcp__memory__.*`, `^Notebook`.
- Non-tool events match other things: `SessionStart` matches `startup|resume|clear|compact`, `Notification` matches notification types, `FileChanged` matches literal filenames.
- MCP tools are named `mcp__<server>__<tool>`.

## Command handler fields

| Field | Notes |
| --- | --- |
| `command` | Executable (exec form) or shell string (shell form) |
| `args` | Presence switches to exec form: spawned directly, NO shell involved |
| `shell` | `"bash"` or `"powershell"`; shell-form only |
| `timeout` | Seconds; default 600 (30 on prompt-ish events) |
| `async` | Run in background, don't block |
| `asyncRewake` | Background; exit 2 later wakes Claude with stderr |
| `if` | Permission-rule filter, e.g. `"Bash(git *)"`, `"Edit(*.ts)"` |
| `statusMessage` | Spinner text while running |

Other handler types exist: `http` (POST the input JSON), `mcp_tool`, `prompt`, `agent`.

## Exec form vs shell form — the cross-platform crux

- **Exec form** (`args` present): `command` resolved on PATH and spawned directly. No shell quoting, no platform divergence. **Prefer this.** Windows caveat: must be a real executable — `.cmd` shims (npm bins) need `"command": "node", "args": ["path/to/cli.js", ...]`.
- **Shell form** (no `args`): runs under `sh -c` on macOS/Linux; on Windows under Git Bash if installed, **else PowerShell** — the same string must parse in both, which is why shell-form one-liners are a portability trap.

## Input (stdin JSON / HTTP body)

Common fields: `session_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`. Tool events add `tool_name` and `tool_input` (e.g. `tool_input.file_path` for Edit/Write, `tool_input.command` for Bash). Subagent events add `agent_id` / `agent_type`.

Windows note: `file_path` values may use `\` — split on both separators.

## Exit codes

| Exit | Meaning |
| --- | --- |
| `0` | Success. Stdout parsed as JSON if it starts with `{` and ends with `}`; otherwise debug-logged (except UserPromptSubmit/SessionStart, where plain stdout becomes context) |
| `2` | Blocking error on events that can block (see table above). Reason = decision reason or stderr |
| other | Non-blocking; valid JSON output still honored. A crashing guardrail FAILS OPEN |

## Output schema (current — older `continue`/`decision` top-level fields are gone)

Tool-permission events (`PreToolUse`, `PermissionRequest`, …):

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "why"
  }
}
```

`permissionDecision`: `"deny"` | `"allow"` | `"default"`.

Block-style events (`UserPromptSubmit`, `Stop`, `SubagentStop`, `ConfigChange`, …):

```json
{
  "hookSpecificOutput": { "hookEventName": "Stop", "block": true, "blockReason": "why" }
}
```

Also available on most events: `systemMessage` (string shown to Claude), `additionalContext`, `updatedInput` (rewrite tool input), `terminalSequence` (bell/notification escape codes).

## Placeholders and environment

| Name | Meaning |
| --- | --- |
| `${CLAUDE_PROJECT_DIR}` / `$CLAUDE_PROJECT_DIR` | Project root where the session started (stays put in worktrees — read `cwd` from input for the live dir) |
| `${CLAUDE_PLUGIN_ROOT}` | Installed plugin directory (for plugin-bundled hooks) |
| `${CLAUDE_PLUGIN_DATA}` | Plugin persistent data dir |

## Debugging

- `/hooks` menu lists every configured hook and its source file.
- Exit-0 stdout/stderr go to the debug log, not the transcript — run `claude --debug` when a hook seems silent.
- A hook that never blocks despite firing usually outputs an outdated schema: the JSON parses, fails validation, and the action proceeds as a non-blocking error.
