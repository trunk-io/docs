---
description: standardrb is a linter for Ruby
title: Trunk | How to run standardrb
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

# standardrb

[**standardrb**](https://github.com/testdouble/standard#readme) is a linter for Ruby.

You can enable the standardrb linter with:

```shell
trunk check enable standardrb
```

## Settings

**standardrb** uses the same config files as the
upstream [standardrb](https://github.com/testdouble/standard#readme) project, so you can continue to use any
existing configuration files (ex: `.standard.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/standardrb) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [standardrb site](https://github.com/testdouble/standard#readme)
* standardrb Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/standardrb)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
