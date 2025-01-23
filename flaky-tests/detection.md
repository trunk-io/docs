---
description: Learn how Trunk detects flaky tests.
---

# Detection

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption></figcaption></figure>

Trunk Flaky Tests detects flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

{% hint style="info" %}
Trunk typically requires 10+ runs per test on CI to start accurately detecting flaky tests. For example, detecting a flaky test that fails 25% of the time takes 9 runs to achieve 90% confidence in having seen it flake. Depending on the repository’s velocity, this could take hours or days.
{% endhint %}

{% include "../.gitbook/includes/slack-callout.md" %}

### Uploaded Test Results

Trunk detects flaky tests by analyzing the test results uploaded from your CI jobs. Each new upload is processed and compared with historical test results to detect flaky tests. Trunk emphasizes each result differently depending on which branch it's run on. \
\
**This is an asynchronous process, and it may take up to an hour for an upload's results to be reflected in the** [**dashboard**](dashboard.md)**.**

<figure><picture><source srcset="../.gitbook/assets/uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/uploads-light.png" alt=""></picture><figcaption><p>The Uploads tab contains results received from past CI jobs.</p></figcaption></figure>

If you have [PR Comments](github-pull-request-comments.md) enabled, you can follow the link in the PR comments to see a report for each upload.

### How Tests Are Labeled

Trunk classifies all tests into one of three categories based on the history of each test:

<table><thead><tr><th width="218">Test Status</th><th>Description</th></tr></thead><tbody><tr><td>Flaky</td><td>This test is not deterministic. Given the same inputs, the test will occasionally produce different outputs. This means you <strong>cannot trust the results</strong> of these tests.</td></tr><tr><td>Broken</td><td>This test is reproducible but always fails; even when it should pass. This is not helpful and needs to be fixed or removed.</td></tr><tr><td>Healthy</td><td>This test is reproducible. Given the same inputs, the test will produce the same outputs.</td></tr></tbody></table>

### Branches

Trunk analyzes test failures based on the context in which they are run. A test failing on `main` has a different impact on flake detection than a test failing on a pull request.

{% hint style="warning" %}
Uploading all test results from your repository will result in the fastest and most accurate detection. Trunk relies on test results from `main`, pull requests, and (if you use one) merge queues.
{% endhint %}

#### Merge Queue Support

Merge queues use temporary branches to test changes again before merging into `main`. Failures on merge queue branches are unexpected and are used as a signal when detecting flaky tests. Trunk currently auto-detects merge queue CI jobs from Trunk Merge Queues, GitHub Merge Queues, GitLab Merge Trains, and Graphite Merge Queues.

#### Pull Requests

Flaky tests produce inconsistent results even when run on the same code with the same input. This behavior is often seen in pull requests: an engineer opens a pull request, sees a test fail, re-runs the code, and sees the test pass. We track this behavior (different results for a test on the same git commit) as a sign that a test is flaky.

{% hint style="info" %}
Expect test results for individual PRs to be up-to-date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes post-upload and all other metrics to be up-to-date within an hour.
{% endhint %}

### Test Status Transitions

A test’s health status can transition between broken, flaky, and healthy as new test runs with new results are uploaded to Trunk Flaky Tests. Trunk Flaky Tests determines if a test is flaky based on analyzing the results of recent runs. The process is deterministic and based on thresholds set by Trunk.

This means if a test is healthy, it can transition into a broken or flaky status after new results appear that show failures. This also means if a test that was previously labeled as broken or flaky sees consistently passing runs, it can transition into a healthy test.&#x20;

{% include "../.gitbook/includes/retries.md" %}

<figure><picture><source srcset="../.gitbook/assets/status-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/status-history-light.png" alt=""></picture><figcaption></figcaption></figure>

Tests may transition between flaky, broken, and healthy states multiple times over their lifetime. You can see previous changes in the detected health status of a test under Status History, as well as an explanation for why it was detected to have a new state.
