---
title: Configuring vitest
description: A guide for generating Trunk-compatible test reports with Vitest
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

# Vitest

You can automatically [detect and manage flaky tests](../../detection.md) in your Vitest projects by integrating with Trunk. This document explains how to configure Vitest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

You can configure Vitest to produce a Trunk-compatible JUnitXML report by updating your `vitest.config.ts`.

{% code title="vitest.config.ts" %}
```javascript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    reporters: [
      ['junit', { outputFile: './junit.xml' }],
    ],
  },
});
```
{% endcode %}

#### Report File Path

The `outputFile: './junit.xml'` option specifies the path of the JUnit report. You'll need this path later when configuring automatic uploads to Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you've enabled retries, you can disable them following the [Vitest docs](https://vitest.dev/api/) for more accurate results.

### Try It Locally

#### The Validate Command

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

