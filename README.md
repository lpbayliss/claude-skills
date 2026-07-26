# Claude Software Specification

A portable [Agent Skill](https://agentskills.io/) for creating, reviewing, and transforming software specifications into decision-ready, implementation-ready contracts.

It supports:

- new specifications from ideas, requirements, issues, or repository context;
- critical review and repair of existing specs, RFCs, PRDs, ADRs, plans, diagrams, and design notes;
- conversion of rough or solution-first material into testable requirements;
- repository-grounded implementation slices for human or agentic development;
- explicit readiness verdicts, blockers, evidence, verification, rollout, and rollback.

The workflow is intentionally specification-first:

```text
problem evidence → goals/non-goals → requirements → design decisions →
verification → rollout/operations → implementation slices
```

## Install in Claude Code

### Recommended: plugin marketplace

Run these commands inside Claude Code:

```text
/plugin marketplace add lpbayliss/claude-software-specification
/plugin install software-specification@lpbayliss-skills
/reload-plugins
```

Or install non-interactively from a shell:

```bash
claude plugin marketplace add lpbayliss/claude-software-specification
claude plugin install software-specification@lpbayliss-skills
```

Claude can then select the skill automatically, or you can invoke it directly:

```text
/software-specification:specify
/software-specification:specify docs/proposal.md
```

### Personal skill

```bash
git clone https://github.com/lpbayliss/claude-software-specification.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/claude-software-specification/skills/specify" ~/.claude/skills/specify
```

Copy instead of symlinking if preferred:

```bash
cp -R claude-software-specification/skills/specify ~/.claude/skills/specify
```

Invoke it as `/specify`.

### Project skill

From an existing project root:

```bash
mkdir -p .claude/skills
cp -R /path/to/claude-software-specification/skills/specify .claude/skills/specify
```

Commit `.claude/skills/specify/` if the workflow should travel with the project. Claude cloud sessions can load committed project skills.

## Example requests

```text
Create an implementation-ready specification for passkey login. Inspect this repository first. Do not implement it.
```

```text
Review docs/payments-redesign.md. Preserve accepted product intent, identify unsupported claims and blockers, then produce a corrected spec suitable for parallel agent implementation.
```

```text
Turn this architecture diagram, ticket set, and rough notes into a coherent mini-spec. Mark interpretations that need owner confirmation rather than guessing.
```

## Repository structure

```text
.claude-plugin/                 Claude marketplace and plugin metadata
skills/specify/SKILL.md         Main workflow
skills/specify/references/      Templates, review criteria, examples, source basis
skills/specify/evals/           Realistic skill evaluation prompts
scripts/check.py                Dependency-free repository checks
scripts/package_skill.py        Builds dist/specify.skill
```

## Validate and package

```bash
python3 scripts/check.py
python3 scripts/package_skill.py
```

When Claude Code is installed:

```bash
claude plugin validate .
```

The packaged `dist/specify.skill` is a zip-compatible Agent Skill archive for clients that accept skill uploads. A prebuilt archive is available from the [latest GitHub release](https://github.com/lpbayliss/claude-software-specification/releases/latest/download/specify.skill). Claude.ai and Cowork installations are account-scoped; upload that archive through **Customize → Skills** rather than expecting local `~/.claude/skills/` to sync.

## Design principles

- Inspect the source of truth before proposing repository-specific design.
- Preserve product intent while challenging premature mechanisms.
- Separate facts, requirements, constraints, decisions, assumptions, risks, and open questions.
- Do not fabricate repository paths, metrics, targets, architecture, or approvals.
- Give consequential requirements stable IDs and objective pass conditions.
- Treat security, privacy, migration, public interfaces, destructive changes, and rollback as explicit decision boundaries.
- Do not mark a spec ready while implementation still requires inventing product behaviour.

## License

MIT. See [LICENSE](LICENSE).
