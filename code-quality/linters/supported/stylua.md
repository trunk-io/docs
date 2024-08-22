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

## Auto Enabling

stylua will be auto-enabled if any of its config files are present: *`stylua.toml`, `.stylua.toml`*.

## Settings

stylua supports the following config files:
* `stylua.toml`
* `.stylua.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk Code Quality provides a default `stylua.toml` if your project does not already have one.



## Links

- [stylua site](https://github.com/JohnnyMorganz/StyLua/tree/main)
- stylua Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stylua)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
