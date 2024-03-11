# Flaky Tests

{% hint style="warning" %}
Flaky Tests is available by invite only. Please [**contact**](https://trunk.io/about) us if you would like to try the product early.
{% endhint %}

## Monitoring Flaky Tests

Flaky tests are monitored by regularly running your test suites on branches that should not have test failures and tracking those failures. This is typically `main` or `master`, but can also be other branches that are expected not to fail like `production`, `release`, etc., depending on your workflow.

To start monitoring flaky tests, set up an automated CI job that runs your tests and uploads the resulting JUnit XML test report.

## Detecting Flaky Tests on Pull Requests

By uploading JUnit XML test results on pull requests, you get:

1. Metrics about how flaky tests affect your team's velocity
2. Metrics about how flaky tests reduce trust in your test suite
3. Reports on each Pull Request about which failed tests are known to be flaky
