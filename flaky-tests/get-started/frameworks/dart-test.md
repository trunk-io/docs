---
description: A guide for generating Trunk-compatible test reports for Dart tests
---

# Dart Test

You can automatically [detect and manage flaky tests](../../detection.md) in your Dart projects by integrating with Trunk. This document explains how to configure Dart to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before you can upload to Trunk, you need to output a Trunk-compatible report. Dart supports JUnit outputs by using the `tojunit` library. You can install the `tojunit` library using the following command:

```sh
dart pub global activate junitreport
```

Then, you can convert test reports to a JUnit format by piping it to `tojunit`and piping the output to a file like this:&#x20;

<pre class="language-sh"><code class="lang-sh"><strong>dart test &#x3C;TEST_PATH> --reporter json | tojunit > junit.xml
</strong></code></pre>

#### Report File Path

The JUnit report is written to the location specified by the `tojunit >` pipe. In the example above, the test results will be written to `./junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Dart provides retries through the [retry class annotations](https://pub.dev/documentation/test/latest/test/Retry-class.html). Disable retry, use Trunk to [detect](../../detection.md)[ flaky tests](../../detection.md), and use Quarantining to isolate flaky tests dynamically at run time.

### Try It Locally

#### **The Validate Command**

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

