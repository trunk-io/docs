---
title: Configuring go-junit-report
description: go-junit-report is a test reporter for the Go programming language
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
# go-junit-report

go-junit-report is a testing framework for Go.

### Enabling XML Output
go-junit-report converts the output of `go test` to [JUnit compatible XML](https://github.com/testmoapp/junitxml). First install it with

```shell
go install github.com/jstemmer/go-junit-report/v2@latest
```
then run it from inside your go project like this:

```shell
go test -v 2>&1 ./... | go-junit-report -set-exit-code > report.xml
```


### Test Suite Naming

[go-junit-report](https://github.com/jstemmer/go-junit-report) produces JUnit XML with the name and classname fields set by the function name and classnames being tested. For example, this function in the module `example/hello`

```go
func TestHelloName(t *testing.T) {
    name := "Gladys"
    want := regexp.MustCompile(`\b`+name+`\b`)
    msg, err := Hello("Gladysx")
    if !want.MatchString(msg) || err != nil {
        t.Fatalf(`Hello("Gladys") = %q, %v, want match for %#q, nil`, msg, err, want)
    }
}
```
will produce XML output that looks like:

```xml
<testsuites tests="1" failures="1">
  <testsuite name="example/hello" tests="1" failures="1" errors="0" id="0" hostname="Joshs-MacBook-Air.local" time="0.386" timestamp="2024-08-06T11:51:57-07:00">
    <testcase name="TestHelloName" classname="example/hello" time="0.000">
      <failure message="Failed"><![CDATA[    hello_test.go:17: Hello("Gladys") = "Great to see you, Gladysx!", <nil>, want match for `\bGladys\b`, nil]]></failure>
    </testcase>
  </testsuite>
</testsuites>

```






