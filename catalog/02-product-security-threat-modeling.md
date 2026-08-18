# 2. Product Security & Threat Modeling

Design-time security: decompose a system, find threats before code exists, map them
to mitigations. Proactive counterpart to Application Security.

## Entries

### threat-modeling
- **Status:** build
- **Harness-runnable:** yes
- **Kind:** skill (may ship paired sub-skills)
- **Source:** `skills/threat-modeling/`
- **Purpose:** structured threat modeling: STRIDE per-element decomposition, PASTA, DFD-driven trust-boundary analysis, attack-tree construction, threat → mitigation → residual-risk mapping. Supersedes the STRIDE section of the earlier `adversarial-security` skill. Optional `.tm7` (Microsoft Threat Modeling Tool) export path.
- **Sub-skills (candidate):** stride-analysis, attack-tree-construction, threat-mitigation-mapping.

### Curated

The `threat-modeling-expert` agent and its paired STRIDE/attack-tree skills, plus
`.tm7` export tooling for round-tripping into the Microsoft Threat Modeling Tool.
Picks and licenses in [curated/](../curated/#2-product-security--threat-modeling).
