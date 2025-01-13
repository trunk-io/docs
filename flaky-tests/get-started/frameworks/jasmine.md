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

## 1. Generate JUnit

Install the [`jasmine-reporters`](https://www.npmjs.com/package/jasmine-reporters) package:

```shell
npm install --save-dev jasmine-reporters
```

### In-Browser tests

When used for in-browser tests, the reporters are registered on a jasmineReporters object in the global scope (i.e. `window.jasmineReporters`).

```javascript
var junitReporter = new jasmineReporters.JUnitXmlReporter({
    savePath: "test_reports",
    consolidateAll: false
});
jasmine.getEnv().addReporter(junitReporter);
```

### NodeJS

In Node.js, jasmine-reporters exports an object with all the reporters which you can use however you like.

```javascript
var reporters = require('jasmine-reporters');
var junitReporter = new reporters.JUnitXmlReporter({
    savePath: "test_reports",
    consolidateAll: false
});
jasmine.getEnv().addReporter(junitReporter)

```

## 2. Output Location

Jasmine will generate a JUnit report at the location specified by the `savePath` property. In the examples above, the JUnit report will be written to a directory named `test_reports/`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

If you're using a package like [protractor-flake](https://www.npmjs.com/package/protractor-flake), disable it to get more accurate results from Trunk.

## Next Step

JUnit files generated with Jasmine are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
