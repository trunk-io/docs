---
title: Configuring xctest
description: XCTest unit test framework for XCode and xcodebuild
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

# XCTest

## Enabling XML Output

Test written in ObjectiveC and Swift projects using the XCTest framework can be run from the command line with `xcodebuild`. By default it only produces output in XCode's internal proprietary format. Using the [xcbeautify](https://github.com/cpisciotta/xcbeautify) open source tool, `xcodebuild` can produce JUnit compatible XML output that Trunk can ingest.

Install **xcbeautify** it on macOS with Homebrew. Alternative installation instructions [here](https://github.com/cpisciotta/xcbeautify?tab=readme-ov-file#installation).

```shell
brew install xcbeautify
```

Then pipe the output of xcodebuild to xcbeautify with the `--report junit` option.

```shell
xcodebuild test -scheme Testo2 | xcbeautify --report junit 
```

This will produce a `build/reports/junit.xml` output file.

## Test Suite Naming

`xcbeautify` will use the name of file the tests are in as the name of the output `<testsuite>` and the function name as the `name` attribute of each `<testcase>` element.

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.