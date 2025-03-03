---
title: Configuring pytest
description: A guide for generating Trunk-compatible test reports for Pytest
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

# pytest

## 1. Generate JUnit

Add the `--junit-xml` and `junit_family=xunit1` argument to your `pytest` command:

```shell
pytest --junit-xml=junit.xml -o junit_family=xunit1
```

This `--junit-xml` argument specifies the path of the JUnit report and `junit_family=xunit1` is required for file paths to be reported.&#x20;

## 2. Output Location

The JUnit report will be written to the location specified by the `--junit-xml` argument. In the example above, it would be at `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the [ `--lf` or `--ff` options](https://docs.pytest.org/en/stable/how-to/cache.html) if you've previously configured your CI with these options to disable retries.

## Next Step

JUnit files generated with pytest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
