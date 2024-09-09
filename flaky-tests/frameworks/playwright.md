---
title: Configuring playwright
description: How to configure JUnit XML output for the Playwright testing framework
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---
# Playwright

Playwright is a testing framework for Webapp.

### Enabling XML Output
Playwright has multiple built in reporters. To get [XML output](https://github.com/testmoapp/junitxml) use the `junit` reporter.

```shell
npx playwright test --reporter=junit
```
The output file can be set by either using the `PLAYWRIGHT_JUNIT_OUTPUT_NAME` environment variable or the `outputFile` attribute in the `playwright.config.ts` file.

```shell
PLAYWRIGHT_JUNIT_OUTPUT_FILE=tests/results.xml npx playwright test --reporter=junit
```
or

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [['junit', { outputFile: 'tests/results.xml' }]],
});
```
See the [Playwright JUnit reporter docs](https://playwright.dev/docs/test-reporters#junit-reporter) for more information.



### Test Suite Naming

Playwright tests are driven by functions in `*.spec.ts` files. The XML testsuite `name` attributes will automatically be set by the description parameters to the test functions.  The `name` attribute of the `<testsuites>` element can be set with the `PLAYWRIGHT_JUNIT_SUITE_NAME` environment variable.

Playwright does not support including the full filepath of the failed test in the XML output.









