# Eval Results

Run 2026-08-18. Each agent reviewed its fixture with no hints beyond its own spec.
Recall counts planted issues found; precision tracks invented issues.

| Agent | Fixture | Recall | Precision | Notes |
|-------|---------|--------|-----------|-------|
| pipeline-security-engineer | ci_workflow.yml | 4/4 | clean | Also traced the fork-PR → injection → token+secret theft chain. |
| infrastructure-security-engineer | main.tf | 4/4 | clean | Bonus: missing public-access-block. Correctly scored default SSE-S3 as Low, not a gap. |
| security-reviewer | app.py | 4/4 | clean | Bonus: second suspected IDOR, correctly hedged as "needs confirmation." |
| ai-agent-security | subagent.md | 3/3 | clean | Bonus: flagged "does everything" unbounded scope. |

All four found every planted issue, assigned defensible severities, and invented
nothing. Three surfaced accurate bonus findings; the infra agent corrected an
imprecision in the expected set (default S3 encryption), which has been folded back in.

## Method

Each agent was run by pointing a subagent at the agent's `.md` as its operating spec
and the fixture as the target, then scoring the returned findings against
[expected.md](expected.md). Small fixtures, single-file, no tool access beyond Read —
so the result measures the prompt, not the harness.

## Limits

- One fixture per agent. A real eval suite wants several per agent, including
  clean files (to test precision) and near-miss cases (to test false-positive rate).
- No coverage yet for the skills (threat-modeling, incident-response, security-review,
  security-scan, safety-guard, deploy-block), which are reference-shaped rather than
  finding-shaped and need a different rubric.
