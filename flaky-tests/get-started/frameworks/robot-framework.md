---
description: A guide for generating Trunk-compatible test reports for Robot Framework
---

# Robot Framework

## 1. Generate JUnit

Add the `--xunit` argument to your `robot` command:

```shell
robot --xunit=junit.xml TestSuite.robot
```

## 2. Output Location

The JUnit report will be written to the location specified by the `--xunit` argument. In the example above, it would be at `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the [`--rerunfailed`](https://docs.robotframework.org/docs/flaky_tests#re-execute-failed-tests-and-merge-results) flag and remove any [RetryFailed Listeners](https://docs.robotframework.org/docs/flaky_tests#retryfailed-listener) previously configured to run as part of your CI pipeline to disable retries.&#x20;

## Next Step

JUnit files generated with Robot Framework are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
