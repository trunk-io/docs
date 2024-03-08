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

## Auto Enabling

pyright will be auto-enabled if any of its config files are present: *`pyrightconfig.json`*

## Settings

pyright supports the following config files:
* `pyrightconfig.json`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [pyright site](https://github.com/microsoft/pyright)
- pyright Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/pyright)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
