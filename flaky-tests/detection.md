# Detection

Trunk Flaky Tests detect flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

{% hint style="info" %}
Trunk typically requires 10+ runs per test on CI to start accurately detecting flaky tests. For example, detecting a flaky test that fails 25% of the time takes 9 runs to achieve 90% confidence in having seen it flake. Depending on the repository’s velocity, this could take hours or days.
{% endhint %}

{% include "../.gitbook/includes/slack-callout.md" %}

### How Tests Are Labeled

Trunk classifies all tests into one of three categories based on the history of each test:

<table><thead><tr><th width="218">Test Status</th><th>Description</th></tr></thead><tbody><tr><td>Flaky</td><td>This test is not deterministic. Given the same inputs, the test will occasionally produce different outputs. This means you <strong>cannot trust the results</strong> of these tests.</td></tr><tr><td>Broken</td><td>This test is reproducible but is always failing. These tests that always fail are not useful and should be fixed.</td></tr><tr><td>Healthy</td><td>This test is reproducible. Given the same inputs, the test will produce the same outputs.</td></tr></tbody></table>

#### Branches

Trunk analyzes test failures based on the context in which they are run. A test failing on `main` has a different impact on flake detection than a test failing on a pull request.

{% hint style="warning" %}
Uploading all test results from your repository will result in the fastest and most accurate detection. Trunk relies on test results from `main`, pull requests, and (if you use one) merge queues.
{% endhint %}

#### Mergequeue support

Mergequeues use temporary branches to test changes again before merging into `main`. Failures on merge queue branches are unexpected and are used as a signal when detecting flaky tests. Trunk currently auto-detects merge queue CI jobs from Trunk Merge Queues, GitHub Merge Queues, GitLab Merge Trains, and Graphite Merge Queues.

#### Pull Request

Tests that are run on pull requests are expected to fail, so failures on pull requests are not used in the detection of flaky tests.

Flaky tests will produce inconsistent results even when run on the same code with the same input. Pull requests is where we see this behavior the most often: an engineer opens a pull request, sees a test fail, re-runs the code, and sees the test pass. We track this behavior (different results for a test on the same git commit) as sign that a test is flaky.

{% hint style="info" %}
Expect test results for individual PRs to be up to date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes and all other metrics to be up to date within an hour of a new upload.
{% endhint %}

### Test Status Transitions

A test’s health status transitions between broken, flaky, and healthy as new test runs with new results are uploaded to Trunk Flaky Tests. Trunk Flaky Tests determine if a test is flaky based on analyzing the results of recent runs. The process is deterministic and based on appropriate thresholds.

This means if a test is healthy, it can transition into a broken or flaky status after new results appear that show failures. This also means if a test that was previously labeled as broken or flaky sees consistently passing runs, it can transition into a healthy test.&#x20;

{% include "../.gitbook/includes/retries.md" %}

<figure><picture><source srcset="../.gitbook/assets/status-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/status-history-light.png" alt=""></picture><figcaption></figcaption></figure>

Tests may transition between flaky, broken, and healthy states multiple times over their lifetime. You can see previous changes in the detected health status of a test under Status History, as well as an explanation for why it was detected to have a new state.
