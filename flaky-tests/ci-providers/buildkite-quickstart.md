---
description: Configure Flaky Tests using BuildKite
---

# Buildkite

### Getting Started

You can use the Trunk Analytics CLI within your Buildkite workflows to upload your test results.

{% hint style="info" %}
The Trunk Flaky Tests CLI currently only supports x86\_64 and arm64 for both Linux and macOS. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

### Create workflow

Create a Buildkite workflow that runs the tests you want to monitor. In order for us to use the results, these tests **must** produce a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to **Settings** -> **Manage** -> **Organization**. Copy your organization slug. You can find your Trunk token by navigating to **Settings** → **Manage** **Organization** → **Organization API Token** and clicking "View." Store your Trunk token in a [secret](https://buildkite.com/docs/pipelines/secrets) named `TRUNK_TOKEN`.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Setup Buildkite workflow

You can upload test results to Flaky Tests with the [`trunk-analytics-cli`](https://github.com/trunk-io/analytics-cli) by running it in a stage after your tests are complete. There are four different OS/arch builds of the CLI in the latest release. Pick the one you need for your testing platform and be sure to download the release on every CI run. **Do not bake the CLI into a container or VM.** This ensures your CI runs are always using the latest build.

#### Sample Buildkite workflow steps:

{% tabs %}
{% tab title="Linux x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
        - ./trunk-analytics-cli upload --junit-paths *.xml --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endcode %}
{% endtab %}

{% tab title="Linux arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
        - ./trunk-analytics-cli upload --junit-paths *.xml --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endcode %}
{% endtab %}

{% tab title="macOS x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
        - ./trunk-analytics-cli upload --junit-paths *.xml --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endcode %}
{% endtab %}

{% tab title="macOS arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
        - ./trunk-analytics-cli upload --junit-paths *.xml --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The `trunk-analytics-cli` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument. The `--junit-paths` argument accepts the xml file locations as both a list of globs or absolute paths.
{% endhint %}

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
