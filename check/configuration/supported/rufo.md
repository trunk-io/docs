---
description: rufo is a linter for Ruby
title: Trunk | How to run rufo
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

# rufo

[**rufo**](https://github.com/ruby-formatter/rufo#readme) is a linter for Ruby.

You can enable the rufo linter with:

```shell
trunk check enable rufo
```

## Settings

**rufo** uses the same config files as the
upstream [rufo](https://github.com/ruby-formatter/rufo#readme) project, so you can continue to use any
existing configuration files (ex: `.rufo`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rufo) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [rufo site](https://github.com/ruby-formatter/rufo#readme)
* rufo Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rufo)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
