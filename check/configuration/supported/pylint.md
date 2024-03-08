---
description: Learn about Pylint, the versatile Python linter for error detection, code smell elimination, and PEP 8 enforcement.
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

# Pylint

**Pylint** is a linter for Python.

You can enable the Pylint plugin with

```shell
trunk check enable pylint
```

## Settings


**Pylint** uses the same config files as the
upstream [Pylint](https://pypi.org/project/pylint/) project, so you can continue to use any
existing configuration files (ex: `pylintrc`, `.pylintrc`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/pylint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

You may specify additional pylint plugins in your `.pylintrc`, using the line `load-plugins=...`

If you want to run the plugin `pylint-django` as part of your setup, you would add the line `load-plugins=pylint_django` to your `.pylintrc`, but you **also** need to tell trunk to install the package:

```yaml
- pylint@2.11.0:
    packages:
      - pylint-django@2.4.4

```




