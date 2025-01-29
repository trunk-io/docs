---
title: Configuring minitest
description: A guide for generating Trunk-compatible test reports for minitest
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# minitest

## 1. Generate JUnit&#x20;

Install the `minitest-reporters` gem:

```shell
gem install minitest-reporters
```

Configure the `JUnitReporter` reporter in your `test_helper.rb` file:

{% code title="test_helper.rb" %}
```ruby
require "minitest/reporters"
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter.new(:reports_dir => "results")
```
{% endcode %}

## 2. Output Location

This will automatically write all test results to JUnit XML files in the `results` directory.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Minitest doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

## Next Step

JUnit files generated with `minitest` are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
