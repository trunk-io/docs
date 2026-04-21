---
title: Configuring minitest
description: A guide for generating Trunk-compatible test reports for minitest
---

# minitest

You can automatically [detect and manage flaky tests](../../detection/) in your minitest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Trunk detects flaky tests by analyzing test results automatically uploaded from your CI jobs. You can do this by generating Trunk-compatible XML reports from your test runs.

To generate XML reports, install the `minitest-reporters` gem:

```shell
gem install minitest-reporters
```

Configure the `JUnitReporter` reporter in your `test_helper.rb` file:

{% code title="test_helper.rb" %}
```ruby
require "minitest/reporters"
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter.new
```
{% endcode %}

#### Report File Path

You can specify a file path for your minitest results with the `MINITEST_REPORTERS_REPORTS_DIR` environment variable:

```sh
MINITEST_REPORTERS_REPORTS_DIR="./junit.xml" ruby -Ilib:test <FILES>
```

This will automatically write all test results to JUnit XML files in the `results` directory.

{% include "../../../.gitbook/includes/retries.md" %}

Minitest doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
