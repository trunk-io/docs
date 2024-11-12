---
title: Configuring vitest
description: A guide for generating JUnit test reports for Vitest tests
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

{% code title="vitest.config.ts" %}
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
{% endcode %}

## 2. Output Location

The JUnit report will be written to the `outputFile` specified in the Vite config. In the example above, the report would be written to `./junit.xml.`

## Next Step

JUnit files generated with Vitest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/ci-providers) for a guide on how to upload test results to Trunk.
