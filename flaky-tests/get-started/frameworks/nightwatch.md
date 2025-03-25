---
description: A guide for generating Trunk-compatible test reports for Nightwatch
---

# Nightwatch

You can automatically [detect and manage flaky tests](../../detection.md) in your Nightwatch projects by integrating with Trunk. This document explains how to configure Nightwatch to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Nightwatch will automatically report test results in multiple formats. You can configure the output location by updating the `nightwatch.conf.cjs` config file.

```javascript
module.exports = {
  output_folder: 'test-reports',
  ...
}
```

You can also specify output at runtime with the command line option `--output <OUTPUT_FOLDER>`:

```sh
nightwatch --output ./test-reports
```

#### Report File Path

Nightwatch outputs multiple reports for each test suite under the specified output folder.

If you configured your output folder to be under `./test-reports`, the JUnit XML files will be found under `./test-reports/**`. You can upload multiple JUnit reports by using a glob like `./test-reports/**/*.xml`.

{% hint style="warning" %}
**Duplicate Uploads**

When using globs, it's important to clean up old test reports between test runs. If your glob path contains old JUnit files, uploading old test results can cause tests to be mislabeled.
{% endhint %}

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Nightwatch doesn't implement any form of automatic retry for failed or flaky tests by default. If you have a custom implementation of retries, remember to disable them.

### Try It Locally

#### **The Validate Command**

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./test-reports/**/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

