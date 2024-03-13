---
description: buf-format is a linter for Protobuf
title: Trunk | How to run buf-format
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

# buf-format

[**buf-format**](https://github.com/bufbuild/buf#readme) is a linter for Protobuf.

You can enable the buf-format linter with:

```shell
trunk check enable buf-format
```

## Auto Enabling

buf-format will never be auto-enabled. It must be enabled manually.

## Settings

buf-format supports the following config files:
* `buf.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [buf-format site](https://github.com/bufbuild/buf#readme)
- buf-format Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buf)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
