---
description: A guide for generating Trunk-compatible test reports for Behave
---

# Behave

You can automatically [detect and manage flaky tests](../../detection/) in your projects running Behave by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. Behave can output JUnit XML reports which are compatible with Trunk. You can do so with the `--junit` option:

```sh
behave --junit
```

#### Report File Path

You can customize the file path of the reports using the `--junit-directory` option.

```sh
behave --junit --junit-directory ./junit-reports
```

Behave outputs multiple XML reports under the JUnit directory. You can locate these when uploading the reports in CI with the `"./junit-reports/*.xml"` glob.

{% include "../../../.gitbook/includes/retries.md" %}

You must remove the [rerun formatter](https://behave.readthedocs.io/en/latest/formatters/#formatters) from your `behave.ini` file if it is being used to automatically rerun failed tests.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
