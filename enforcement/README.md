# Enforcement

Guardrails and hooks that make a harness enforce its own security posture instead of
trusting an agent to remember it. These apply across all seven branches.

### safety-guard · skill + hook
Blocks destructive operations in autonomous or production sessions.
Planned.

### deploy-block · skill + hook
Blocks production deploy and release commands. Agents open PRs, humans promote.
Planned.

## Patterns to copy

### Frontmatter-hook read-only enforcement
A subagent declares `hooks.PreToolUse` and `disallowedTools` in its frontmatter to
block Write, Edit, and Bash at the harness level, so the block holds no matter what the
agent decides. The Red Team and audit entries use it. Modeled on the open-source
`read-only-auditor` (see [curated/](../curated/#3-offensive-security--red-team)).

### Config self-modification protection
A `PreToolUse` hook that blocks an agent from editing its own governance: settings,
identity, agent and hook definitions. The hook itself lives in each operator's harness
config; this is the pattern to copy.
