# Security-Engineering Agents & Skills

A unified, taxonomy-organized catalog of security-engineering agents and skills
for Claude Code — the reference bundle for a workshop on using agents and skills
in a security context. Reuse what fits, curate the best open-web pieces, build
the real gaps.

Successor to `security-agents-bundle`. Licensed MIT (see [LICENSE](LICENSE)).

## The catalog

Seven branches of security engineering. Governance, risk, and compliance (GRC) is
a deliberately separate sibling discipline and is out of scope here.

| # | Branch | Covers | Index |
|---|--------|--------|-------|
| 1 | Application Security | code review, secure coding, SAST, API security | [catalog/01](catalog/01-application-security.md) |
| 2 | Product Security & Threat Modeling | STRIDE, PASTA, DFD, attack trees | [catalog/02](catalog/02-product-security-threat-modeling.md) |
| 3 | Offensive Security / Red Team | attack-path enumeration, pentest, recon (authorized) | [catalog/03](catalog/03-offensive-red-team.md) |
| 4 | Supply Chain & Pipeline Security | CI/CD, SCA, SBOM, SLSA, secrets-in-pipeline, signing | [catalog/04](catalog/04-supply-chain-pipeline.md) |
| 5 | Infrastructure / Cloud / Container | IaC, K8s, Docker, CSPM, CIS, IAM, WAF | [catalog/05](catalog/05-infrastructure-cloud-container.md) |
| 6 | Detection & Response / IR | incident runbooks, on-call, postmortems, detection eng | [catalog/06](catalog/06-detection-response-ir.md) |
| 7 | AI / Agent Security | prompt injection, MCP-server audit, OWASP-for-agents | [catalog/07](catalog/07-ai-agent-security.md) |

Cross-cutting: [Enforcement](enforcement/) — operational guardrails and hooks (how
to *enforce* security posture in a harness). Optional for the workshop.

Curated open-web entries we point at rather than ship: [curated/](curated/).

## How to read a catalog entry

Every entry is a card:

- **Status** — `build` (original to this repo), `reuse` (rewritten original), or
  `curate` (pointer to an external source, not shipped here).
- **Harness-runnable** — `yes` (a real agent/skill you install and invoke) or
  `no` (education/reference only).
- **Kind** — agent, skill, or hook.
- **Source** — a path in this repo, or an external URL + license.

## Install (runnable entries)

```bash
git clone https://github.com/LV-262/security-agents-bundle
cd security-agents-bundle
cp -R agents/*  ~/.claude/agents/
cp -R skills/*  ~/.claude/skills/
```

Install only what you need — each catalog branch lists its runnable entries.

## The agentic security team (roadmap)

A runnable subset of this catalog composes into an agentic security team. The team
orchestration (a dispatcher / lead agent) is a follow-on, not part of this bundle.
For now the runnable entries work individually.

## Attribution

See [ATTRIBUTION.md](ATTRIBUTION.md). Curated entries retain their own upstream
licenses; this repo's original agents and skills are MIT under the copyright above.
