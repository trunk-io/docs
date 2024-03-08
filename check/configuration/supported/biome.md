---
description: biome is a linter for JavaScript, TypeScript, jsx and json
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

**biome** is a linter for JavaScript, TypeScript, jsx and json.

You can enable the biome plugin with

```shell
trunk check enable biome
```

## Settings


biome uses the same config files as the
upstream [biome](https://biomejs.dev/) project, so you can continue to use any
existing configuration files (ex: `biome.json`, `rome.json`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/biome) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
