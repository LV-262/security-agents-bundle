# Security-Engineering Agents & Skills

A catalog of security-engineering agents and skills for Claude Code, organized the
way a security team is: by discipline. Built to teach from and to install from.

MIT (see [LICENSE](LICENSE)).

## The catalog

Seven branches. Each is a slice of security engineering with its own entries.

| # | Branch | Covers | Index |
|---|--------|--------|-------|
| 1 | Application Security | code review, secure coding, SAST, API security | [catalog/01](catalog/01-application-security.md) |
| 2 | Product Security & Threat Modeling | STRIDE, PASTA, DFD, attack trees | [catalog/02](catalog/02-product-security-threat-modeling.md) |
| 3 | Offensive Security / Red Team | attack-path enumeration, pentest, recon (authorized) | [catalog/03](catalog/03-offensive-red-team.md) |
| 4 | Supply Chain & Pipeline Security | CI/CD, SCA, SBOM, SLSA, secrets-in-pipeline, signing | [catalog/04](catalog/04-supply-chain-pipeline.md) |
| 5 | Infrastructure / Cloud / Container | IaC, K8s, Docker, CSPM, CIS, IAM, WAF | [catalog/05](catalog/05-infrastructure-cloud-container.md) |
| 6 | Detection & Response / IR | incident runbooks, on-call, postmortems, detection eng | [catalog/06](catalog/06-detection-response-ir.md) |
| 7 | AI / Agent Security | prompt injection, MCP-server audit, OWASP-for-agents | [catalog/07](catalog/07-ai-agent-security.md) |

[Enforcement](enforcement/) holds the guardrails and hooks that keep a harness to its
own rules. [curated/](curated/) points at the best security work already published
across the ecosystem.

## Install

```bash
git clone https://github.com/LV-262/security-agents-bundle
cd security-agents-bundle
cp -R agents/*  ~/.claude/agents/
cp -R skills/*  ~/.claude/skills/
```

Take what you need. Each branch lists what it ships and where.

## The security team

A subset of these compose into an agentic security team. That orchestration is the
next build. Today each entry stands on its own.

## Attribution

See [ATTRIBUTION.md](ATTRIBUTION.md). Everything original here is MIT; curated entries
keep their upstream licenses.
