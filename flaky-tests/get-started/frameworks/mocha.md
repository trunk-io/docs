---
title: Configuring mocha
description: A guide for generating Trunk-compatible test reports for Mocha
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

# Mocha

You can automatically [detect and manage flaky tests](../../detection.md) in your Mocha projects by integrating with Trunk. This document explains how to configure Mocha to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before integrating with Trunk, you need to generate Trunk-compatible reports. For Mocha, the easiest approach is to generate XML reports.

First, install the `mocha-junit-reporter` package:

```shell
npm install --save-dev mocha-junit-reporter
```

You can then generate reports when you run your tests by providing the `--reporter` and `--reporter-options` options when you run your tests:

```sh
mocha --reporter mocha-junit-reporter --reporter-options mochaFile=./junit.xml
```

You can configure your Mocha runner to use the reporter programmatically as well:&#x20;

```javascript
var mocha = new Mocha({
    reporter: 'mocha-junit-reporter',
    reporterOptions: {
        mochaFile: './junit.xml'
    }
});
```

#### Report File Path

The resulting JUnit XML file will be written to the location specified by the `mochaFile` property in `reporterOptions`. In the examples above, the results would be at `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

You can disable retry by omitting the `--retries` CLI option and [removing retries for individual tests](https://mochajs.org/#retry-tests).

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

