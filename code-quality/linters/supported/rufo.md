---
description: rufo is a linter for Ruby
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

## Auto Enabling

rufo will be auto-enabled if a `.rufo` config file is present.

## Settings

rufo supports the following config files:

* `.rufo`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [rufo site](https://github.com/ruby-formatter/rufo#readme)
* rufo Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rufo)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
