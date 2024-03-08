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

**swiftlint** is a linter for Swift.

You can enable the swiftlint plugin with

```shell
trunk check enable swiftlint
```

## Settings


swiftlint uses the same config files as the
upstream [swiftlint](https://github.com/realm/SwiftLint#readme) project, so you can continue to use any
existing configuration files (ex: `.swiftlint.yml`, `.swiftlint.yaml`, `.swiftlint`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/swiftlint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
