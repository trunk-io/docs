---
description: >-
  Learn to find flaky tests and understand their impact using the Flaky Tests
  dashboard
---

# Dashboard

Trunk Flaky Tests detects flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard.

### Repositories overview

When you navigate to `/<your-org>/flaky-tests`, you land on a repositories overview showing all monitored repositories at a glance.

Each repository row displays:

| Column | Description |
|--------|-------------|
| **Tests** | Total tracked test cases in the repository (60-day window) |
| **Flaky** | Number of currently flaky test cases, with a 10-day trend sparkline |
| **Broken** | Number of currently broken test cases, with a 10-day trend sparkline |
| **Runs / Day** | Bar chart of test run volume over the last 10 days, with per-day tooltips |

A quarantine status icon appears next to each repository name when quarantining is configured:

| Icon | Meaning |
|------|---------|
| Shield | Quarantining is enabled for this repository — auto-quarantine is off |
| Shield with checkmark | Auto-quarantine is enabled — flaky tests are quarantined automatically |

Active repositories (with test data in the last 30 days) appear at the top of the list. Repositories with no recent data are collapsed under an **Inactive Repositories** section that you can expand to view.

Selecting a repository opens its detailed dashboard. If your organization has no repositories connected yet, the page redirects to onboarding. See [Quarantining](quarantining.md) to learn how to configure quarantine settings.

### Key repository metrics

<figure><picture><source srcset="../.gitbook/assets/key-metrics-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/key-metrics-light.png" alt=""></picture><figcaption><p>Key repo metrics</p></figcaption></figure>

Trunk Flaky Tests provides key repo metrics based on the detected health status of your tests. You'll find metrics for the following information at the top of the Flaky Tests dashboard.

<table><thead><tr><th width="209">Metric</th><th>Description</th></tr></thead><tbody><tr><td>Flaky tests</td><td>Number of flaky test cases in your repo.</td></tr><tr><td>PRs blocked by failed tests</td><td>PRs that have been blocked by failed tests in CI.</td></tr></tbody></table>

These numbers are important for understanding the overall health of your repo’s tests, how flaky tests impact your developer productivity, and the developer hours saved from quarantining tests. You can also view the trends in these numbers in the trend charts.

The trend charts display the New Test Cases added by day, as well as Test Transitions and Quarantined Runs. Test Transitions represent the number of tests that have transitioned to a particular status on a particular day, excluding new test cases (which default to a status of Healthy). If a bar shows 5 Healthy, 10 Flaky, and 2 Broken on a single day, that indicates 5 tests transitioned to Healthy, 10 to Flaky, and 2 to Broken on that day. Quarantined Runs represents the number of runs of quarantined tests by day.

### Tests cases overview

<figure><picture><source srcset="../.gitbook/assets/flaky-tests-overview-table-v2-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/flaky-tests-overview-table-v2-light.png" alt=""></picture><figcaption></figcaption></figure>

You can view a table of all your test cases and their current status in Trunk Flaky Tests.

Filters can also be set on the table to narrow test results down by test status, quarantine setting, ticket status, or by the name, file, or suite name of the test case.

The table is sorted by default by the number of PRs impacted by the case, which is the best way to measure the impact of a flaky test. You can click on each test case to view [the test case’s details](dashboard.md#test-case-details).

<table><thead><tr><th width="188">Column</th><th>Description</th></tr></thead><tbody><tr><td>Tests</td><td>The variant, file path, and name of the test case.</td></tr><tr><td>Status</td><td>The health status of the test case: <strong>Healthy</strong>, <strong>Flaky</strong>, or <strong>Broken</strong>. Broken indicates consistent high-rate failures; Flaky indicates intermittent failures.</td></tr><tr><td>Failure Rate</td><td>The percentage of CI runs failed due to this test case.</td></tr><tr><td>PRs Impacted</td><td>The number of PRs that have been affected by this test case failing in CI.</td></tr><tr><td>Last Run</td><td>The most recent timestamp for an upload test run.</td></tr></tbody></table>

{% hint style="info" %}
Test Deletion & History

* Inactive tests disappear from the dashboard automatically after 30 days and are fully removed after 45 days. Tests cannot be manually deleted.
* Changing test identifiers (e.g., adding file paths) creates new test entries — merging with old history isn’t supported.
{% endhint %}

### Test case details

You can _click_ on any of the test cases listed on the Flaky Tests dashboard to access the test case’s details. The test details page uses a tabbed layout:

* **Summary**: Run result charts and failure types grouped by unique failure reason.
* **Test History**: A searchable, paginated table of every individual test run with filtering and a detail panel.
* **Monitors**: Detection monitors configured for this test (visible when the detection engine is enabled).
* **Events**: A timeline of detection events, quarantine actions, ticketing events, and status transitions (Healthy, Flaky, Broken) for this test (visible when the detection engine is enabled). Use the category filter to scope to **Flake Detection** events to see which monitor triggered each transition.

In addition to the tabbed content, the test details page shows the test’s current status (Healthy, Flaky, or Broken), ticket status, and codeowner information.

### **Code owners**

If you have a codeowners file configured in your repos, you will see who owns each flaky test in the test details view. We support code owners for [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) and [GitLab](https://docs.gitlab.com/ee/user/project/codeowners/) repos.

<figure><picture><source srcset="../.gitbook/assets/details-code-owners-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/details-code-owners-light.png" alt=""></picture><figcaption><p>You can find the code owners of each test on the top right of the test details screen.</p></figcaption></figure>

This information will also be provided when creating a ticket with the [Jira integration](ticketing-integrations/jira-integration.md) or [webhooks](webhooks/).

### Summary tab

<figure><picture><source srcset="../.gitbook/assets/flaky-tests-failure-details-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/flaky-tests-failure-details-light.png" alt=""></picture><figcaption></figcaption></figure>

The Summary tab shows an overview of the test’s recent run results and groups past failures by unique failure type.

#### Failure types

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption></figcaption></figure>

The Failure Types table shows the history of past test runs grouped by unique failure types.

The Failure Type is a summary of the stack trace of the test run. You can click on the failure type to see a list of test runs labeled by branch, PR, Author, CI Job link, duration, and time.

#### Failure details

You can click on any of these test runs to see the detailed stack trace:

<figure><picture><source srcset="../.gitbook/assets/run-details-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/run-details-light.png" alt=""></picture><figcaption></figcaption></figure>

You can flip through the stack traces of similar failures across different test runs by clicking the left and right arrow buttons. You can also see other similar failures on this and other tests.

##### Go to the CI job logs

If you want to see full logging of the original CI job for an individual test failure, you can click **Logs** in the expanded failure details panel to go to the job’s page in your CI provider.

<figure><picture><source srcset="../.gitbook/assets/failure-logs-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/failure-logs-light.png" alt=""></picture><figcaption></figcaption></figure>

### Test History tab

The Test History tab gives you full visibility into every individual run of a test. Use it to investigate patterns across branches, find specific failing runs, and drill into error details.

#### Daily runs chart

A stacked bar chart at the top of the tab shows daily test run counts. The legend identifies four categories:

* **Green**: Pass
* **Red**: Fail
* **Blue**: Quarantined
* **Gray**: Skipped

Click and drag on the chart to select a date range, which scopes the table below to runs from the selected days. The selected range appears next to the legend with an X button to clear just the range. The **Reset** button on the filter bar clears all filters at once, including the date range.

#### Filters

A filter bar below the chart provides four independent controls:

<table><thead><tr><th width="160">Filter</th><th>Description</th></tr></thead><tbody><tr><td>Result</td><td>Segmented control with <strong>All</strong>, <strong>Pass</strong>, and <strong>Fail</strong> to scope the table to a specific outcome.</td></tr><tr><td>Quarantined</td><td>Segmented control with <strong>Include</strong> (default), <strong>Exclude</strong>, and <strong>Only</strong> to control whether quarantined runs are mixed in, hidden, or shown exclusively.</td></tr><tr><td>SHA</td><td>Filter by commit hash. Matches runs whose SHA starts with the entered text.</td></tr><tr><td>Branch</td><td>Filter by branch name. Accepts exact names or glob patterns. Use <code>*</code> to match any sequence of characters and <code>?</code> to match a single character.</td></tr></tbody></table>

Branch filter examples:

| Pattern | Matches |
|---|---|
| `main` | The branch named `main` exactly |
| `release/*` | All release branches, e.g. `release/1.0`, `release/2.3` |
| `feature-??` | Feature branches with a two-character suffix, e.g. `feature-v2` |
| `trunk-merge/*` | All merge queue branches |

All filters combine using AND logic, so you can use them together. For example, set **Result** to **Fail** and **Quarantined** to **Only** to surface only quarantined failures. The **Reset** button clears every filter at once, including the chart date range.

Filter state is saved in the URL, so you can share or bookmark a filtered view. The Result filter accepts `result=pass` or `result=fail`. The Quarantined filter accepts `quarantined=include`, `quarantined=exclude`, or `quarantined=only`.

#### Runs table

The runs table displays a paginated list of individual test runs (25 per page) with the following columns:

<table><thead><tr><th width="160">Column</th><th>Description</th></tr></thead><tbody><tr><td>Timestamp</td><td>When the test ran, displayed in your local time zone.</td></tr><tr><td>Duration</td><td>How long the test took to execute.</td></tr><tr><td>PR</td><td>The pull request number associated with the run, e.g. <code>#1234</code>. Empty for runs that aren't tied to a PR.</td></tr><tr><td>Branch</td><td>The branch the test ran against, e.g. <code>main</code>, <code>feature/x</code>, or <code>trunk-merge/pr-1234/...</code> for merge queue branches.</td></tr><tr><td>Commit</td><td>The first 7 characters of the commit SHA.</td></tr></tbody></table>

Each row has a colored left border indicating the run's outcome. Quarantined runs always show blue, regardless of whether the run passed or failed. For non-quarantined runs, the border is green for pass, red for fail, orange for error, and a neutral gray for any other state.

#### Run detail panel

Click any row in the runs table to open a detail panel on the right side of the page. The panel shows:

* **Run header**: Timestamp, a result badge (Pass, Fail, Error, or Quarantined), and run duration.
* **Source control**: A CI job link (with the provider's icon, the job name, and the CI duration), the linked pull request, branch, and commit. Merge queue runs also include a **View in Merge Queue** link.
* **Error details**: For failed, errored, or quarantined runs, an optional AI summary of the failure followed by the raw error text or stack trace.
