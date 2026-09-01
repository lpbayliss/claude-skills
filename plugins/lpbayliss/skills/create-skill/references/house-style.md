# House Style — Full Conventions

Load this when actually authoring; SKILL.md carries the summary.

## Naming

| Good | Bad | Why |
| --- | --- | --- |
| `write-dockerfile` | `dockerfile-best-practices` | Verb-first says what you DO |
| `plan-presentation` | `presentation-planning` | Action, not gerund noun |
| `create-skill` | `skill-creator-lpb` | No namespacing suffixes; the verb disambiguates |

## Trigger descriptions

Shape: `Use when <specific situations>. Do not use for <adjacent-but-out-of-scope work>.`

- Specific beats exhaustive: name the artifacts and symptoms that should trigger, not every synonym.
- Never describe the skill's process or contents — agents will follow the summary instead of reading the skill.
- Third person. Two sentences is the ceiling.

## Eval files

Every skill ships `evals/` with both files. Fixtures go in `evals/files/` when a prompt needs a repo or document to work against.

`evals/trigger-evals.json` — positive, negative, AND boundary cases:

```json
[
  { "query": "Draft a skill for reviewing database migrations", "should_trigger": true },
  { "query": "The trigger description on my metrics skill fires too eagerly — tighten it", "should_trigger": true },
  { "query": "Install the skill-creator plugin for me", "should_trigger": false },
  { "query": "Use the write-dockerfile skill to containerize this app", "should_trigger": false }
]
```

`evals/evals.json` — behavioral cases with assertions:

```json
{
  "skill_name": "example",
  "evals": [
    {
      "id": 1,
      "kind": "authoring",
      "prompt": "…realistic task prompt…",
      "expected_output": "…one-sentence shape of a good answer…",
      "assertions": [
        "Checkable, specific claims about the output",
        "Each assertion independently verifiable"
      ],
      "files": []
    }
  ]
}
```

## Registration

Own skills all live inside the single base plugin `plugins/lpbayliss/` — do NOT create a new plugin or marketplace entry per skill. To register a new skill:

1. Add its directory under `plugins/lpbayliss/skills/<verb-name>/`.
2. Bump the `version` in `plugins/lpbayliss/.claude-plugin/plugin.json` and mention the skill in its `description`.
3. Add a row to the README's curated table.
4. Run `claude plugin validate .` before committing.

## Complete skeleton

```
plugins/lpbayliss/
  .claude-plugin/plugin.json      # base plugin: semver version, author, license MIT
  skills/<verb-name>/
    SKILL.md                      # <500 words; XML-tagged sections; one worked example
    references/<topic>.md         # depth, loaded on demand
    evals/evals.json
    evals/trigger-evals.json
    evals/files/                  # fixtures, only if evals need them
```

## Model selection for delegating skills

When a skill instructs Claude to dispatch subagents, it states the model per task:

- **haiku** — mechanical transforms, file listing, format checks
- **sonnet** — default authoring, research, review
- **opus** — architectural judgment, adversarial verification, subtle tradeoffs

Silence means the dispatching agent picks; house style is to be explicit.
