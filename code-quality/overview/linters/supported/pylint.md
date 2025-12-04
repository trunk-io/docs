---
title: Trunk | How to run Pylint
description: >-
  Learn about Pylint, the versatile Python linter for error detection, code
  smell elimination, and PEP 8 enforcement.
---

# Pylint

[**Pylint**](https://pypi.org/project/pylint/) is a linter for Python.

You can enable the Pylint linter with:

```shell
trunk check enable pylint
```

![pylint example output](../../../../.gitbook/assets/pylint.gif)

## Auto Enabling

Pylint will be auto-enabled if any of its config files are present: _`pylintrc`, `.pylintrc`_.

## Settings

Pylint supports the following config files:

* `pylintrc`
* `.pylintrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Usage Notes

You may specify additional pylint plugins in your `.pylintrc`, using the line `load-plugins=...`

If you want to run the plugin `pylint-django` as part of your setup, you would add the line `load-plugins=pylint_django` to your `.pylintrc`, but you **also** need to tell trunk to install the package:

```yaml
- pylint@2.11.0:
    packages:
      - pylint-django@2.4.4

```

## Links

* [Pylint site](https://pypi.org/project/pylint/)
* Pylint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/pylint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
