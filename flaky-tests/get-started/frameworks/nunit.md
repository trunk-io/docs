---
description: A guide for generating Trunk-compatible test reports for NUnit
---

# NUnit

You can automatically [detect and manage flaky tests](../../detection/) in your NUnit projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

You can do this in dotnet with the NUnit's built-in JUnit reporter:

```sh
dotnet test -o build  -- NUnit.TestOutputXml="junit"
```

#### Report File Path

.NET will output each build to the path specified by `-o <BUILD_PATH>` and test results under a sub-folder of `<BUILD PATH>/test-reports`, specified by the `-- NUnit.TestOutputXml="<XML PATH>"` option.

In the example command from the [Generating Reports step](nunit.md#generating-reports), the XMLs will be located under `./build/test-reports/junit/*.xml`. This is also the glob you'll use to locate the results when uploading test results.

{% include "../../../.gitbook/includes/retries.md" %}

Omit `[Retry(n)]` from tests to disable retries.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
