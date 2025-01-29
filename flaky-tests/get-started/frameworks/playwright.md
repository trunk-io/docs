---
title: Configuring playwright
description: A guide for generating Trunk-compatible test reports for Playwright
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

# Playwright

## 1. Generate JUnit

Configure Playwright to generate JUnit:

{% code title="playwright.config.ts" %}
```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['junit', { outputFile: 'junit.xml' }]
  ],
});
```
{% endcode %}

## 2. Output Location

The JUnit file will be written to the `outputFile` specified in the configuration. In the example above, the results will be written to `junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

You can disable retries in Playwright by omitting the `--retries` command line option and [removing retries in your `playwright.config.ts` file](https://playwright.dev/docs/test-retries#retries).

## Next Step

JUnit files generated with Playwright are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
