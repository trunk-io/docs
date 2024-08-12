---
description: Configure Flaky Tests using BuildKite
---

# Buildkite

### Getting Started

You can use the analytics test uploader within your Buildkite workflows to upload your test results.

{% hint style="info" %}
The Trunk Flaky Tests Uploader currently only supports Linux x64 and macOS for Intel and Arm. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

### Create workflow

Create a Buildkite workflow that runs the tests you want to monitor. In order for us to use the results, these tests **must** produces a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to **Settings** -> **Manage** -> **Organization**. Copy your organization slug. You can find your Trunk token by navigating to **Settings** → **Manage** **Organization** → **Organization API Token** and clicking "View." Store your Trunk token in a [secret](https://buildkite.com/docs/pipelines/secrets) named `TRUNK_TOKEN`.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" fullWidth="true" %}

### Setup Buildkite workflow

You can upload test results to Flaky Tests with the [`trunk-analytics-uploader`](https://github.com/trunk-io/analytics-uploader) by running it in a stage after your tests are complete. There are five different OS/arch builds of the uploader in the latest release. Pick the one you need for your testing platform and be sure to download the release on every CI run. **Do not bake the CLI into a container or VM**. This ensures your CI runs are always using the latest build.

Right click and copy the appropriate link from this table.

| CPU Architecture    | Link                                                                                                                                                   |
|---------------------| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| macOS Intel         | [x68\_64-apple-darwin](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86\_64-apple-darwin.tar.gz)             |
| macOS Apple Silicon | [aarch64-apple-darwin](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-apple-darwin.tar.gz)             |
| Arm64 Linux         | [aarch64-unknown-linux-musl](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-unknown-linux-musl.tar.gz) |
| Intel Linux         | [x86\_64-unknown-linux-musl](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86\_64-unknown-linux-musl.tar.gz) |

#### Sample Buildkite workflow steps:

```
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - curl -fsSL --retry 3 "UPLOADER_LINK" -o ./trunk-analytics-uploader
      - chmod +x ./trunk-analytics-uploader
      - ./trunk-analytics-uploader upload --junit-paths *.xml --org-url-slug trunk --token $$TRUNK_TOKEN
    key: upload
    depends_on:
       - tests
```

{% hint style="info" %}
The `trunk-analytics-uploader` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument. The `--junit-paths` argument accepts the xml file locations as both a list of globs or absolute paths.
{% endhint %}

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
