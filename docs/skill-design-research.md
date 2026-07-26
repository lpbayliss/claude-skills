# Evidence Basis for the Specify Skill

This note records the skill-authoring research used to refine Specify. It is maintainer documentation, not runtime skill context.

## Source hierarchy

The research prioritized:

1. The Agent Skills specification and first-party authoring/evaluation guidance.
2. Anthropic's Claude Platform and Claude Code documentation.
3. Anthropic's engineering article and public production/example skills.
4. OpenAI's official Codex skill documentation and public skill implementations as a cross-client portability check.

Community tutorials and generic prompt-engineering articles were excluded because the primary sources already cover the relevant mechanics.

## Findings and implications

| Evidence-backed pattern | Why it matters | Application to Specify |
|---|---|---|
| **Description controls discovery.** It should say what the skill does, when it applies, and where its boundary lies. Key intent should appear first because clients may truncate skill listings. | A strong workflow adds no value if the host does not load it, while an over-broad description wastes context and interferes with adjacent work. | Front-load software-specification intent, include natural trigger contexts, and exclude straightforward coding/debugging where no planning or specification decision is needed. |
| **Spend context only on non-obvious procedural knowledge.** Both Anthropic and Agent Skills guidance assume the model is capable and recommend removing generic explanation. | Loaded skill text competes with the user's request, conversation, repository evidence, and other skills. | Keep the decision workflow and hard-earned safeguards in `SKILL.md`; move maintainer evidence and conditional detail out of the runtime path. |
| **Use progressive disclosure.** Keep the core workflow in `SKILL.md`; link one level deep to references with explicit conditions for loading them. Longer references need a visible contents list. | Conditional loading preserves context and makes navigation predictable. | Route transform, review, full-spec, and example needs to dedicated references; add contents lists to references over 100 lines. |
| **Calibrate control to fragility.** Use judgment where valid approaches vary; use strong gates where an error is dangerous or irreversible. | Uniformly rigid skills become brittle, while uniformly vague skills skip safety-critical work. | Keep artifact depth and design exploration flexible; make non-fabrication, provenance, destructive-change gates, and readiness claims strict. |
| **Provide defaults rather than menus.** Give one normal path and an escape hatch. | Equal-weight option lists cause unnecessary exploration and inconsistent results. | Default to the smallest sufficient artifact and the simplest accepted design; escalate depth only when risk or uncertainty justifies it. |
| **Use conditional workflows and explicit checkpoints.** Complex skills benefit from a short progress checklist and mode-specific branches. | Agents otherwise apply every instruction to every task or skip validation steps. | Separate Create, Transform, Review, Update, and Spike outputs; add a compact progress loop shared by all modes. |
| **Use a draft-review-fix loop.** Validate against a script or reference checklist and revise before delivery. | Self-checking catches omissions and contradictions before users or implementers depend on them. | Make the readiness checklist an explicit validator: draft, review, repair, then publish the verdict. |
| **Ground skills in real expertise and observed corrections.** Generic best-practice prose is less valuable than procedures extracted from successful work and failures. | Domain-specific gotchas are what the base model is least likely to infer reliably. | Preserve the established evidence chain, source transformation rules, non-fabrication controls, and implementation-readiness gate; add a compact gotchas section. |
| **Examples should communicate shape, not become mandatory bulk.** Concrete examples are useful when a task's intended level is ambiguous. | Agents pattern-match examples strongly and can overproduce if the only example is large. | Keep a compact mini-spec example and explicitly treat it as a proportionality example, not a required section list. |
| **Scripts are for stable deterministic work.** Instruction-only is preferable for judgment-heavy workflows; bundle scripts when repeated mechanical logic emerges. | Premature validators can reward heading completion rather than specification quality. | Keep specification reasoning instruction-led. Use repository checks for packaging and schema integrity; use the review checklist for semantic validation. |
| **Evaluate triggering and output quality separately.** Use realistic prompts, difficult near-miss negatives, fresh contexts, previous-version baselines, objective assertions, timing/token costs, and human or blind review. | A skill can trigger correctly but produce poor work, or produce excellent work only when invoked manually. | Add output assertions and a balanced trigger suite; compare the revised skill with the v1.0.0 snapshot and judge usefulness per token as well as completeness. |
| **Audit installable skills and avoid surprising capability grants.** | Skills can carry scripts, dependencies, network actions, or broad tool permissions. | Keep runtime frontmatter portable and avoid pre-approved tools, shell injection, external dependencies, and hidden side effects. |

## Refinement decisions

The research leads to these concrete changes:

1. Shorten and restructure the core workflow around a mode/depth decision, a six-stage progress loop, and a readiness gate.
2. Add explicit proportionality rules so a mini-spec does not become a full architecture dossier by default.
3. Strengthen the triggering boundary and test it with realistic positive and near-miss negative queries.
4. Make source precedence, confidence, and artifact transformation more explicit while keeping the original immutable by default.
5. Add a draft → checklist review → fix → verdict feedback loop.
6. Keep safety-critical requirements strict but make optional coverage conditional on material relevance.
7. Move source/research provenance out of the runtime skill folder.
8. Expand evals with objective assertions and compare the revision against the v1.0.0 snapshot in fresh contexts.

## Primary sources

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills: best practices for skill creators](https://agentskills.io/skill-creation/best-practices)
- [Agent Skills: evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills)
- [Agent Skills: optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Anthropic engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic public skills repository](https://github.com/anthropics/skills)
- [OpenAI: Build skills](https://developers.openai.com/codex/build-skills)
- [OpenAI public skills repository](https://github.com/openai/skills)
