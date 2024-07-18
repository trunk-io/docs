---
description: Configure Flaky Tests using any CI Provider
---

# Other CI Providers

## Getting Started

After running tests, you must upload your test results to Trunk. You can use the analytics uploader binary.

{% hint style="info" %}
The Trunk Flaky Tests Uploader currently only supports Linux x64 and macOS for Intel and Arm. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

Create a CI job that runs the tests you want to monitor and produces a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format. Be careful that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to Settings -> Manage -> Organization. Copy your organization slug. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View." Copy this token.

{% @supademo/embed demoid="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

After the test step, download and run the test uploader binary. Use the token and slug you copied above.

```bash
$ curl -fsSL --retry 3 "https://trunk.io/releases/analytics-cli/latest" -o ./trunk-analytics-uploader
$ chmod +x ./trunk-analytics-uploader
$ ./trunk-analytics-uploader upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}"
```

{% hint style="info" %}
The `trunk-analytics-uploader` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument.
{% endhint %}

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
