# Authoring Guide — House Template

How agents and skills in this bundle are written. Derived from Anthropic's current
guidance ("Building Effective Agents", "Effective context engineering for AI agents",
"Writing tools for agents"), the Claude Code docs at `code.claude.com/docs/en/sub-agents`
and `.../skills`, and the strongest shipped exemplars (wshobson `threat-modeling-expert`,
davila7 `supply-chain-security` and `read-only-auditor`). Current as of 2026-08-18.

## Agent `.md` skeleton

```
---
name: <lowercase-hyphenated>          # required
description: <what + WHEN; front-load the trigger>   # required; drives auto-delegation
tools: Read, Grep, Glob, Bash         # allowlist; omit = inherit ALL. Least-privilege.
model: inherit                        # inherit (default) | opus | sonnet | haiku | fable | full id
disallowedTools: Write, Edit          # denylist (applied before tools); enforce read-only
hooks: { PreToolUse: [...] }          # hard boundary enforcement (read-only-auditor pattern)
effort: high                          # per-agent reasoning budget
skills: [stride-analysis-patterns]    # preload paired reference skills
---

# <Role title>
<1-2 sentence identity: who this agent is and its single responsibility.>

## When to use / When NOT to use
<Concrete triggers, mirroring the description. Explicit non-goals so it doesn't sprawl.>

## Capabilities
<6-10 scoped competencies. A scope fence, not a tutorial.>

## Workflow
<Numbered steps the agent follows. The spine. 6-9 steps.>

## Finding / issue catalog
<The domain checklist grouped by class. Canonical examples, one per class, NOT an
 exhaustive edge-case dump.>

## Output format
<Severity rubric (Critical/High/Medium) + how findings report: fix + location.>

## Boundaries
<Hard limits: no writes, authorized-scope only, no destructive commands, escalation path.>
```

## Sizing rule

Aim for the smallest set of high-signal tokens that gets the outcome. Dense beats both
bloated and bare. Practical bounds for this catalog:

- Agent body under ~1,500 words / ~200 lines: a numbered workflow plus a bounded finding
  catalog. Below that, a security agent reverts to generic review (no catalog, no rubric).
  Above that, it fights the model.
- Push deep, reusable reference material into paired **skills** loaded on demand. A subagent
  body is a per-invocation cost in a fresh context; a skill body "stays in context across
  turns," so every line there is a recurring cost. Keep both lean, skills leanest.
- Canonical examples over exhaustive lists. A `security-reviewer`'s OWASP catalog is
  canonical classes with one example each, not every CWE variant.

## Do / Don't (security-reviewer-style agents)

- Front-load the trigger in `description` (it plus `when_to_use` is truncated at ~1,536
  chars in the listing). Don't bury "when to use" or write it vague, and weak descriptions
  kill auto-delegation.
- Least-privilege `tools`, and enforce read-only with `disallowedTools` + a `PreToolUse`
  hook. Don't inherit every tool; a reviewer that can Write/Edit is a footgun.
- Encode a bounded finding catalog, grouped, one example per class. Don't dump an
  exhaustive CWE/edge-case list.
- Give a numbered workflow and a severity rubric so output is decidable. Don't leave the
  output shape implicit.
- Name non-goals and scope fences explicitly (authorized targets only, no destructive
  commands). Offensive and IR agents especially need hard scope.
- Aim for the right altitude: specific enough to guide, flexible enough to leave heuristics.
  Don't hardcode brittle logic, and don't stay vague.
- Start minimal on the best model, then add instructions only where you observe a failure
  mode. Smarter models need less prescriptive engineering.

## 2026 specifics

- Subagent frontmatter now supports `disallowedTools`, `permissionMode`, `maxTurns`,
  `skills` (preload), `mcpServers`, `hooks`, `memory`, `background`, `effort`,
  `isolation: worktree`, `color`, `initialPrompt`. Three matter most here: `hooks` (read-only
  enforceable at harness level), `effort` (per-agent budget), `skills` (keep the body lean).
- `model` defaults to `inherit` and accepts `fable` + next-gen ids (`claude-opus-5`,
  `claude-sonnet-5`) alongside aliases. Resolution: `CLAUDE_CODE_SUBAGENT_MODEL` env →
  per-invocation param → frontmatter → main conversation.
- Commands merged into skills, so ship new work as **skills**, not commands (skills support
  supporting files and auto-loading).
- Skills frontmatter now includes `when_to_use`, `allowed-tools`, `disallowed-tools`,
  `license`, `compatibility`, `metadata`. Favor just-in-time retrieval: keep lightweight
  identifiers in the body, load reference files only when named.
