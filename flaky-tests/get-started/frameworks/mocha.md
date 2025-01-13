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

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

You can disable retry by omitting the `--retries` CLI option and [removing retries for individual tests](https://mochajs.org/#retry-tests).

## Next Step

JUnit files generated with Mocha are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
