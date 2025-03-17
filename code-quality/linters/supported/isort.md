---
title: Trunk | How to run isort
description: >-
  isort is a Python utility for sorting imports alphabetically and automatically
  separating them into sections and by type.
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

# isort

[**isort**](https://pycqa.github.io/isort/) is a formatter for Python.

You can enable the isort formatter with:

```shell
trunk check enable isort
```

![isort example output](../../../.gitbook/assets/isort.gif)

## Auto Enabling

isort will be auto-enabled if any _Python_ files are present.

## Settings

isort supports the following config files:

* `.isort.cfg`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `.isort.cfg` if your project does not already have one.

## Links

* [isort site](https://pycqa.github.io/isort/)
* isort Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/isort)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
