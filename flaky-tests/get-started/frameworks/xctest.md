---
title: Configuring xctest
description: A guide for generating Trunk-compatible test reports for XCode and xcodebuild
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

# XCTest

You can automatically [detect and manage flaky tests](../../detection.md) in your XCTest projects by integrating with Trunk. This document explains how to configure XCTest to output XCResult reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Running XCTests from `xcodebuild` produces a `.xcresult` in an obscure directory by default. You can specify a `-resultBundlePath` option to generate the results locally:

```sh
xcodebuild test -scheme <YOUR_SCHEME> \
  -resultBundlePath ./test-results.xcresult
```

You can upload `.xcresult` directories directly to Trunk Flaky Tests.&#x20;

#### Report File Path

The test reports will be written to the `./test-results.xcresult` directory when running tests with the `-resultBundlePath ./test-results.xcresult`option. You will need this path when uploading results to Trunk in CI.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you run tests in CI with [the `-retry-tests-on-failure` option](https://keith.github.io/xcode-man-pages/xcodebuild.1.html#retry-tests-on-failure), disable it for more accurate results.

### Try It Locally

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --xcresults-path "./test-results.xcresult" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Step

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

