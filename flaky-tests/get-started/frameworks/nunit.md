---
description: A guide for generating Trunk-compatible test reports for NUnit
---

# NUnit

You can automatically [detect and manage flaky tests](../../detection.md) in your NUnit projects by integrating with Trunk. This document explains how to configure NUnit to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

You can do this in dotnet with the NUnit's built-in JUnit reporter:&#x20;

```sh
dotnet test -o build  -- NUnit.TestOutputXml="junit"
```

#### Report File Path

.NET will output each build to the path specified by `-o <BUILD_PATH>` and test results under a sub-folder of `<BUILD PATH>/test-reports`, specified by the `-- NUnit.TestOutputXml="<XML PATH>"` option.

In the example command from the [Generating Reports step](nunit.md#generating-reports), the XMLs will be located under `./build/test-reports/junit/*.xml`. This is also the glob you'll use to locate the results when uploading test results.

#### Disable Retries

You need to disable automatic retries if you previously included them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit `[Retry(n)]` from tests to disable retries.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./build/test-reports/junit/*.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./build/test-reports/junit/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
