---
title: Configuring rspec
description: >-
  A guide for generating Trunk-compatible test reports for RSpec without using
  Trunk's RSpec plugin
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

# RSpec (Manual Uploads)

You can automatically [detect and manage flaky tests](../../../detection.md) in your projects running RSpec by integrating with Trunk. This document explains how to configure RSpec to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% hint style="warning" %}
We highly recommend using [Trunk's RSpec plugin](./) to upload test results for the best accuracy when detecting flaky tests.
{% endhint %}

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](manual-uploads.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../../ci-providers/).

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this for your Rspec tests by generating JUnit XML reports from your test runs.

To generate Trunk-compatible reports, install the `rspec_junit_formatter`:

```shell
gem install rspec_junit_formatter
```

You can use `rspec_junit_formatter` like this:

```shell
rspec --format RspecJunitFormatter --out junit.xml
```

#### Report File Path

The JUnit report will be written to the location specified by the `--out` argument. In the example above, the report would be at `./junit.xml`. You will need this when you update your CI config to integrate with Trunk.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

If you have a step in CI to rerun failed tests with the `--only-failures` option, or you're using a package like [rspec-retry](https://github.com/NoRedInk/rspec-retry), remember to disable them.

### Try It Locally

#### **The Validate Command**

You can validate your test reports using the [Trunk CLI](../../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./junit.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

You can find your Trunk organization slug and token in the settings or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system). After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the report has issues.

<figure><picture><source srcset="../../../../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../../.gitbook/includes/ci-providers.md" %}



