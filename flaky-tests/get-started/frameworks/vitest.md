---
title: Configuring vitest
description: A guide for generating Trunk-compatible test reports with Vitest
---

# Vitest

You can automatically [detect and manage flaky tests](../../detection/) in your Vitest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

You can configure Vitest to produce a Trunk-compatible JUnitXML report by updating your `vitest.config.ts`.

{% code title="vitest.config.ts" %}
```javascript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    reporters: [
      ['junit', { outputFile: './junit.xml', addFileAttribute: true }],
    ],
  },
});
```
{% endcode %}

{% hint style="warning" %}
**Important**: The `addFileAttribute: true` option is required for the JUnit report to pass `trunk-analytics-cli` validation. This option adds file path information to each test case in the XML output, which Trunk uses to associate test results with source files.
{% endhint %}

#### Report File Path

The `outputFile: './junit.xml'` option specifies the path of the JUnit report. You'll need this path later when configuring automatic uploads to Trunk.

{% include "../../../.gitbook/includes/retries.md" %}

If you've enabled retries, you can disable them following the [Vitest docs](https://vitest.dev/api/) for more accurate results.

{% hint style="info" %}
**Note**: Configuration errors can sometimes mask themselves as consistent test failures. If you're seeing file-level test entries instead of individual test cases, resolve configuration issues first before adjusting retry settings. A properly configured test suite should show individual test case names in the JUnit output, not file names.
{% endhint %}

### Troubleshooting

**Configuration Errors and File-Level Test Failures**

**Issue**: You might see Trunk identifying flaky tests with names that match your test file names (e.g., `auth.test.ts` instead of `should login successfully`) rather than individual test case names.

**Root Cause**: This typically occurs when Vitest encounters configuration errors that prevent it from properly parsing or running the tests in a file. Common scenarios include:

* TypeScript configuration errors in `tsconfig.json`
* Missing dependencies or import resolution failures
* Syntax errors in test setup files
* Invalid Vitest configuration options

**What Happens**: When Vitest cannot execute the individual tests within a file due to configuration issues, it generates a single JUnit test case entry named after the file itself, regardless of how many actual test cases exist in that file.

**How to Diagnose**:

1. Run your tests locally with verbose output: `vitest --reporter=verbose`
2. Check for configuration warnings or errors in the test output
3. Look for test files that show as single entries in your JUnit report when they should contain multiple test cases

**How to Fix**:

1. **Check TypeScript Configuration**: Ensure your `tsconfig.json` is valid and includes all necessary paths
2. **Verify Dependencies**: Make sure all imported modules are properly installed and accessible
3. **Review Setup Files**: Check any test setup files referenced in your Vitest config for errors
4. **Validate Vitest Config**: Make sure your `vitest.config.ts` doesn't contain invalid options

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
