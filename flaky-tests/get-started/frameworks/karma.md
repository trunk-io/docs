---
title: Configuring karma
description: A guide for generating Trunk-compatible test reports for Karma tests
---

# Karma

You can automatically [detect and manage flaky tests](../../detection/) in your Karma projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating XML reports from your test runs.

To generate a Trunk-compatible XML report, install the `karma-junit-reporter` package:

```shell
npm install --save-dev karma-junit-reporter
```

Add the `junit` reporter to your karma config file:

{% code title="karma.conf.js" %}
```javascript
module.exports = function(config) {
  config.set(
    {
      reporters: ['junit'],
      junitReporter: {
        outputDir: 'test-reports',
      }
    }
  )
}
```
{% endcode %}

#### Report File Path

The `outputDir` and `outputFile` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test-reports/{$browserName}.xml`. You can locate the reports during uploads with the glob `./test-reports/*.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

Karma doesn't support retries out of the box, but if you implemented retries, remember to disable them.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
