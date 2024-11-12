---
title: Configuring karma
description: A guide for generating JUnit test reports for Karma tests
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

## 2. Output Location

The `outputDir` and `outputFile` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test_results/$browserName/report.xml`.

## Next Step <a href="#next-step" id="next-step"></a>

JUnit files generated with Karma are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.

\
