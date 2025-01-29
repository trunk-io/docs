---
title: Configuring jest
description: A guide for generating Trunk-compatible test reports for Jest tests
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

# Jest

## 1. Generate JUnit

Install the `jest-junit` package:

```bash
npm install --save-dev jest-junit
```

Update your Jest config to add `jest-junit` as a reporter:

{% code title="jest.config.json" %}
```json
{
  "reporters": [
    [
      "jest-junit",
      {
        "outputDirectory": "./test_results",
        "outputName": "report.xml",
        "addFileAttribute": "true"
      }
    ]
  ]
}
```
{% endcode %}

## 2. Output Location

The `outputDirectory` and `outputName` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test_results/report.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

If you have retries configured using the [jest.retryTimes method](https://jestjs.io/docs/jest-object#jestretrytimesnumretries-options), disable them for more accurate results.

## Next Step

JUnit files generated with Jest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
