# 1. Application Security

Finding and fixing vulnerabilities in application code: OWASP Top 10, secrets,
injection, broken auth, unsafe crypto, and the secure-coding patterns that head them
off. The code-level layer, reviewed after the code is written.

## Entries

### security-reviewer
- **Status:** reuse (rewritten, MIT-original)
- **Harness-runnable:** yes
- **Kind:** agent
- **Source:** `agents/security-reviewer.md`
- **Purpose:** vulnerability detection on written code. OWASP Top 10, secrets, SSRF, injection, unsafe crypto. Reports findings and fixes.

### security-review
- **Status:** reuse (rewritten, MIT-original)
- **Harness-runnable:** yes
- **Kind:** skill
- **Source:** `skills/security-review/`
- **Purpose:** secure-coding checklist and patterns for auth, input handling, secrets, and endpoints.

### Curated

Secure-coding-by-layer (backend, frontend, mobile) for advising while code gets
written, plus a dedicated API-security reviewer. Picks and licenses in
[curated/](../curated/#1-application-security).
