# 3. Offensive Security / Red Team

Taking the attacker's seat under explicit authorization: attack-path enumeration,
exploit-scenario reasoning, abuse cases, recon patterns. Scoped to authorized
engagements, CTF, and defensive validation. No destructive actions, no DoS, no mass
targeting.

## Entries

### red-team-review
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent (with a read-only PreToolUse hook)
- **Source:** `agents/red-team-review.md`
- **Purpose:** offensive review of code and systems: attack-path enumeration, exploit-scenario reasoning, abuse cases. Review-shaped, not a full pentest persona. Ships a `PreToolUse` hook that blocks Write/Edit/MultiEdit/Bash for a structural non-destructive guarantee.
- **Guardrails:** explicit authorization/scope check in the agent body; declines destructive/DoS/mass-targeting requests.

### Curated

The deep offensive tooling (Burp Suite, Metasploit, sqlmap, Shodan recon, priv-esc,
IDOR/SSRF) already exists as skills worth installing from source, alongside a
`read-only-auditor` whose hook pattern the agent above borrows. Picks and licenses in
[curated/](../curated/#3-offensive-security--red-team).
