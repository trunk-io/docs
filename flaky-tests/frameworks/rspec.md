---
description: RSpec is a unit test runner for Ruby code
title: Configuring rspec
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

RSpec is a testing framework for Ruby.

# Enabling XML Output
RSpec can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by installing the `rspec_junit_formatter `module. 

```shell
gem install rspec_junit_formatter
```
Add the formatter to your command line like this:

```shell
rspec src --format RspecJunitFormatter
```


# Test Suite Naming

The output file can bet set with the `--out` option like this:

```undefined
rspec src --format RspecJunitFormatter --out rspec_test.xml
```


## Further Information
See an example of using RSpec in a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/ruby-tests.yaml#L22).


