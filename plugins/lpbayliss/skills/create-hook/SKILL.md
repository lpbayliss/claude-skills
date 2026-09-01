---
name: create-hook
description: Use when writing, editing, or debugging a Claude Code hook — hook scripts, settings.json hook configuration, matchers, or hook JSON output. Do not use for authoring skills or slash commands, git hooks, or MCP servers.
license: MIT
metadata:
  author: lpbayliss
  version: "1.0.0"
---

# Create Hook

Hooks are small programs the harness runs at lifecycle events. Keep them simple, lightweight, and working on macOS, Linux, and Windows alike.

<workflow>
1. Pick the narrowest event and matcher that observes what you need — full event table in `references/hooks-reference.md`.
2. Write the handler following <principles>, modeled on <example>.
3. Wire it into settings at the right scope (user `~/.claude/settings.json` vs project `.claude/settings.json`), then verify BOTH cases: the event fires and acts, and unrelated activity passes through untouched.
</workflow>

<principles>
- **Simple**: one script, one decision. A hook that wants config files and helpers wants to be a skill or CLI instead.
- **Lightweight**: hooks run often and block the loop. Do the check, exit. No network calls unless `async: true`; stay well inside the event's timeout.
- **Cross-platform by default**: exec form (`"command": "node", "args": [...]`) so no shell ever parses the command; script logic in Node or Python stdlib — no `jq`, `grep`, or bash-isms. Split paths on both `/` and `\`. Only write shell-form one-liners when a single platform is the explicit target.
- **Paths**: always `${CLAUDE_PROJECT_DIR}` (or `${CLAUDE_PLUGIN_ROOT}` inside plugins), never relative — cwd moves during sessions.
- **Current output schema**: block via `hookSpecificOutput` decisions or exit code 2. `{"continue": false}`-style fields are outdated and silently ignored — a hook that "works" but never blocks usually has this bug. Exit 0 with no output means no opinion.
- **Choose your failure mode**: a crashing hook (exit 1) does NOT block. If the hook is a guardrail, route errors to exit 2 (fail closed); if it's a convenience, let it fail open.
</principles>

<example>
Block edits to `.env` files, everywhere:

`.claude/hooks/block-env-edit.mjs`
```js
const chunks = [];
for await (const c of process.stdin) chunks.push(c);
const input = JSON.parse(Buffer.concat(chunks).toString());

const file = input.tool_input?.file_path ?? "";
const name = file.split(/[\\/]/).pop() ?? "";   // handles / and \

if (name === ".env" || name.startsWith(".env.")) {
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: `${name} is blocked by hook; edit it manually.`,
    },
  }));
}
// no output, exit 0: no opinion — normal permission flow applies
```

`.claude/settings.json`
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/block-env-edit.mjs"]
          }
        ]
      }
    ]
  }
}
```

Exec form + Node stdlib: identical behavior on all three platforms, no shell quoting, no external dependencies.
</example>

<references>
- `references/hooks-reference.md` — events, matchers, config shape, stdin fields, exit codes, output schema, placeholders, platform shell behavior. Distilled September 2026 from the canonical docs: https://code.claude.com/docs/en/hooks — recheck there when behavior surprises.
</references>
