---
title: Configuring Go
description:  Go Testing is a test runner for the Go language
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

Go Testing is a test runner for the Go language.

## Enabling XML Output
Go can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by installing the [gotestsum](https://github.com/gotestyourself/gotestsum) package and using that instead of `go test`.

1. Install gotestsum

```shell
go install gotest.tools/gotestsum@latest
```

2. Use gotestsum to run your tests with JUnit XML outputs:
```
gotestsum --junitfile junit.xml ./...
```

## Further Information
- [gotestsum documentation](https://github.com/gotestyourself/gotestsum)

