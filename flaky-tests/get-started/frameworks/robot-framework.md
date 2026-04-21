---
description: A guide for generating Trunk-compatible test reports for Robot Framework
---

# Robot Framework

You can automatically [detect and manage flaky tests](../../detection/) in your projects running tests with Robot by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To output compatible reports, add the `--xunit` argument to your `robot` command:

```shell
robot --xunit=junit.xml TestSuite.robot
```

#### Report File Path

The JUnit report will be written to the location specified by the `--xunit` argument. In the example above, it would be at `./junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

Omit the [`--rerunfailed`](https://docs.robotframework.org/docs/flaky_tests#re-execute-failed-tests-and-merge-results) flag and remove any [RetryFailed Listeners](https://docs.robotframework.org/docs/flaky_tests#retryfailed-listener) previously configured to run as part of your CI pipeline to disable retries.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
