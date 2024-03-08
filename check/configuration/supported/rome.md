---
description: rome is a linter for JavaScript and TypeScript
title: Trunk | How to run rome
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

# rome

[**rome**](https://github.com/rome/tools#readme) is a linter for JavaScript and TypeScript.

You can enable the rome linter with:

```shell
trunk check enable rome
```

## Settings

**rome** uses the same config files as the
upstream [rome](https://github.com/rome/tools#readme) project, so you can continue to use any
existing configuration files (ex: `rome.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rome) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [rome site](https://github.com/rome/tools#readme)
* rome Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rome)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
