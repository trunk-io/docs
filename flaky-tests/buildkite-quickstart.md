# Buildkite Quickstart

You can use the analytics uploader binary to upload test your test results.

{% hint style="info" %}
The trunk analytics uploader currently only supports Linux x64. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io).
{% endhint %}

1. Create a CI job that runs the tests you want to monitor. In order for us to use the results, these tests **must** produces a test report in [**JUnit XML**](https://www.ibm.com/docs/en/developer-for-zos/14.1?topic=formats-junit-xml-format) format.
{% hint style="info" %}
For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}
2. Store your trunk token in a [secret](https://buildkite.com/docs/pipelines/secrets) name `TRUNK_TOKEN`
3. Update your Buildkite workflow to download and run the test uploader binary after you've executed your tests:
```

steps:
  - label: "Installing Trunk"
    commands:
      - "curl -fsSL --retry 3 https://trunk.io/releases/analytics-cli/latest -o ./trunk-analytics-uploader"
      - "chmod +x ./trunk-analytics-uploader"
    key: download

  - label: "Run tests"
    command: <YOUR TESTS HERE>
    key: tests
    depends_on: download_uploader

  - label: "Upload test results"
    command: "./trunk-analytics-uploader upload --junit-paths <JUNIT PATHS> --org-url-slug <ORG SLUG> --token $$TRUNK_TOKEN"
    key: upload
    depends_on:
       - tests
       - download_uploader
```

{% hint style="info" %}
The `trunk-analytics-uploader` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument.
The `--junit-paths` argument accepts the xml file locations as both a list of globs or absolute paths.
{% endhint %}

3. To find your organization slug, you can open [app.trunk.io](http://app.trunk.io). Once logged in, you should be automatically redirected to a URL like [https://app.trunk.io/**my-org-slug**/repo-owner/repo-name/ci-analytics](https://app.trunk.io/my-org-slug/repo-owner/repo-name/ci-analytics).
4. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View."

***

The uploader action uploads the following environment variables from Buildkite:

**Buildkite**: `BUILDKITE_BRANCH`, `BUILDKITE_BUILD_ID`, `BUILDKITE_BUILD_NUMBER`, `BUILDKITE_BUILD_URL`, `BUILDKITE_COMMIT`, `BUILDKITE_JOB_ID`, `BUILDKITE_LABEL`, `BUILDKITE_ORGANIZATION_SLUG`, `BUILDKITE_PIPELINE_ID`, `BUILDKITE_PIPELINE_SLUG`, `BUILDKITE_PROJECT_SLUG`, `BUILDKITE_PULL_REQUEST`, `BUILDKITE_PULL_REQUEST_BASE_BRANCH`, `BUILDKITE_PULL_REQUEST_REPO`, `BUILDKITE_REBUILT_FROM_BUILD_ID`, `BUILDKITE_REBUILT_FROM_BUILD_NUMBER`, `BUILDKITE_REPO`, `BUILDKITE_RETRY_COUNT`, `BUILDKITE_TAG`.
