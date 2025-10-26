---
description: Eliminate merge bottlenecks and flaky test failures at scale
---

# Trunk Platform

### Modern CI is fast. But scale breaks everything else.

Your build system (Bazel, Nx, Gradle) gives you massive parallelization and smart caching. But at high velocity, two critical reliability problems emerge:

#### **Merge queue bottlenecks**

Without a merge queue, PRs break `main` when independently-passing changes conflict.

With a traditional merge queue, you've solved stability—but created a serial processing bottleneck. PRs test one-at-a-time in a single queue, so frontend changes wait behind unrelated backend tests. Queue wait times grow linearly with PR volume.

#### **Flaky test multiplication**

At tens of thousands of tests, even 1% flake rates mean false failures on every test run. In merge queues, each flaky failure blocks multiple PRs—turning minor issues into major bottlenecks.

Worse, flaky tests erode trust: When developers know there's a chance a re-run will pass, they stop trusting test failures altogether.

**Trunk eliminates both bottlenecks:** Graph-based parallel merge lanes that test non-overlapping changes simultaneously (while guaranteeing `main` stability), plus automated flaky test quarantine that prevents false failures from blocking your pipeline.

#### Trusted by

{% columns %}
{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Brex_Inc_White.png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Brex_Inc._Corporate_Logo.png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Zillow Logo_Secondary_RGB (1).png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Zillow Logo_Primary_RGB (2).png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Faire logo white.png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Faire logo (1).png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/descript-logo-png_seeklogo-448113 (2).png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/descript-logo-png_seeklogo-448113.png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Handshake_Wordmark_White_RGB1 (1).png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Handshake_Wordmark_Nori_RGB.png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Metabase copy.png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Metabase.png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/Glydways-horizontal-logos-white2.png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/Glydways-horizontal-black (1).png" alt=""></picture><figcaption></figcaption></figure>
{% endcolumn %}

{% column width="25%" valign="middle" %}
<figure><picture><source srcset=".gitbook/assets/waabi-logo-rev copy.png" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/waabi-logo.png" alt=""></picture><figcaption></figcaption></figure>
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
