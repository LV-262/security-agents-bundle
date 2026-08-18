---
name: incident-response
description: Runbooks and checklists for handling a production incident end to end: triage, severity, containment, eradication, recovery, on-call handoff, and the blameless postmortem. Use during an active incident or when building incident-response process.
when_to_use: A production incident or security event is active; setting up on-call and incident process; writing a postmortem after an incident.
license: MIT
---

# Incident Response

Move fast without making it worse. This is the path from "something is wrong" to
"fixed, and we learned from it."

## Triage

1. Confirm it is real. Reproduce the signal or corroborate it from a second source.
2. Set severity (below). Severity drives who you page and how fast.
3. Name an incident commander. One person coordinates; everyone else has a clear job.
4. Open a timeline. Every action and finding gets a timestamp from here on.

## Severity

- **SEV1:** major outage or active security breach. Customer-facing, no workaround. Page now.
- **SEV2:** significant degradation or a contained security issue. Workaround exists. Urgent.
- **SEV3:** minor or localized. Handle in hours, not minutes.

## Containment, eradication, recovery

- **Contain first.** Stop the bleeding before you chase root cause: isolate the host, revoke the credential, disable the feature flag, block the IP. For a security incident, preserve evidence while you contain.
- **Eradicate.** Remove the cause: patch, rotate secrets, kill the malicious process, fix the bug.
- **Recover.** Restore service, verify it holds, and watch for recurrence before you stand down.

## On-call handoff

When an incident crosses a shift, hand off in writing: current status and severity,
what is confirmed, what is still unknown, what has been tried, and the next planned
action. The incoming responder should need no verbal briefing to continue.

## Postmortem

Write it blameless. Focus on the system and the conditions, not the person.

- Timeline: what happened and when, from first signal to resolution.
- Impact: who was affected, how much, for how long.
- Root cause and the contributing factors around it.
- What went well, what was hard, where you got lucky.
- Action items with owners and dates. Fix the class of problem, not just the instance.

## Boundaries

- This covers production-incident response. Deep forensic work (chain-of-custody, evidence integrity) is a heavier discipline handled separately.
- Contain before you investigate root cause. A perfect diagnosis on a still-burning fire is the wrong order.
