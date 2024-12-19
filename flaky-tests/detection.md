# Detection

Trunk Flaky Tests detect flaky tests by analyzing test runs uploaded from your CI jobs. The health of your repository’s test suite is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

{% hint style="info" %}
It’s recommended to upload test results from CI jobs consistently to Trunk Flaky Tests for 14 days before expecting accurate detection results.
{% endhint %}

### How Tests Are Labeled

Trunk Flaky Tests processes test runs uploaded on a schedule, which means new uploads may not be immediately available on Trunk Flaky Tests. Expect test results for individual PRs to be up to date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes and all other metrics to be up to date within an hour of a new upload.

{% include "../.gitbook/includes/slack-callout.md" %}

### Test State Transitions

A test’s health status transitions between broken, flaky, and healthy as new test runs with new results are uploaded to Trunk Flaky Tests. Trunk Flaky Tests determine if a test is flaky based on analyzing the results of recent runs. The process is deterministic and based on appropriate thresholds.

This means if a test is healthy, it can transition into a broken or flaky status after new results appear that show failures. This also means if a test that was previously labeled as broken or flaky sees consistently passing runs, it can transition into a healthy test.&#x20;

Flaky Tests considers failures on PRs to be a weaker signal for flaky tests than inconsistent runs on the main branch. When a test fails on the main branch, it will immediately transition from a healthy to a non-healthy status.

### Key Repo Metrics

<figure><picture><source srcset="../.gitbook/assets/key-metrics-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/key-metrics-light.png" alt=""></picture><figcaption><p>Key repo metrics</p></figcaption></figure>

Trunk Flaky Test provides key repo metrics based on the detected health status of your tests. At the top of the Flaky Test dashboard, you’ll find metrics for the following information.

| Metric                      | Description                                                                                                                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flaky tests                 | Number of flaky test cases in your repo.                                                                                                                                                                                           |
| Broken tests                | Number of broken test cases in your repo.                                                                                                                                                                                          |
| PRs blocked by failed tests | PRs that have been blocked by failed tests in CI.                                                                                                                                                                                  |
| PRs rescued by quarantining | This figure is available if you have [quarantining](quarantining.md) set to preview or enabled. This shows the PRs with CI jobs containing quarantined flaky tests that would have failed if all flaky tests were not quarantined. |
| Engineering hours saved     | Estimated engineering hours saved based on the study [The Cost of Interrupted Work](https://ics.uci.edu/~gmark/chi08-mark.pdf), where each context switch to debug a flaky test costs 23 minutes of focused productivity.          |

These numbers are important for understanding the overall health of your repo’s tests, how much flaky and broken tests impact your developer productivity, and the developer hours saved from quarantining tests. You can also view the trends in these numbers in the trend charts.

### Tests Cases Overview

<figure><picture><source srcset="../.gitbook/assets/dashboard-test-list-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/dashboard-test-list-light.png" alt=""></picture><figcaption></figcaption></figure>

You can view a table of all your test cases and their current status in Trunk Flaky Tests. There are three different tables for tests labeled Flaky, Broken, and Healthy. \


<table data-header-hidden><thead><tr><th width="218"></th><th></th></tr></thead><tbody><tr><td>Status</td><td>Description</td></tr><tr><td>Flaky</td><td>The test is labeled as flaky, which means it’s show to fail inconsistently and spuriously in recent runs.</td></tr><tr><td>Broken</td><td>The test is labeled as broken, which means the test is consistently failing in recent runs.</td></tr><tr><td>Healthy</td><td>The test is labeled as healthy, which means the test is consistently passing in recent runs. </td></tr></tbody></table>

The table is sorted by default by the number of PRs impacted by the case, which is the best way to measure the impact of a flaky test. You can _click on each test_ case to view the [test case’s details](detection.md#test-case-details).

<table><thead><tr><th width="188">Column</th><th>Description</th></tr></thead><tbody><tr><td>Status</td><td>The health status of the test case.</td></tr><tr><td>Tests</td><td>The file path and name of the test case.</td></tr><tr><td>PRs Impacted</td><td>The number of PRs that have been affected by this test case failing in CI.</td></tr><tr><td>Since</td><td>How long this test has been labeled with its current status.</td></tr><tr><td>Ticket</td><td>If a ticket has been created in your issue tracker integration, it will show the status of the ticket.</td></tr></tbody></table>

### Test Case Details

You can click on any of the test cases listed on the Flaky Test dashboard to access the test case’s details. In the details, you can find summary metrics at the top of the page, which covers the following information.

<table data-header-hidden><thead><tr><th width="297"></th><th></th></tr></thead><tbody><tr><td><strong>Metric</strong></td><td><strong>Description</strong></td></tr><tr><td>PRs impacted by test</td><td>Describes the number of PRs affected by failures from this test case, the percent of PRs impact, and % change period over period.</td></tr><tr><td>PRs rescued by quarantining</td><td>If quarantining is enabled, describes the number of PRs with CI jobs containing quarantined flaky tests that would have failed, but were rescued by quarantining flaky failures. Also covers estimated engineer hours saved by quarantining flaky tests and unblocking PRs, as well as % change period over period.</td></tr><tr><td>Failure rate</td><td>Describes the failure rate of this test case and the % change period over period.</td></tr><tr><td>Earliest failure in last 7 days</td><td>Earliest failure in the selected data time range.</td></tr><tr><td>Most recent failure in last 7 days</td><td>Latest failure in the selected data time range.</td></tr><tr><td>Ticket Status</td><td>If a ticket was created using the Ticket Creation feature, this reflects the ID and status of the created ticket. You can click the ID to be redirected to your ticket.</td></tr></tbody></table>

### **Unique Failure Reasons**

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption></figcaption></figure>

Unique failures show a history of all past runs for this test case over the selected time period with a list of unique failure types. You can click a failure type to see them highlighted in the timeline.

The test types are a summary of the stack trace of the test run. You can click on the failure type to see a list of test runs labeled by branch, PR, Author, CI Job link, commit hash, duration, and time. You can click on a test run to see the detailed stack trace and similar failures on this test case and other test cases.

### **PRs Impacted**

<figure><picture><source srcset="../.gitbook/assets/prs-impacted-dark (1).png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/prs-impacted-light (1).png" alt=""></picture><figcaption></figcaption></figure>

You can see a list of PRs impacted by failures for this test case. Each entry has links to the PR, and the CI jobs impacted.&#x20;

### **Status History**

<figure><picture><source srcset="../.gitbook/assets/status-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/status-history-light.png" alt=""></picture><figcaption></figcaption></figure>

Tests may transition between flaky, broken, and healthy states multiple times over its lifetime. You can see previous changes in the detected health status of the test under Status History, as well as an explanation for why it was detected to have a new state.
