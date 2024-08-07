---
title: Configuring bazel
description: Bazel is a scalable build and test system
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

Bazel is a testing framework for Bazel.

## Enabling XML Output
By default `bazel test` will output JUnit compatible XML.  If you are using gtest for your testing framework, Bazel is still in control of running the tests and will still produce XML output.  By default the XML output will go to `./bazel-testlogs/TEST_NAME/test.xml` along with the other test outputs.



## Test Suite Naming

By default `bazel test` will produce XML output in a file named `test.xml`You can override this default using the `XML_OUTPUT_FILE`variable. See the [Bazel Testing docs](https://bazel.build/reference/test-encyclopedia) for more information.



## Further Information
See an example of running Bazel inside of a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/bazel.yaml).


