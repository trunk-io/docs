---
description: pytest is a testing framework for Python that can be configured to output XML
title: Configuring pytest
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

pytest is a testing framework for Python.

# Enabling XML Output
pytest can produce [JUnit XML](https://github.com/testmoapp/junitxml) output by running with the `--junit-xml=` option.

```shell
pytest --junit-xml=filepath.xml 
```


# Test Suite Naming

**pytest** will automatically fill in values for the _<testcase>_ and _<testsuite>_ `name` and `classname` attributes. 

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
                  name="test_95_percent"/>
     ...
</testsuites>
```
The suite name [can be configured](https://docs.pytest.org/en/7.2.x/how-to/output.html) in the `pytest.ini` or [similar config file](https://docs.pytest.org/en/8.1.x/reference/customize.html#pytest-ini). 

```ini
[pytest]
junit_suite_name = my_suite
```
Configuring other XML output values is not currently supported, but experimental options are [available](https://docs.pytest.org/en/7.2.x/how-to/output.html#record-xml-attribute).  To include the test filenames in the XML output, use the `-o junit_family=xunit1` option.

```shell
pytest --junitxml=output/path.xml -o junit_family=xunit1
```




## Further Information
See an example of running **pytest** in a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/python-tests.yaml#L34).


