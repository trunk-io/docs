---
description: swiftlint is a linter for Swift
title: Trunk | How to run swiftlint
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

# swiftlint

[**swiftlint**](https://github.com/realm/SwiftLint#readme) is a linter for Swift.

You can enable the swiftlint linter with:

```shell
trunk check enable swiftlint
```

## Settings

**swiftlint** uses the same config files as the
upstream [swiftlint](https://github.com/realm/SwiftLint#readme) project, so you can continue to use any
existing configuration files (ex: `.swiftlint.yml`, `.swiftlint.yaml`, `.swiftlint`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/swiftlint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [swiftlint site](https://github.com/realm/SwiftLint#readme)
* swiftlint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/swiftlint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
