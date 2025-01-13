---
title: Configuring rspec
description: A guide for generating Trunk-compatible test reports for RSpec
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

# RSpec

## 1. Generate JUnit

Install the gem:

```shell
gem install rspec_junit_formatter
```

Use it:

```shell
rspec --format RspecJunitFormatter --out junit.xml
```

## 2. Output Location

The JUnit report will be written to the location specified by the `--out` argument. In the example above, the report would be at `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

If you have a step in CI to rerun failed tests with the `--only-failures` option, or you're using a package like [rspec-retry](https://github.com/NoRedInk/rspec-retry), remember to disable them.

## Next Step

JUnit files generated with RSpec are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
