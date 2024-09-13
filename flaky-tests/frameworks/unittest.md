---
title: Configuring unittest
description: unittest is a testing framework built into the Python standard library.
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

# unittest

unittest is a testing framework for Python.

### Enabling XML Output

Though unittest is a part of the standard Python library, it does not support [JUnit XML](https://github.com/testmoapp/junitxml) output. However [**pytest**](https://trunk.io/testing/pytest), another Python unit testing framework, supports running unittest tests [out of the box](https://docs.pytest.org/en/6.2.x/unittest.html).

pytest can produce output by running with the `--junit-xml=` option.

```shell
pytest --junit-xml=filepath.xml 
```

### Test Suite Naming

**pytest** will automatically fill in values for the and `name` and `classname` attributes.&#x20;

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

## Further Information

See an example of running **pytest** in a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/python-tests.yaml#L34).
