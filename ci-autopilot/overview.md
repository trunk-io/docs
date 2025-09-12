---
description: >-
  Trunk's CI Autopilot offers AI root cause analysis and fixes for test and CI
  failures
---

# Overview

{% hint style="success" %}
## CI Autopilot is currently invite-only in private beta.

Sign up for the [waitlist](https://trunk.io/ci-autopilot) to be the next to get access. We'll reach out when we're ready to onboard you.
{% endhint %}



**Stop debugging CI failures manually.** CI Autopilot's AI investigates every test failure, identifies root causes, and provides ready-to-apply fixes in minutes - not hours.



### How It Works

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

CI Autopilot monitors your CI jobs and tests, rapidly identifying root causes of failures and providing fixes far quicker than manual debugging.



**It integrates seamlessly with GitHub Actions and your** [**test execution framework**](../flaky-tests/get-started/frameworks/)**.**&#x20;



When your CI fails, CI Autopilot:

* **Investigates failures** by analyzing code, logs, test results, and git history
* **Posts detailed explanations** as GitHub comments with precise root cause analysis
* **Provides instant fixes** via stacked pull requests or direct AI assistant integration
* **Groups related failures** to resolve multiple issues with a single fix



### Two Ways to Get Fixes

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Stacked Pull Requests</strong></td><td>Perfect for team workflows and code review processes. CI Autopilot creates separate PRs with proposed fixes that you can review and merge.</td><td><a href="../use-ci-autopilot/request-fixes-on-prs.md">request-fixes-on-prs.md</a></td></tr><tr><td><strong>AI Assistant Integration</strong> <strong>(MCP)</strong></td><td>Work with Cursor, GitHub Copilot, Claude Code or other AI coding tools. Your assistant accesses the root cause analysis and applies fixes directly in your IDE.</td><td><a href="../use-ci-autopilot/apply-fixes-with-mcp.md">apply-fixes-with-mcp.md</a></td></tr></tbody></table>



### Key Features

**AI-Powered Root Cause Analysis** Analyzes repository files, CI logs, test results, PR diffs, git history, and even checks for external outages to pinpoint exact failure causes.

**Intelligent Fix Application**\
Choose between automated stacked pull requests for team workflows or direct AI assistant integration for immediate fixes in your IDE.

**Seamless GitHub Integration** Works within your existing development workflow—no new tools to learn or processes to change.



### Get Started Now!

{% hint style="success" %}
## CI Autopilot is currently invite-only in private beta.

Sign up for the [waitlist](https://trunk.io/ci-autopilot) to be the next to get access. We'll reach out when we're ready to onboard you.
{% endhint %}

#### [Basic Setup (5 minutes)](get-started/connect-to-github.md)

Connect CI Autopilot to GitHub for immediate failure analysis from CI logs.

* ✅ Instant root cause identification
* ✅ Fix recommendations in GitHub comments
* ✅ Works with any test framework

#### [Enhanced Setup (+10 minutes)](get-started/upload-test-reports.md)

Add structured test reports for precise, test-level analysis.

* ✅ Test-specific, targeted fixes
* ✅ Better accuracy and detail
* ✅ Enhanced failure grouping

