# Enforcement

Guardrails and hooks that make a harness enforce its own security posture instead of
trusting an agent to remember it. These apply across all seven branches.

## Entries

### safety-guard
- **Status:** reuse (rewritten from scratch; earlier version was ECC-derived)
- **Harness-runnable:** yes
- **Kind:** skill / hook
- **Source:** `skills/safety-guard/`
- **Purpose:** blocks destructive operations in autonomous or production sessions.

### deploy-block
- **Status:** reuse (rewritten from scratch; earlier version was ECC-derived)
- **Harness-runnable:** yes
- **Kind:** skill / hook
- **Source:** `skills/deploy-block/`
- **Purpose:** blocks production deploy/release commands; agents open PRs, humans promote.

## Reference patterns

### Frontmatter-hook read-only enforcement
- **Status:** reference (document, not shipped)
- **Kind:** reference
- **Purpose:** a subagent declares `hooks.PreToolUse` (and `disallowedTools`) in its
  frontmatter to block `Write`/`Edit`/`MultiEdit`/`Bash` at the harness level, so the
  harness enforces the block directly. The Red Team and audit entries use it. Modeled
  on the open-source `read-only-auditor` pattern (see `curated/`).

### Config self-modification protection
- **Status:** reference (document, not shipped)
- **Kind:** reference
- **Purpose:** a `PreToolUse` hook that blocks an agent from editing its own governance
  (settings, identity, agent/hook definitions). The concrete hook lives in each
  operator's harness config; this documents the pattern to copy.
