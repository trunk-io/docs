---
description: taplo is a linter for TOML
title: Trunk | How to run taplo
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

# taplo

[**taplo**](https://github.com/tamasfe/taplo#readme) is a linter for TOML.

You can enable the taplo linter with:

```shell
trunk check enable taplo
```

## Settings

**taplo** uses the same config files as the
upstream [taplo](https://github.com/tamasfe/taplo#readme) project, so you can continue to use any
existing configuration files (ex: `.taplo.toml`, `taplo.toml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/taplo) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [taplo site](https://github.com/tamasfe/taplo#readme)
* taplo Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/taplo)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
