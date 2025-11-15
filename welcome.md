---
description: CI reliability platform for high-velocity engineering teams
---

# Trunk Platform

### What is Trunk?

Trunk is a CI reliability platform that solves the two bottlenecks killing velocity at scale: merge queue serialization and flaky test multiplication.

* **Trunk Merge Queue** parallelizes your merge queue by testing non-overlapping changes simultaneously—so frontend PRs don't wait behind unrelated backend tests.
* **Trunk Flaky Tests** automatically detects and quarantines unreliable tests—so false failures stop blocking your pipeline.

Teams typically start with whichever problem is more urgent, then expand as their CI scales. Caseware cut merge time from 6 hours to 90 minutes. Zillow eliminated all pipeline blockages from flaky tests.

<details>

<summary>Want to see how it works? Have questions? </summary>

[Schedule time here](https://calendly.com/trunk/demo) or email [support@trunk.io](mailto:support@trunk.io)

</details>

### The Problems We Solve

Modern build systems (Bazel, Nx, Gradle) give you parallelization and caching. But at scale, two critical bottlenecks emerge that break everything else:

#### 1. Merge Queue Bottlenecks

**Without a merge queue:** Independently-passing PRs break `main` when they conflict.

**With a traditional merge queue:** You've solved stability but created a serial processing bottleneck. PRs test one-at-a-time in a single queue, so frontend changes wait behind unrelated backend tests. Queue wait times grow linearly with PR volume.

At 150+ PRs/day, this becomes a disaster. At 3,000 PRs/day, it's completely unworkable.

#### 2. Flaky Test Multiplication

At tens of thousands of tests, even a 1% flake rate means false failures on every test run.

In merge queues, each flaky failure blocks multiple PRs—turning minor issues into major bottlenecks. Worse, when developers know there's a chance a re-run will pass, they stop trusting test failures altogether.

### Our Solution

**Graph-based parallel merge lanes** that test non-overlapping changes simultaneously while guaranteeing `main` stability, plus **automated flaky test detection and quarantine** that prevents false failures from blocking your pipeline.

#### Merge Queue

* **Parallel queues**: Analyzes which code each PR touches to create independent test lanes for non-overlapping changes—transforming queue bottlenecks from a single line into an efficient graph where unrelated PRs test simultaneously
* **Intelligent batching with bisection**: Test multiple PRs together in a single CI run (reducing costs up to 90%), with automatic bisection to isolate failures without ejecting entire batches. Caseware processes 4-8 PRs per batch with zero manual intervention, reducing their median merge time from 6 hours to 90 minutes
* **Scale-tested reliability**: Validated at 250+ PRs/hour over 24-hour periods (6,000+ PRs/day)&#x20;
* **Anti-flake protection**: Failed PRs get additional chances to pass as later PRs retest their code—if subsequent PRs (that include the failed code) pass, all merge together without blocking the queue. Combines Optimistic Merging and Pending Failure Depth
* **Predictive testing**: Tests each PR against the predicted future state of main (including all PRs ahead in queue), guaranteeing branch stability without endless rebase-retest loops. Faire prevented 20% of main branch failures from green-green conflicts
* **API & webhook integrations**: Submit PRs programmatically, build custom merge bot, or trigger workflows on queue events. Faire built custom Chrome extensions and automation services using the API to handle unique deployment workflows

#### Flaky Tests

* **Branch-aware detection**: Analyzes test failures differently on main, PRs, and merge queues—a test showing inconsistent results on the same commit gets flagged as flaky, while expected failures during PR development don't trigger false positives
* **No-code quarantine**: Quarantine flaky tests through the dashboard without touching source code or navigating merge queues—eliminating the recursive nightmare of merging test fixes through an already-broken pipeline. With auto-quarantine enabled, tests flagged as flaky are automatically isolated while continuing to run and collect data for prioritization. Zillow achieved zero pipeline blockages from known flaky tests
* **Continuous analysis**: Analyzes every pipeline execution (not just periodic sampling) to detect patterns across your entire organization—see whether a test flaked once or 45 times today, preventing developers from "gaslighting themselves" about whether failures are related to their code
* **AI-powered debugging**: Summarizes errors and identifies patterns across aggregated failures to drastically reduce diagnostic time, especially for issues that can't be reproduced locally due to CI environment differences
* **In-PR visibility**: Flaky test information surfaces directly in pull request comments, providing immediate feedback without leaving your code review workflow. Metabase uses this alongside webhook integrations to automatically create Linear tickets for tracking and prioritization

#### Trusted by

<figure><picture><source srcset=".gitbook/assets/4x2 Logos (Dark-NoBG).png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/4x2 Logos (Light-NoBG).png" alt=""></picture><figcaption></figcaption></figure>

### Technical Details

#### Works With Your Stack

* **CI-agnostic**: GitHub Actions, GitLab CI, Jenkins, BuildKite, CircleCI, Azure DevOps, and any other CI provider—integrates via CLI that uploads test results from your existing pipelines
* **Language-agnostic**: Go, TypeScript, Python, Swift, Java, Kotlin, Ruby, Solidity, Rust, and any other language—works by analyzing test output formats (JUnit XML, XCTest, etc.), not your source code
* **Test framework-agnostic**: Jest, Pytest, XCTest, Cypress, Playwright, RSpec, JUnit, GoogleTest, and 25+ other frameworks—if your test runner can produce structured output, Trunk can analyze it
* **Build system support**: Native integrations for Bazel, Nx, and Gradle to calculate impacted targets for parallel merge queues, with API for custom build systems

#### Integration Points

* **Merge Queue API**: Submit PRs with custom priorities, cancel/restart tests, set impacted targets for parallel queues, query queue state and PR readiness, update queue state (RUNNING/PAUSED/DRAINING)—build custom merge bots and automation workflows
* **Flaky Tests API**: List quarantined/unhealthy tests (filter by FLAKY/BROKEN), link Jira/Linear tickets to test cases, fetch test metadata (failure rates, common failures, codeowners, PR impact)—integrate into local dev environments, dashboards, or CI/CD pipelines
* **Webhooks**: Subscribe to PR events (`submitted`, `queued`, `testing`, `merged`, `failed`, `canceled`), batch events (`pull_request_batch.merged`), and test events (`status_changed`, `quarantining_setting_changed`)—trigger custom workflows with Svix transformations (filter by PR impact, format for Slack/Teams/GitHub Issues, auto-assign via CODEOWNERS)
* **CLI**: Platform-agnostic `trunk` CLI uploads test results (JUnit XML, Bazel BEP, XCResult), validates reports locally, wraps test commands to override exit codes for quarantined tests, manages merge queue operations (submit/cancel/status/pause)
* **Native integrations**: Slack notifications for Merge Queue events (PR state changes, queue updates) and Flaky Test webhooks; Jira & Linear ticket creation with auto-generated descriptions, configurable labels/assignees, and API linking for existing tickets

### Why Teams Choose Trunk Over Alternatives

**vs. Basic Merge Queues (GitHub native, Bors)**

* **Sequential bottlenecks**: Basic queues test PRs one-at-a-time. At 100+ PRs/day, frontend changes wait hours behind unrelated backend tests. Trunk's parallel processing tests independent changes simultaneously.
* **No flake protection**: One flaky test blocks multiple PRs in the queue. Trunk's anti-flake protection prevents false failures from cascading.
* **Missing cost optimization**: Running full CI for every PR combination is expensive. Trunk's intelligent batching reduces CI costs by up to 90%.

**vs. Observability Platforms (Datadog, etc.)**

* **Flaky test detection isn't their core focus**: General observability tools bolt on test analytics. Trunk is purpose-built for CI reliability with transparent detection showing exactly why each test is classified as flaky.
* **Black-box vs. active analysis**: Observability platforms stop running quarantined tests, hiding the problem. Trunk continues running them for root cause analysis—you see the data you need to actually fix issues.
* **Disconnected tools**: Using separate vendors for flaky tests, merge queues, and CI debugging means integration overhead and finger-pointing.

**vs. Building In-House**

* **Data engineering at scale**: Processing 50k-100k tests per run requires real-time ETL pipelines, specialized storage, and classification algorithms to identify flaky vs. broken tests—then surfacing that data in high-performance UIs engineers actually use.
* **Complex coordination problems**: At 100+ PRs/day, you need parallel graph computation, bisection algorithms to isolate failures in batched PRs, intelligent restarts to recompute predicted main state, and robust GitHub API orchestration. These aren't one-time problems to solve.
* **Operational risk on mission-critical infrastructure**: Merge queues block your entire team when they fail. If the engineers who built your system leave, you're maintaining complex infrastructure in your deployment path without the knowledge to fix it.
* **Opportunity cost**: Every sprint on merge queue or flaky test tooling is a sprint not building features that differentiate your product.

### Getting Started

Most teams schedule a 30-minute call before integrating—we'll help you plan for security reviews, understand your CI architecture, and avoid common implementation gotcas. We'll also set up a direct Slack Connect, MS Teams, or email channel for ongoing engineering support.

#### [**Schedule a call**](https://calendly.com/trunk/trunk-integration-planning) ← Recommended for most teams

**Prefer to explore on your own first?**&#x20;

You can create an account and follow the integration guides below. Note that GitHub app installation typically requires security approval at most companies, and integration complexity varies significantly based on your CI setup.

* [Create a Trunk account →](https://app.trunk.io/signup)

#### **Integration Guides**

Start with whichever problem is more urgent:

**Start with Flaky Tests** if you're dealing with unreliable tests blocking CI:

* [Flaky Tests Integration Guide](https://docs.trunk.io/flaky-tests/get-started)

**Start with Merge Queue** if you're dealing with merge bottlenecks:

* [Merge Queue Setup Guide](https://docs.trunk.io/merge-queue/set-up-trunk-merge)

#### Support

* **Direct engineering support**: We maintain Slack Connect or MS Teams channels with most of our customers. This direct line of communication with our engineers is one of the key benefits of working with Trunk—whether you're debugging a production issue or need help optimizing your setup. Email [support@trunk.io](mailto:support@trunk.io) to get started.

#### Security & Compliance

* **SOC 2 Type II Certified**: Independently audited controls for security, availability, and confidentiality—[request report](mailto:security@trunk.io)
* **Encryption**: TLS/HSTS for data in transit, AES-256 for data at rest
* **Infrastructure**: AWS-hosted in secure U.S. data centers with network isolation (private VPCs, no direct internet access)
* **Access Control**: MFA required for sensitive systems, principle of least privilege, access logging and monitoring
* **Security Testing**: Quarterly vulnerability scans, annual third-party penetration tests
* **Data Retention**: Test results retained for 45 days for historical flakiness analysis
* **What we don't access**: Source code (only test results and CI metadata), secrets, environment variables, customer data

{% hint style="info" %}
**Want to see how it works? Have questions?** [**Schedule time here**](https://calendly.com/trunk/demo) **or email** [**support@trunk.io**](mailto:support@trunk.io)
{% endhint %}

### Learn More

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Merge Queue</strong></td><td>A merge queue to make merging code in GitHub safer and easier</td><td></td><td><a href="merge-queue/merge-queue.md">merge-queue.md</a></td><td><a href=".gitbook/assets/Merge.png">Merge.png</a></td></tr><tr><td><strong>Flaky Tests</strong></td><td>Detect, quarantine, and eliminates flaky tests from your codebase</td><td></td><td><a href="broken-reference">Broken link</a></td><td><a href=".gitbook/assets/FlakyTests.png">FlakyTests.png</a></td></tr><tr><td><strong>CI Autopilot (beta)</strong></td><td>AI root cause analysis and fixes for test and CI failures</td><td></td><td><a href="broken-reference">Broken link</a></td><td><a href=".gitbook/assets/CIAnalytics.png">CIAnalytics.png</a></td></tr></tbody></table>
