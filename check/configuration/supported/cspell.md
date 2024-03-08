---
description: cspell is a linter for All
title: Trunk | How to run cspell
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

# cspell

[**cspell**](https://github.com/streetsidesoftware/cspell#readme) is a linter for All.

You can enable the cspell linter with:

```shell
trunk check enable cspell
```

## Settings

**cspell** uses the same config files as the
upstream [cspell](https://github.com/streetsidesoftware/cspell#readme) project, so you can continue to use any
existing configuration files (ex: `.cspell.json`, `cspell.json`, `.cSpell.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/cspell) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [cspell site](https://github.com/streetsidesoftware/cspell#readme)
* cspell Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/cspell)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
