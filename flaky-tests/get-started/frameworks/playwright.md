---
title: Configuring playwright
description: A guide for generating JUnit test reports for Playwright tests
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

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['junit', 
      { outputFile: 'junit.xml' }
    ]
  ],
});
```

## 2. Output Location

The JUnit file will be written to the `outputFile` specified in the configuration. In the example above, the results will be written to `junit.xml`.

## Next Step

JUnit files generated with Playwright are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.
