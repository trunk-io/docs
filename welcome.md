---
description: Your AI DevEx Agent.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
---

# Welcome

### Your AI DevEx Agent

Trunk is a DevEx (Developer Experience) platform using autonomous, agentic AI to help you detect and root cause problems – before they block you team.

By collecting insights from your CI jobs and test results, Trunk can automatically detect problems in your CI, detect the root cause, alert developers, and help you take action through the Trunk MCP server.

{% hint style="success" %}
Sign up for the waitlist in the [Trunk Web App](https://app.trunk.io/trunk/devex-ai?repo=trunk-io%2Fflake-factory), and we'll reach out when we're ready to onboard you.
{% endhint %}

{% code title="Trunk's architecture" %}
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
{% endcode %}

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Connect to Trunk</strong></td><td><a href="setup-and-configuration/connecting-to-trunk.md">connecting-to-trunk.md</a></td></tr><tr><td><strong>Configure Flaky Tests</strong></td><td><a href="flaky-tests/get-started/">get-started</a></td></tr><tr><td><strong>Install the CLI</strong></td><td><a href="references/cli/install.md">install.md</a></td></tr></tbody></table>

### Features

#### Flaky & broken test detection

An autonomous agent continuously detects and quarantines flaky or broken tests before they block developers.

[Learn more about Detection](welcome.md#flaky-and-broken-test-detection)

#### Root-cause analysis

Finds and explains the root cause of failed tests or CI jobs using AI, in GitHub, Slack, and even Cursor via the Trunk MCP Server.

[Sign up for the waitlist](https://app.trunk.io/trunk/devex-ai?repo=trunk-io%2Fflake-factory)

#### Automated developer notifications

Slack DMs, GitHub comments, and GitHub PR annotations with root cause analysis, classification, impact, and suggestions of CI and test failures.

[Learn more about Automated Notifications](flaky-tests/webhooks/)

#### CI health dashboard

Unified dashboard showing current and historical CI and test suite health with status classification.

[Learn more about CI health dashboard](flaky-tests/dashboard.md)

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Flaky Tests (beta)</strong></td><td>Detect, quarantine, and eliminates flaky tests from your codebase</td><td></td><td><a href="flaky-tests/overview.md">overview.md</a></td><td><a href=".gitbook/assets/FlakyTests.png">FlakyTests.png</a></td></tr><tr><td><strong>Merge Queue</strong></td><td>A merge queue to make merging code in GitHub safer and easier</td><td></td><td><a href="merge-queue/merge-queue.md">merge-queue.md</a></td><td><a href=".gitbook/assets/Merge.png">Merge.png</a></td></tr><tr><td><strong>Code Quality</strong></td><td>An extensible superlinter with a builtin language server and pre-existing issue detection</td><td></td><td><a href="code-quality/code-quality.md">code-quality.md</a></td><td><a href=".gitbook/assets/CodeQuality.png">CodeQuality.png</a></td></tr></tbody></table>

### Join Our Community

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Slack</strong></td><td>Join the Trunk Community Slack to get help, give feedback, and talk dev-experience best practices</td><td></td><td></td><td><a href="https://slack.trunk.io">https://slack.trunk.io</a></td></tr><tr><td><strong>GitHub</strong></td><td>Browse or contribute to Trunk's open source integrations</td><td></td><td></td><td><a href="https://github.com/orgs/trunk-io">https://github.com/orgs/trunk-io</a></td></tr><tr><td><strong>Feature Requests</strong></td><td>Request features you'd like to see Trunk tackle next</td><td></td><td></td><td><a href="https://github.com/orgs/trunk-io/discussions">https://github.com/orgs/trunk-io/discussions</a></td></tr></tbody></table>
