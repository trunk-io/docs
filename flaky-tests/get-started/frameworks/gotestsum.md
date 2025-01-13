---
title: Configuring gotestsum
description: A guide for generating Trunk-compatible test reports for Go tests
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

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.\
\
If you're using a package like [**retry**](https://pkg.go.dev/github.com/hashicorp/consul/sdk/testutil/retry), disable it to get more accurate results from Trunk.

## Next Step

JUnit files generated with `gotestsum` are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
