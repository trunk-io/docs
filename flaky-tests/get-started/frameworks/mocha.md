---
title: Configuring mocha
description: A guide for generating JUnit test reports for Mocha tests
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

## 1. Generate JUnit

Install the `mocha-junit-reporter` package:

```shell
npm install --save-dev mocha-junit-reporter
```

Configure your Mocha runner to use the JUnit reporter:

```javascript
var mocha = new Mocha({
    reporter: 'mocha-junit-reporter',
    reporterOptions: {
        mochaFile: './test_results/junit.xml'
    }
});
```

## 2. Output Location

The resulting JUnit XML file will be written to the location specified by the `mochaFile` property in `reporterOptions`. In the example above, the results would be at `./test_results/junit.xml`.

## Next Step

JUnit files generated with Mocha are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
