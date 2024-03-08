---
description: renovate is a linter for Renovate
title: Trunk | How to run renovate
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

# renovate

[**renovate**](https://github.com/renovatebot/renovate#readme) is a linter for Renovate.

You can enable the renovate linter with:

```shell
trunk check enable renovate
```

## Settings

**renovate** uses the same config files as the
upstream [renovate](https://github.com/renovatebot/renovate#readme) project, so you can continue to use any
existing configuration files (ex: `renovate.json`, `renovate.json5`, `.github/renovate.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/renovate) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [renovate site](https://github.com/renovatebot/renovate#readme)
* renovate Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/renovate)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
