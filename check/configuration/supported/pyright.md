---
description: pyright is a linter for Python
title: Trunk | How to run pyright
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

# pyright

[**pyright**](https://github.com/microsoft/pyright) is a linter for Python.

You can enable the pyright linter with:

```shell
trunk check enable pyright
```

## Settings

**pyright** uses the same config files as the
upstream [pyright](https://github.com/microsoft/pyright) project, so you can continue to use any
existing configuration files (ex: `pyrightconfig.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/pyright) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [pyright site](https://github.com/microsoft/pyright)
* pyright Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/pyright)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
