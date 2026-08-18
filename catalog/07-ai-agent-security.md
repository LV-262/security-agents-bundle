# 7. AI / Agent Security

Securing AI agents and the harnesses that run them: prompt injection, tool-surface
abuse, MCP-server exposure. The newest branch and the thinnest on the open web. It
hits closest to home, since a Claude Code harness is itself an agent system.

### ai-agent-security · agent
Reviews AI-agent systems for security flaws. Prompt-injection paths (untrusted tool
output reaching context, hook injection, subagent prompt boundaries), MCP-server audit
(tool surface, auth, over-broad scopes), and an OWASP-for-agents baseline.
Install: `agents/ai-agent-security.md`

### security-scan · skill
Audits a `.claude/` configuration for misconfiguration and injection risk: settings,
MCP servers, hooks, agent definitions.
Install: `skills/security-scan/`

### From the ecosystem
MCP-server auditors, a prompt-injection red-team persona, and an OWASP-for-agents
conformance check. Every pick is MIT. See [curated/](../curated/#7-ai--agent-security).
