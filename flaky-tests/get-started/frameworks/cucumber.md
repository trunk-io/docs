---
title: Configuring cucumber
description: A guide for generating JUnit test reports for Cucumber tests
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

# Cucumber

## 1. Generate JUnit

Add `--format junit:path/to/junit/output` to your cucumber test command line. For example:

```bash
cucumber tests/test.feature --format junit:output/report.xml
```

## 2. Output Location

JUnit files will be written according to the path passed to the `--format` option. In the above example, a JUnit file will be written to `output/report.xml`.

## Next Step

JUnit files generated with Cucumber are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.
