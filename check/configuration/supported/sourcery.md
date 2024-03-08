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

## Settings

**sourcery** uses the same config files as the
upstream [sourcery](https://sourcery.ai/) project, so you can continue to use any
existing configuration files (ex: `.sourcery.yaml`, `sourcery.yaml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/sourcery) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [sourcery site](https://sourcery.ai/)
* sourcery Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/sourcery)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
