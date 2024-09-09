---
title: Configuring gotestsum
description: gotestsum is a test reporter for the Go programming language
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
# gotestsum

gotestsum is a testing framework for Go.

### Enabling XML Output
Since `go test` does not support XML output directly, you can use [**gotestsum**](https://github.com/gotestyourself/gotestsum) to convert the native output to [JUnit XML](https://github.com/testmoapp/junitxml). First install it with

```shell
go install gotest.tools/gotestsum@latest
```
Then run your tests with

```shell
gotestsum --junitfile gotestsum_test.xml
```


### Test Suite Naming

**gotestsum** produces JUnit XML with the name and classname fields set by the function name and classnames being tested. For example, this function in the module `example/hello`

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
produces XML that looks like this:

```xml
<testsuites tests="1" failures="1" errors="0" time="0.555454">
    <testsuite tests="1" failures="1" time="0.363000" name="example/hello" timestamp="2024-08-06T14:25:47-07:00">
        <properties>
            <property name="go.version" value="go1.22.5 darwin/arm64"></property>
        </properties>
        <testcase classname="example/hello" name="TestHelloName" time="0.000000">
            <failure message="Failed" type="">=== RUN   TestHelloName&#xA;
                hello_test.go:17: Hello(&#34;Gladys&#34;) = &#34;
                Hail, Gladysx! Well met!&#34;, &lt;nil&gt;, want 
                match for `\bGladys\b`, nil&#xA;--- FAIL: TestHelloName (0.00s)
                </failure>
        </testcase>
    </testsuite>
</testsuites>

```






