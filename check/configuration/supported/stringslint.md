---
description: stringslint is a linter for Swift
title: Trunk | How to run stringslint
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

# stringslint

[**stringslint**](https://github.com/dral3x/StringsLint#readme) is a linter for Swift.

You can enable the stringslint linter with:

```shell
trunk check enable stringslint
```

## Settings

**stringslint** uses the same config files as the
upstream [stringslint](https://github.com/dral3x/StringsLint#readme) project, so you can continue to use any
existing configuration files (ex: `.stringslint.yml`, `.stringslint.yaml`, `.stringslint`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/stringslint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [stringslint site](https://github.com/dral3x/StringsLint#readme)
* stringslint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stringslint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
