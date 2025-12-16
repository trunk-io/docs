---
title: Configuring cargo-nextest
description: A guide for generating Trunk-compatible test reports for Rust
---

# cargo-nextest

You can automatically [detect and manage flaky tests](../../detection.md) in your Rust projects by integrating with Trunk. This document explains how to configure cargo-nextest to output JUnit XML reports that can be uploaded to Trunk for analysis.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](rust.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../ci-providers/).

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

`cargo-nextest` outputs artifacts at `target/nextest` by default. When you provide a profile and a file name via the config example above, it produces a report at `target/nextest/ci/junit.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Omit the `--retries` option.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

{% tabs %}
{% tab title="Linux (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./target/nextest/ci/junit.xml"
```
{% endtab %}

{% tab title="Linux (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./target/nextest/ci/junit.xml"
```
{% endtab %}

{% tab title="macOS (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./target/nextest/ci/junit.xml"
```
{% endtab %}

{% tab title="macOS (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli validate --junit-paths "./target/nextest/ci/junit.xml"
```
{% endtab %}
{% endtabs %}

This will not upload anything to Trunk. To improve detection accuracy, you should address all errors and warnings before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
./trunk-analytics-cli upload --junit-paths "./target/nextest/ci/junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Azure DevOps Pipelines</strong></td><td></td><td><a href="../ci-providers/azure-devops-pipelines.md">azure-devops-pipelines.md</a></td><td><a href="../../../.gitbook/assets/azure.png">azure.png</a></td></tr><tr><td><strong>BitBucket Pipelines</strong></td><td></td><td><a href="../ci-providers/bitbucket-pipelines.md">bitbucket-pipelines.md</a></td><td><a href="../../../.gitbook/assets/bitbucket.png">bitbucket.png</a></td></tr><tr><td><strong>BuildKite</strong></td><td></td><td><a href="../ci-providers/buildkite.md">buildkite.md</a></td><td><a href="../../../.gitbook/assets/buildkite.png">buildkite.png</a></td></tr><tr><td><strong>CircleCI</strong></td><td></td><td><a href="../ci-providers/circleci.md">circleci.md</a></td><td><a href="../../../.gitbook/assets/circle-ci.png">circle-ci.png</a></td></tr><tr><td><strong>Drone CI</strong></td><td></td><td><a href="../ci-providers/droneci.md">droneci.md</a></td><td><a href="../../../.gitbook/assets/drone.png">drone.png</a></td></tr><tr><td><strong>GitHub Actions</strong></td><td></td><td><a href="../ci-providers/github-actions.md">github-actions.md</a></td><td><a href="../../../.gitbook/assets/github.png">github.png</a></td></tr><tr><td><strong>Gitlab</strong></td><td></td><td><a href="../ci-providers/gitlab.md">gitlab.md</a></td><td><a href="../../../.gitbook/assets/gitlab.png">gitlab.png</a></td></tr><tr><td><strong>Jenkins</strong></td><td></td><td><a href="../ci-providers/jenkins.md">jenkins.md</a></td><td><a href="../../../.gitbook/assets/jenkins.png">jenkins.png</a></td></tr><tr><td><strong>Semaphore</strong></td><td></td><td><a href="../ci-providers/semaphoreci.md">semaphoreci.md</a></td><td><a href="../../../.gitbook/assets/semaphore.png">semaphore.png</a></td></tr><tr><td><strong>TeamCity</strong></td><td></td><td><a href="broken-reference/">broken-reference</a></td><td><a href="../../../.gitbook/assets/teamcity.png">teamcity.png</a></td></tr><tr><td><strong>Travis CI</strong></td><td></td><td><a href="../ci-providers/travisci.md">travisci.md</a></td><td><a href="../../../.gitbook/assets/travis.png">travis.png</a></td></tr><tr><td><strong>Other CI Providers</strong></td><td></td><td><a href="../ci-providers/otherci.md">otherci.md</a></td><td><a href="../../../.gitbook/assets/other.png">other.png</a></td></tr></tbody></table>
