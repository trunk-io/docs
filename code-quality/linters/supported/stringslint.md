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

## Auto Enabling

stringslint will be auto-enabled if any of its config files are present: *`.stringslint.yml`, `.stringslint.yaml`, `.stringslint`*.

## Settings

stringslint supports the following config files:
* `.stringslint.yml`
* `.stringslint.yaml`
* `.stringslint`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.




## Links

- [stringslint site](https://github.com/dral3x/StringsLint#readme)
- stringslint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stringslint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
