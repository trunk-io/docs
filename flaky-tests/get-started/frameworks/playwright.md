---
title: Configuring playwright
description: A guide for generating Trunk-compatible test reports for Playwright
---

# Playwright

You can automatically [detect and manage flaky tests](../../detection/) in your Playwright projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Playwright has multiple built-in reporters, including JUnit XML which Trunk can ingest. To get XML reports, add the following to your Playwright config:

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

Alternatively, you can specify reporting behavior inline in your CI:

```sh
npx playwright test --reporter=junit
```

#### Report File Path

You can specify the report's output location with the `PLAYWRIGHT_JUNIT_OUTPUT_FILE` environment variable:

```sh
export PLAYWRIGHT_JUNIT_OUTPUT_FILE=junit.xml
```

You can also specify the report's location in your `playwright.config.ts` file:

```typescript
export default defineConfig({
  reporter: [
    ['junit', { outputFile: 'junit.xml' }]
  ],
});
```

{% include "../../../.gitbook/includes/retries.md" %}

You can disable retries in Playwright by omitting the `--retries` command line option and [removing retries in your `playwright.config.ts` file](https://playwright.dev/docs/test-retries#retries).

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
