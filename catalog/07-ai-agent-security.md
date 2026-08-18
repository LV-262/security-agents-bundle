# 7. AI / Agent Security

Securing AI agents and the harnesses that run them: prompt injection, tool-surface
abuse, and MCP-server exposure. The fastest-emerging and least-saturated branch —
and directly relevant, since a Claude Code harness *is* an agent system.

## Entries

### ai-agent-security
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/ai-agent-security.md`
- **Purpose:** reviews AI-agent systems for security flaws — prompt-injection paths (untrusted tool output flowing into context, hook injection, subagent prompt boundaries), MCP-server audit (tool surface, auth, over-broad scopes), and an OWASP-for-agents baseline. One entry, not split.

### security-scan
- **Status:** reuse (rewritten from scratch; earlier version was ECC-derived)
- **Harness-runnable:** yes
- **Kind:** skill
- **Source:** `skills/security-scan/`
- **Purpose:** audits a `.claude/` configuration for misconfiguration and injection risk — settings, MCP servers, hooks, agent definitions.

### Curated
- **mcp-security-audit** / **mcp-implementation-security-review** (Copilot) — MCP-server auditors. Pointers.
- **llm-redteam-specialist** (davila7 / wshobson) — prompt-injection red-team persona. Pointer.
- **agent-owasp-compliance** (Copilot) — OWASP-for-agents conformance. Pointer.

See [curated/](../curated/) for links and licenses.
