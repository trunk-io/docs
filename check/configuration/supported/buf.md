---
description: buf is a linter for Protobuf
title: Trunk | How to run buf
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

# buf

[**buf**](https://github.com/bufbuild/buf#readme) is a linter for Protobuf.

You can enable the buf linter with:

```shell
trunk check enable buf
```

## Auto Enabling

buf will never be auto-enabled. It must be enabled manually.

## Settings

buf supports the following config files:
* `buf.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [buf site](https://github.com/bufbuild/buf#readme)
- buf Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buf)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
