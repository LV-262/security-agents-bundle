# Enforcement

Guardrails and hooks that make a harness enforce its own security posture instead of
trusting an agent to remember it. These apply across all seven branches.

### safety-guard · skill + hook
Blocks destructive operations in autonomous or production sessions.
Install: `skills/safety-guard/`

### deploy-block · skill + hook
Blocks production deploy and release commands. Agents open PRs, humans promote.
Install: `skills/deploy-block/`

## Patterns to copy

### Read-only reviewers
Every reviewer in this bundle declares `disallowedTools: Write, Edit, MultiEdit` in its
frontmatter, so it reads and reports but never changes what it reviews. For a stronger
guarantee, add a `hooks.PreToolUse` block that also stops mutating Bash commands.
Modeled on the open-source `read-only-auditor` (see
[curated/](../curated/#3-offensive-security--red-team)).

### Config self-modification protection
A `PreToolUse` hook that blocks an agent from editing its own governance: settings,
identity, agent and hook definitions. The hook itself lives in each operator's harness
config; this is the pattern to copy.
