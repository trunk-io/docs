---
title: Configuring gotestsum
description: A guide for generating Trunk-compatible test reports for Go tests
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

# Go

You can automatically [detect and manage flaky tests](../../detection.md) in your Go projects by integrating with Trunk. This document explains how to configure Go to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

To generate compatible test reports, we will use `gotestsum`. Download `gotestsum` from [releases](https://github.com/gotestyourself/gotestsum/releases), or build from source with `go install gotest.tools/gotestsum@latest`.&#x20;

You can now run your tests using the `gotestsum`, which runs the test with `go test` under-the-hood before formatting the test results into a test report.&#x20;

```bash
gotestsum --junitfile ./junit.xml
```

#### Report File Path

`gotestsum` will write a JUnit test report to the file specified by the `--junitfile` argument. In the example above, the JUnit report would be written to `junit.xml`. You'll need this path later when configuring automatic uploads to Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.\
\
If you're using a package like [**retry**](https://pkg.go.dev/github.com/hashicorp/consul/sdk/testutil/retry), disable it to get more accurate results from Trunk.

### Try It Locally

#### **The Validate Command**

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

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

