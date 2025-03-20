---
title: Configuring jasmine
description: A guide for generating Trunk-compatible test reports for Jasmine tests
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

# Jasmine

You can automatically [detect and manage flaky tests](../../detection.md) in your Jasmine projects by integrating with Trunk. This document explains how to configure Jasmine to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before integrating with Trunk, you need to generate Trunk-compatible reports. For Jasmine, the easiest approach is to generate XML reports.

First, install the [`jasmine-reporters`](https://www.npmjs.com/package/jasmine-reporters) package:

```shell
npm install --save-dev jasmine-reporters
```

#### In-Browser tests

When used for in-browser tests, the reporters are registered on a `jasmineReporters` object in the global scope (i.e. `window.jasmineReporters`). You can register it like this in your Jasmine config under `/spec/support/jasmine.mjs`:

{% code title="/spec/support/jasmine.mjs" %}
```javascript
import jasmineReporters from 'jasmine-reporters';

var junitReporter = new jasmineReporters.JUnitXmlReporter({
    savePath: "test-reports",
    consolidateAll: false
});
jasmine.getEnv().addReporter(junitReporter);
```
{% endcode %}

#### NodeJS

In Node.js, `jasmine-reporters` exports an object with all the reporters. You can register it like this in your Jasmine config under `/spec/support/jasmine.mjs`:

```javascript
var reporters = require('jasmine-reporters');
var junitReporter = new reporters.JUnitXmlReporter({
    savePath: "test-reports",
    consolidateAll: false
});
jasmine.getEnv().addReporter(junitReporter)

```

#### Report File Path

Jasmine will generate an XML report at the location specified by the `savePath` property. In the examples above, the XML report can be located with the glob `test_reports/*.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

If you're using a package like [protractor-flake](https://www.npmjs.com/package/protractor-flake), disable it to get more accurate results from Trunk. Instead, you can mitigate flaky tests using the [Quarantining](../../quarantining.md) feature in Trunk.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./junit-reports/*.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit-reports/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

