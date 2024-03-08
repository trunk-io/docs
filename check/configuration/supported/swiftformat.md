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

## Settings

**swiftformat** uses the same config files as the
upstream [swiftformat](https://github.com/nicklockwood/SwiftFormat#readme) project, so you can continue to use any
existing configuration files (ex: `.swiftformat`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/swiftformat) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [swiftformat site](https://github.com/nicklockwood/SwiftFormat#readme)
* swiftformat Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/swiftformat)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
