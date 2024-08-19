---
description: Configure Flaky Tests using any CI Provider
---

# Other CI Providers

## Getting Started

After running tests, you must upload your test results to Trunk. You can use the Flaky Tests CLI.

{% hint style="info" %}
The Trunk Flaky Tests CLI currently only supports x86_64 and arm64 for both Linux and macOS. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

Create a CI job that runs the tests you want to monitor and produces a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format. Be careful that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to Settings -> Manage -> Organization. Copy your organization slug. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View." Copy this token.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Add Uploader to Testing Workflow

After the test step, download and run the test uploader binary. Use the token and slug you copied above.

You can upload test results to Flaky Tests with the [`trunk-analytics-cli`](https://github.com/trunk-io/analytics-cli) by running
it in a stage after your tests are complete. There are four different OS/arch builds of the CLI in the latest release. Pick the
one you need for your testing platform and be sure to download the release on every CI run. **Do not bake the CLI into a
container or VM.** This ensures your CI runs are always using the latest build.

{% tabs %}


{% tab title="Linux x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```bash
$ curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
$ ./trunk-analytics-cli upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}"
```
{% endcode %}
{% endtab %}

{% tab title="Linux arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```bash
$ curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
$ ./trunk-analytics-cli upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}"
```
{% endcode %}
{% endtab %}

{% tab title="macOS x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```bash
$ curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
$ ./trunk-analytics-cli upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}"
```
{% endcode %}
{% endtab %}

{% tab title="macOS arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```bash
$ curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
$ ./trunk-analytics-cli upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}"
```
{% endcode %}
{% endtab %}

{% endtabs %}

{% hint style="info" %}
The `trunk-analytics-cli` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument.
{% endhint %}

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
