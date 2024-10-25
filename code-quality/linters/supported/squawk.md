---
description: squawk is a linter for SQL
title: Trunk | How to run Squawk
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

# Squawk

[**Squawk**](https://github.com/sbdchd/squawk) is a linter for SQL.

You can enable the Squawk linter with:

```shell
trunk check enable squawk
```

## Auto Enabling

Squawk will be auto-enabled if a `.squawk.toml` config file is present.

## Settings

Squawk supports the following config files:
* `.squawk.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.





asdfasdf



## Links

- [Squawk site](https://github.com/sbdchd/squawk)
- Squawk Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/squawk)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
