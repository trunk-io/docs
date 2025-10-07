---
description: Detect, quarantine, and eliminates flaky tests from your codebase
---

# Overview

Trunk Flaky Tests lets your teams detect, track, quarantine, and fix **flaky tests** in your codebase. Flaky Tests is language, environment, and framework-agnostic.

Let's explore how Trunk Flaky Tests' features help you tackle Flaky Tests. If you can't wait to try Trunk, follow our [getting started guide](https://docs.trunk.io/flaky-tests/get-started).

You can see an overview of Trunk Flaky Tests in this video.

{% embed url="https://youtu.be/ORE30UUvOJk" %}

### Understand the impact

Your dashboard shows a comprehensive overview of your test suite's health at a glance. It lets you see important impact metrics like the number of flaky tests, broken tests, PRs impacted by flaky tests, and PRs rescued by quarantining flaky tests.

<figure><picture><source srcset="../.gitbook/assets/key-metrics-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/key-metrics-light.png" alt=""></picture><figcaption><p>Key repo metrics</p></figcaption></figure>

To learn more, [see how Flaky Tests does detection](https://docs.trunk.io/flaky-tests/detection).

### Track every flaky test

You can find a list of known flaky tests complete with important information like their impact on PRs and if someone's working on a fix. For more granularity, you can also inspect individual tests for their execution history, results, and status changes.

<figure><picture><source srcset="../.gitbook/assets/flaky-tests-overview-table-v2-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/flaky-tests-overview-table-v2-light.png" alt=""></picture><figcaption><p>List of flaky tests</p></figcaption></figure>

To learn more, [see how Flaky Tests does detection](https://docs.trunk.io/flaky-tests/detection).

### Stay in sync

<figure><picture><source srcset="../.gitbook/assets/github-comment-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/github-comment-light.png" alt="PR comment linking to PR Test Summary"></picture><figcaption><p>PR comment linking to PR Test Summary</p></figcaption></figure>

Flaky Tests helps everyone in your team stay in sync about flaky test failures with [GitHub PR comments](https://docs.trunk.io/flaky-tests/github-pull-request-comments), so no time is wasted debugging failures from known flaky tests.

To learn more, [see our docs about GitHub Comments and Test Summaries](github-pull-request-comments.md).

### Investigate flaky failures

Flaky Tests creates detailed reports for individual test failures so you can debug faster.

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption><p>Summary of unique failure types</p></figcaption></figure>

Test details will summarize all the unique ways a flaky test fails and let you flip through the relevant stack traces in the Trunk app.

<figure><picture><source srcset="../.gitbook/assets/run-details-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/run-details-light.png" alt=""></picture><figcaption><p>Full failure stack traces</p></figcaption></figure>

To learn more, [see our docs about the detection of flaky tests](detection.md#test-case-details).

### **Quarantine flaky failures**

Flaky Tests allows you to [quarantine](https://docs.trunk.io/flaky-tests/quarantining) detected flaky tests, stopping them from failing your CI jobs. This prevents failed flaky tests from impacting your CI pipelines, so you won’t have to disable tests and won’t be slowed down by flaky CI jobs.

<figure><picture><source srcset="../.gitbook/assets/override-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/override-light.png" alt=""></picture><figcaption><p>flaky tests can be quarantined automatically or manually</p></figcaption></figure>

To learn more, [see our docs about quarantining tests](quarantining.md).

### Manage tickets

<figure><picture><source srcset="../.gitbook/assets/jira-ticket-creation-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/jira-ticket-creation-light.png" alt=""></picture><figcaption><p>Creating a Jira ticket for a flaky test</p></figcaption></figure>

Trunk enables the automation of quickly creating and assigning tickets through integrations with platforms like Jira and Linear, as well as custom workflows with webhooks. The status of tickets created will be reflected in real-time in the Trunk web app. This helps you track efforts to fix high-impact, flaky tests.

To learn more, [learn about our ticketing integrations](ticketing-integrations/jira-integration.md).

### **Next steps**

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Getting started</strong></td><td></td><td><a href="get-started/">get-started</a></td></tr><tr><td><strong>Create an account</strong></td><td></td><td><a href="https://app.trunk.io/signup?intent=flaky+tests">https://app.trunk.io/signup?intent=flaky+tests</a></td></tr></tbody></table>

Start finding flaky tests today by [signing up for Trunk](https://app.trunk.io/signup?intent=flaky%20tests) or reading our [Getting Started guides](get-started/).
