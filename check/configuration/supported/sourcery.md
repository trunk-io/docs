---
description: sourcery is a linter for Python
title: Trunk | How to run sourcery
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

# sourcery

[**sourcery**](https://sourcery.ai/) is a linter for Python.

You can enable the sourcery linter with:

```shell
trunk check enable sourcery
```

## Auto Enabling

sourcery will never be auto-enabled. It must be enabled manually.

## Settings

sourcery supports the following config files:
* `.sourcery.yaml`
* `sourcery.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [sourcery site](https://sourcery.ai/)
- sourcery Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/sourcery)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
