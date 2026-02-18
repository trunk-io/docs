---
title: Configuring cypress
description: A guide for generating Trunk-compatible test reports for Cypress tests
---

# Cypress

You can automatically [detect and manage flaky tests](../../detection.md) in your Cypress projects by integrating with Trunk. This document explains how to configure Cypress to output JUnit XML reports that can be uploaded to Trunk for analysis.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](cypress.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report (with file paths for best results)
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../ci-providers/).

### Generating Reports

Cypress supports JUnit XML output through its built-in Mocha reporter and through third-party plugins. We recommend the **Sauce Labs Cypress JUnit Plugin** for the best experience with Trunk.

#### Recommended: Sauce Labs Cypress JUnit Plugin

The [`cypress-junit-plugin`](https://github.com/saucelabs/cypress-junit-plugin) produces JUnit XML reports with properly structured file paths on each test case. This enables Trunk features like **file path filtering** and **Code Owners** matching.

Install the plugin:

```bash
npm install --save-dev @saucelabs/cypress-junit-plugin
```

Update your Cypress config to use the plugin:

{% code title="cypress.config.js" %}
```javascript
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  reporter: '@saucelabs/cypress-junit-plugin',
  reporterOptions: {
    outputDirectory: './',
    outputFileName: 'junit.xml',
  },
})
```
{% endcode %}

#### Alternative: Built-in Mocha Reporter

Cypress also has a built-in Mocha JUnit reporter. This reporter works for basic uploads, but it places the `file` attribute on a sibling `<testsuite>` element rather than directly on test cases. Because Trunk expects a hierarchical structure for inheriting attributes like file paths, this means **file paths and Code Owners will not be available** for your tests in the Trunk dashboard.

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
If you use the built-in reporter, you will see a warning during upload: `report has test cases with missing file or filepath`. This warning does not prevent the upload from succeeding, but tests will not have file paths or Code Owners associated with them.
{% endhint %}

<details>

<summary>Why does the built-in reporter cause this warning?</summary>

The built-in Mocha reporter produces XML where the `file` attribute and the `<testcase>` elements are in **sibling** `<testsuite>` elements rather than in a parent-child hierarchy:

```xml
<testsuites name="Mocha Tests">
  <!-- file attribute is here... -->
  <testsuite name="Root Suite" file="cypress/e2e/example.cy.js">
  </testsuite>
  <!-- ...but test cases are in a sibling, not a child -->
  <testsuite name="My Test Suite">
    <testcase name="should do something" classname="does something">
    </testcase>
  </testsuite>
</testsuites>
```

Trunk resolves attributes like `file` by walking **up** the XML hierarchy from each `<testcase>`. Because the `file` attribute lives on an adjacent `<testsuite>` rather than a parent, it is not inherited by the test cases.

The Sauce Labs plugin solves this by placing file path information directly on each test case in a properly nested structure.

</details>

#### Report File Path

When using the Sauce Labs plugin, the report location is specified by the `outputDirectory` and `outputFileName` options. When using the built-in Mocha reporter, the location is specified by the `mochaFile` property. In both examples above, the file will be at `./junit.xml`.

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

#### **The Validate Command**

{% tabs %}
{% tab title="Linux (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./junit.xml"
```
{% endtab %}

{% tab title="Linux (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./junit.xml"
```
{% endtab %}

{% tab title="macOS (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./junit.xml"
```
{% endtab %}

{% tab title="macOS (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./junit.xml"
```
{% endtab %}
{% endtabs %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
./trunk-analytics-cli upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

You can find your Trunk organization slug and token in the settings or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system). After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the report has issues.

<figure><picture><source srcset="../../../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

## Next Step

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Azure DevOps Pipelines</strong></td><td></td><td><a href="../ci-providers/azure-devops-pipelines.md">azure-devops-pipelines.md</a></td><td><a href="../../../.gitbook/assets/azure.png">azure.png</a></td></tr><tr><td><strong>BitBucket Pipelines</strong></td><td></td><td><a href="../ci-providers/bitbucket-pipelines.md">bitbucket-pipelines.md</a></td><td><a href="../../../.gitbook/assets/bitbucket.png">bitbucket.png</a></td></tr><tr><td><strong>BuildKite</strong></td><td></td><td><a href="../ci-providers/buildkite.md">buildkite.md</a></td><td><a href="../../../.gitbook/assets/buildkite.png">buildkite.png</a></td></tr><tr><td><strong>CircleCI</strong></td><td></td><td><a href="../ci-providers/circleci.md">circleci.md</a></td><td><a href="../../../.gitbook/assets/circle-ci.png">circle-ci.png</a></td></tr><tr><td><strong>Drone CI</strong></td><td></td><td><a href="../ci-providers/droneci.md">droneci.md</a></td><td><a href="../../../.gitbook/assets/drone.png">drone.png</a></td></tr><tr><td><strong>GitHub Actions</strong></td><td></td><td><a href="../ci-providers/github-actions.md">github-actions.md</a></td><td><a href="../../../.gitbook/assets/github.png">github.png</a></td></tr><tr><td><strong>Gitlab</strong></td><td></td><td><a href="../ci-providers/gitlab.md">gitlab.md</a></td><td><a href="../../../.gitbook/assets/gitlab.png">gitlab.png</a></td></tr><tr><td><strong>Jenkins</strong></td><td></td><td><a href="../ci-providers/jenkins.md">jenkins.md</a></td><td><a href="../../../.gitbook/assets/jenkins.png">jenkins.png</a></td></tr><tr><td><strong>Semaphore</strong></td><td></td><td><a href="../ci-providers/semaphoreci.md">semaphoreci.md</a></td><td><a href="../../../.gitbook/assets/semaphore.png">semaphore.png</a></td></tr><tr><td><strong>TeamCity</strong></td><td></td><td><a href="broken-reference/">broken-reference</a></td><td><a href="../../../.gitbook/assets/teamcity.png">teamcity.png</a></td></tr><tr><td><strong>Travis CI</strong></td><td></td><td><a href="../ci-providers/travisci.md">travisci.md</a></td><td><a href="../../../.gitbook/assets/travis.png">travis.png</a></td></tr><tr><td><strong>Other CI Providers</strong></td><td></td><td><a href="../ci-providers/otherci.md">otherci.md</a></td><td><a href="../../../.gitbook/assets/other.png">other.png</a></td></tr></tbody></table>
