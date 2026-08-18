---
name: threat-modeling
description: Structured threat modeling for a system or feature: STRIDE, PASTA, DFD-driven decomposition, attack-tree construction, and threat-to-mitigation mapping. Use at design time, during architecture review, before a security-sensitive release, or after an incident. Supersedes ad-hoc STRIDE passes with a repeatable method.
when_to_use: Designing a new system or feature with security implications; reviewing architecture before implementation; pre-release security assessment; post-incident hardening; evaluating a third-party integration.
license: MIT
---

# Threat Modeling

Find threats before the code exists. Decompose the system, reason about how each
trust boundary can be attacked, map every credible threat to a mitigation, and record
the residual risk. This is the deep, repeatable method. Pick the technique that fits
the question.

## Pick the method

- **STRIDE**: per-element decomposition. The default for "what can go wrong at this
  component." Six threat categories against each element crossing a trust boundary.
  Deep reference: [references/stride.md](references/stride.md).
- **PASTA**: risk-centric, seven stages from business objectives to attack simulation.
  Use it when threats need prioritizing by business impact, not just a list.
- **Attack trees**: goal-oriented. Root is the attacker's objective; branches are the
  paths. Use it to reason about one high-value target end to end.
- **DFD-driven**: draw the data-flow diagram first, then apply STRIDE to each element
  and flow. Use it when the system is large enough that "which components" isn't obvious.

## Workflow

1. Scope the model: the system or feature, its assets, and what an attacker would want.
2. Draw the data-flow diagram: external entities, processes, data stores, and the flows
   between them. Mark every trust boundary a flow crosses.
3. Enumerate entry points: routes, webhooks, queues, file uploads, sockets, admin paths.
4. Apply the chosen method per element/boundary (STRIDE by default; see the reference).
5. For each credible threat, rate likelihood and impact, then map it to a mitigation
   (existing control, new control, or accepted risk).
6. Record residual risk: what remains after mitigations, and who owns the acceptance.
7. Produce the threat-model artifact: DFD, threat table (threat → element → mitigation →
   residual), and a prioritized action list.

## Output

A threat-model document with: a data-flow diagram, a threat table
(`threat | element | STRIDE/category | likelihood | impact | mitigation | residual`),
and a prioritized list of mitigations to implement. Optionally emit a machine-readable
`.tm7` (Microsoft Threat Modeling Tool) export for round-tripping into existing tooling.

## Boundaries

- Design-time analysis, not a code audit. Route code-level findings to `security-reviewer`.
- Model credible threats, not every theoretical one; prioritize by likelihood × impact.
- Name the residual risk and its owner; a threat model with no accepted-risk line is
  incomplete.

## References

- [references/stride.md](references/stride.md): STRIDE categories, per-element questions,
  and worked examples. Loaded on demand.
- Planned: `references/attack-trees.md`, `references/pasta.md`, `references/dfd.md`.
