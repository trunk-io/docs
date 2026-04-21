---
title: Configuring mocha
description: A guide for generating Trunk-compatible test reports for Mocha
---

# Mocha

You can automatically [detect and manage flaky tests](../../detection/) in your Mocha projects by integrating with Trunk Flaky Tests.

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

You can configure your Mocha runner to use the reporter programmatically as well:

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

{% include "../../../.gitbook/includes/retries.md" %}

You can disable retry by omitting the `--retries` CLI option and [removing retries for individual tests](https://mochajs.org/#retry-tests).

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
