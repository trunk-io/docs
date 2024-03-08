---
description: gokart is a linter for Go
title: Trunk | How to run gokart
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

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk check provides a default `analyzers.yml` if your project does not already have one.



## Links

- [gokart site](https://github.com/praetorian-inc/gokart)
- gokart Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/gokart)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
