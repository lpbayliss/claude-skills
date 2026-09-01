---
name: create-skill
description: Use when creating, editing, or reviewing a Claude skill in this collection — a new SKILL.md, a trigger description, references, or skill evals. Do not use for installing skills or for tasks a skill merely assists with.
license: MIT
metadata:
  author: lpbayliss
  version: "1.0.0"
---

# Create Skill

Anthropic's `skill-creator` skill owns the authoring craft. This skill owns the house style. Every skill authored here passes through both.

<workflow>
1. Invoke the `skill-creator` skill and follow its process for scoping, drafting, and packaging. If it is not installed, install it first: `/plugin install skill-creator@lpbayliss-skills`.
2. Shape everything it produces with <house-style>.
3. Add evals before calling the skill done — formats in `references/house-style.md`.
4. Register the skill: it lives inside the base plugin `plugins/lpbayliss/skills/<name>/` — bump that plugin's version and add a README table row. No new plugin, no new marketplace entry.
</workflow>

<house-style>
- **Name**: verb-first action — `create-skill`, `write-dockerfile`, `plan-presentation`. Never a noun pile (`dockerfile-best-practices`).
- **Description**: "Use when … Do not use for …" — specific triggers only. No summary of what the skill covers, no workflow. If it exceeds two sentences, cut.
- **Scope**: one skill = one job. If the description needs "and" to join two jobs, split into two skills.
- **Body**: XML tags for sections. SKILL.md stays under ~500 words.
- **Depth**: bundle `references/*.md` and point to them from the body so they load only when needed. Never inline heavy reference material.
- **Teaching**: one excellent worked example beats a list of rules. Show the shape; keep rules to what an example cannot carry.
- **Delegation**: when a skill dispatches agents, it names the cheapest capable model — haiku for mechanical work, sonnet by default, opus for complex reasoning.
- **Frontmatter**: `license: MIT`; `metadata:` with `author: lpbayliss` and a semver `version`.
</house-style>

<example>
A skill for authoring Dockerfiles, in house style:

```yaml
---
name: write-dockerfile
description: Use when authoring or reviewing a Dockerfile — base image choice, layers, caching, multi-stage builds, or image size. Do not use for docker-compose files or CI pipelines.
license: MIT
metadata:
  author: lpbayliss
  version: "1.0.0"
---
```

```
plugins/lpbayliss/skills/write-dockerfile/
  SKILL.md                    # <workflow>, <example> (one full annotated Dockerfile), <references>
  references/hardening.md     # loaded only when security comes up
  references/multi-stage.md   # loaded only for size/build-speed work
  evals/evals.json
  evals/trigger-evals.json
```

Body centers on one annotated multi-stage Dockerfile; hardening detail waits in references. Compose and CI are separate skills.
</example>

<references>
- `references/house-style.md` — full conventions: eval file formats, marketplace registration snippet, naming table, complete skeleton.
</references>
