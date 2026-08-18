# 4. Supply Chain & Pipeline Security (DevSecOps)

Securing the build and release process and everything it pulls in: CI/CD config,
dependencies, artifacts, provenance.

### pipeline-security-engineer · agent
Reviews CI/CD pipelines and the build supply chain. SAST triage, SCA and
dependency-CVE review, secrets-in-pipeline detection, token and action-pinning checks,
SBOM and SLSA provenance, signature verification, malicious-package detection
(typosquat, dependency confusion, protestware), and license conflicts.
Install: `agents/pipeline-security-engineer.md`

### From the ecosystem
`supply-chain-security` reads almost like a scope spec for this work, alongside
command-form SCA/SAST/hardening runs for CI and a DAST-onboarding agent that writes
the workflow for you. See [curated/](../curated/#4-supply-chain--pipeline-security).
