# 5. Infrastructure / Cloud / Container Security

Hardening the deployed substrate: infrastructure-as-code, cloud posture, and
container configuration.

## Entries

### infrastructure-security-engineer
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/infrastructure-security-engineer.md`
- **Purpose:** reviews IaC, cloud posture, and container hardening — Terraform, K8s manifests/Helm, Dockerfiles; CIS-benchmark alignment; network/identity misconfig, public exposure, over-broad IAM across AWS/Azure/GCP.
- **Scope deltas (locked):** cloud security posture management (CSPM) framing, WAF configuration review.
- **Boundary:** owns the deployed substrate; the build/release *process* belongs to `pipeline-security-engineer`. SBOM sits with Pipeline; CIS benchmarks sit here. Cites `cmmc-advisor` for compliance mapping rather than duplicating it.

### Curated
- **cloud / k8s / terraform** specialist pointers — TBD from research.

See [curated/](../curated/) for links and licenses.
