---
title: Configuring jest
description: A guide for generating JUnit test reports for Jest tests
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
    "default",
    "jest-junit": {
      "outputDirectory": "./test_results",
      "outputName": "report.xml"
    }
  ]
}
```
{% endcode %}

## 2. Output Location

The `outputDirectory` and `outputName` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test_results/report.xml`.

## Next Step

JUnit files generated with Jest are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.
