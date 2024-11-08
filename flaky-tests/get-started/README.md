# Get Started

### Introduction

Trunk Flaky Tests works by changing all of your CI jobs that run tests to upload their test results to Trunk. This setup looks slightly different depending on which CI system and test framework(s) you use, but we have guides for all the popular systems.

### 1. Sign up for [app.trunk.io](https://app.trunk.io)

You must create an account and Trunk organization to complete the steps below.&#x20;

### 2. Configure your test framework to output test results

For Trunk to start detecting flaky tests, it needs to ingest the results from all of your CI test runs. To get started, configure your test framework (jest, pytest, gtest, etc) to output results. You'll do this only for CI jobs, _not_ for running tests locally.

Check out our guides to many of the most popular test frameworks: [frameworks](frameworks/ "mention")

### 3. Configure your CI jobs to upload test results to Trunk

After you've set your test framework to output test results, you're ready to actually change your CI testing jobs to upload those results to Trunk.

Check out our guides to the most popular CI systems: [ci-providers](ci-providers/ "mention")

Once you've merged changes to your CI test jobs, make sure you've run at least 1 testing job and your newly added upload step has completed.

### 4. Confirm your configuration, analyze your dashboard

In [app.trunk.i](https://app.trunk.io)[o](https://app.trunk.io/), select the repo you're working in, and navigate to `Flaky Tests` -> `Uploads`. Confirm that you see the upload(s) from the previous step.

Trunk needs to ingest a large amount of test data from a variety of pull request branches and protected branches (like `main` or `master`) before it can start accurately detecting flaky tests. This may happen quickly if you have a very high-velocity repo and run test jobs hundreds of times a day.

Once you've confirmed data is flowing properly into Trunk, let data accumulate for several days and check back to analyze the results. We'll also email you when your first flaky test is detected.

### 5. Enable test summary comments on PRs

Flaky Tests can post comments on GitHub pull requests to provide a summary of all the tests run on this PR, across multiple CI jobs or even CI systems, as well as whether those failures are due to flakiness, the history of the failures of that test, and more.

To enable PR Comments, see our documentation: [github-pull-request-comments.md](../github-pull-request-comments.md "mention")

### 6. (Optional) Enable Quarantining

Quarantining is an advanced feature that allows your CI test jobs to pass even if a flaky test is failing on them. This eliminates the pain developers feel from dealing with flaky tests.

To enable Quarantining, see our documentation: [quarantining.md](../quarantining.md "mention")
