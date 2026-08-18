# Eval Cases — Planted Findings

Each fixture carries known vulnerabilities. An agent passes a case when it flags every
planted issue (recall) without inventing issues that are not there (precision). Run the
agent against the fixture and score its findings against this list.

## ci_workflow.yml → pipeline-security-engineer

1. Token over-privilege: `permissions: write-all` on a build workflow.
2. Unpinned action: `actions/checkout@v4` (mutable tag, not a SHA).
3. Script injection: `${{ github.event.pull_request.title }}` interpolated into a `run` shell step.
4. Hardcoded secret: `API_KEY: "sk_live_..."` inline in the workflow.

## main.tf → infrastructure-security-engineer

1. Public storage: S3 bucket ACL `public-read`.
2. Open ingress: security group allows `0.0.0.0/0` on port 22 (SSH).
3. Wildcard IAM: policy with `Action: "*"` on `Resource: "*"`.
4. Missing `aws_s3_bucket_public_access_block` (the guardrail that would stop the public ACL).
5. (Hardening) No customer-managed KMS key. New buckets default to SSE-S3, so this is a
   hardening recommendation, not a cleartext-storage gap — score a Low here, not a miss.

## app.py → security-reviewer

1. SQL injection: `"... WHERE id = " + order_id` string concatenation.
2. SQL injection: f-string `user_id = {uid}` from a request param.
3. IDOR / missing authz: `user_id` taken from the request with no ownership check.
4. Hardcoded secret: `DB_PASSWORD = "..."` and used in a connection string.

## subagent.md → ai-agent-security

1. Over-broad tool grant: holds `Write, Edit, Bash` with no `disallowedTools`.
2. Prompt injection: instructed to fetch web/file content and follow instructions found in it.
3. Prompt-only guardrail: "Never delete production files" with no enforcement.
