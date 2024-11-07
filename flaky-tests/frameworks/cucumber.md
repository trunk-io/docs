---
title: Configuring cucumber
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

## How to output test results to upload to Trunk

Cucumber can be configured to produce [JUnit compatible XML](https://github.com/testmoapp/junitxml), that Trunk can ingest, from the command line with the `--format` command line option. For example, to print the report at `output/report.xml`, use a command line like this:

```shell
cucumber tests/test.feature --format junit:output/report.xml
```

## Test Suite Naming

Cucumber's JUnit report formatter has limited configuration options, but does let you set the `testsuite`s `name` attribute. You can set the suite name in the config file or on the command line:

```shell
cucumber --format junit:report.xml --format-options='{"junit": {"suiteName":"mySuite"} }'
```

The `--format-options` setting **must** be JSON that is escaped using single quotes. For more details see the [Cucumber Reporting documentation](https://cucumber.io/docs/cucumber/reporting/?lang=java).

## Next Step

Once youv'e configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
