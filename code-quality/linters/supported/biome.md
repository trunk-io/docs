---
description: Biome is a linter for JavaScript and TypeScript, improving code quality by automatically fixing issues, enforcing standards, and ensuring consistency.
title: Trunk | How to run Biome
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

# Biome

[**Biome**](https://biomejs.dev/) is a linter for JavaScript, TypeScript, jsx and json.

You can enable the Biome linter with:

```shell
trunk check enable biome
```

## Auto Enabling

Biome will be auto-enabled if any of its config files are present: *`biome.json`, `rome.json`*.

## Settings

Biome supports the following config files:
* `biome.json`
* `rome.json`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.




## Links

- [Biome site](https://biomejs.dev/)
- Biome Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/biome)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
