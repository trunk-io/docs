---
title: Configuring rspec
description: A guide for generating Trunk-compatible test reports for RSpec
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

# RSpec

You can automatically [detect and manage flaky tests](../../detection.md) in your projects running RSpec by integrating with Trunk. This document explains how to configure RSpec to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this for your Rspec tests by generating JUnit XML reports from your test runs.

To generate Trunk-compatible reports, install the `rspec_junit_formatter`:

```shell
gem install rspec_junit_formatter
```

You can use `rspec_junit_formatter` like this:

```shell
rspec --format RspecJunitFormatter --out junit.xml
```

#### Report File Path

The JUnit report will be written to the location specified by the `--out` argument. In the example above, the report would be at `./junit.xml`. You will need this when you update your CI config to integrate with Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

If you have a step in CI to rerun failed tests with the `--only-failures` option, or you're using a package like [rspec-retry](https://github.com/NoRedInk/rspec-retry), remember to disable them.

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

