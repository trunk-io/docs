---
title: Configuring gotestsum
description: A guide for generating JUnit test reports for Go tests
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

# Go

## 1. Generate JUnit

Download `gotestsum` from [releases](https://github.com/gotestyourself/gotestsum/releases), or build from source with `go install gotest.tools/gotestsum@latest`.

Add the `--junitfile` argument to your `gotestsum` test command:

```bash
gotestsum --junitfile junit.xml
```

## 2. Output Location

`gotestsum` will write a JUnit test report to the file specified by the `--junitfile` argument. In the example above, the JUnit report would be written to `junit.xml`.

## Next Step

JUnit files generated with `gotestsum` are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.
