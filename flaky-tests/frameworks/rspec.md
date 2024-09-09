---
title: Configuring rspec
description: RSpec is a unit test runner for Ruby code
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
# RSpec

RSpec is a testing framework for Ruby.

### Enabling XML Output
RSpec can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by installing the `rspec_junit_formatter `module. 

```shell
gem install rspec_junit_formatter
```
Add the formatter to your command line like this:

```shell
rspec src --format RspecJunitFormatter
```


### Test Suite Naming

The output file can be set with the `--out` option like this:

```shell
rspec src --format RspecJunitFormatter --out rspec_test.xml
```
By default, RSpec will include the `file` attribute in the output XML like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="rspec" tests="3" skipped="0" failures="1" errors="0">
  <testcase classname="ruby.rspec.spec.calculator_spec" 
            name="Calculator.halve given the number 3 returns 1.5" 
            file="./ruby/rspec/spec/calculator_spec.rb" 
            time="0.010126">
            <failure message="
expected: 1.5
     got: 1

(compared using ==)
" type="RSpec::Expectations::ExpectationNotMetError">Failure/Error: expect(Calculator.halve(3)).to eq(1.5)

  expected: 1.5
       got: 1

  (compared using ==)
./ruby/rspec/spec/calculator_spec.rb:25:in `block (4 levels) in &lt;top (required)&gt;&apos;</failure>
  </testcase>
</testsuite>

```




## Further Information
See an example of using RSpec in a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/ruby-tests.yaml#L22).


