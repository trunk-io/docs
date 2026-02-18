---
description: Learn how Trunk detects and labels flaky tests
---

# Flaky test detection

Trunk detects flaky tests by analyzing test results uploaded from your CI jobs. This page covers how flaky tests are detected and how they're labeled after Trunk receives uploaded test results.

<figure><picture><source srcset="../.gitbook/assets/unique-failure-reason-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/unique-failure-reason-light.png" alt=""></picture><figcaption></figcaption></figure>

Trunk Flaky Tests detects flaky tests by analyzing test results. The health of your tests is displayed in the Flaky Tests dashboard. This page covers how flaky tests are detected and how to analyze your test suite’s health using the dashboard.

You can learn more about how tests are uploaded to Trunk before they're labeled in the [Get Started docs](get-started/). You can learn more about how detection results are displayed in the [Dashboard docs](dashboard.md).

{% hint style="info" %}
Trunk typically requires 10+ runs per test on CI to start accurately detecting flaky tests. For example, detecting a flaky test that fails 25% of the time takes 9 runs to achieve 90% confidence in having seen it flake. Depending on the repository’s velocity, this could take hours or days.
{% endhint %}

Trunk detects flaky tests by analyzing the test results uploaded from your CI jobs. Each new upload is processed and compared with historical test results to detect flaky tests. Trunk emphasizes each result differently depending on which branch it's run on.\
\
**This is an asynchronous process, and it may take up to an hour for an upload's results to be reflected in** [**the dashboard**](get-started/#id-4.-confirm-your-configuration-analyze-your-dashboard)**.**

<figure><picture><source srcset="../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption><p>The uploads tab contains results received from past CI jobs.</p></figcaption></figure>

### How Trunk detects flakiness

Trunk analyzes test failures based on the context in which they are run. A test failing on `main` has a different impact on flake detection than a test failing on a pull request. After tests are uploaded to Trunk, they're analyzed based on different rules depending on which branch they were run on.

{% hint style="warning" %}
Uploading all test results from your repository will result in the fastest and most accurate detection. Trunk relies on test results from `main`, pull requests, and (if you use one) merge queues.
{% endhint %}

### Stable branches

Trunk detects flaky tests with the assumption that automated tests should be passing before being merged into stable branches like `main`. This means failures on `main` are unexpected and indicate flakiness or a broken test.

{% hint style="info" %}
Stable branches are sometimes referred to as _protected_ or _default_ branches.
{% endhint %}

Flaky Tests will use `main` as a stable branch by default. You can override the default selection and set a custom stable branch, for example, `master` or `develop`.

#### Overriding stable branch defaults

It is important to set your stable branch correctly to ensure fast and accurate detection of flaky tests.

Flaky Test users with the administrator role can update the current stable branch in the repository settings:

1. Click on your profile and open **Settings.**
2. Click on your repository in the left nav.
3. Update the **Override Default Stable Branch** setting with the name of your stable branch.

{% hint style="warning" %}
Changing the stable branch will not rebuild your test history, a stable branch change will only be applied to new test runs.

Flaky Tests will require additional CI runs on the updated stable branch to detect test flakes.
{% endhint %}

#### Pull requests

Flaky tests are only detected on pull requests (PRs) when a test produces different results on the same git commit. This often occurs when a PR is opened, the tests initially fail, and then pass when re-run.

Tests failing on different git commits in PRs are not used as a signal of flakiness. This is because code changes in PRs can lead to expected test failures that will be fixed before the PR is merged.

#### Merge queue

Merge queues use temporary branches to test changes again before merging into `main`. Failures on merge queue branches are unexpected and are used as a signal when detecting flaky tests. Trunk currently auto-detects merge queue CI jobs from Trunk Merge Queues, GitHub Merge Queues, GitLab Merge Trains, and Graphite Merge Queues.

#### Examples

To help illustrate the implications of these rules, consider the following scenarios.

* Scenario 1: A test fails on a CI job run on the `main` branch, which is a protected branch. It will be marked as **flaky** because we expect PRs to pass automated tests before being merged, which means its results are inconsistent. If it continues to fail consistently on `main`, it will be marked as broken.
* Scenario 2: A test fails on a PR branch. A new commit is pushed, which fixes the test. Later, another commit breaks the test again, and it fails consistently for the next 3 commits and fails on reruns. It is **not marked flaky or broken** because it's displaying consistent behavior on the same commit, and it's failing on a development/PR branch, which is expected to fail and be fixed during development to catch regressions.
* Scenario 3: A test fails on a PR. A developer reruns the tests, and they pass. This test will be marked as **flaky** because it demonstrates inconsistent results on the same commit, which means it's flaky because the results changed without code changes.

{% hint style="info" %}
Expect test results for individual PRs to be up-to-date for [PR Test Summaries](github-pull-request-comments.md) within 15 minutes post-upload and all other metrics to be up-to-date within an hour.
{% endhint %}

### Use variants to track environment-specific flakes

If you run the same tests across different environments or architectures, you can use variants to separate these runs into distinct test cases. This allows Flaky Tests to detect environment-specific flakes.

For example, a test for a mobile app might be flaky on iOS but stable on Android. Using variants, Flaky Tests can isolate flakes on the iOS variant instead of marking the test as flaky across all environments.

You can specify a variant during upload using the [`--variant` option](uploader.md#full-command-reference):

{% code title="Upload an iOS variant " %}
```
./trunk flakytests upload --junit-paths "test_output.xml" \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN \
   --variant ios
```
{% endcode %}

Variant names are displayed in brackets next to test names in your dashboard:

<figure><picture><source srcset="../.gitbook/assets/variants-dark-border.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/variants-light-border.png" alt=""></picture><figcaption><p>The same test, but the first is a macOS variant.</p></figcaption></figure>

### Test status

Trunk classifies all tests into one of three categories based on the history of each test:

<table><thead><tr><th width="178">Test Status</th><th>Description</th></tr></thead><tbody><tr><td>Flaky</td><td>This test is not deterministic. Given the same inputs, the test will occasionally produce different outputs. This means you <strong>cannot trust the results</strong> of these tests.</td></tr><tr><td>Broken</td><td>This test is reproducible but is always failing. These tests that always fail are not useful and should be fixed.</td></tr><tr><td>Healthy</td><td>This test is reproducible. Given the same inputs, the test will produce the same outputs.</td></tr></tbody></table>

### Override test status

You can manually override the detected status of any test case. This is useful when a test is stuck in a status that no longer reflects its actual behavior — for example, a test marked as Flaky that has been consistently passing for a while.

To override a test's status:

1. Navigate to the **Tests** tab on the Flaky Tests dashboard.
2. Click the pencil icon dropdown next to the test you want to update.
3. Select the new status: **Healthy**, **Flaky**, or **Broken**.
4. Provide a reason describing why you are overriding the status.
5. Submit the override.

<figure><img src="../.gitbook/assets/manual-test-mark.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Be sure to include a meaningful description when overriding the test status. This reason is displayed alongside the override in the test's [status history](dashboard.md#test-history), helping your team understand why the status was changed.
{% endhint %}

#### How overrides interact with the detection engine

When you override a test's status, the detection engine resets its classification for that test and begins re-evaluating from the override point forward. This means:

1. **All test runs up to the override are processed.** The detection engine completes its analysis of any pending runs before applying the override.
2. **Classification resets at the override.** The engine clears any partial rule matches and starts fresh from the new status you set.
3. **Detection continues normally after the override.** New test runs uploaded after the override are analyzed using the standard detection rules, starting from the status you selected.

{% hint style="warning" %}
Overriding a test's status does **not** suppress future detection. If a test you mark as Healthy starts failing again, the detection engine will reclassify it as Flaky or Broken based on the new failures.
{% endhint %}

#### Example scenarios

<details>

<summary>Override to Healthy — test starts failing again</summary>

A test has been marked as Flaky by the detection engine but has been passing consistently. You override the status to **Healthy**.

After the override, if the test experiences a flaky failure on a subsequent CI run, the detection engine will reclassify it as **Flaky** — just as it would for any healthy test that starts failing. The override does not grant any special protection.

</details>

<details>

<summary>Override to Flaky — test starts passing consistently</summary>

A test has been incorrectly classified as Healthy, but you know it is unreliable. You override the status to **Flaky**.

After the override, if the test accumulates enough consistent passes to meet the detection engine's criteria for a healthy test, it will be reclassified as **Healthy** automatically. The override sets the starting point, but the detection engine is free to reclassify based on new evidence.

</details>

<details>

<summary>Override to Broken — detection continues from that point</summary>

You can also override a test's status to **Broken** if it is consistently failing but has not yet been reclassified by the detection engine. The engine will continue classification from the Broken status, and if the test starts passing again, it will transition back to Healthy or Flaky based on the detection rules.

</details>

#### Viewing overrides in status history

Both manual overrides and engine-generated status changes appear together in the test's [status history timeline](dashboard.md#test-history). Manual overrides display the reason you provided when submitting the override, while engine-generated transitions display the detection rule that triggered the change.

### Next steps

If you have not set up your CI jobs to upload results to Trunk, follow the [Get Started docs](get-started/) to start uploading test results to Trunk.

If you're curious about why certain tests are labeled as flaky, you can visit each test's status history. [Learn more about Status History.](dashboard.md#status-history)

<figure><picture><source srcset="../.gitbook/assets/test-history-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/test-history-light.png" alt=""></picture><figcaption></figcaption></figure>
