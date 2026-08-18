# 3. Offensive Security / Red Team

Taking the attacker's seat under explicit authorization: attack-path enumeration,
exploit-scenario reasoning, abuse cases, recon patterns. Scoped to authorized
engagements, CTF, and defensive validation. No destructive actions, no DoS, no mass
targeting.

### red-team-review · agent
Offensive review of code and systems: attack-path enumeration, exploit-scenario
reasoning, abuse cases. Ships a `PreToolUse` hook that blocks Write, Edit, and Bash,
so a review runs against real systems without touching them. Declines destructive,
DoS, and mass-targeting requests.
Planned.

### From the ecosystem
Deep offensive tooling already exists as skills worth installing from source: Burp
Suite, Metasploit, sqlmap, Shodan recon, privilege escalation, IDOR/SSRF. A
`read-only-auditor` demonstrates the hook pattern above. See
[curated/](../curated/#3-offensive-security--red-team).
