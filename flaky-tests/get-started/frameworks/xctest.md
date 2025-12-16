---
title: Configuring xctest
description: A guide for generating Trunk-compatible test reports for XCode and xcodebuild
---

# XCTest

You can automatically [detect and manage flaky tests](../../detection.md) in your XCTest projects by integrating with Trunk. This document explains how to configure XCTest to output XCResult reports that can be uploaded to Trunk for analysis.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](xctest.md#next-step) to configure your CI provider.

* [ ] Generate a compatible test report
* [ ] Configure the report file path or glob
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

After correctly generating reports following the above steps, you'll be ready to move on to the next steps to [configure uploads in CI](../ci-providers/).

### Generating Reports

Running XCTests from `xcodebuild` produces a `.xcresult` in an obscure directory by default. You can specify a `-resultBundlePath` option to generate the results locally:

```sh
xcodebuild test -scheme <YOUR_SCHEME> \
  -resultBundlePath ./test-results.xcresult
```

You can upload `.xcresult` directories directly to Trunk Flaky Tests.

{% hint style="warning" %}
Only XCode versions 16 or higher are supported.
{% endhint %}

#### Report File Path

The test reports will be written to the `./test-results.xcresult` directory when running tests with the `-resultBundlePath ./test-results.xcresult`option. You will need this path when uploading results to Trunk in CI.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you run tests in CI with [the `-retry-tests-on-failure` option](https://keith.github.io/xcode-man-pages/xcodebuild.1.html#retry-tests-on-failure), disable it for more accurate results.

### Try It Locally

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

{% tabs %}
{% tab title="Linux (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli upload --xcresult-path "./test-results.xcresult" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```
{% endtab %}

{% tab title="Linux (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli upload --xcresult-path "./test-results.xcresult" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```
{% endtab %}

{% tab title="macOS (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli upload --xcresult-path "./test-results.xcresult" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```
{% endtab %}

{% tab title="macOS (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
./trunk-analytics-cli upload --xcresult-path "./test-results.xcresult" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```
{% endtab %}
{% endtabs %}

You can find your Trunk organization slug and token in the settings or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system). After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the report has issues.

<figure><picture><source srcset="../../../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

### Next Step

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Azure DevOps Pipelines</strong></td><td></td><td><a href="../ci-providers/azure-devops-pipelines.md">azure-devops-pipelines.md</a></td><td><a href="../../../.gitbook/assets/azure.png">azure.png</a></td></tr><tr><td><strong>BitBucket Pipelines</strong></td><td></td><td><a href="../ci-providers/bitbucket-pipelines.md">bitbucket-pipelines.md</a></td><td><a href="../../../.gitbook/assets/bitbucket.png">bitbucket.png</a></td></tr><tr><td><strong>BuildKite</strong></td><td></td><td><a href="../ci-providers/buildkite.md">buildkite.md</a></td><td><a href="../../../.gitbook/assets/buildkite.png">buildkite.png</a></td></tr><tr><td><strong>CircleCI</strong></td><td></td><td><a href="../ci-providers/circleci.md">circleci.md</a></td><td><a href="../../../.gitbook/assets/circle-ci.png">circle-ci.png</a></td></tr><tr><td><strong>Drone CI</strong></td><td></td><td><a href="../ci-providers/droneci.md">droneci.md</a></td><td><a href="../../../.gitbook/assets/drone.png">drone.png</a></td></tr><tr><td><strong>GitHub Actions</strong></td><td></td><td><a href="../ci-providers/github-actions.md">github-actions.md</a></td><td><a href="../../../.gitbook/assets/github.png">github.png</a></td></tr><tr><td><strong>Gitlab</strong></td><td></td><td><a href="../ci-providers/gitlab.md">gitlab.md</a></td><td><a href="../../../.gitbook/assets/gitlab.png">gitlab.png</a></td></tr><tr><td><strong>Jenkins</strong></td><td></td><td><a href="../ci-providers/jenkins.md">jenkins.md</a></td><td><a href="../../../.gitbook/assets/jenkins.png">jenkins.png</a></td></tr><tr><td><strong>Semaphore</strong></td><td></td><td><a href="../ci-providers/semaphoreci.md">semaphoreci.md</a></td><td><a href="../../../.gitbook/assets/semaphore.png">semaphore.png</a></td></tr><tr><td><strong>TeamCity</strong></td><td></td><td><a href="broken-reference/">broken-reference</a></td><td><a href="../../../.gitbook/assets/teamcity.png">teamcity.png</a></td></tr><tr><td><strong>Travis CI</strong></td><td></td><td><a href="../ci-providers/travisci.md">travisci.md</a></td><td><a href="../../../.gitbook/assets/travis.png">travis.png</a></td></tr><tr><td><strong>Other CI Providers</strong></td><td></td><td><a href="../ci-providers/otherci.md">otherci.md</a></td><td><a href="../../../.gitbook/assets/other.png">other.png</a></td></tr></tbody></table>
