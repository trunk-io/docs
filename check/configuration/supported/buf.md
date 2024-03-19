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


buf is composed of several linter commands.
    
`buf-format` only runs the reformatting, not lint checking.

You can enable the `buf-format` linter with:

```shell
trunk check enable buf-format
```

`buf-lint` only runs the lint checking, not reformatting.

You can enable the `buf-lint` linter with:

```shell
trunk check enable buf-lint
```

`buf-breaking` only checks for breaking proto changes.

You can enable the `buf-breaking` linter with:

```shell
trunk check enable buf-breaking
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
