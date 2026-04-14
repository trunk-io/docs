---
title: Configuring phpunit
description: A guide for generating Trunk-compatible test reports for PHPUnit
---

# PHPUnit

You can automatically [detect and manage flaky tests](../../detection/) in your PHP projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To generate XML reports, append `--log-junit junit.xml` to your `phpunit` test command:

```undefined
phpunit ./tests --log-junit junit.xml
```

#### Report File Path

The JUnit report is written to the location specified by `--log-junit`. In the example above, the test results will be written to `./junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

PHPUnit doesn't support retries out of the box, but if you implemented retries, remember to disable them.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
