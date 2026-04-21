---
title: Configuring cypress
description: A guide for generating Trunk-compatible test reports for Cypress tests
---

# Cypress

You can automatically [detect and manage flaky tests](../../detection/) in your Cypress projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Cypress has a built-in Mocha JUnit reporter which outputs XML test reports. However, the built-in reporter does not include file paths in test case elements, which means Trunk cannot match tests to code owners or enable file-based filtering in the dashboard.

#### Recommended: Use cypress-junit-plugin for file paths

For full functionality including code owner detection and file-based search, use the [`cypress-junit-plugin`](https://github.com/saucelabs/cypress-junit-plugin) reporter. It outputs test cases with the correct nested structure and file path attributes that Trunk expects.

Install the plugin:

```bash
npm install --save-dev @saucelabs/cypress-junit-plugin
```

Update your Cypress config:

{% code title="cypress.config.js" %}
```javascript
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  reporter: '@saucelabs/cypress-junit-plugin',
  reporterOptions: {
    mochaFile: './junit.xml',
  },
})
```
{% endcode %}

#### Alternative: Built-in Mocha reporter

If you don't need file path matching or code owner detection, you can use the built-in reporter. Uploads will still work, but you will see warnings about missing file paths and won't be able to search by file in the dashboard.

{% code title="cypress.config.js" %}
```javascript
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  reporter: 'junit',
  reporterOptions: {
    mochaFile: './junit.xml',
    toConsole: true,
  },
})
```
{% endcode %}

{% hint style="info" %}
The built-in Mocha JUnit reporter places the `file` attribute on `<testsuite>` elements but not on individual `<testcase>` elements. Trunk requires file paths on test cases for code owner matching. If you see warnings like "report has test cases with missing file or filepath", switch to the `cypress-junit-plugin` above.
{% endhint %}

#### Report File Path

The JUnit report location is specified by the `mochaFile` property in your Cypress config. In the above example, the file will be at `./junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

You can disable retries by setting `retries: 0` in your Cypress config file.

{% code title="cypress.config.js" %}
```javascript
module.exports = defineConfig({
  retries: 0,
})
```
{% endcode %}

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
