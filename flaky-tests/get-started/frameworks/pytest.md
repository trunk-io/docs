---
title: Configuring pytest
description: A guide for generating Trunk-compatible test reports for Pytest
---

# Pytest

You can automatically [detect and manage flaky tests](../../detection/) in your Pytest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating JUnit XML reports from your test runs.

In your CI job, update your `pytest` command to include the `--junit-xml` and `junit_family=xunit1` arguments to generate XML reports:

```shell
pytest --junit-xml=junit.xml -o junit_family=xunit1
```

The `junit_family=xunit1` is necessary so that the generated XML report includes file paths for each test case. File paths for test cases are used for features that use code owners like the [Jira integration](../../ticketing-integrations/jira-integration.md) and [webhooks](../../webhooks/).

#### Report File Path

The `--junit-xml` argument specifies the path of the JUnit report. You'll need this path later when configuring automatic uploads to Trunk.

{% include "../../../.gitbook/includes/retries.md" %}

Omit the [`--lf` or `--ff` options](https://docs.pytest.org/en/stable/how-to/cache.html) if you've previously configured your CI with these options to disable retries.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
