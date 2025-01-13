---
title: Configuring phpunit
description: A guide for generating Trunk-compatible test reports for PHPUnit
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

# PHPUnit

## 1. Generate JUnit

Append `--log-junit junit.xml` to your `phpunit` test command:

```undefined
phpunit ./tests --log-junit junit.xml
```

## 2. Output Location

The JUnit report is written to the location specified by `--log-junit`. In the example above, the test results will be written to `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

PHPUnit doesn't support retries out of the box, but if you implemented retries, remember to disable them.

## Next Step

JUnit files generated with PHPUnit are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
