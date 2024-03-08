---
description: biome is a linter for JavaScript, TypeScript, jsx and json
title: Trunk | How to run biome
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

# biome

[**biome**](https://biomejs.dev/) is a linter for JavaScript, TypeScript, jsx and json.

You can enable the biome linter with:

```shell
trunk check enable biome
```

## Settings

**biome** uses the same config files as the
upstream [biome](https://biomejs.dev/) project, so you can continue to use any
existing configuration files (ex: `biome.json`, `rome.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/biome) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [biome site](https://biomejs.dev/)
* biome Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/biome)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
