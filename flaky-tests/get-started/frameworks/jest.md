---
title: Configuring jest
description: A guide for generating Trunk-compatible test reports for Jest tests
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

# Jest

You can automatically [detect and manage flaky tests](../../detection.md) in your Jest projects by integrating with Trunk. This document explains how to configure Jest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating XML reports from your test runs.

To generate a Trunk-compatible XML report, install the `jest-junit` package:

```bash
npm install --save-dev jest-junit
```

Update your Jest config to add `jest-junit` as a reporter:

{% code title="jest.config.json" %}
```json
{
  "reporters": [
    [
      "jest-junit",
      {
        "outputDirectory": "./",
        "outputName": "junit.xml",
        "addFileAttribute": "true"
      }
    ]
  ]
}
```
{% endcode %}

#### Report File Path

The `outputDirectory` and `outputName` options specify the path of the XML report. You'll need this path later when configuring automatic uploads to Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you have retries configured using the [jest.retryTimes method](https://jestjs.io/docs/jest-object#jestretrytimesnumretries-options), disable them for more accurate results.

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

