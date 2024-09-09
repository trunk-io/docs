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

XCTest is a testing framework for Apple.

### Enabling XML Output

Test written in ObjectiveC and Swift projects using the XCTest framework can be run from the command line with `xcodebuild`. Unfortunately it only produces output in XCodes internal proprietary format. `xcodebuild` can produce JUnit compatible XML output using the [xcbeautify](https://github.com/cpisciotta/xcbeautify) open source tool.

Install it on macOS with Homebrew. Alternative installation instructions [here](https://github.com/cpisciotta/xcbeautify?tab=readme-ov-file#installation).

```shell
brew install xcbeautify
```
Then pipe the output of xcodebuild to xcbeautify with the `--report junit` option.

```shell
xcodebuild test -scheme Testo2 | xcbeautify --report junit 
```
This will produce a `build/reports/junit.xml` output file.



### Test Suite Naming

`xcbeautify` will use the name of file the tests are in as the name of the output `<testsuite>` and the function name as the `name` attribute of each `<testcase>` element.





