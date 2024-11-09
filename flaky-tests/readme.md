---
description: Detect, quarantine, and eliminates flaky tests from your codebase
---

# Flaky Tests (beta)

{% hint style="info" %}
Flaky Tests is currently available by invite only. Please [sign up for the waitlist](https://trunk.io/flaky-tests) for access.
{% endhint %}

## Monitoring Flaky Tests

Flaky tests are monitored by regularly running your test suites on branches that should not have test failures and tracking those failures. This is typically `main` or `master`, but there can also be other branches that are expected not to fail, like `production`, `release`, etc., depending on your workflow.

To start monitoring flaky tests, set up an automated CI job that runs your tests and uploads the resulting JUnit XML test report. See [Framework Configuration](get-started/frameworks/) to learn how to enable XML output for your particular testing framework.

### Quickstart

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>GitHub Actions</strong></td><td></td><td><a href="get-started/ci-providers/github-actions.md">github-actions.md</a></td><td><a href="../.gitbook/assets/GitHub (1).png">GitHub (1).png</a></td></tr><tr><td><strong>BuildKite</strong></td><td></td><td><a href="get-started/ci-providers/buildkite.md">buildkite.md</a></td><td><a href="../.gitbook/assets/BuildKite (1).png">BuildKite (1).png</a></td></tr><tr><td><strong>CircleCI</strong></td><td></td><td><a href="get-started/ci-providers/circleci.md">circleci.md</a></td><td><a href="../.gitbook/assets/CircleCI.png">CircleCI.png</a></td></tr><tr><td><strong>Jenkins</strong></td><td></td><td><a href="get-started/ci-providers/otherci.md">otherci.md</a></td><td><a href="../.gitbook/assets/jenkins-padded.png">jenkins-padded.png</a></td></tr><tr><td><strong>Semaphore</strong></td><td></td><td><a href="get-started/ci-providers/semaphoreci.md">semaphoreci.md</a></td><td><a href="../.gitbook/assets/semaphore-logo.png">semaphore-logo.png</a></td></tr><tr><td>GitLab</td><td></td><td><a href="get-started/ci-providers/gitlab.md">gitlab.md</a></td><td><a href="../.gitbook/assets/gitlab (1).png">gitlab (1).png</a></td></tr></tbody></table>

## Detecting Flaky Tests on Pull Requests

By uploading JUnit XML test results on pull requests, you get:

1. Metrics about how flaky tests affect your team's velocity
2. Metrics about how flaky tests reduce trust in your test suite
3. Reports on each Pull Request about which failed tests are known to be flaky
