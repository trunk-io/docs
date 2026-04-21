---
title: Configuring jest
description: A guide for generating Trunk-compatible test reports for Jest tests
---

# Jest

You can automatically [detect and manage flaky tests](../../detection/) in your Jest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating XML reports from your test runs.

To generate a Trunk-compatible XML report, install the `jest-junit` package:

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
        "outputDirectory": "./",
        "outputName": "junit.xml",
        "addFileAttribute": "true",
        "reportTestSuiteErrors": "true"
      }
    ]
  ]
}
```
{% endcode %}

#### Report File Path

The `outputDirectory` and `outputName` options specify the path of the XML report. You'll need this path later when configuring automatic uploads to Trunk.

{% include "../../../.gitbook/includes/retries.md" %}

If you have retries configured using the [jest.retryTimes method](https://jestjs.io/docs/jest-object#jestretrytimesnumretries-options), disable them for more accurate results.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
