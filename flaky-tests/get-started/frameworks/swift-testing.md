---
title: Configuring swift-testing
description: A guide for generating Trunk-compatible test reports with Swift Testing
---

# Swift Testing

You can automatically [detect and manage flaky tests](../../detection/) in your Swift projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To output a compatible report, add the `--xunit-output` argument to your Swift test command:

```shell
swift test --xunit-output junit.xml --parallel
```

Due to a [known bug](https://github.com/swiftlang/swift-package-manager/issues/4752) with Swift, you must include the `--parallel` flag for the XML report to output properly.

#### Report File Path

The test report will be written to the location specified by the `--xunit-output` argument. In the example above, it would be at `./junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

Swift Testing doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
