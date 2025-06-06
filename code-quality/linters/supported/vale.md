---
title: Trunk | How to run vale
description: vale is a linter for prose
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

# vale

[**vale**](https://vale.sh/) is a linter for prose.

You can enable the vale linter with:

```shell
trunk check enable vale
```

## Auto Enabling

vale will be auto-enabled if a `.vale.ini` config file is present.

## Settings

vale supports the following config files:

* `.vale.ini`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `.vale.ini` if your project does not already have one.

## Links

* [vale site](https://vale.sh/)
* vale Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/vale)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
