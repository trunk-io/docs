---
title: Configuring cucumber
description: null
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

# Cucumber

Cucumber is a testing framework for all.

### Enabling XML Output

Cucumber has built in support for producing [JUnit compatible XML output](https://github.com/testmoapp/junitxml). It can be enabled from the command line with the `--format` command line option. To generate the report file at `output/report.xml` use a command line like this:

```shell
cucumber tests/test.feature --format junit:output/report.xml
```

### Test Suite Naming

Cucumber's JUnit report formatter has limited configuration, but it does let you set the `testsuite`s `name` attribute. You can set it in the config file or on the command line like this:

```shell
cucumber --format junit:out.xml --format-options='{"junit": {"suiteName":"mySuite"} }'
```
The `--format-options` setting must be JSON  that is escaped using single quotes. For more details see the [Cucumber Reporting documentation](https://cucumber.io/docs/cucumber/reporting/?lang=java).


