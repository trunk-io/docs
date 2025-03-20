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

You can automatically [detect and manage flaky tests](../../detection.md) in your Playwright projects by integrating with Trunk. This document explains how to configure Playwright to output JUnit XML reports that can be uploaded to Trunk for analysis.

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

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

You can disable retries in Playwright by omitting the `--retries` command line option and [removing retries in your `playwright.config.ts` file](https://playwright.dev/docs/test-retries#retries).

### Try It Locally

#### The Validate Command

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make a upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

## Next Step

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

