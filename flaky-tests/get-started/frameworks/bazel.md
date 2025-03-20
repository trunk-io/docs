---
title: Configuring bazel
description: A guide for generating Trunk-compatible test reports with Bazel
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

# Bazel

You can automatically [detect and manage flaky tests](../../detection.md) in your Bazel projects by integrating with Trunk. This document explains how to configure Bazel to output compatible reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk can parse JSON serialized [Build Event Protocol (BEP) ](https://bazel.build/remote/bep)files to detect flaky tests. You can run tests with Bazel in CI with the `nobuild_event_json_file_path_conversion` option to produce a serialized BEP file:

```sh
bazel test <TARGETS> \
    --nobuild_event_json_file_path_conversion
```

#### Report File Path

You can specify the path of the generated report through the  `build_event_json_file` option:

```sh
bazel test <TARGETS> \
    --nobuild_event_json_file_path_conversion
    --build_event_json_file=build_events.json
```

Trunk can parse the `build_events.json` file to locate your test reports. You will still need to **configure your test runners to output compatible reports**, and you can refer to the guides for [individual test frameworks](./).

#### Disable Retries

You need to disable automatic retries if you previously enabled them for more accurate detection results.

Disable retries if you're retrying tests using the `--flaky_test_attempts` command line option or retrying in your test runner.

### Try It Locally

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --bazel-bep-path=build_events.json \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

