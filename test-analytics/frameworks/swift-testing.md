---
title: Configuring swift-testing
description: a testing framework for pure Swift applications and libraries.
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

Swift Testing is a testing framework for Apple platforms.

## Enabling XML Output
Swift testing has built in XUnit XML reporting support. When you run your tests from the command line add `--xunit-output report.xml`to output an XML report to a file. Ex:

```swift
import Testing

@Test func helloworld() {
    let greeting = "hello, world!"
    #expect(greeting == "hello, worldz!")
}
```
```shell
swift test --xunit-output report.xml
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
  <testsuite name="TestResults" errors="0" tests="1" failures="1" time="0.001664833">
    <testcase classname="MyCLITests" name="helloworld()" time="0.000832083">
      <failure message="Expectation failed: (greeting &#8594; &quot;hello, world!&quot;) == &quot;hello, worldz!&quot;" />
    </testcase>
  </testsuite>
</testsuites>

```


## Test Suite Naming

The format of Swift Testing's XML output is intended to match XCTests, which does not support changing test names using the `@Suite` and `@Test` description parameters. However, Swift Testing is in the process of building a more flexible, JSON-based output mechanism which includes, among other data, the display names for tests. For more information about this feature see this [issue](https://github.com/apple/swift-testing/pull/479).







