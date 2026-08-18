---
name: security-scan
description: Audits a Claude Code configuration for security risks. Checks the .claude directory (settings, permissions, MCP servers, hooks, agent definitions) for over-broad permissions, injectable hooks, unsafe MCP config, and instructions that could be abused. Use after changing harness config or before sharing it.
when_to_use: Setting up a new Claude Code project; after editing .claude/settings.json, CLAUDE.md, hooks, or MCP config; before committing or sharing a harness configuration.
license: MIT
---

# Security Scan

Your harness config is attack surface. This audits the `.claude/` directory the way
an attacker would read it: what can run, what can be injected, and what is trusted
that should not be.

## What to inspect

### Permissions and settings
- Look for broad allow rules (wildcard Bash, blanket auto-approve) that skip prompts on dangerous actions.
- Confirm `--dangerously-skip-permissions` is not baked into scripts or docs.
- Check that write, delete, and network actions are gated, not blanket-allowed.

### Hooks
- Read every hook command. A hook runs with your shell's privileges on each matching event.
- Flag hooks that execute fetched or untrusted content, or that interpolate tool input into a shell unquoted.
- Confirm hooks that guard governance (config protection, deploy blocks) are present and not disabled.

### MCP servers
- Inventory each server's tools and scopes. Flag any that grant more than the project needs.
- Check auth: no shared or committed tokens; per-user auth where the server supports it.
- Flag servers that reach untrusted external content and feed it back into context.

### Agent and skill definitions
- Check tool grants for least privilege. A reviewer agent should not hold Write, Edit, or Bash.
- Read system prompts and skill bodies for instructions that could be abused if the file is edited by an attacker.
- Flag any definition that disables safety guardrails.

### CLAUDE.md and instruction files
- These are loaded into context and trusted. Treat them as code.
- Flag instructions that would exfiltrate data, weaken permissions, or run untrusted commands.

## Report

List findings by severity: what is exposed, where (`file:line`), why it matters, and
the fix. Rate Critical / High / Medium / Low by how directly the issue leads to code
execution, data exposure, or a bypassed guardrail.

## Boundaries

- This audits harness configuration, not application code (`security-reviewer`) or the agents themselves at runtime (`ai-agent-security`).
- Read and report. Recommend fixes; let the operator apply them.
