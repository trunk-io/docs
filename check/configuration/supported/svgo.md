---
description: SVGO, or Scalable Vector Graphics Optimizer, is a tool designed to optimize SVG files, making them smaller and more efficient without compromising on quality.
title: Trunk | How to run SVGO
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

# SVGO

[**SVGO**](https://github.com/svg/svgo) is a linter for SVG.

You can enable the SVGO linter with:

```shell
trunk check enable svgo
```

## Settings

**SVGO** uses the same config files as the
upstream [SVGO](https://github.com/svg/svgo) project, so you can continue to use any
existing configuration files (ex: `svgo.config.js`, `svgo.config.mjs`, `svgo.config.cjs`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/svgo) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [SVGO site](https://github.com/svg/svgo)
* SVGO Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/svgo)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
