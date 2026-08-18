# Curated

The best security agents and skills already published across the ecosystem. Each
links to its home repository; install it from the source.

Everything here is MIT or CC0, so it's clean to adopt (`awesome-cursorrules` is
CC0-1.0, public domain). A repo occasionally carries per-file headers, so check
before you vendor a single file out of one.

## 1. Application Security
- **backend-security-coder:** `wshobson/agents` `plugins/backend-api-security/agents/` (MIT). Proactive secure backend coding: input validation, authn, API security. Fills the "advise while writing" gap.
- **frontend-security-coder / mobile-security-coder:** `wshobson/agents` `plugins/frontend-mobile-security/agents/` (MIT). XSS/output-sanitization; WebView/mobile patterns.
- **sast-sca-security-analyzer:** `github/awesome-copilot` `agents/sast-sca-security-analyzer.agent.md` (MIT). Combined SAST + SCA in one pass.
- **api-security-audit:** `davila7/claude-code-templates` `.../agents/security/api-security-audit.md` (MIT). REST authn/authz/injection audit.

## 2. Product Security & Threat Modeling
- **threat-modeling-expert (+ paired skills):** `wshobson/agents` `plugins/security-scanning/` (MIT). STRIDE/PASTA/attack-trees/DFD; agent-thin + skills-deep. A lean agent plus deep skills, the cleanest structure to learn from.
- **tm7-threat-model:** `github/awesome-copilot` `skills/tm7-threat-model` (MIT). Emits Microsoft Threat Modeling Tool `.tm7` for machine-readable export.
- **threat-model-analyst:** `github/awesome-copilot` `skills/threat-model-analyst` (MIT). Structured threat-model authoring.
- **security-threat-model / regulatory-threat-model:** `davila7` `.../skills/security/` (MIT). Includes a regulatory-driven variant.

## 3. Offensive Security / Red Team
- **davila7 offensive skill library:** `davila7` `.../skills/security/` (MIT): red-team-tactics, red-team-tools, metasploit-framework, burp-suite-testing, sqlmap-database-pentesting, shodan-reconnaissance, idor-testing, privilege-escalation-methods, ethical-hacking-methodology, pentest-checklist. The deepest permissive offensive catalog on the open web. Point at the subset you need.
- **penetration-tester:** `VoltAgent/awesome-claude-code-subagents` `categories/04-quality-security/penetration-tester.md` (MIT). An authorized-exploitation-and-validation persona with clear scope guardrails.
- **read-only-auditor:** `davila7` `.../agents/security/read-only-auditor.md` (MIT). PreToolUse hooks block Write/Edit/Bash. The safety pattern for authorized non-destructive testing.
- **solanabr/auditor-skill:** `solanabr/auditor-skill` (MIT). Domain-specific (Solana), but the strongest executable-PoC audit workflow of the set.

## 4. Supply Chain & Pipeline Security
- **supply-chain-security:** `davila7` `.../agents/security/supply-chain-security.md` (MIT). SBOM (SPDX/CycloneDX), SLSA, Sigstore/cosign, in-toto, typosquat/dep-confusion, OpenSSF Scorecard, license compliance.
- **supply-chain-guard:** `davila7` `.../skills/security/supply-chain-guard` (MIT). Skill-form checklist companion.
- **security-scanning commands:** `wshobson/agents` `plugins/security-scanning/commands/` + `dependency-management/commands/deps-audit` (MIT). CI-invocable dependency/SAST/hardening runs.
- **stackhawk-security-onboarding:** `github/awesome-copilot` `agents/` (MIT). Generates DAST config + GitHub Actions workflow, concrete pipeline wiring.

## 5. Infrastructure / Cloud / Container Security
- **security-engineer:** `VoltAgent` `categories/03-infrastructure/security-engineer.md` (MIT). Infra + CI/CD controls, compliance automation.
- **cloud / aws pentest + WAF skills:** `davila7` `.../skills/security/` (MIT): cloud-penetration-testing, aws-penetration-testing, google-cloud-waf-security, google-cloud-auth. Cloud-posture + WAF depth.
- **kubernetes-specialist / terraform-engineer:** `VoltAgent` `categories/03-infrastructure/` (MIT). K8s/IaC checklists for CIS hardening.
- **wg-code-sentinel:** `davila7` `.../agents/security/wg-code-sentinel.md` (MIT). Lightweight config/IaC misconfig review.

## 6. Detection & Response / Incident Response
- **incident-response plugin:** `wshobson/agents` `plugins/incident-response/` (MIT). incident-responder agent + skills (incident-runbook-templates, on-call-handoff-patterns, postmortem-writing). The most complete IR bundle on the open web.
- **devops-incident-responder:** `VoltAgent` `categories/03-infrastructure/devops-incident-responder.md` (MIT). SRE-flavored diagnosis + fix + postmortem.
- **incident-reporting-navigator / cra-vulnerability-obligations:** `davila7` `.../skills/security/` (MIT). Regulatory incident-reporting timelines, including the EU CRA.
- **signed-audit-trails-recipe / ai-agent-audit-specialist:** `wshobson` `plugins/signed-audit-trails/` and `davila7` `.../agents/security/ai-agent-audit-specialist.md` (MIT). Closest thing to a DFIR/forensics pointer.

> **Detection engineering:** no Sigma/SIEM/detection-rule agent or skill surfaced in
> any coding-agent collection we searched. It lives in security-ops tooling. A slice
> here would be net-new, with nothing open-source to point at.

## 7. AI / Agent Security
- **mcp-security-audit / mcp-implementation-security-review:** `github/awesome-copilot` `skills/` (MIT). The only shipped MCP-server security auditors found, directly relevant to a Claude Code harness.
- **agent-owasp-compliance:** `github/awesome-copilot` `skills/agent-owasp-compliance` (MIT). OWASP-for-AI-agents conformance.
- **llm-redteam-specialist:** `davila7` `.../agents/security/llm-redteam-specialist.md` (also `wshobson`) (MIT). Prompt-injection harness + output-safety eval.
- **ai-agent-audit-specialist:** `davila7` `.../agents/security/ai-agent-audit-specialist.md` (MIT). Forensic audit trails for AI coding agents in regulated environments.
