# 3. Offensive Security / Red Team

Taking the attacker's seat under explicit authorization: attack-path enumeration,
exploit-scenario reasoning, abuse cases, recon patterns. Framed for authorized
engagements, CTF, and defensive validation only — no destructive actions, DoS, or
mass targeting.

## Entries

### red-team-review
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** agent (with a read-only PreToolUse hook)
- **Source:** `agents/red-team-review.md`
- **Purpose:** offensive review of code and systems — attack-path enumeration, exploit-scenario reasoning, abuse cases. Review-shaped, not a full pentest persona. Ships a `PreToolUse` hook that blocks Write/Edit/MultiEdit/Bash for a structural non-destructive guarantee.
- **Guardrails:** explicit authorization/scope check in the agent body; declines destructive/DoS/mass-targeting requests.

### Curated
- **Offensive tooling skills** (Burp Suite, Metasploit, sqlmap, Shodan recon, priv-esc, IDOR/SSRF) — pointers, TBD from research. Deep offensive tooling is recommended, not shipped here.

See [curated/](../curated/) for links and licenses.
