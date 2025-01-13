---
title: Configuring swift-testing
description: A guide for generating Trunk-compatible test reports with Swift Testing
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

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Swift Testing doesn't support retries out of the box, but if you implemented retries or imported a package, remember to disable them.

## Next Step

JUnit files generated with Swift Test are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
