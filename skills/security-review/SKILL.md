---
name: security-review
description: A secure-coding checklist and patterns for building auth, input handling, secrets, API endpoints, and payment or other sensitive features. Use while writing the code, not just after. Complements the security-reviewer agent, which reviews code once written.
when_to_use: Adding authentication or authorization; handling user input; working with secrets or tokens; creating API endpoints; implementing payments or any feature touching sensitive data.
license: MIT
---

# Security Review

Build it secure the first time. This is the checklist to work against while writing
security-sensitive code, grouped by the surface you are touching.

## Authentication & sessions

- Hash passwords with bcrypt or argon2, never a fast hash or a home-rolled scheme.
- Issue short-lived tokens; rotate on privilege change; invalidate on logout.
- Bind sessions to the client where you can; regenerate the session ID on login.
- Rate-limit login, password reset, and token endpoints.

## Authorization

- Check authorization on every state-changing and data-returning path, not just at the gateway.
- Verify object ownership per request. Authentication is not authorization.
- Default deny. Grant the specific permission, never a wildcard.

## Input handling

- Validate at the boundary: type, length, range, and format, against an allowlist.
- Parameterize every query. Never concatenate input into SQL, a shell, or a template.
- Encode output for its context (HTML, attribute, URL, JS) to stop injection.
- Treat all external data as untrusted: request bodies, headers, webhooks, file contents, API responses.

## Secrets

- Read secrets from the environment or a secrets manager. Never commit them.
- Fail fast at startup if a required secret is missing.
- Keep secrets out of logs, error messages, and URLs.

## API endpoints

- Authenticate and authorize before doing work.
- Rate-limit and set request-size limits.
- Return generic errors to the client; keep detail server-side.
- Set the security headers the framework offers (CSRF protection, content type, CORS scope).

## Sensitive features (payments, PII)

- Minimize what you collect and how long you keep it.
- Encrypt sensitive data at rest and in transit.
- Log an audit trail for money movement and data access, without logging the sensitive values.

## Before you commit

- No hardcoded secrets or debug credentials.
- Every input validated, every query parameterized.
- Every sensitive path authorized.
- Errors handled without leaking internal detail.
