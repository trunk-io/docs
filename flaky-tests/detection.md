# Detection

Trunk Flaky Tests detect flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

{% hint style="info" %}
It’s recommended to upload test results from CI jobs consistently to Trunk Flaky Tests for 14 days before expecting accurate detection results.
{% endhint %}

### How Tests Are Labeled

Trunk Flaky Tests processes test runs uploaded on a schedule, which means new uploads may not be immediately available on Trunk Flaky Tests. Expect test results for individual PRs to be up to date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes and all other metrics to be up to date within an hour of a new upload.

{% include "../.gitbook/includes/slack-callout.md" %}

<table><thead><tr><th width="218">Test Status</th><th>Description</th></tr></thead><tbody><tr><td>Flaky</td><td>This test is not deterministic. Given the same inputs, the test will occasionally produce different outputs. This means you <strong>cannot trust the results</strong> of these tests.</td></tr><tr><td>Broken</td><td>This test is reproducible but is always failing. These tests that always fail are not useful and should be fixed.</td></tr><tr><td>Healthy</td><td>This test is reproducible. Given the same inputs, the test will produce the same outputs.</td></tr></tbody></table>

#### Branches

Trunk analyzes test failures based on the context in which they are run. A test failing on main has a different impact on flake detection that a test failing on a pull request.

{% hint style="warning" %}
Uploading all test results from from your repository will result in the fastest and most accurate detection. Trunk relies on test results from main, pull requests, and (if you use one) mergequeues.
{% endhint %}

#### Protected/Default/Stable Branches

In a [trunk-based development](https://trunkbaseddevelopment.com/) flow, do work on feature branches and merge their changes back into `main`. Typically, new code must pass automated tests before being merged. Tests that fail on `main` are unexpected and are a sign of flakiness.

#### Mergequeue

Mergequeues use temporary branches to test changes again before merging into `main`. Failures on mergequeue branches are unexpected and are used as a signal when detecting flaky tests.

#### Pull Request

Tests that are run on pull requests are expected to fail, so failure on pull requests is not used in detection of flaky tests.

Flaky tests will produce inconsistent results even when run on the same code with the same input. Pull requests is where we see this behavior the most often: an engineer opens a pull request, sees a test fail, re-runs the code, and sees the test pass. We track this behavior (different results for a test on the same git commit) as sign that a test is flaky.

### Test State Transitions

A test’s health status transitions between broken, flaky, and healthy as new test runs with new results are uploaded to Trunk Flaky Tests. Trunk Flaky Tests determine if a test is flaky based on analyzing the results of recent runs. The process is deterministic and based on appropriate thresholds.

This means if a test is healthy, it can transition into a broken or flaky status after new results appear that show failures. This also means if a test that was previously labeled as broken or flaky sees consistently passing runs, it can transition into a healthy test.&#x20;

Flaky Tests considers failures on PRs to be a weaker signal for flaky tests than inconsistent runs on the main branch. When a test fails on the main branch, it will immediately transition from a healthy to a non-healthy status.

### **Status History**

<figure><picture><source srcset="../.gitbook/assets/status-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/status-history-light.png" alt=""></picture><figcaption></figcaption></figure>

Tests may transition between flaky, broken, and healthy states multiple times over their lifetime. You can see previous changes in the detected health status of a test under Status History, as well as an explanation for why it was detected to have a new state.
