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

## Settings

**buf** uses the same config files as the
upstream [buf](https://github.com/bufbuild/buf#readme) project, so you can continue to use any
existing configuration files (ex: `buf.yaml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/buf) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [buf site](https://github.com/bufbuild/buf#readme)
* buf Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buf)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
