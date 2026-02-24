---
description: Ship Software as Fast as AI Writes It
---

# Trunk Platform

AI generates code at machine speed, but code review, CI, and delivery still move at human pace. That gap is widening, and it gets worse every time you add another AI agent to the loop.

Trunk enables continuous delivery: any commit on your main branch could be deployed to production. We do this by eliminating the two bottlenecks that prevent it. Flaky tests that waste developer time, and serialized merge queues that cap your throughput.

Teams start with whichever problem hurts more, then expand. Caseware cut merge time from 6 hours to 90 minutes. Zillow eliminated all pipeline blockages from flaky tests. Faire prevented 20% of main branch failures from green-green conflicts.

<details>

<summary>Want to see how it works? Have questions?</summary>

[Schedule time here](https://calendly.com/trunk/demo) or email [support@trunk.io](mailto:support@trunk.io)

</details>

#### Why This Matters Now

You check out main on Monday morning, grab your coffee, open a pull request, and CI fails for reasons that have nothing to do with your code. You're reading logs, pinging Slack, trying to figure out who broke what. That happens to every engineer, every day. Continuous delivery means every commit on main is known-good. Every CI failure is yours to fix, not something you inherited.

That problem has existed for years. What makes it urgent now is volume. AI agents are generating 50+ PRs a day, and they hit the same merge queue serialization and flaky test noise that slows humans. Except agents can't context-switch to other work while they wait. Every bottleneck in your CI pipeline that used to cost you hours now costs you days.

#### Trunk Flaky Tests

At tens of thousands of tests, even a 1% flake rate means false failures on nearly every run. Each flake costs 10 to 15 minutes: the developer waits, reads logs, reruns, confirms it was noise. If your CI target is five-minute PR jobs, every flake doubles or triples that.

Trunk detects flakes through branch-aware analysis that treats main, PRs, and merge queues differently. We fingerprint failure modes using stack trace embeddings, which means quarantine decisions are based on the actual failure pattern, not just the test name. If a quarantined test fails with a known flaky pattern, CI passes. If it fails in a new way, CI fails normally. Business-critical tests can be pinned as never-quarantine. Developers see all of this in PR comments: what failed, why, and whether it's their code or a known issue. No code changes required.

On the repair side, we're working with design partners on AI-powered fixing through MCP integration with the likes of Claude Code, Codex, or Cursor. Trunk provides the failure data and CI context, and the agent uses that to iterate on the actual fix. Think of it as a Roomba for flaky tests. Teams in the program are already running it to detect flakes, figure out root causes, and submit fixes without a human in the loop.

[Full Flaky Tests documentation →](flaky-tests/overview.md)

#### Trunk Merge Queue

Traditional merge queues guarantee main stability by testing PRs one at a time. At 100+ PRs/day, that becomes a bottleneck. Monorepos make this easier to solve. If you have mobile, frontend, and backend code in the same repo, those PRs can test and merge independently because they don't touch the same targets. Linear merge queues don't know that. They put everything in one line.

Trunk's merge queue runs in parallel mode. It knows which targets each PR affects, finds non-overlapping sets, and tests them at the same time. When queue depth grows, it batches multiple PRs into a single CI run and bisects automatically if the batch fails. Anti-flake protection keeps flaky failures from stalling the queue: if a later batch that includes the same code passes, both merge.

Validated at 250+ PRs/hour sustained over 24 hours. Peaked at 300+ simultaneous PRs in parallel testing.

[Full Merge Queue documentation →](merge-queue/merge-queue.md)

#### How They Work Together

Without flaky test handling, a merge queue backs up every time a test becomes unreliable. One recurring flake means batches fail, need re-isolation, and the queue goes serial again. With both products running, flakes get quarantined by failure mode so CI stays clean, parallel mode and batching keep the queue moving, and anti-flake protection in the queue catches what slips through.

#### Trusted by

<figure><picture><source srcset=".gitbook/assets/4x2 Logos (Dark-NoBG).png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/4x2 Logos (Light-NoBG).png" alt=""></picture><figcaption></figcaption></figure>

#### Works With Your Stack

* **CI providers**: Works with any CI provider. Common setups include GitHub Actions, GitLab CI, Jenkins, BuildKite, CircleCI, and Azure DevOps. Integrates via CLI that uploads test results from existing pipelines.
* **Languages**: Works with any language. We analyze test output formats, not source code, so there's nothing language-specific to configure.
* **Test frameworks**: Works with any runner that produces JUnit XML, XCResult, or Bazel BEP. That covers Jest, Pytest, XCTest, Cypress, Playwright, RSpec, JUnit, GoogleTest, and most others.
* **Build systems**: Bazel, Nx, Gradle with native impacted-target calculation. API for custom build systems.
* **Integrations**: Full APIs for both products, webhooks with Svix transformations, CLI for local and CI use, Slack notifications, Jira and Linear ticket creation. [API documentation →](setup-and-administration/apis/)

#### Why Teams Choose Trunk

**vs. GitHub native merge queue, Bors, Mergify.** Sequential by design. No parallel lane logic, no flake protection, no batching with bisection.

**vs. Datadog, Buildkite Analytics.** They show you flake data but don't quarantine at runtime or integrate with your merge queue. Most stop running quarantined tests entirely, which hides the problem. Trunk keeps running them to collect evidence for root cause analysis.

**vs. building in-house.** Merge queues at scale need parallel graph computation, bisection, and robust GitHub API orchestration. Flaky test detection at 50k+ tests needs real-time ETL, embeddings, and classification. If the engineers who built your internal system leave, you're maintaining deployment-path infrastructure without the knowledge to fix it.

#### Getting Started

Most teams schedule a 30-minute call before integrating. We help plan for security reviews, understand your CI architecture, and flag common gotchas.

* [**Schedule a call**](https://calendly.com/trunk/trunk-integration-planning) ← Recommended

Or explore on your own: [Create a Trunk account →](https://app.trunk.io/signup)

* [Flaky Tests Integration Guide](https://docs.trunk.io/flaky-tests/get-started)
* [Merge Queue Setup Guide](https://docs.trunk.io/merge-queue/set-up-trunk-merge)

We set up a direct Slack Connect channel with our engineers for your team. Feature requests, debugging, planning. Not a vendor you file tickets with.

#### Security & Compliance

SOC 2 Type II certified. TLS/HSTS in transit, AES-256 at rest. AWS-hosted in U.S. data centers with private VPCs. MFA, least privilege, access logging. Regular vulnerability scans, annual third-party pen tests. 45-day test result retention. We don't access your source code, secrets, environment variables, or customer data. [Request SOC 2 report](mailto:security@trunk.io).

{% hint style="info" %}
**Want to see how it works? Have questions?** [**Schedule time here**](https://calendly.com/trunk/demo) **or email** [**support@trunk.io**](mailto:support@trunk.io)
{% endhint %}

#### Learn More

<table data-card-size="large" data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Merge Queue</strong></td><td>A merge queue to make merging code in GitHub safer and easier</td><td></td><td><a href="merge-queue/merge-queue.md">merge-queue.md</a></td><td><a href=".gitbook/assets/Merge.png">Merge.png</a></td></tr><tr><td><strong>Flaky Tests</strong></td><td>Detect, quarantine, and eliminates flaky tests from your codebase</td><td></td><td><a href="flaky-tests/overview.md">overview.md</a></td><td><a href=".gitbook/assets/FlakyTests.png">FlakyTests.png</a></td></tr></tbody></table>
