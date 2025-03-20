---
title: Configuring minitest
description: A guide for generating Trunk-compatible test reports for minitest
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

# minitest

You can automatically [detect and manage flaky tests](../../detection.md) in your minitest projects by integrating with Trunk. This document explains how to configure minitest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To generate XML reports, install the `minitest-reporters` gem:

```shell
gem install minitest-reporters
```

Configure the `JUnitReporter` reporter in your `test_helper.rb` file:

{% code title="test_helper.rb" %}
```ruby
require "minitest/reporters"
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter.new
```
{% endcode %}

#### Report File Path

You can specify a file path for your minitest results with the `MINITEST_REPORTERS_REPORTS_DIR` environment variable:

```sh
MINITEST_REPORTERS_REPORTS_DIR="./junit.xml" ruby -Ilib:test <FILES>
```

This will automatically write all test results to JUnit XML files in the `results` directory.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Minitest doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

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

