---
title: Configuring swift-testing
description: A guide for generating Trunk-compatible test reports with Swift Testing
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

# Swift Testing

You can automatically [detect and manage flaky tests](../../detection.md) in your Swift projects by integrating with Trunk. This document explains how to configure Swift Testing to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To output a compatible report, add the `--xunit-output` argument to your Swift test command:

```shell
swift test --xunit-output junit.xml --parallel
```

Due to a [known bug](https://github.com/swiftlang/swift-package-manager/issues/4752) with Swift, you must include the `--parallel` flag for the XML report to output properly.

#### Report File Path

The test report will be written to the location specified by the `--xunit-output` argument. In the example above, it would be at `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Swift Testing doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

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
