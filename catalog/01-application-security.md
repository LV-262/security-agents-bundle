# 1. Application Security

Finding and preventing vulnerabilities in application code: OWASP Top 10, secrets,
injection, auth flaws, unsafe crypto, and secure-coding patterns. The reactive,
code-level layer of the discipline.

## Entries

### security-reviewer
- **Status:** reuse (rewritten MIT-original)
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/security-reviewer.md`
- **Purpose:** vulnerability detection on written code — OWASP Top 10, secrets, SSRF, injection, unsafe crypto. Reports findings and fixes.

### security-review
- **Status:** reuse (rewritten from scratch; earlier version was ECC-derived)
- **Harness-runnable:** yes
- **Kind:** skill
- **Source:** `skills/security-review/`
- **Purpose:** secure-coding checklist and patterns for auth, input handling, secrets, and endpoints.

### Curated
- **secure-coding-by-layer** (backend/frontend/mobile) — pointer, TBD from research.
- **API security** — pointer, TBD from research.

See [curated/](../curated/) for links and licenses.
