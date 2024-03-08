---
description: stylua is a linter for Lua
title: Trunk | How to run stylua
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

# stylua

[**stylua**](https://github.com/JohnnyMorganz/StyLua/tree/main) is a linter for Lua.

You can enable the stylua linter with:

```shell
trunk check enable stylua
```

## Settings

**stylua** uses the same config files as the
upstream [stylua](https://github.com/JohnnyMorganz/StyLua/tree/main) project, so you can continue to use any
existing configuration files (ex: `stylua.toml`, `.stylua.toml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/stylua) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [stylua site](https://github.com/JohnnyMorganz/StyLua/tree/main)
* stylua Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stylua)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
