---
title: Configuring minitest
description: A guide for generating JUnit test reports for minitest tests
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

```ruby
require "minitest/reporters"
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter.new(:reports_dir => "results")
```

## 2. Output Location

This will automatically write all test results to JUnit XML files in the `results` directory.

## Next Step

JUnit files generated with `minitest` are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
