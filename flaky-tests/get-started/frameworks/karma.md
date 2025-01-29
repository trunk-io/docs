---
title: Configuring karma
description: A guide for generating Trunk-compatible test reports for Karma tests
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

# Karma

## 1. Generate JUnit

Install the `karma-junit-reporter` package:

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
        outputDir: 'test_results',
        outputFile: 'junit.xml'
      }
    }
  )
}
```
{% endcode %}

## 2. Output Location

The `outputDir` and `outputFile` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test_results/$browserName/report.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Karma doesn't support retries out of the box, but if you implemented retries, remember to disable them.

## Next Step <a href="#next-step" id="next-step"></a>

JUnit files generated with Karma are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
