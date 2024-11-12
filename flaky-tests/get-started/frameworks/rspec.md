---
title: Configuring rspec
description: A guide for generating JUnit test reports for RSpec tests
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

## Next Step

JUnit files generated with RSpec are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
