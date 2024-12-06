---
title: Configuring swift-testing
description: A guide for generating JUnit test reports for Swift Test
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

# Swift Testing

## 1. Generate JUnit

Add the `--xunit-output` argument to your Swift test command:

```shell
swift test --xunit-output junit.xml
```

## 2. Output Location

The test results JUnit report will be written to the location specified by the `--xunit-output` argument. In the example above, it would be at `./junit.xml`.

## Next Step

JUnit files generated with Swift Test are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
