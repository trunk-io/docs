---
description: A guide for generating Trunk-compatible test reports for Pest
---

# Pest

You can automatically [detect and manage flaky tests](../../detection.md) in your PHP projects by integrating with Trunk. This document explains how to configure Pest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To generate XML reports, append `--log-junit junit.xml` to your `pest` test command:

```undefined
pest --log-junit junit.xml
```

#### Report File Path

The JUnit report is written to the location specified by `--log-junit`. In the example above, the test results will be written to `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Pest doesn't support retries out of the box, but if you implemented retries, remember to disable them.

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

