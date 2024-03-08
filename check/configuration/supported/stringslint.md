---
description: stringslint is a linter for Swift
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

**stringslint** is a linter for Swift.

You can enable the stringslint plugin with

```shell
trunk check enable stringslint
```

## Settings


stringslint uses the same config files as the
upstream [stringslint](https://github.com/dral3x/StringsLint#readme) project, so you can continue to use any
existing configuration files (ex: `.stringslint.yml`, `.stringslint.yaml`, `.stringslint`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/stringslint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
