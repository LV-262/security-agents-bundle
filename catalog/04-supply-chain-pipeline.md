# 4. Supply Chain & Pipeline Security (DevSecOps)

Securing the build and release process and everything it pulls in: CI/CD config,
dependencies, artifacts, provenance. The DevSecOps layer.

## Entries

### pipeline-security-engineer
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/pipeline-security-engineer.md`
- **Purpose:** reviews CI/CD pipelines and build supply chain — SAST triage, SCA / dependency-CVE review, secrets-in-pipeline detection, pipeline config (least-privilege tokens, pinned actions, injection via untrusted inputs).
- **Scope deltas (locked):** OpenSSF Scorecard, Sigstore/cosign signature *verification* (not just SBOM generation), in-toto attestations, SBOM (SPDX/CycloneDX), SLSA provenance, malicious-package detection (typosquat / dependency-confusion / protestware), license-conflict auditing.
- **Boundary:** reviews *project* CI/CD; distinct from `security-scan` (harness config) and `deploy-block` (runtime command block).

### Curated
- **supply-chain-security** reference agent — pointer, TBD from research.

See [curated/](../curated/) for links and licenses.
