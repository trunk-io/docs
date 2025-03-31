---
description: A guide for generating Trunk-compatible test reports for Behave
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

# Behave

You can automatically [detect and manage flaky tests](../../detection.md) in your projects running Behave by integrating with Trunk. This document explains how to configure Behave to output JUnit XML reports that can be uploaded to Trunk for analysis.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](behave.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../ci-providers/).

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. Behave can output JUnit XML reports which are compatible with Trunk. You can do so with the `--junit` option:

```sh
behave --junit
```

#### Report File Path

You can customize the file path of the reports using the `--junit-directory` option.

```sh
behave --junit --junit-directory ./junit-reports
```

Behave outputs multiple XML reports under the JUnit directory. You can locate these when uploading the reports in CI with the `"./junit-reports/*.xml"` glob.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

You must remove the [rerun formatter](https://behave.readthedocs.io/en/latest/formatters/#formatters) from your `behave.ini` file if it is being used to automatically rerun failed tests.

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

You make a upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit-reports/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

You can find your Trunk organization slug and token in the settings or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system). After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the report has issues.

<figure><picture><source srcset="../../../.gitbook/assets/uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../.gitbook/assets/uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

