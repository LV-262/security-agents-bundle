---
name: safety-guard
description: Blocks destructive shell operations in autonomous or production sessions. A PreToolUse guard that stops irreversible commands (recursive deletes, disk writes, force pushes, table drops) before they run. Use in any session that runs with reduced supervision.
when_to_use: Running an agent autonomously or with auto-approved permissions; any session on or near production; long unattended runs.
license: MIT
---

# Safety Guard

Some commands have no undo. This guard blocks the irreversible ones before they run,
so an autonomous session cannot destroy state on a bad step.

## What it blocks

- Recursive force deletes: `rm -rf` on broad or absolute paths.
- Disk and device writes: `dd` to a device, `mkfs`, `> /dev/`.
- History rewrites on shared branches: `git push --force` to main or a protected branch.
- Destructive database statements: `DROP TABLE`, `DROP DATABASE`, `TRUNCATE` outside a sandbox.
- Mass permission or ownership changes: `chmod -R` / `chown -R` on system paths.

Blocking returns a clear message naming the command and why it was stopped, so the
agent can choose a safer path or ask for a human.

## Wiring it

Register a `PreToolUse` hook on `Bash` that matches the patterns above and exits
non-zero to block. Sketch:

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "safety-guard-check" }] }
    ]
  }
}
```

The check reads the proposed command, tests it against the blocklist, and exits
non-zero with a reason to block. Keep the blocklist strict and the message specific.

## Tuning

- Scope by session: enforce hardest in autonomous and production sessions, relax for a sandbox.
- Prefer an allowlist for the narrow cases you truly want (a known-safe cleanup path) over loosening the whole rule.
- Pair with [deploy-block](../deploy-block/) for release and deploy commands.

## Boundaries

- This guards destructive shell actions. Production deploy and release commands belong to `deploy-block`.
- A guard is a floor, not a substitute for review. It stops the obvious catastrophes; it does not make an unsupervised session safe on its own.
