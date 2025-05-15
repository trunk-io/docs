---
title: Configuring karma
description: A guide for generating Trunk-compatible test reports for Karma tests
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

# Karma

You can automatically [detect and manage flaky tests](../../detection.md) in your Karma projects by integrating with Trunk. This document explains how to configure Karma to output JUnit XML reports that can be uploaded to Trunk for analysis.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](karma.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../ci-providers/).

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating XML reports from your test runs.

To generate a Trunk-compatible XML report, install the `karma-junit-reporter` package:

```shell
npm install --save-dev karma-junit-reporter
```

Add the `junit` reporter to your karma config file:

{% code title="karma.conf.js" %}
```javascript
module.exports = function(config) {
  config.set(
    {
      reporters: ['junit'],
      junitReporter: {
        outputDir: 'test-reports',
      }
    }
  )
}
```
{% endcode %}

#### Report File Path

The `outputDir` and `outputFile` specify the location of the JUnit test report. In the example above, the JUnit would be at `./test-reports/{$browserName}.xml`. You can locate the reports during uploads with the glob `./test-reports/*.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Karma doesn't support retries out of the box, but if you implemented retries, remember to disable them.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./junit-reports/*.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit-reports/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

You can find your Trunk organization slug and token in the settings or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system). After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the report has issues.

<figure><picture><source srcset="../../../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

