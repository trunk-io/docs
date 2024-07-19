---
description: buf-breaking is a linter for Protobuf
title: Trunk | How to run buf-breaking
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

# buf-breaking

[**buf-breaking**](https://github.com/bufbuild/buf#readme) is a linter for Protobuf.

You can enable the buf-breaking linter with:

```shell
trunk check enable buf-breaking
```

## Auto Enabling

buf-breaking will never be auto-enabled. It must be enabled manually.

## Settings

buf-breaking supports the following config files:
* `buf.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [buf-breaking site](https://github.com/bufbuild/buf#readme)
- buf-breaking Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buf)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
