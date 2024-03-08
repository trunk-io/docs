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

## Auto Enabling

biome will be auto-enabled if any of its config files are present: *`biome.json`, `rome.json`*

## Settings

biome supports the following config files:
* `biome.json`
* `rome.json`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [biome site](https://biomejs.dev/)
- biome Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/biome)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
