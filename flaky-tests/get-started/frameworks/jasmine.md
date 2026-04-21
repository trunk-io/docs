---
title: Configuring jasmine
description: A guide for generating Trunk-compatible test reports for Jasmine tests
---

# Jasmine

You can automatically [detect and manage flaky tests](../../detection/) in your Jasmine projects by integrating with Trunk Flaky Tests.

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

{% include "../../../.gitbook/includes/retries.md" %}

If you're using a package like [protractor-flake](https://www.npmjs.com/package/protractor-flake), disable it to get more accurate results from Trunk. Instead, you can mitigate flaky tests using the [Quarantining](../../quarantining.md) feature in Trunk.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
