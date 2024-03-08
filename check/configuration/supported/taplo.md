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

## Auto Enabling

taplo will be auto-enabled if any of the following filetypes are present: *toml*

## Settings

taplo supports the following config files:
* `.taplo.toml`
* `taplo.toml`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [taplo site](https://github.com/tamasfe/taplo#readme)
- taplo Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/taplo)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
