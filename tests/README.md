# Tests

Two layers: structural smoke tests that run anywhere, and behavioral evals that
exercise the agents against planted vulnerabilities.

## Smoke tests (deterministic)

```bash
python3 tests/smoke_test.py
```

Validates every agent and skill: frontmatter parses, required fields are present,
`name` matches the filename, models and tools are valid, reviewers disallow Write and
Edit, catalog `Install:` paths resolve, and internal links are not broken. No model
calls. Exits non-zero on any failure, so it drops straight into CI.

## Evals (behavioral)

Each fixture in `evals/fixtures/` carries known vulnerabilities, listed in
`evals/expected.md`. Run the matching agent against its fixture and score its findings:

- **Recall:** did it flag every planted issue.
- **Precision:** did it avoid inventing issues that are not there.

| Fixture | Agent | Planted |
|---------|-------|---------|
| `ci_workflow.yml` | pipeline-security-engineer | write-all token, unpinned action, script injection, hardcoded secret |
| `main.tf` | infrastructure-security-engineer | public S3, open SSH ingress, wildcard IAM, missing encryption |
| `app.py` | security-reviewer | two SQL injections, IDOR, hardcoded secret |
| `subagent.md` | ai-agent-security | over-broad tools, prompt injection, prompt-only guardrail |

To run one: point the agent at its fixture and compare the findings to the expected
list. In Claude Code, install the bundle and invoke the agent, or dispatch a subagent
with the agent file as its spec and the fixture as the target.
