---
description: squawk is a linter for SQL
title: Trunk | How to run squawk
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

# squawk

[**squawk**](https://github.com/sbdchd/squawk) is a linter for SQL.

You can enable the squawk linter with:

```shell
trunk check enable squawk
```

## Auto Enabling

squawk will be auto-enabled if a `.squawk.toml` config file is present.

## Settings

squawk supports the following config files:
* `.squawk.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [squawk site](https://github.com/sbdchd/squawk)
- squawk Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/squawk)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
