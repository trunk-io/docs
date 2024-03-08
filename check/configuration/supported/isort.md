---
description: isort is a Python utility for sorting imports alphabetically and automatically separating them into sections and by type. 
title: Trunk | How to run isort
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

## Settings

**isort** uses the same config files as the
upstream [isort](https://pycqa.github.io/isort/) project, so you can continue to use any
existing configuration files (ex: `.isort.cfg`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/isort) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [isort site](https://pycqa.github.io/isort/)
* isort Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/isort)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
