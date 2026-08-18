# STRIDE Reference

Apply STRIDE to every element that crosses a trust boundary. Each letter is a threat
category with a guiding question and the security property it violates.

| Threat | Question | Violates | Canonical example |
|--------|----------|----------|-------------------|
| **S**poofing | Can an attacker pretend to be someone else? | Authentication | Forged JWT, session hijack, stolen API key |
| **T**ampering | Can data be modified in transit or at rest? | Integrity | MITM on an unsigned webhook, DB record manipulation |
| **R**epudiation | Can a user deny an action? | Non-repudiation | Missing audit logs, no request correlation IDs |
| **I**nformation disclosure | Can sensitive data leak? | Confidentiality | Stack traces in errors, verbose logs, timing side channels |
| **D**enial of service | Can the system be made unavailable? | Availability | Unbounded query, missing rate limit, ReDoS |
| **E**levation of privilege | Can a user gain unauthorized access? | Authorization | IDOR, missing authz check, role manipulation |

## Per-element applicability

STRIDE categories don't all apply to every element type. Use this to avoid noise:

| Element | S | T | R | I | D | E |
|---------|---|---|---|---|---|---|
| External entity (user, third party) | ✓ | | ✓ | | | |
| Process (service, function) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Data store | | ✓ | ✓ | ✓ | ✓ | |
| Data flow (in transit) | | ✓ | | ✓ | ✓ | |

## Workflow within STRIDE

1. Take one element from the DFD.
2. For each applicable category above, ask the guiding question against this element.
3. If a credible threat exists, write it down with the attack path.
4. Map it to a mitigation (control that raises the cost or removes the path).
5. Note the residual risk after the mitigation.

## Worked example — API endpoint behind an auth gateway

- **Spoofing:** token replay if tokens are long-lived and not bound to a session. Mitigate with short expiry + rotation.
- **Tampering:** request body altered if integrity isn't checked past the gateway. Mitigate with signed requests or mutual TLS internally.
- **Information disclosure:** verbose 500s leak stack traces. Mitigate with generic error bodies + server-side detail only.
- **Elevation of privilege:** IDOR: `/orders/{id}` returns another tenant's order. Mitigate with per-request ownership checks, not just authentication.

Residual after mitigation: token theft within the expiry window remains; accept and monitor.
