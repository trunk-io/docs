---
description: Enterprise CI Reliability at Scale
---

# Trunk Platform

### Eliminate CI Bottlenecks and Ship Faster

Trunk is a platform for CI reliability that eliminates pipeline bottlenecks with intelligent merge queue management, automated flaky test detection, and agent-powered failure analysis.

#### Keeping CI Green At

{% columns %}
{% column width="25%" valign="middle" %}
<figure><img src=".gitbook/assets/Brex-logo-ink.svg" alt="" width="150"><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><img src=".gitbook/assets/Zillow Logo_Primary_RGB (1).png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}

{% column valign="middle" %}
<figure><img src=".gitbook/assets/idQDcTgM6U_1761333212059.png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}

{% column valign="middle" %}
<figure><img src=".gitbook/assets/Faire logo.svg" alt="" width="134"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

### Features

#### Advanced Merge Queue

Enterprise-grade merge queue that accelerates PR throughput while protecting your main branch. Purpose-built for high-velocity monorepos with intelligent batching to reduce CI costs by up to 90%, parallel queues for testing independent code changes simultaneously, and anti-flake protection to prevent transient failures from blocking merges.

Learn more about [Merge Queue](broken-reference)

#### Automated Flaky Test Management

Trunk Flaky Tests automatically detects flaky tests and quarantines them to prevent CI failures. Track, manage, and fix flaky tests across any language, environment, or test framework.

Learn more about [Flaky Tests](flaky-tests/detection.md)

#### Agent-Powered Root Cause Analysis (beta)

Automatically identifies and explains the root cause of test and CI failures using autonomous AI agents. Delivers actionable insights directly in GitHub PR comments and Slack, including failure classification, impact assessment, and suggested fixes. Also available in Cursor and VSCode via the Trunk MCP Server.

{% hint style="info" %}
CI Autopilot is currently in private beta. Sign up for the [waitlist](https://trunk.io/ci-autopilot) to be the next to get access.

Learn more about [CI Autopilot](broken-reference)
{% endhint %}

### Get Started

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Merge Queue</strong></td><td>A merge queue to make merging code in GitHub safer and easier</td><td></td><td><a href="merge-queue/set-up-trunk-merge/">set-up-trunk-merge</a></td><td><a href=".gitbook/assets/Merge.png">Merge.png</a></td></tr><tr><td><strong>Flaky Tests</strong></td><td>Detect, quarantine, and eliminates flaky tests from your codebase</td><td></td><td><a href="flaky-tests/get-started/">get-started</a></td><td><a href=".gitbook/assets/FlakyTests.png">FlakyTests.png</a></td></tr><tr><td><strong>CI Autopilot (beta)</strong></td><td>AI root cause analysis and fixes for test and CI failures</td><td></td><td><a href="ci-autopilot/get-started/">get-started</a></td><td><a href=".gitbook/assets/CIAnalytics.png">CIAnalytics.png</a></td></tr></tbody></table>
