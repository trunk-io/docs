---
description: buf-lint is a linter for Protobuf
title: Trunk | How to run buf-lint
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

# buf-lint

[**buf-lint**](https://github.com/bufbuild/buf#readme) is a linter for Protobuf.

You can enable the buf-lint linter with:

```shell
trunk check enable buf-lint
```

## Auto Enabling

buf-lint will never be auto-enabled. It must be enabled manually.

## Settings

buf-lint supports the following config files:
* `buf.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [buf-lint site](https://github.com/bufbuild/buf#readme)
- buf-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buf-lint)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
