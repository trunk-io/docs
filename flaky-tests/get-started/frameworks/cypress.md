---
title: Configuring cypress
description: A guide for generating Trunk-compatible test reports for Cypress tests
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

# Cypress

## 1. Generate JUnit

Update your Cypress config to output JUnit reports:

{% code title="cypress.config.js" %}
```javascript
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  reporter: 'junit',
  reporterOptions: {
    mochaFile: 'results/junit.xml',
    toConsole: true,
  },
})
```
{% endcode %}

## 2. Output Location

The JUnit report location is specified by the `mochaFile` property in your Cypress config. In the above example, the file will be at `results/junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

You can disable retries by setting `retries: 0`in your Cypress config file.

```javascript
module.exports = defineConfig({
  retries: 1,
})
```

## Next Step

JUnit files generated with Cypress are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
