---
title: Configuring cargo-nextest
description: A guide for generating Trunk-compatible test reports for Rust
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

# cargo-nextest

You can automatically [detect and manage flaky tests](../../detection.md) in your Rust projects by integrating with Trunk. This document explains how to configure cargo-nextest to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

`cargo-nextest` has built-in reporting for JUnit XML reports, which is trunk-compatible. You can enable JUnit reporting by adding the following to your nextest config:

{% code title=".config/nextest.toml" %}
```toml
[profile.ci.junit]
path = "junit.xml"
```
{% endcode %}

You can invoke this profile when running tests with:

```sh
cargo nextest run --profile ci
```

#### Report File Path

`cargo-nextest` outputs artifacts at `target/nextest` by default. When you provide a profile and a file name via the config example above, it produces a report at `target/nextest/ci/junit.xml`.&#x20;

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the `--retries` option.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./target/nextest/ci/junit.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./target/nextest/ci/junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

