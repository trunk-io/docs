---
description: A guide for generating Trunk-compatible test reports for Robot Framework
---

# Robot Framework

You can automatically [detect and manage flaky tests](../../detection.md) in your projects running tests with Robot by integrating with Trunk. This document explains how to configure Robot to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To output compatible repports, add the `--xunit` argument to your `robot` command:

```shell
robot --xunit=junit.xml TestSuite.robot
```

#### Report File Path

The JUnit report will be written to the location specified by the `--xunit` argument. In the example above, it would be at `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable them and prefer using the [Quarantine](../../quarantining.md) feature to mitigate the negative impact of Flaky Tests.

Omit the [`--rerunfailed`](https://docs.robotframework.org/docs/flaky_tests#re-execute-failed-tests-and-merge-results) flag and remove any [RetryFailed Listeners](https://docs.robotframework.org/docs/flaky_tests#retryfailed-listener) previously configured to run as part of your CI pipeline to disable retries.&#x20;

### Try It Locally

#### The Validate Command

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

