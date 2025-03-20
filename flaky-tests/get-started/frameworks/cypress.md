---
title: Configuring cypress
description: A guide for generating Trunk-compatible test reports for Cypress tests
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

# Cypress

You can automatically [detect and manage flaky tests](../../detection.md) in your Cypress projects by integrating with Trunk. This document explains how to configure Cypress to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Cypress has a built-in XML reporter which you can use to output a Trunk-compatible report.

Update your Cypress config, such as you `cypress.config.js` or `cypress.config.ts` file to output XML reports:

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

#### Report File Path

The JUnit report location is specified by the `mochaFile` property in your Cypress config. In the above example, the file will be at `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

You can disable retries by setting `retries: 0` in your Cypress config file.

{% code title="cypress.config.js" %}
```javascript
module.exports = defineConfig({
  retries: 0,
})
```
{% endcode %}

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

