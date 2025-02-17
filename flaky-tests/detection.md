---
description: Learn how Trunk detects and labels flaky tests
---

# Flaky Test Detection

Trunk detects flaky tests by analyzing test results uploaded from your CI jobs. This page covers how flaky tests are detected and how they're labeled after Trunk receives uploaded test results.&#x20;

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption></figcaption></figure>

Trunk Flaky Tests detects flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

You can learn more about how tests are uploaded to Trunk before they're labeled in the [Get Started docs](get-started/). You can learn more about how detection results are displayed in the [Dashboard docs](dashboard.md).

{% hint style="info" %}
Trunk typically requires 10+ runs per test on CI to start accurately detecting flaky tests. For example, detecting a flaky test that fails 25% of the time takes 9 runs to achieve 90% confidence in having seen it flake. Depending on the repository’s velocity, this could take hours or days.
{% endhint %}

Trunk detects flaky tests by analyzing the test results uploaded from your CI jobs. Each new upload is processed and compared with historical test results to detect flaky tests. Trunk emphasizes each result differently depending on which branch it's run on. \
\
**This is an asynchronous process, and it may take up to an hour for an upload's results to be reflected in** [**the dashboard**](get-started/#id-4.-confirm-your-configuration-analyze-your-dashboard)**.**

<figure><picture><source srcset="../.gitbook/assets/uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/uploads-light.png" alt=""></picture><figcaption><p>The uploads tab contains results received from past CI jobs.</p></figcaption></figure>

### How We Detect Flakiness

Trunk analyzes test failures based on the context in which they are run. A test failing on `main` has a different impact on flake detection than a test failing on a pull request. After tests are uploaded to Trunk, they're analyzed based on different rules depending on which branch they were run on.

{% hint style="warning" %}
Uploading all test results from your repository will result in the fastest and most accurate detection. Trunk relies on test results from `main`, pull requests, and (if you use one) merge queues.
{% endhint %}

#### Main Branch

Trunk detects flaky tests with the assumption that automated tests should be passing before being merged into protected branches like `main` or `master`. This means failures on `main` or `master` are unexpected and indicate flakiness or a broken test.&#x20;

#### Pull Requests

Tests that are run on pull requests are expected to fail, so failures on pull requests are not directly used in the detection of flaky tests.

Flaky tests will produce inconsistent results even when run on the same code with the same input. Pull requests are where we see this behavior the most often: an engineer opens a pull request, sees a test fail, re-runs the code, and sees the test pass. If a test is detected to produce different results on the same git commit, which means different results on the same code, we consider that test to be flaky.

#### Merge Queue

Merge queues use temporary branches to test changes again before merging into `main`. Failures on merge queue branches are unexpected and are used as a signal when detecting flaky tests. Trunk currently auto-detects merge queue CI jobs from Trunk Merge Queues, GitHub Merge Queues, GitLab Merge Trains, and Graphite Merge Queues.

{% hint style="info" %}
Expect test results for individual PRs to be up-to-date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes post-upload and all other metrics to be up-to-date within an hour.
{% endhint %}

### Test Status

Trunk classifies all tests into one of three categories based on the history of each test:

<table><thead><tr><th width="178">Test Status</th><th>Description</th></tr></thead><tbody><tr><td>Flaky</td><td>This test is not deterministic. Given the same inputs, the test will occasionally produce different outputs. This means you <strong>cannot trust the results</strong> of these tests.</td></tr><tr><td>Broken</td><td>This test is reproducible but is always failing. These tests that always fail are not useful and should be fixed.</td></tr><tr><td>Healthy</td><td>This test is reproducible. Given the same inputs, the test will produce the same outputs.</td></tr></tbody></table>

### Next Steps

If you have not set up your CI jobs to upload results to Trunk, follow the [Get Started docs](get-started/) to start uploading test results to Trunk.

If you're curious about why certain tests are labeled as flaky, you can visit each test's status history. [Learn more about Status History.](dashboard.md#status-history)

<figure><picture><source srcset="../.gitbook/assets/status-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/status-history-light.png" alt=""></picture><figcaption></figcaption></figure>
