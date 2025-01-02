---
title: Configuring pytest
description: A guide for generating JUnit test reports for pytest tests
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

Add the `--junit-xml` argument to your pytest command:

```shell
pytest --junit-xml=junit.xml 
```

## 2. Output Location

The test results JUnit report will be written to the location specified by the `--junit-xml` argument. In the example above, it would be at `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the [ `--lf` or `--ff` options](https://docs.pytest.org/en/stable/how-to/cache.html) if you've previously configured your CI with these options to disable retries.

## Next Step

JUnit files generated with pytest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
