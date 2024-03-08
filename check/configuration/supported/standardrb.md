---
description: standardrb is a linter for Ruby
title: Trunk | How to run standardrb
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

# standardrb

[**standardrb**](https://github.com/testdouble/standard#readme) is a linter for Ruby.

You can enable the standardrb linter with:

```shell
trunk check enable standardrb
```

## Auto Enabling

standardrb will be auto-enabled if a `.standard.yml` config file is present.

## Settings

standardrb supports the following config files:
* `.standard.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [standardrb site](https://github.com/testdouble/standard#readme)
- standardrb Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/standardrb)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
