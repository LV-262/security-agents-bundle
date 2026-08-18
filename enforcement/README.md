# Enforcement

The "how to enforce" cross-cut — operational guardrails and hooks that make security
posture structural rather than advisory. Not a domain branch; it applies across all
seven. Optional for the workshop, valuable in a real harness.

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
- **Purpose:** a subagent can declare `hooks.PreToolUse` (and `disallowedTools`) in its
  frontmatter to block `Write`/`Edit`/`MultiEdit`/`Bash` at the harness level — a
  structural non-destructive guarantee, not a prose promise. Adopted by the Red Team
  and audit entries. Modeled on the open-web `read-only-auditor` pattern (see `curated/`).

### Config self-modification protection
- **Status:** reference (document, not shipped)
- **Kind:** reference
- **Purpose:** a `PreToolUse` hook that blocks an agent from editing its own governance
  (settings, identity, agent/hook definitions). Documents the pattern; the concrete
  hook lives in the operator's own harness config, not this bundle.
