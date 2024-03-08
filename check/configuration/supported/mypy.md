---
description: mypy is a linter for Python
title: Trunk | How to run mypy
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

# mypy

[**mypy**](https://github.com/python/mypy#readme) is a linter for Python.

You can enable the mypy linter with:

```shell
trunk check enable mypy
```

## Settings

**mypy** uses the same config files as the
upstream [mypy](https://github.com/python/mypy#readme) project, so you can continue to use any
existing configuration files (ex: `mypy.ini`, `.mypy.ini`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/mypy) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [mypy site](https://github.com/python/mypy#readme)
* mypy Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/mypy)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
