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

## Auto Enabling

SVGO will be auto-enabled if any *Svg* files are present.

## Settings

SVGO supports the following config files:
* `svgo.config.js`
* `svgo.config.mjs`
* `svgo.config.cjs`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk check provides a default `svgo.config.js` if your project does not already have one.



## Links

- [SVGO site](https://github.com/svg/svgo)
- SVGO Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/svgo)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
