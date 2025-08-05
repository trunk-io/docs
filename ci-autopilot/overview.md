---
description: AI root cause analysis and fixes for test and CI failures
---

# Overview

{% hint style="success" %}
## CI Autopilot is currently invite-only in private beta.

Sign up for the [waitlist](https://trunk.io/insights) to be the next to get access. We'll reach out when we're ready to onboard you.
{% endhint %}

### How CI Autopilot works

Trunk's CI Autopilot monitors your CI jobs and tests, rapidly identifying root causes of failures and providing fixes far quicker than manual debugging.

It integrates seamlessly with GitHub Actions and your [test execution framework](../flaky-tests/get-started/frameworks/). Whenever a failure occurs, Trunk's specialized [AI DevOps Agent](../ai-devops-agent/overview.md):

* Investigates the failure and identifies the root cause
* Posts detailed explanations and fixes directly as GitHub comments
* Opens stacked PRs with fixes

If you like the suggested fixes, simply merge them into your PR. You can also further modify them by checking out the stacked PR branch before merging.

When failures happen on your `main` branch, CI Autopilot detects these immediately and proactively opens PRs to resolve the root issues.

```
                                           ╔═ trunk ═══════════════════════════════════╗ 
╔════════════╗      ╔═══════════╗          ║                         ┏━━━━━━━━━━━━━━┓  ║░
║            ║░     ║           ║░         ║  ┏━━━━━━━━━━━━━━━━┓     ┃   GitHub     ┃  ║░
║   CI Jobs  ║░────▶║   Tests   ║░───API──▶║  ┃  AI Root Cause ┃────▶┃   Slack      ┃  ║░
║            ║░     ║           ║░         ║  ┃    Analysis    ┃     ┃   Linear     ┃  ║░
╚════════════╝░     ╚═══════════╝░         ║  ┗━━━━━━━━━━━━━━━━┛     ┃   MCP        ┃  ║░
 ░░░░░░░░░░░░░░      ░░░░░░░░░░░░░         ║                         ┃   Webhooks   ┃  ║░
      │                                    ║                         ┃   Dashboard  ┃  ║░
      └─────────────── API ───────────────▶║                         ┗━━━━━━━━━━━━━━┛  ║░
                                           ╚═══════════════════════════════════════════╝░
                                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

### Features

Trunk integrates directly into your existing developer workflow, enhancing efficiency, accuracy, and speed in resolving CI and test failures.

#### AI-Powered Debugging and Fixes

The AI DevOps Agent continuously loops, analyzing:

* Your repository files (search and read capabilities).
* CI output and historical data.
* Test results and historical data.
* PR details and diffs.
* Git history.
* Web searches for external outages.

This extensive analysis accurately determines the true root causes of CI and test failures.

#### GitHub Comments

Receive clear GitHub comments pinpointing exactly why tests and CI jobs failed and how to fix them.

#### Stacked PRs

Automatically opened PRs stacked on your existing PR, containing ready-to-merge fixes for your failing tests.

#### Main Branch Protection

Immediate detection and automated PR creation to swiftly fix CI job failures occurring on your `main` branch.



{% hint style="success" %}
## CI Autopilot is currently invite-only in private beta.

Sign up for the [waitlist](https://trunk.io/insights) to be the next to get access. We'll reach out when we're ready to onboard you.
{% endhint %}
