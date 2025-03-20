---
title: Configuring pytest
description: A guide for generating Trunk-compatible test reports for Pytest
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Pytest

You can automatically [detect and manage flaky tests](../../detection.md) in your Pytest projects by integrating with Trunk. This document explains how to configure Pytest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating JUnit XML reports from your test runs.

In your CI job, update your `pytest` command to include the `--junit-xml` and `junit_family=xunit1` arguments to generate XML reports:

```shell
pytest --junit-xml=junit.xml -o junit_family=xunit1
```

The `junit_family=xunit1` is necessary so that the generated XML report includes file paths for each test case. File paths for test cases are used for features that use code owners like the [Jira integration](../../jira-integration.md) and [webhooks](../../webhooks/).

#### Report File Path

The `--junit-xml` argument specifies the path of the JUnit report. You'll need this path later when configuring automatic uploads to Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

Omit the [ `--lf` or `--ff` options](https://docs.pytest.org/en/stable/how-to/cache.html) if you've previously configured your CI with these options to disable retries.

### Try It Locally

#### The Validate Command

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make a upload to Trunk using the following command:

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

