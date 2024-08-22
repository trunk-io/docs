---
description: swiftlint is a linter for Swift
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

## Auto Enabling

swiftlint will be auto-enabled if any of its config files are present: _`.swiftlint.yml`, `.swiftlint.yaml`, `.swiftlint`_.

## Settings

swiftlint supports the following config files:

* `.swiftlint.yml`
* `.swiftlint.yaml`
* `.swiftlint`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [swiftlint site](https://github.com/realm/SwiftLint#readme)
* swiftlint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/swiftlint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
