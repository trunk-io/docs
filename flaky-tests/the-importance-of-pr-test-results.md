# The Importance of PR Test Results

Uploading test results from pull requests (PRs) is a critical step for enabling Trunk Flaky Tests. This data provides a primary signal for _detecting_ flaky tests and is the key metric for _measuring_ their impact. Without it, you lose the most significant source of information for identifying and prioritizing these disruptive tests.

Here's a breakdown of the key features that depend on PR test results:

#### Crucial Flakiness Detection

The most common and critical signal for identifying a flaky test happens on PRs. Flakiness is detected when a test produces different results on the same git commit.

This typically happens when:

1. A developer opens a PR, and a test fails.
2. The developer reruns the exact same tests without changing any code.
3. The test now passes.

This "fail then pass" sequence on the same commit is a clear indication of non-deterministic, or "flaky," behavior. Since the majority of test runs occur during the development and review cycle, PRs are the largest source of this vital signal.

#### Measuring Test Impact

The Flaky Tests dashboard is designed to help you prioritize which tests to fix first. The single most important metric for this is `PRs Impacted`. By default, the overview table is sorted by this metric because it's the best way to measure a flaky test's true impact on developer productivity.

If you don't upload test results from PRs:

* The `PRs Impacted` count for every test will be zero.
* You will have no way to determine which flaky or broken tests are causing the most disruption.
* You lose the ability to prioritize fixes based on real-world data, potentially wasting time on less important issues.

#### Unblocking Developers with Quarantining

Quarantining is one of the most powerful features of Trunk Flaky Tests. Its core purpose is to prevent known flaky tests from blocking developers and breaking CI pipelines, especially merge queues.

The entire quarantining workflow is predicated on analyzing test results from PRs. Without PR data, you cannot:

* **Identify tests as flaky from PR test runs:** The system needs to see a test pass and fail on the same commit (a signal primarily gathered from PRs) to classify it as flaky.
* **Apply Quarantine Logic at Runtime:** Uploading a test result and checking if it should be quarantined are part of the same, single step in your CI job. When a test fails on a PR, the `Trunk Analytics CLI` uploads the failure and, in the same operation, checks with the Trunk service to see if that test is on the quarantine list. If it is, the CLI overrides the job's exit code, allowing the build to pass. Without running the `Trunk Analytics CLI` on your PR jobs, this real-time check cannot occur, and even known flaky tests will continue to block your PRs.

#### Immediate CI Feedback and Error Summaries

The `Trunk Analytics CLI` provides a detailed summary directly in the CI job's output log. This is the fastest, most immediate feedback a developer gets about their test run.

Without uploading PR results, you lose:

* A Clear Test Report Summary: A quick overview of `Total`, `Pass`, `Fail`, and `Quarantined` tests.
* In-Log Failure Details: A snippet of the stack trace and assertion error for any failed test, providing immediate context without digging through full CI logs.
* Actionable Exit Codes: The CLI intelligently determines the job's outcome.
  * When a real test fails, it exits with a non-zero code: `⚠️ Some test failures were not quarantined, using exit code: 1`
  * When _only_ a known flaky test fails, it passes the job: `🎉 All test failures were quarantined, overriding exit code to be exit_success (0)`

This immediate, in-CI feedback loop is invaluable for developers trying to quickly understand why their build failed.

#### Enabling Developer Productivity Features

Trunk Flaky Tests offers features directly within the developer workflow that depend entirely on PR data, most significantly the automated pull request comment.

These comments provide a summary of all tests run on a specific PR, highlighting failures and indicating whether they are due to a known flaky test. This feature prevents developers from wasting time investigating a failure that is already identified as flaky. Without uploading PR test results, this valuable, time-saving context is completely lost.

#### Next Steps: Enable PR Uploads

Now that you understand why uploading test results from pull requests is essential, the next step is to configure your CI pipeline. This single step is the key to unlocking accurate flakiness detection, true impact measurement, and powerful features like quarantining.

Our documentation provides step-by-step guides for all major CI providers to make this setup simple.

[➡️ Find your CI provider and start uploading test results](get-started/ci-providers/)
