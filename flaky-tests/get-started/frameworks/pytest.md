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

## Next Step

JUnit files generated with pytest are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.
