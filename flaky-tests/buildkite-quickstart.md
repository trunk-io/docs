# Buildkite Quickstart

### Getting Started

You can use the analytics test uploader within your Buildkite workflows to upload your test results.

{% hint style="info" %}
The trunk analytics test uploader currently only supports Linux x64. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

### Create workflow

Create a Buildkite workflow that runs the tests you want to monitor. In order for us to use the results, these tests **must** produces a test report in [**JUnit XML**](https://www.ibm.com/docs/en/developer-for-zos/14.1?topic=formats-junit-xml-format) format.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to Settings -> Manage -> Organization.  Copy your organization slug. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View." Store your trunk token in a [secret](https://buildkite.com/docs/pipelines/secrets) named `TRUNK_TOKEN`.&#x20;

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Setup Buildkite workflow

Update your Buildkite workflow to download and run the test uploader binary after you've run your tests:

#### Sample Buildkite workflow steps:

```
steps:
  - label: "Run tests"
    command: echo "hello world"
    key: tests
  - label: "Upload test results"
    commands:
      - "curl -fsSL --retry 3 https://trunk.io/releases/analytics-cli/latest -o ./trunk-analytics-uploader"
      - "chmod +x ./trunk-analytics-uploader"
      - "./trunk-analytics-uploader upload --junit-paths *.xml --org-url-slug trunk --token $$TRUNK_TOKEN"
    key: upload
    depends_on:
       - tests
```

{% hint style="info" %}
The `trunk-analytics-uploader` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument. The `--junit-paths` argument accepts the xml file locations as both a list of globs or absolute paths.
{% endhint %}

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
