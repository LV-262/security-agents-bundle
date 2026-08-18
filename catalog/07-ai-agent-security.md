# 7. AI / Agent Security

Securing AI agents and the harnesses that run them: prompt injection, tool-surface
abuse, MCP-server exposure. The newest branch and the thinnest on the open web. It
hits closest to home, since a Claude Code harness is itself an agent system.

## Entries

### ai-agent-security
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/ai-agent-security.md`
- **Purpose:** reviews AI-agent systems for security flaws. Prompt-injection paths (untrusted tool output reaching context, hook injection, subagent prompt boundaries), MCP-server audit (tool surface, auth, over-broad scopes), and an OWASP-for-agents baseline.

### security-scan
- **Status:** reuse (rewritten, MIT-original)
- **Harness-runnable:** yes
- **Kind:** skill
- **Source:** `skills/security-scan/`
- **Purpose:** audits a `.claude/` configuration for misconfiguration and injection risk. Settings, MCP servers, hooks, agent definitions.

### Curated

MCP-server auditors, a prompt-injection red-team persona, and an OWASP-for-agents
conformance check. Every pick is MIT, with little competition yet. Picks and licenses
in [curated/](../curated/#7-ai--agent-security).
