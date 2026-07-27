# LPBayliss Claude Skills

A versioned Claude Code plugin and portable [Agent Skills](https://agentskills.io/) collection for software engineering work.

## Skills

### `specify`

Creates, reviews, repairs, and transforms software specifications into decision-ready, implementation-ready contracts.

Use it for specs, RFCs, PRDs, technical designs, scoped issue contracts, migrations, readiness reviews, and transforming rough artifacts into testable requirements.

```text
/software-specification:specify docs/proposal.md
```

### `metrics`

Identifies, defines, implements, and verifies trustworthy software, product, delivery, reliability, experiment, and AI-system metrics.

Use it to decide what to measure, audit misleading metrics, add repository instrumentation, design metric contracts, or verify dashboards and alerts without inventing targets or creating unsafe cardinality.

```text
/software-specification:metrics Add retry-safe worker outcome and latency metrics to this repository.
```

The plugin namespace remains `software-specification` for compatibility with existing installations. The repository and plugin content are now general-purpose; a future namespace/repository rename should be handled as an explicit migration rather than silently breaking installed commands.

## Install in Claude Code

### Plugin marketplace

Run inside Claude Code:

```text
/plugin marketplace add lpbayliss/claude-software-specification
/plugin install software-specification@lpbayliss-skills
/reload-plugins
```

Or from a shell:

```bash
claude plugin marketplace add lpbayliss/claude-software-specification
claude plugin install software-specification@lpbayliss-skills
```

Claude can select a skill automatically from its description or you can invoke a namespaced skill directly.

### Install individual personal skills

```bash
git clone https://github.com/lpbayliss/claude-software-specification.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/claude-software-specification/skills/specify" ~/.claude/skills/specify
ln -s "$(pwd)/claude-software-specification/skills/metrics" ~/.claude/skills/metrics
```

Copy instead of symlinking if preferred. Standalone personal skills are invoked as `/specify` and `/metrics`.

### Install a project skill

From a project root:

```bash
mkdir -p .claude/skills
cp -R /path/to/this-repo/skills/metrics .claude/skills/metrics
```

Commit the skill directory if the workflow should travel with the project.

## Example requests

```text
Create an implementation-ready specification for passkey login. Inspect this repository first. Do not implement it.
```

```text
Review docs/payments-redesign.md. Preserve accepted intent, identify blockers, and produce a corrected spec suitable for parallel implementation.
```

```text
We are adding recurring reminders. Identify the smallest outcome, driver, and guardrail metric set, then add the instrumentation and tests using this repository's existing analytics stack.
```

```text
Audit weekly_active_user from source event through warehouse query and dashboard. Fix semantic drift, cardinality, and tests; do not invent a target.
```

## Repository structure

```text
.claude-plugin/                 Marketplace and plugin metadata
skills/specify/                 Software specification skill, references, and evals
skills/metrics/                 Metrics skill, references, fixtures, and evals
docs/                           Design evidence and evaluation notes
scripts/check.py                Dependency-free multi-skill repository checks
scripts/package_skill.py        Builds each .skill archive and the complete plugin zip
dist/                           Generated archives
```

Each skill is independently portable. The repository root is the multi-skill Claude Code plugin.

## Validate and package

```bash
python3 scripts/check.py
python3 scripts/package_skill.py
for archive in dist/*.skill dist/*.zip; do python3 -m zipfile -t "$archive"; done
```

When Claude Code is installed:

```bash
claude plugin validate .
claude --plugin-dir .
```

Expected archives:

- `dist/specify.skill`
- `dist/metrics.skill`
- `dist/lpbayliss-skills.zip`

`.skill` files are for clients that accept individual skill uploads. The plugin zip contains the complete collection for local plugin loading.

## Skill quality rules

- Use precise trigger descriptions with realistic positive and difficult negative trigger evals.
- Keep the core workflow under 500 lines and load deeper references conditionally.
- Inspect source evidence before making repository-specific claims.
- Do not fabricate product decisions, targets, paths, commands, approvals, or observed results.
- Scale output and implementation to the decision and risk.
- Pair semantic review with deterministic checks for package shape, links, eval schemas, and fixtures.
- Keep each skill independently installable and testable.
- Implement requested work and verify it with real execution rather than stopping at advice.

Evidence for the authoring approach is in [docs/skill-design-research.md](docs/skill-design-research.md). Specification sources are in [docs/specification-workflow-basis.md](docs/specification-workflow-basis.md). Metrics sources are in [docs/metrics-design-basis.md](docs/metrics-design-basis.md). Specify evaluation results are in [docs/evaluation.md](docs/evaluation.md).

## Adding another skill

1. Create `skills/<name>/SKILL.md` with matching `name` frontmatter and a trigger-focused description.
2. Put optional depth in `references/`, deterministic helpers in `scripts/`, and realistic inputs in `evals/files/`.
3. Add at least three output evals to `evals/evals.json` and 20 balanced trigger cases to `evals/trigger-evals.json`.
4. Update this README and plugin metadata keywords when the new domain changes discovery.
5. Run repository checks, package all artifacts, validate the plugin, and exercise representative skill prompts before release.

## License

MIT. See [LICENSE](LICENSE).
