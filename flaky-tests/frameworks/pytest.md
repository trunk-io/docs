---
title: Configuring pytest
description: pytest is a testing framework for Python that can be configured to output XML
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

# pytest

## How to output test results to upload to Trunk

pytest can produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by running with the `--junit-xml=` option.

```shell
pytest --junit-xml=report.xml 
```

## Test Suite Naming

**pytest** will automatically fill in values for the `<testcase/>` and `<testsuite/>` `name` and `classname` attributes.&#x20;

```python
def test_95_percent():
    random_number = secrets.randbelow(100)
    assert random_number <= 95
```

would produce output that looks like this:

```xml
<testsuites>
    <testsuite name="pytest">
        <testcase classname="random_test" 
                  name="test_95_percent"
                  file="python/pytest/random_test.py"
                  />
     ...
</testsuites>
```

The suite name [can be configured](https://docs.pytest.org/en/7.2.x/how-to/output.html) in the `pytest.ini` or [similar config file](https://docs.pytest.org/en/8.1.x/reference/customize.html#pytest-ini).

```ini
[pytest]
junit_suite_name = my_suite
```

Configuring other XML output values is not currently supported, but experimental options are [available](https://docs.pytest.org/en/7.2.x/how-to/output.html#record-xml-attribute).  To include the test filenames in the XML output, use the `-o junit_family=xunit1` option.

```shell
pytest --junitxml=output/path.xml -o junit_family=xunit1
```

By default, **pytest** will include the `file` attribute in the output XML.

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
