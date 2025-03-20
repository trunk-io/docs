---
description: A guide for generating Trunk-compatible test reports for GoogleTest
---

# GoogleTest

You can automatically [detect and manage flaky tests](../../detection.md) in your GoogleTest projects by integrating with Trunk. This document explains how to configure GoogleTest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before you can integrate with Trunk, you need to generate a Trunk-compatible report. For GoogleTest, the built in XML reporter will work. You can use the [`--gtest_output=xml`](https://google.github.io/googletest/advanced.html#generating-an-xml-report) argument when you run your built test project:

```shell
./build/run_test --gtest_output=xml
```

#### Report File Path

By default, the JUnit report will be written to a `test_detail.xml` file.

You can specify a custom directory and filename with:

```bash
--gtest_output=xml:<path/to/file.xml>
```

For example, the following argument writes a JUnit report to `./junit.xml`:

```bash
--gtest_output=xml:junit.xml
```

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the[ ](https://docs.pytest.org/en/stable/how-to/cache.html)[`--gtest_repeat`](https://google.github.io/googletest/advanced.html#repeating-the-tests) argument if you've previously configured your CI with these options to disable retries.

### Try It Locally

#### The Validate Command

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

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

