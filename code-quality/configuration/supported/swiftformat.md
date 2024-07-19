---
description: swiftformat is a linter for Swift
title: Trunk | How to run swiftformat
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

# swiftformat

[**swiftformat**](https://github.com/nicklockwood/SwiftFormat#readme) is a linter for Swift.

You can enable the swiftformat linter with:

```shell
trunk check enable swiftformat
```

## Auto Enabling

swiftformat will be auto-enabled if a `.swiftformat` config file is present.

## Settings

swiftformat supports the following config files:
* `.swiftformat`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [swiftformat site](https://github.com/nicklockwood/SwiftFormat#readme)
- swiftformat Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/swiftformat)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
