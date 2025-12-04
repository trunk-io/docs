---
title: Trunk | How to run gokart
description: gokart is a linter for Go
---

# gokart

[**gokart**](https://github.com/praetorian-inc/gokart) is a linter for Go.

You can enable the gokart linter with:

```shell
trunk check enable gokart
```

## Auto Enabling

gokart will be auto-enabled if a `analyzers.yml` config file is present.

## Settings

gokart supports the following config files:

* `analyzers.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `analyzers.yml` if your project does not already have one.

## Links

* [gokart site](https://github.com/praetorian-inc/gokart)
* gokart Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/gokart)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
