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

## 1. Generate JUnit

Update your Vitest config to include the `junit` reporter:

```typescript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    reporters: [
      ['junit', { outputFile: './junit.xml' }],
    ],
  },
});
```

## 2. Output Location

The JUnit report will be written to the `outputFile` specified in the Vite config. In the example above, the report would be written to `./junit.xml.`

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

If you've enabled retries, you can disable them following the [Vitest docs](https://vitest.dev/api/) for more accurate results.

## Next Step

JUnit files generated with Vitest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
