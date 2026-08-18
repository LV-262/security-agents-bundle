---
name: deploy-block
description: Blocks production deploy and release commands in agent sessions. A PreToolUse guard so agents open PRs and humans promote to production. Stops direct deploys, publishes, and releases before they run. Use in any session where an agent has shell access.
when_to_use: Any agent session with shell access to deploy tooling; CI-adjacent automation; enforcing that promotion to production is a human decision.
license: MIT
---

# Deploy Block

Agents build and open PRs. Humans promote to production. This guard enforces that
split by blocking the commands that ship, before they run.

## What it blocks

- Platform deploys: `vercel --prod`, `netlify deploy --prod`, `fly deploy`, `railway up`, `heroku`.
- Cloud CLIs against prod: `gcloud app deploy`, `aws` deploy/update, `kubectl apply` / `helm` on a prod context.
- Infra apply: `terraform apply`, `pulumi up`, `cdk deploy`.
- Package publishes: `npm publish`, `cargo publish`, `pip upload` / `twine upload`.
- Releases: `gh release create`, `docker push` to a release registry.

Blocking returns a message naming the command and pointing at the PR-and-promote path,
so the agent routes the work to a human instead of shipping.

## Wiring it

Register a `PreToolUse` hook on `Bash` that matches the release patterns and exits
non-zero to block. Sketch:

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "deploy-block-check" }] }
    ]
  }
}
```

The check tests the proposed command against the release patterns and exits non-zero
with a reason. Provide an explicit escape hatch (an env flag) for the rare authorized
case, so the block is deliberate to bypass, not accidental to hit.

## Tuning

- Match your real deploy tooling; add the commands your stack actually uses.
- Distinguish preview from production where the CLI does: block `--prod`, allow preview deploys.
- Pair with [safety-guard](../safety-guard/) for destructive shell actions.

## Boundaries

- This guards deploy and release commands. Destructive shell actions (deletes, disk writes) belong to `safety-guard`.
- The guard enforces the workflow; it does not judge whether a release is ready. That stays a human call.
